#!/usr/bin/env python3
"""Build kb_data.json and inject offline fallback bundle into index.html.

Zero external dependencies (Python 3 standard library only).
Source of truth: papers/*.md, quizzes/quiz_bank.json, compare_presets.json, recommendations.json.
"""
import glob
import json
import os
import re
from datetime import datetime

KB_DIR = os.path.dirname(os.path.abspath(__file__))
# "논문" 폴더가 들어 있는 상위 폴더. 기본값은 이 스크립트 폴더의 부모이며, HEART_LAB_DIR 환경변수로 바꿀 수 있습니다.
HEART_LAB_DIR = os.environ.get("HEART_LAB_DIR") or os.path.dirname(KB_DIR)
PAPERS_DIR = os.path.join(KB_DIR, "papers")
QUIZ_PATH = os.path.join(KB_DIR, "quizzes", "quiz_bank.json")
COMPARE_PATH = os.path.join(KB_DIR, "compare_presets.json")
REC_PATH = os.path.join(KB_DIR, "recommendations.json")
OUT_JSON = os.path.join(KB_DIR, "kb_data.json")
TEMPLATE_HTML = os.path.join(KB_DIR, "app_template.html")
OUT_HTML = os.path.join(KB_DIR, "index.html")


def parse_frontmatter(text: str):
    """Parse simple YAML frontmatter without PyYAML."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
    if not m:
        return {}, text
    raw_meta, body = m.group(1), m.group(2)
    meta = {}
    for line in raw_meta.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if val.startswith("[") or val.startswith('"') or val.startswith("{"):
            try:
                meta[key] = json.loads(val)
            except json.JSONDecodeError:
                meta[key] = val.strip('"')
        elif re.fullmatch(r"-?\d+", val):
            meta[key] = int(val)
        else:
            meta[key] = val
    return meta, body


def parse_sections(body: str):
    sections = {}
    current = None
    buf = []
    for line in body.splitlines():
        if line.startswith("## "):
            if current is not None:
                sections[current] = "\n".join(buf).strip()
            current = line[3:].strip()
            buf = []
        else:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).strip()

    tldr = sections.get("한 줄 요약", "")
    mech_raw = sections.get("핵심 메커니즘", "")
    mechanisms = [
        re.sub(r"^[-*]\s+", "", ln).strip()
        for ln in mech_raw.splitlines()
        if ln.strip()
    ]
    diff = sections.get("기존 대비 차이", "")
    limits = sections.get("한계 & 연결", "")
    return tldr, mechanisms, diff, limits


def load_papers():
    papers = []
    for path in sorted(glob.glob(os.path.join(PAPERS_DIR, "*.md"))):
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
        meta, body = parse_frontmatter(raw)
        tldr, mechanisms, diff, limits = parse_sections(body)
        pid = meta.get("id") or os.path.splitext(os.path.basename(path))[0]
        pdf_rel = meta.get("pdf", "")
        pdf_exists = bool(pdf_rel) and os.path.exists(os.path.join(HEART_LAB_DIR, pdf_rel))
        papers.append({
            "id": pid,
            "short": meta.get("short", pid),
            "title": meta.get("title", pid),
            "year": meta.get("year", 2024),
            "venue": meta.get("venue", ""),
            "category": meta.get("category", "Other"),
            "tags": meta.get("tags", []),
            "pdf": pdf_rel,
            "pdfExists": pdf_exists,
            "predecessors": meta.get("predecessors", []),
            "successors": meta.get("successors", []),
            "tldr": tldr,
            "mechanisms": mechanisms,
            "diff": diff,
            "limits": limits,
            "mdFile": f"papers/{os.path.basename(path)}",
        })
    papers.sort(key=lambda p: (p["category"], p["year"], p["short"]))
    return papers


def build_recall_cards(papers):
    """Auto-generate concise single-model active-recall flashcards for every single paper."""
    cards = []
    for p in papers:
        cards.append({
            "id": f"rc-{p['id']}",
            "papers": [p["id"]],
            "type": "recall",
            "scope": "single",
            "category": p["category"],
            "question": f"[{p['short']} ({p['year']})] 이 모델 자체의 핵심 아이디어와 동작 메커니즘을 떠올려 보세요.",
            "hint": " · ".join(p["tags"][:3]),
            "answerText": p["tldr"],
            "mechanisms": p["mechanisms"],
            "diff": p["diff"],
            "limits": p["limits"]
        })
    return cards


def enrich_recommendations(recs):
    """Check whether local PDF files exist for each recommended paper."""
    out = {}
    for axis, items in recs.items():
        enriched = []
        for item in items:
            c = dict(item)
            rel = c.get("local_pdf", "")
            c["pdfExists"] = bool(rel) and os.path.exists(os.path.join(HEART_LAB_DIR, rel))
            enriched.append(c)
        out[axis] = enriched
    return out


def compute_domain_stats(papers):
    counts = {}
    for p in papers:
        counts[p["category"]] = counts.get(p["category"], 0) + 1
    # Include strategic adjacent domains with 0 papers so coverage gaps are explicit
    for empty_dom in ["RL & Agent", "World Model & 3D"]:
        counts.setdefault(empty_dom, 0)
    return [
        {"domain": k, "count": v}
        for k, v in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    ]


def build():
    papers = load_papers()
    mcqs = json.load(open(QUIZ_PATH, "r", encoding="utf-8")) if os.path.exists(QUIZ_PATH) else []
    compare_presets = json.load(open(COMPARE_PATH, "r", encoding="utf-8")) if os.path.exists(COMPARE_PATH) else []
    recs_raw = json.load(open(REC_PATH, "r", encoding="utf-8")) if os.path.exists(REC_PATH) else {}

    recall_cards = build_recall_cards(papers)
    quizzes = mcqs + recall_cards
    recommendations = enrich_recommendations(recs_raw)
    domain_stats = compute_domain_stats(papers)

    single_cnt = sum(1 for q in quizzes if q.get("scope") == "single" or q.get("type") in ("single_mcq", "recall"))
    link_cnt = len(quizzes) - single_cnt

    data = {
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "paperCount": len(papers),
        "quizCount": len(quizzes),
        "mcqCount": len(mcqs),
        "recallCount": len(recall_cards),
        "singleQuizCount": single_cnt,
        "linkQuizCount": link_cnt,
        "papers": papers,
        "quizzes": quizzes,
        "comparePresets": compare_presets,
        "recommendations": recommendations,
        "domainStats": domain_stats,
    }

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    if os.path.exists(TEMPLATE_HTML):
        with open(TEMPLATE_HTML, "r", encoding="utf-8") as f:
            html = f.read()
        embedded = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
        html = html.replace("/*__EMBEDDED_KB_DATA__*/null", embedded)
        with open(OUT_HTML, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Built {OUT_JSON} and {OUT_HTML} ({len(papers)} papers, {len(quizzes)} quiz items).")
    else:
        print(f"Built {OUT_JSON} ({len(papers)} papers, {len(quizzes)} quiz items). Template not found yet.")
    return data


if __name__ == "__main__":
    build()
