#!/bin/zsh
# 원할 때 언제든 수동으로 서버를 켜고 Mac 브라우저를 엽니다 (자동 종료 없음).
set -e
# 스크립트가 있는 폴더를 기준으로 삼습니다. 다른 위치를 쓰려면 KB_DIR 환경변수로 덮어쓰세요.
KB_DIR="${KB_DIR:-${0:A:h}}"
PORT=8765
cd "$KB_DIR"

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
PY3="/opt/homebrew/bin/python3"
[ -x "$PY3" ] || PY3="/usr/bin/python3"

if ! lsof -iTCP:$PORT -sTCP:LISTEN >/dev/null 2>&1; then
  nohup "$PY3" "$KB_DIR/server.py" --port $PORT --idle-minutes 180 </dev/null > "$KB_DIR/.manual_server.log" 2>&1 &
  disown 2>/dev/null || true
  sleep 1.2
fi

LAN_IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo "127.0.0.1")
TS_BIN=$(command -v tailscale 2>/dev/null || echo /usr/local/bin/tailscale)
TS_IP=$("$TS_BIN" ip -4 2>/dev/null | head -n 1 || echo "")
echo "Mac       : http://127.0.0.1:$PORT"
echo "Phone WiFi: http://$LAN_IP:$PORT"
[ -n "$TS_IP" ] && echo "Tailscale : http://$TS_IP:$PORT"
open "http://127.0.0.1:$PORT"
