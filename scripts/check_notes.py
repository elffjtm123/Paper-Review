#!/usr/bin/env python3
"""papers/*.md 노트와 퀴즈/비교표 JSON의 형식을 검사합니다.

표준 라이브러리만 사용합니다. build.py의 parse_frontmatter / parse_sections를
그대로 가져와 쓰므로, 이 검사를 통과하면 build.py가 읽는 방식과 일치합니다.

사용법 (지식베이스 루트에서):
    python3 scripts/check_notes.py            # 오류가 있으면 종료 코드 1
    python3 scripts/check_notes.py --strict   # 경고도 오류로 취급

오류(ERROR): 빌드 결과가 깨지거나 사이트에서 잘못 보이는 문제
경고(WARN) : 당장은 동작하지만 손볼 만한 문제
"""
import argparse
import glob
import json
import os
import re
import sys
from datetime import date

KB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KB_DIR)
import build  # noqa: E402  (KB_DIR를 경로에 넣은 뒤 가져옴)

PAPERS_DIR = os.path.join(KB_DIR, "papers")
QUIZ_PATH = os.path.join(KB_DIR, "quizzes", "quiz_bank.json")
COMPARE_PATH = os.path.join(KB_DIR, "compare_presets.json")
REC_PATH = os.path.join(KB_DIR, "recommendations.json")
HEART_LAB_DIR = build.HEART_LAB_DIR  # build.py와 같은 기준(HEART_LAB_DIR 환경변수 지원)

REQUIRED_KEYS = ["id", "short", "title", "year", "venue", "category",
                 "tags", "pdf", "predecessors", "successors"]
LIST_KEYS = ["tags", "predecessors", "successors"]
STRING_KEYS = ["id", "short", "title", "venue", "category", "pdf"]

# [추측] 현재 63편에 쓰인 10개 분류를 그대로 허용 목록으로 둡니다.
# 새 분야를 추가할 때는 여기에도 한 줄 추가하세요.
# (build.py는 "RL & Agent", "World Model & 3D"를 0편 분야로 표시하므로 함께 허용)
ALLOWED_CATEGORIES = {
    "VLA", "Generative", "Transformer & LLM", "Optimization",
    "Dataset & Robustness", "Multimodal", "Vision", "Sequence & Audio",
    "Robot Control", "Time Series",
    "RL & Agent", "World Model & 3D",
}

REQUIRED_SECTIONS = ["한 줄 요약", "핵심 메커니즘", "기존 대비 차이", "한계 & 연결"]
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MIN_YEAR = 1950  # [추측] ARIMA(1970) 등 고전 논문도 통과하도록 넉넉히


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"{where}: {msg}")


def raw_frontmatter_lines(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    return m.group(1).splitlines() if m else None


def check_note(path, rep):
    name = os.path.relpath(path, KB_DIR)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    lines = raw_frontmatter_lines(text)
    if lines is None:
        rep.error(name, "맨 앞에 '---'로 감싼 YAML 메타데이터가 없습니다")
        return None

    meta, body = build.parse_frontmatter(text)

    # 중복 키 (build.py는 조용히 마지막 값으로 덮어씀)
    seen = set()
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith("#") or ":" not in s:
            continue
        key = s.split(":", 1)[0].strip()
        if key in seen:
            rep.error(name, f"메타데이터 키 '{key}'가 두 번 나옵니다")
        seen.add(key)
        # 대괄호/따옴표로 시작했는데 JSON 해석에 실패하면 build.py는 문자열로 넘겨버림
        val = s.split(":", 1)[1].strip()
        if val[:1] in ("[", "{"):
            try:
                json.loads(val)
            except json.JSONDecodeError as e:
                rep.error(name, f"'{key}' 값이 올바른 목록 형식이 아닙니다 ({e.msg}). "
                                f'예: ["a", "b"] — 큰따옴표와 쉼표를 확인하세요')

    for k in REQUIRED_KEYS:
        if k not in meta:
            rep.error(name, f"필수 키 '{k}'가 없습니다")
    for k in meta:
        if k not in REQUIRED_KEYS:
            rep.warn(name, f"알 수 없는 키 '{k}' (오타인지 확인하세요)")

    stem = os.path.splitext(os.path.basename(path))[0]
    pid = meta.get("id")
    if isinstance(pid, str):
        if pid != stem:
            rep.error(name, f"id '{pid}'가 파일 이름 '{stem}'과 다릅니다")
        if not ID_RE.match(pid):
            rep.error(name, f"id '{pid}'는 소문자·숫자·하이픈만 써야 합니다")

    for k in STRING_KEYS:
        if k in meta and not isinstance(meta[k], str):
            rep.error(name, f"'{k}'는 문자열이어야 합니다 (현재 {type(meta[k]).__name__})")
    for k in ("id", "short", "title", "category"):
        if isinstance(meta.get(k), str) and not meta[k].strip():
            rep.error(name, f"'{k}'가 비어 있습니다")
    if isinstance(meta.get("venue"), str) and not meta["venue"].strip():
        rep.warn(name, "'venue'가 비어 있습니다")

    year = meta.get("year")
    if "year" in meta:
        if not isinstance(year, int):
            rep.error(name, f"year '{year}'는 정수여야 합니다 (따옴표 없이)")
        elif not (MIN_YEAR <= year <= date.today().year + 1):
            rep.error(name, f"year {year}가 범위({MIN_YEAR}~{date.today().year + 1}) 밖입니다")

    cat = meta.get("category")
    if isinstance(cat, str) and cat and cat not in ALLOWED_CATEGORIES:
        rep.error(name, f"category '{cat}'는 허용 목록에 없습니다 "
                        f"(새 분야라면 scripts/check_notes.py의 ALLOWED_CATEGORIES에 추가)")

    for k in LIST_KEYS:
        v = meta.get(k)
        if k in meta and not isinstance(v, list):
            rep.error(name, f"'{k}'는 목록이어야 합니다. 예: {k}: [\"a\", \"b\"]")
        elif isinstance(v, list):
            if any(not isinstance(x, str) or not x.strip() for x in v):
                rep.error(name, f"'{k}' 안에 비었거나 문자열이 아닌 항목이 있습니다")
            dups = {x for x in v if v.count(x) > 1}
            if dups:
                rep.warn(name, f"'{k}'에 중복 항목: {sorted(dups)}")
    if isinstance(meta.get("tags"), list) and not meta["tags"]:
        rep.warn(name, "tags가 비어 있습니다 (복습 카드 힌트가 비게 됩니다)")

    pdf = meta.get("pdf")
    if isinstance(pdf, str):
        if not pdf:
            rep.warn(name, "pdf 경로가 비어 있습니다")
        elif not pdf.lower().endswith(".pdf"):
            rep.error(name, f"pdf '{pdf}'가 .pdf로 끝나지 않습니다")
        elif os.path.isabs(pdf):
            rep.error(name, "pdf는 Heart-Lab 폴더 기준 상대 경로여야 합니다 (예: 논문/VLA/RT-1.pdf)")
        elif os.path.isdir(os.path.join(HEART_LAB_DIR, "논문")):
            # 논문 PDF 폴더가 옆에 있을 때(=로컬 Mac)만 실제 존재를 확인. CI에서는 건너뜀.
            if not os.path.exists(os.path.join(HEART_LAB_DIR, pdf)):
                rep.warn(name, f"pdf 파일을 찾을 수 없습니다: {pdf}")

    # 본문 4칸
    tldr, mechanisms, diff, limits = build.parse_sections(body)
    headings = [ln[3:].strip() for ln in body.splitlines() if ln.startswith("## ")]
    for sec in REQUIRED_SECTIONS:
        if sec not in headings:
            rep.error(name, f"'## {sec}' 섹션이 없습니다")
    for h in headings:
        if headings.count(h) > 1:
            rep.error(name, f"'## {h}' 섹션이 두 번 나옵니다")
            break
    for h in headings:
        if h not in REQUIRED_SECTIONS:
            rep.warn(name, f"알 수 없는 섹션 '## {h}' (사이트에 표시되지 않습니다)")
    for sec, val in zip(REQUIRED_SECTIONS, (tldr, mechanisms, diff, limits)):
        if sec in headings and not val:
            rep.error(name, f"'## {sec}' 섹션이 비어 있습니다")
    mech_raw = body.split("## 핵심 메커니즘", 1)[-1].split("\n## ", 1)[0]
    if "## 핵심 메커니즘" in body and not re.search(r"^\s*[-*]\s+\S", mech_raw, re.M):
        rep.warn(name, "'핵심 메커니즘'에 '- ' 글머리표 항목이 없습니다")

    return meta


def check_links(metas, rep):
    ids = {}
    for path, meta in metas:
        pid = meta.get("id")
        if not isinstance(pid, str):
            continue
        if pid in ids:
            rep.error(os.path.relpath(path, KB_DIR), f"id '{pid}'가 {ids[pid]}와 겹칩니다")
        ids[pid] = os.path.relpath(path, KB_DIR)
    by_id = {m.get("id"): m for _, m in metas}

    for path, meta in metas:
        name = os.path.relpath(path, KB_DIR)
        pid = meta.get("id")
        for k in ("predecessors", "successors"):
            v = meta.get(k)
            if not isinstance(v, list):
                continue
            for ref in v:
                if ref == pid:
                    rep.error(name, f"'{k}'에 자기 자신이 들어 있습니다")
                elif ref not in by_id:
                    rep.error(name, f"'{k}'의 '{ref}'에 해당하는 노트가 없습니다")
                else:
                    # [추측] 양방향 연결이 원칙인지 몰라 경고로만 둡니다.
                    other = "predecessors" if k == "successors" else "successors"
                    back = by_id[ref].get(other)
                    if isinstance(back, list) and pid not in back:
                        rep.warn(name, f"{k} '{ref}' ↔ 상대 노트의 {other}에 '{pid}'가 없습니다 (단방향 연결)")
    return set(ids)


def load_json(path, rep):
    name = os.path.relpath(path, KB_DIR)
    if not os.path.exists(path):
        rep.warn(name, "파일이 없습니다 (빌드는 빈 값으로 진행)")
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        rep.error(name, f"JSON 형식 오류 (줄 {e.lineno}, 칸 {e.colno}): {e.msg}")
        return None


def check_quizzes(ids, rep):
    data = load_json(QUIZ_PATH, rep)
    if data is None:
        return
    name = os.path.relpath(QUIZ_PATH, KB_DIR)
    if not isinstance(data, list):
        rep.error(name, "최상위가 목록([...])이어야 합니다")
        return
    seen = set()
    for i, q in enumerate(data):
        where = f"{name}[{i}]"
        if not isinstance(q, dict):
            rep.error(where, "항목이 객체가 아닙니다")
            continue
        qid = q.get("id")
        where = f"{name} ({qid or i})"
        for k in ("id", "papers", "type", "question", "options", "answer"):
            if k not in q:
                rep.error(where, f"'{k}'가 없습니다")
        if qid in seen:
            rep.error(where, "퀴즈 id가 겹칩니다")
        seen.add(qid)
        if isinstance(qid, str) and qid.startswith("rc-"):
            rep.error(where, "'rc-'로 시작하는 id는 build.py가 자동 생성하는 카드와 겹칠 수 있습니다")
        for p in q.get("papers", []) or []:
            if p not in ids:
                rep.error(where, f"papers의 '{p}'에 해당하는 노트가 없습니다")
        opts, ans = q.get("options"), q.get("answer")
        if isinstance(opts, list):
            if len(opts) < 2:
                rep.error(where, "보기가 2개 이상이어야 합니다")
            if len(set(map(str, opts))) != len(opts):
                rep.warn(where, "보기에 같은 내용이 있습니다")
            if not isinstance(ans, int) or isinstance(ans, bool) or not (0 <= ans < len(opts)):
                rep.error(where, f"answer {ans!r}가 보기 범위(0~{len(opts) - 1}) 밖입니다")
        # [추측] 지금 쓰는 값만 허용. 새 유형을 만들면 여기에 추가하세요.
        if q.get("type") not in (None, "single_mcq", "compare"):
            rep.warn(where, f"처음 보는 type '{q.get('type')}'")
        if q.get("scope") not in (None, "single", "link"):
            rep.warn(where, f"처음 보는 scope '{q.get('scope')}'")


def check_compare(ids, rep):
    data = load_json(COMPARE_PATH, rep)
    if data is None:
        return
    name = os.path.relpath(COMPARE_PATH, KB_DIR)
    for c in data if isinstance(data, list) else []:
        where = f"{name} ({c.get('id')})"
        ncol = len(c.get("columns", []))
        for r in c.get("rows", []):
            pid = r.get("paperId")
            if pid and pid not in ids:
                rep.error(where, f"paperId '{pid}'에 해당하는 노트가 없습니다")
            if ncol and len(r.get("vals", [])) != ncol:
                rep.error(where, f"'{pid}' 행의 칸 수({len(r.get('vals', []))})가 열 수({ncol})와 다릅니다")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--strict", action="store_true", help="경고도 실패로 처리")
    args = ap.parse_args()

    rep = Report()
    paths = sorted(glob.glob(os.path.join(PAPERS_DIR, "*.md")))
    if not paths:
        rep.error("papers/", "노트(*.md)가 하나도 없습니다")
    metas = []
    for p in paths:
        m = check_note(p, rep)
        if m is not None:
            metas.append((p, m))
    ids = check_links(metas, rep)
    check_quizzes(ids, rep)
    check_compare(ids, rep)
    load_json(REC_PATH, rep)

    for w in rep.warnings:
        print(f"WARN  {w}")
    for e in rep.errors:
        print(f"ERROR {e}")
    # GitHub Actions에서 파일 옆에 표시되도록 주석 형식으로도 출력
    if os.environ.get("GITHUB_ACTIONS") == "true":
        for level, items in (("warning", rep.warnings), ("error", rep.errors)):
            for item in items:
                f, _, msg = item.partition(": ")
                f = f.split(" (")[0].split("[")[0]
                print(f"::{level} file={f}::{msg}")

    print(f"\n노트 {len(paths)}편 검사: 오류 {len(rep.errors)}건, 경고 {len(rep.warnings)}건")
    failed = rep.errors or (args.strict and rep.warnings)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
