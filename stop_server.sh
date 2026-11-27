#!/bin/zsh
# 스크립트가 있는 폴더를 기준으로 삼습니다. 다른 위치를 쓰려면 KB_DIR 환경변수로 덮어쓰세요.
KB_DIR="${KB_DIR:-${0:A:h}}"
curl -s -X POST http://127.0.0.1:8765/api/shutdown >/dev/null 2>&1 || true
if [ -f "$KB_DIR/.server.pid" ]; then
  kill "$(cat "$KB_DIR/.server.pid")" 2>/dev/null || true
  rm -f "$KB_DIR/.server.pid"
fi
echo "Heart-Lab 논문 지식베이스 서버를 종료했습니다."
