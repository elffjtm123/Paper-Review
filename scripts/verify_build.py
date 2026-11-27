#!/usr/bin/env python3
"""build.py가 만든 kb_data.json과 index.html이 온전한지 확인합니다.

사용법 (지식베이스 루트에서, build.py 실행 뒤):
    python3 build.py && python3 scripts/verify_build.py
"""
import glob
import json
import os
import re
import sys

KB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLACEHOLDER = "/*__EMBEDDED_KB_DATA__*/null"

errors = []


def fail(msg):
    errors.append(msg)
    print(f"ERROR {msg}")


def main():
    n_md = len(glob.glob(os.path.join(KB_DIR, "papers", "*.md")))

    # 1) 템플릿에 자리표시자가 정확히 한 번 있어야 build.py가 데이터를 넣을 수 있음
    tpl_path = os.path.join(KB_DIR, "app_template.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()
    cnt = tpl.count(PLACEHOLDER)
    if cnt != 1:
        fail(f"app_template.html에 '{PLACEHOLDER}'가 {cnt}번 있습니다 (정확히 1번이어야 함)")

    # 2) kb_data.json
    json_path = os.path.join(KB_DIR, "kb_data.json")
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        fail(f"kb_data.json을 읽을 수 없습니다: {e}")
        return

    papers = data.get("papers", [])
    if data.get("paperCount") != n_md or len(papers) != n_md:
        fail(f"노트 {n_md}편인데 kb_data.json에는 {data.get('paperCount')}편 (papers {len(papers)}개)")
    if data.get("recallCount") != len(papers):
        fail(f"복습 카드 {data.get('recallCount')}장 ≠ 논문 {len(papers)}편")
    if data.get("quizCount") != data.get("mcqCount", 0) + data.get("recallCount", 0):
        fail("quizCount가 mcqCount + recallCount와 다릅니다")
    if len({p["id"] for p in papers}) != len(papers):
        fail("kb_data.json에 겹치는 논문 id가 있습니다")
    for p in papers:
        missing = [k for k in ("tldr", "mechanisms", "diff", "limits") if not p.get(k)]
        if missing:
            fail(f"{p['mdFile']}: 빌드 결과에서 비어 있는 칸 {missing}")
    if len({q["id"] for q in data.get("quizzes", [])}) != len(data.get("quizzes", [])):
        fail("kb_data.json에 겹치는 퀴즈 id가 있습니다")

    # 3) index.html에 같은 데이터가 들어갔는지
    html_path = os.path.join(KB_DIR, "index.html")
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()
    except OSError as e:
        fail(f"index.html이 없습니다: {e}")
        return
    if PLACEHOLDER in html:
        fail("index.html에 자리표시자가 그대로 남아 있습니다 (데이터가 주입되지 않음)")
    m = re.search(r"const EMBEDDED_DATA = (\{.*?\});\n", html, re.S)
    if not m:
        fail("index.html에서 EMBEDDED_DATA를 찾지 못했습니다")
    else:
        try:
            embedded = json.loads(m.group(1).replace("<\\/", "</"))
        except json.JSONDecodeError as e:
            fail(f"index.html에 넣은 데이터가 JSON으로 읽히지 않습니다: {e.msg}")
        else:
            if embedded.get("paperCount") != data.get("paperCount"):
                fail("index.html 안 데이터와 kb_data.json의 논문 수가 다릅니다")

    if not errors:
        print(f"빌드 확인 완료: 논문 {len(papers)}편, 퀴즈 {data.get('quizCount')}개, "
              f"index.html {len(html) // 1024}KB")


if __name__ == "__main__":
    main()
    sys.exit(1 if errors else 0)
