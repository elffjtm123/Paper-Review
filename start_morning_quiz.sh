#!/bin/zsh
# 매일 오전 8:00 launchd가 실행하는 아침 논문 퀴즈 서버 기동 스크립트
set -e
# 스크립트가 있는 폴더를 기준으로 삼습니다. 다른 위치를 쓰려면 KB_DIR 환경변수로 덮어쓰세요.
KB_DIR="${KB_DIR:-${0:A:h}}"
PORT=8765
LOG_FILE="$KB_DIR/.morning_server.log"

cd "$KB_DIR"

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
PY3="/opt/homebrew/bin/python3"
[ -x "$PY3" ] || PY3="/usr/bin/python3"

# 이미 서버가 떠 있으면 중복 실행하지 않고 알림만 표시
if lsof -iTCP:$PORT -sTCP:LISTEN >/dev/null 2>&1; then
  echo "[$(date)] Port $PORT already listening." >> "$LOG_FILE"
else
  nohup "$PY3" "$KB_DIR/server.py" --port $PORT --auto-shutdown --idle-minutes 90 </dev/null >> "$LOG_FILE" 2>&1 &
  disown 2>/dev/null || true
  sleep 1.5
fi

LAN_IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo "127.0.0.1")
TS_BIN=$(command -v tailscale 2>/dev/null || echo /usr/local/bin/tailscale)
TS_IP=$("$TS_BIN" ip -4 2>/dev/null | head -n 1 || echo "")

MSG="Mac: http://127.0.0.1:$PORT | 폰(Wi-Fi): http://$LAN_IP:$PORT"
if [ -n "$TS_IP" ]; then
  MSG="$MSG | 외부(Tailscale): http://$TS_IP:$PORT"
fi

/usr/bin/osascript -e "display notification \"$MSG\" with title \"Heart-Lab 아침 논문 퀴즈 (5문제)\" subtitle \"퀴즈 완료 시 서버가 자동 종료됩니다\"" || true
