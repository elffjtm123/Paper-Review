#!/usr/bin/env python3
"""Heart-Lab Paper Knowledge Base Server.

Features:
- Serves responsive mobile + desktop review web app on 0.0.0.0:8765 (Mac + Phone via Wi-Fi / Tailscale)
- Syncs spaced-repetition state (state.json) across Mac and Phone
- BM25 RAG retrieval over all 63 concise notes (/api/rag)
- Live latest arXiv paper lookup (/api/arxiv)
- Optional LLM proxy for Gemini API or local Ollama (/api/llm) with RAG & 3-axis thinking recommender
- Auto-shutdown after daily quiz completion (with cancel/keep-alive & idle safety timeout)
"""
import argparse
import json
import math
import mimetypes
import os
import re
import signal
import socket
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import build as kb_builder

KB_DIR = os.path.dirname(os.path.abspath(__file__))
# "논문" 폴더가 들어 있는 상위 폴더. 기본값은 이 스크립트 폴더의 부모이며, HEART_LAB_DIR 환경변수로 바꿀 수 있습니다.
HEART_LAB_DIR = os.environ.get("HEART_LAB_DIR") or os.path.dirname(KB_DIR)
STATE_PATH = os.path.join(KB_DIR, "state.json")
DATA_PATH = os.path.join(KB_DIR, "kb_data.json")
INDEX_PATH = os.path.join(KB_DIR, "index.html")
PID_PATH = os.path.join(KB_DIR, ".server.pid")

STATE_LOCK = threading.Lock()


def get_lan_ip():
    try:
        out = subprocess.check_output(["ipconfig", "getifaddr", "en0"], text=True, stderr=subprocess.DEVNULL).strip()
        if out:
            return out
    except Exception:
        pass
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def get_tailscale_ip():
    for cmd in ["/usr/local/bin/tailscale", "tailscale"]:
        try:
            out = subprocess.check_output([cmd, "ip", "-4"], text=True, stderr=subprocess.DEVNULL, timeout=2).strip()
            if out:
                return out.splitlines()[0].strip()
        except Exception:
            continue
    return ""


def load_kb_data():
    if not os.path.exists(DATA_PATH):
        return kb_builder.build()
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def default_state():
    return {
        "sm2": {},            # paperId -> {interval, ease, reps, due, lastScore, attempts, wrong}
        "quizHistory": [],    # [{date, score, total, paperIds, completedAt}]
        "dailyCompleted": {}, # YYYY-MM-DD -> {score, total, completedAt}
        "streak": 0,
        "bookmarks": [],
        "aiRecommendations": None,
        "updatedAt": datetime.now().isoformat(timespec="seconds"),
    }


def load_state():
    with STATE_LOCK:
        if not os.path.exists(STATE_PATH):
            st = default_state()
            with open(STATE_PATH, "w", encoding="utf-8") as f:
                json.dump(st, f, ensure_ascii=False, indent=2)
            return st
        try:
            with open(STATE_PATH, "r", encoding="utf-8") as f:
                st = json.load(f)
            base = default_state()
            base.update(st)
            return base
        except Exception:
            return default_state()


def save_state(st):
    with STATE_LOCK:
        st["updatedAt"] = datetime.now().isoformat(timespec="seconds")
        tmp = STATE_PATH + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(st, f, ensure_ascii=False, indent=2)
        os.replace(tmp, STATE_PATH)
        return st


def tokenize(text: str):
    return re.findall(r"[a-z0-9가-힣π]+", (text or "").lower())


def bm25_search(query: str, papers: list, top_k: int = 6):
    q_tokens = tokenize(query)
    if not q_tokens:
        return papers[:top_k]
    docs = []
    for p in papers:
        blob = " ".join([
            p.get("short", ""), p.get("short", ""),
            p.get("title", ""), p.get("category", ""),
            " ".join(p.get("tags", [])),
            p.get("tldr", ""),
            " ".join(p.get("mechanisms", [])),
            p.get("diff", ""), p.get("limits", ""),
        ])
        toks = tokenize(blob)
        docs.append((p, toks))
    N = max(1, len(docs))
    avgdl = sum(len(t) for _, t in docs) / N
    df = {}
    for _, toks in docs:
        for w in set(toks):
            df[w] = df.get(w, 0) + 1
    k1, b = 1.5, 0.75
    scored = []
    for p, toks in docs:
        dl = len(toks)
        tf = {}
        for w in toks:
            tf[w] = tf.get(w, 0) + 1
        score = 0.0
        for qw in q_tokens:
            # Also allow substring match for Korean/English stems
            freq = tf.get(qw, 0)
            if freq == 0 and len(qw) >= 2:
                for w, cnt in tf.items():
                    if qw in w:
                        freq += cnt * 0.5
            if freq > 0:
                doc_freq = df.get(qw, 1)
                idf = math.log((N - doc_freq + 0.5) / (doc_freq + 0.5) + 1.0)
                score += idf * (freq * (k1 + 1)) / (freq + k1 * (1 - b + b * dl / max(1.0, avgdl)))
        if score > 0:
            scored.append((score, p))
    scored.sort(key=lambda x: -x[0])
    if not scored:
        return papers[:top_k]
    return [p for _, p in scored[:top_k]]


ARXIV_TOPIC_QUERIES = {
    "vla": 'all:"vision-language-action" OR all:"VLA" AND (cat:cs.RO OR cat:cs.CV)',
    "robustness": '(all:"vision-language-action" OR all:"robotic manipulation") AND (all:"robustness" OR all:"perturbation" OR all:"corruption" OR all:"visual noise")',
    "world_model": '(all:"world model" OR all:"JEPA") AND (all:"robot" OR all:"manipulation" OR all:"contact")',
    "rl_vla": '(all:"vision-language-action" OR all:"visuomotor") AND (all:"reinforcement learning" OR all:"online" OR all:"preference")',
    "diffusion_flow": '(all:"flow matching" OR all:"discrete diffusion") AND (all:"robot" OR all:"action" OR all:"policy")',
    "efficiency": '(all:"LoRA" OR all:"quantization" OR all:"efficient") AND (all:"VLA" OR all:"vision-language-action" OR all:"LLM")',
}


def fetch_arxiv(topic: str = "vla", custom_query: str = "", max_results: int = 8):
    q = custom_query.strip() if custom_query.strip() else ARXIV_TOPIC_QUERIES.get(topic, ARXIV_TOPIC_QUERIES["vla"])
    params = urllib.parse.urlencode({
        "search_query": q,
        "start": 0,
        "max_results": min(max(1, max_results), 15),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    url = f"https://export.arxiv.org/api/query?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "HeartLab-PaperKB/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        xml_bytes = resp.read()
    root = ET.fromstring(xml_bytes)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    items = []
    for entry in root.findall("a:entry", ns):
        title = re.sub(r"\s+", " ", (entry.findtext("a:title", "", ns) or "")).strip()
        summary = re.sub(r"\s+", " ", (entry.findtext("a:summary", "", ns) or "")).strip()
        published = (entry.findtext("a:published", "", ns) or "")[:10]
        aid = (entry.findtext("a:id", "", ns) or "").strip()
        authors = [a.findtext("a:name", "", ns) for a in entry.findall("a:author", ns)][:4]
        cats = [c.attrib.get("term", "") for c in entry.findall("a:category", ns)][:3]
        pdf_url = aid.replace("/abs/", "/pdf/") if "/abs/" in aid else aid
        items.append({
            "title": title,
            "summary": summary[:420] + ("..." if len(summary) > 420 else ""),
            "published": published,
            "url": aid,
            "pdfUrl": pdf_url,
            "authors": authors,
            "categories": cats,
        })
    return items


def call_gemini(api_key: str, model: str, system_prompt: str, user_prompt: str, expect_json: bool = False):
    model = model or "gemini-2.5-flash"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{urllib.parse.quote(model)}:generateContent?key={urllib.parse.quote(api_key)}"
    payload = {
        "systemInstruction": {"parts": [{"text": system_prompt}]},
        "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
        "generationConfig": {"temperature": 0.4},
    }
    if expect_json:
        payload["generationConfig"]["responseMimeType"] = "application/json"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["candidates"][0]["content"]["parts"][0]["text"]


def call_ollama(base_url: str, model: str, system_prompt: str, user_prompt: str, expect_json: bool = False):
    base_url = (base_url or "http://localhost:11434").rstrip("/")
    model = model or "qwen2.5:7b"
    url = f"{base_url}/api/chat"
    payload = {
        "model": model,
        "stream": False,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }
    if expect_json:
        payload["format"] = "json"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["message"]["content"]


class ServerController:
    def __init__(self, port: int, auto_shutdown_after_quiz: bool, idle_minutes: int):
        self.port = port
        self.auto_shutdown_after_quiz = auto_shutdown_after_quiz
        self.idle_minutes = idle_minutes
        self.started_at = time.time()
        self.last_activity = time.time()
        self.shutdown_deadline = None
        self.shutdown_reason = None
        self.httpd = None
        self.lan_ip = get_lan_ip()
        self.tailscale_ip = get_tailscale_ip()
        self.kb_data = load_kb_data()
        self._lock = threading.Lock()

    def touch(self):
        with self._lock:
            self.last_activity = time.time()

    def schedule_shutdown(self, delay_sec: int, reason: str):
        with self._lock:
            self.shutdown_deadline = time.time() + delay_sec
            self.shutdown_reason = reason

    def cancel_shutdown(self):
        with self._lock:
            self.shutdown_deadline = None
            self.shutdown_reason = None
            self.last_activity = time.time()

    def status_dict(self):
        with self._lock:
            rem = None
            if self.shutdown_deadline is not None:
                rem = max(0, int(round(self.shutdown_deadline - time.time())))
            return {
                "port": self.port,
                "localUrl": f"http://127.0.0.1:{self.port}",
                "lanUrl": f"http://{self.lan_ip}:{self.port}" if self.lan_ip else "",
                "tailscaleUrl": f"http://{self.tailscale_ip}:{self.port}" if self.tailscale_ip else "",
                "autoShutdownMode": self.auto_shutdown_after_quiz,
                "shutdownRemainingSec": rem,
                "shutdownReason": self.shutdown_reason,
                "idleMinutes": self.idle_minutes,
                "startedAt": datetime.fromtimestamp(self.started_at).isoformat(timespec="seconds"),
            }

    def watchdog_loop(self):
        while True:
            time.sleep(1)
            now = time.time()
            should_stop = False
            reason = ""
            with self._lock:
                if self.shutdown_deadline is not None and now >= self.shutdown_deadline:
                    should_stop = True
                    reason = self.shutdown_reason or "scheduled"
                elif self.idle_minutes > 0 and (now - self.last_activity) >= self.idle_minutes * 60:
                    should_stop = True
                    reason = f"idle_timeout_{self.idle_minutes}m"
            if should_stop:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Shutting down server ({reason})...", flush=True)
                if self.httpd:
                    threading.Thread(target=self.httpd.shutdown, daemon=True).start()
                break


def make_handler(ctrl: ServerController):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            pass  # Keep stdout clean

        def _send_json(self, obj, status=200):
            body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _read_json(self):
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0:
                return {}
            return json.loads(self.rfile.read(length).decode("utf-8"))

        def do_GET(self):
            ctrl.touch()
            parsed = urllib.parse.urlparse(self.path)
            path = parsed.path
            qs = urllib.parse.parse_qs(parsed.query)

            if path in ("/", "/index.html"):
                if not os.path.exists(INDEX_PATH):
                    kb_builder.build()
                with open(INDEX_PATH, "rb") as f:
                    raw = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(raw)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(raw)
                return

            if path == "/api/data":
                self._send_json({
                    "kb": ctrl.kb_data,
                    "state": load_state(),
                    "server": ctrl.status_dict(),
                })
                return

            if path == "/api/state":
                self._send_json({"state": load_state(), "server": ctrl.status_dict()})
                return

            if path == "/api/status":
                self._send_json(ctrl.status_dict())
                return

            if path == "/api/arxiv":
                topic = (qs.get("topic", ["vla"])[0] or "vla").strip()
                q = (qs.get("q", [""])[0] or "").strip()
                max_r = int(qs.get("max", ["8"])[0] or "8")
                try:
                    items = fetch_arxiv(topic=topic, custom_query=q, max_results=max_r)
                    self._send_json({"ok": True, "topic": topic, "query": q, "items": items})
                except Exception as e:
                    self._send_json({"ok": False, "error": str(e), "items": []}, status=502)
                return

            if path.startswith("/api/pdf/"):
                rel = urllib.parse.unquote(path[len("/api/pdf/"):])
                target = os.path.realpath(os.path.join(HEART_LAB_DIR, rel))
                allowed_root = os.path.realpath(os.path.join(HEART_LAB_DIR, "논문"))
                if not target.startswith(allowed_root + os.sep) or not os.path.isfile(target):
                    self._send_json({"error": "PDF not found"}, status=404)
                    return
                ctype, _ = mimetypes.guess_type(target)
                with open(target, "rb") as f:
                    raw = f.read()
                self.send_response(200)
                self.send_header("Content-Type", ctype or "application/pdf")
                self.send_header("Content-Length", str(len(raw)))
                self.end_headers()
                self.wfile.write(raw)
                return

            self._send_json({"error": "Not found"}, status=404)

        def do_POST(self):
            ctrl.touch()
            parsed = urllib.parse.urlparse(self.path)
            path = parsed.path

            if path == "/api/state":
                try:
                    body = self._read_json()
                    saved = save_state(body)
                    self._send_json({"ok": True, "state": saved, "server": ctrl.status_dict()})
                except Exception as e:
                    self._send_json({"ok": False, "error": str(e)}, status=400)
                return

            if path == "/api/quiz-complete":
                try:
                    body = self._read_json()
                    st = load_state()
                    if "state" in body and isinstance(body["state"], dict):
                        st.update(body["state"])
                    today = datetime.now().strftime("%Y-%m-%d")
                    st.setdefault("dailyCompleted", {})[today] = {
                        "score": body.get("score", 0),
                        "total": body.get("total", 5),
                        "completedAt": datetime.now().isoformat(timespec="seconds"),
                    }
                    save_state(st)
                    auto_scheduled = False
                    if ctrl.auto_shutdown_after_quiz:
                        delay = int(body.get("delaySec", 20))
                        ctrl.schedule_shutdown(delay, "daily_quiz_completed")
                        auto_scheduled = True
                    self._send_json({
                        "ok": True,
                        "autoShutdownScheduled": auto_scheduled,
                        "server": ctrl.status_dict(),
                        "state": st,
                    })
                except Exception as e:
                    self._send_json({"ok": False, "error": str(e)}, status=400)
                return

            if path == "/api/cancel-shutdown":
                ctrl.cancel_shutdown()
                self._send_json({"ok": True, "server": ctrl.status_dict()})
                return

            if path == "/api/shutdown":
                ctrl.schedule_shutdown(1, "user_requested")
                self._send_json({"ok": True, "message": "서버를 종료합니다.", "server": ctrl.status_dict()})
                return

            if path == "/api/rebuild":
                try:
                    ctrl.kb_data = kb_builder.build()
                    self._send_json({"ok": True, "paperCount": ctrl.kb_data["paperCount"], "quizCount": ctrl.kb_data["quizCount"]})
                except Exception as e:
                    self._send_json({"ok": False, "error": str(e)}, status=500)
                return

            if path == "/api/rag":
                body = self._read_json()
                query = body.get("query", "")
                top_k = int(body.get("topK", 6))
                hits = bm25_search(query, ctrl.kb_data["papers"], top_k=top_k)
                self._send_json({"ok": True, "hits": hits})
                return

            if path == "/api/llm":
                try:
                    body = self._read_json()
                    provider = body.get("provider", "gemini")
                    api_key = body.get("apiKey", "").strip()
                    model = body.get("model", "").strip()
                    ollama_url = body.get("ollamaUrl", "http://localhost:11434").strip()
                    mode = body.get("mode", "qa")

                    papers = ctrl.kb_data["papers"]
                    state = load_state()

                    if mode == "qa":
                        question = body.get("question", "").strip()
                        hits = bm25_search(question, papers, top_k=7)
                        ctx = "\n\n".join(
                            f"[{p['short']} ({p['year']}, {p['category']})]\n"
                            f"요약: {p['tldr']}\n"
                            f"핵심: {'; '.join(p['mechanisms'])}\n"
                            f"차이: {p['diff']}\n"
                            f"한계: {p['limits']}"
                            for p in hits
                        )
                        sys_p = "너는 Heart-Lab 로봇·VLA 연구자의 논문 복습 파트너다. 제공된 63편 기록 노트 RAG 컨텍스트를 최우선 근거로 삼아 한국어로 간결하고 정확하게 답하라. 논문 간 차이는 표나 불릿으로 또렷하게 대비하라."
                        usr_p = f"[RAG 검색된 내 논문 노트]\n{ctx}\n\n[질문]\n{question}"
                        expect_json = False
                        sources = [p["short"] for p in hits]

                    elif mode == "generate_quiz":
                        focus = body.get("focus", "").strip()
                        count = min(max(1, int(body.get("count", 5))), 8)
                        hits = bm25_search(focus, papers, top_k=8) if focus else papers[:12]
                        # Prioritize weak or due papers when no focus
                        if not focus:
                            sm2 = state.get("sm2", {})
                            ranked = sorted(
                                papers,
                                key=lambda p: (
                                    sm2.get(p["id"], {}).get("wrong", 0) * -10,
                                    sm2.get(p["id"], {}).get("reps", 0),
                                ),
                            )
                            hits = ranked[:10]
                        ctx = "\n".join(
                            f"- {p['id']} | {p['short']} ({p['year']}, {p['category']}): {p['tldr']} | 차이: {p['diff']}"
                            for p in hits
                        )
                        sys_p = (
                            "너는 로봇·VLA·딥러닝 논문 복습 퀴즈 출제자다. 반드시 JSON 배열만 출력하라. "
                            "각 원소는 {question, options(4개 문자열), answer(0~3 정수), explanation, papers(논문 id 배열), category, scope('single' 또는 'link')} 필드를 가진다. "
                            "출제 비중은 반드시 '모델 자체의 아키텍처·손실함수·동작 메커니즘·한계'를 묻는 단일 모델 문제(scope='single') 70%, "
                            "'두 논문 이상의 비교·연결·계보'를 묻는 연결 문제(scope='link') 30%로 구성하라. 단순 연도 암기는 금지하고 한국어로 출제하라."
                        )
                        usr_p = f"아래 내 읽은 논문 노트에서 {count}개의 새로운 객관식 퀴즈를 만들어라.\n{ctx}"
                        expect_json = True
                        sources = [p["short"] for p in hits]

                    elif mode == "recommend_thinking":
                        interest_note = body.get("interest", "VLA 시각 교란 강건성, 접촉력(SURP/CRIA), Flow Matching, 경량화").strip()
                        # Fetch fresh arXiv candidates live!
                        live_arxiv = []
                        for t in ("vla", "robustness", "world_model"):
                            try:
                                live_arxiv.extend(fetch_arxiv(topic=t, max_results=4))
                            except Exception:
                                pass
                        dom_summary = ", ".join(f"{d['domain']}:{d['count']}편" for d in ctrl.kb_data["domainStats"])
                        read_list = ", ".join(f"{p['short']}({p['year']},{p['category']})" for p in papers)
                        arxiv_ctx = "\n".join(
                            f"- [{a['published']}] {a['title']} ({a['url']}): {a['summary'][:220]}"
                            for a in live_arxiv[:10]
                        )
                        sys_p = (
                            "너는 최상위 로봇·AI 연구 멘토다. 사용자의 읽은 논문 63편 프로필, 도메인 분포, 최신 arXiv 논문을 종합 추론하여 "
                            "반드시 JSON 객체로만 답하라. 형식: "
                            '{"gap":[{"title","year","domain","reason","connects_to"}], '
                            '"interest":[{"title","year","domain","url","reason","connects_to"}], '
                            '"bridge":[{"title","year","paperA","paperB","reason"}]}. '
                            "각 배열에 3~4편씩, 이미 읽은 논문 목록에 없는 논문만 추천하라. "
                            "gap은 편수가 적은 취약 도메인 보강, interest는 관심 분야 + 최신 arXiv 심화, bridge는 사용자가 이미 읽은 두 논문 사이의 개념적 징검다리 논문을 깊이 사고해 선정하라."
                        )
                        usr_p = (
                            f"[도메인 분포]\n{dom_summary}\n\n"
                            f"[이미 읽은 63편]\n{read_list}\n\n"
                            f"[사용자 관심사]\n{interest_note}\n\n"
                            f"[오늘 실시간 arXiv 최신 논문 후보]\n{arxiv_ctx}"
                        )
                        expect_json = True
                        sources = [f"arXiv 최신 {len(live_arxiv)}편 + 내 63편 도메인 분포"]
                    else:
                        self._send_json({"ok": False, "error": f"Unknown mode: {mode}"}, status=400)
                        return

                    if provider == "gemini":
                        if not api_key:
                            self._send_json({"ok": False, "error": "Gemini API 키를 설정에 입력해 주세요."}, status=400)
                            return
                        raw_text = call_gemini(api_key, model, sys_p, usr_p, expect_json=expect_json)
                    elif provider == "ollama":
                        raw_text = call_ollama(ollama_url, model, sys_p, usr_p, expect_json=expect_json)
                    else:
                        self._send_json({"ok": False, "error": f"Unknown provider: {provider}"}, status=400)
                        return

                    parsed_out = raw_text
                    if expect_json:
                        cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw_text.strip(), flags=re.S)
                        parsed_out = json.loads(cleaned)

                    self._send_json({"ok": True, "mode": mode, "result": parsed_out, "sources": sources})
                except urllib.error.HTTPError as he:
                    err_body = he.read().decode("utf-8", errors="ignore")[:300]
                    self._send_json({"ok": False, "error": f"LLM HTTP {he.code}: {err_body}"}, status=502)
                except Exception as e:
                    self._send_json({"ok": False, "error": str(e)}, status=500)
                return

            self._send_json({"error": "Not found"}, status=404)

    return Handler


def main():
    parser = argparse.ArgumentParser(description="Heart-Lab Paper KB Server")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--auto-shutdown", action="store_true", help="Auto-shutdown after daily quiz completion")
    parser.add_argument("--idle-minutes", type=int, default=90, help="Safety idle timeout in minutes (0 disables)")
    parser.add_argument("--no-rebuild", action="store_true")
    args = parser.parse_args()

    if not args.no_rebuild:
        kb_builder.build()

    ctrl = ServerController(
        port=args.port,
        auto_shutdown_after_quiz=args.auto_shutdown,
        idle_minutes=args.idle_minutes,
    )

    ThreadingHTTPServer.allow_reuse_address = True
    httpd = ThreadingHTTPServer(("0.0.0.0", args.port), make_handler(ctrl))
    ctrl.httpd = httpd

    with open(PID_PATH, "w", encoding="utf-8") as f:
        f.write(str(os.getpid()))

    def handle_sig(signum, frame):
        threading.Thread(target=httpd.shutdown, daemon=True).start()

    signal.signal(signal.SIGTERM, handle_sig)
    signal.signal(signal.SIGINT, handle_sig)

    wd = threading.Thread(target=ctrl.watchdog_loop, daemon=True)
    wd.start()

    st = ctrl.status_dict()
    print("============================================================")
    print("  Heart-Lab 논문 지식베이스 서버 실행 중")
    print(f"  Mac       : {st['localUrl']}")
    if st["lanUrl"]:
        print(f"  Phone WiFi: {st['lanUrl']}")
    if st["tailscaleUrl"]:
        print(f"  Tailscale : {st['tailscaleUrl']}")
    print(f"  자동 종료 : {'퀴즈 완료 후 자동 종료 ON' if args.auto_shutdown else '수동 종료 모드'} (유휴 {args.idle_minutes}분 안전망)")
    print("============================================================", flush=True)

    try:
        httpd.serve_forever()
    finally:
        httpd.server_close()
        if os.path.exists(PID_PATH):
            try:
                os.remove(PID_PATH)
            except OSError:
                pass
        print("Server stopped cleanly.", flush=True)


if __name__ == "__main__":
    main()
