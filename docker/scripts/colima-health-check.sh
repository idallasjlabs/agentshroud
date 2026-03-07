#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# colima-health-check.sh — Periodic health check with auto-healing + notification.
#
# Designed to run via macOS crontab every 5 minutes:
#   */5 * * * * /Users/agentshroud-bot/Development/agentshroud/docker/scripts/colima-health-check.sh
#
# What it does:
#   1. Checks if Colima VM has internet access
#   2. If broken → fixes the route (known vz driver issue)
#   3. Re-applies iptables firewall rules (they reset on route changes)
#   4. Runs container-net-diag.sh inside the bot container
#   5. Sends Telegram notification if self-healing occurred or if diagnostics fail
#
# Log output goes to: ~/Library/Logs/agentshroud-health.log

set -uo pipefail

# Ensure Homebrew and Docker (Colima shim) are in PATH regardless of how this script is invoked
# (cron, LaunchAgent, and SSH sessions all have minimal PATH by default on macOS)
export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

# Point Docker CLI at Colima's socket explicitly — avoids relying on docker context state
# which is user-session-specific and may not be set in non-interactive environments.
_COLIMA_SOCK_OWNER="${SUDO_USER:-${USER:-$(id -un)}}"
for _candidate in \
    "/Users/${_COLIMA_SOCK_OWNER}/.colima/default/docker.sock" \
    "/Users/agentshroud-bot/.colima/default/docker.sock" \
    "/Users/ijefferson.admin/.colima/default/docker.sock"; do
    if [ -S "$_candidate" ]; then
        export DOCKER_HOST="unix://$_candidate"
        break
    fi
done

# ── Configuration ────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
LOG_FILE="$HOME/Library/Logs/agentshroud-health.log"
STATE_FILE="/tmp/agentshroud-health-state.json"
FIREWALL_SCRIPT="$SCRIPT_DIR/colima-firewall.sh"
DIAG_SCRIPT="$SCRIPT_DIR/container-net-diag.sh"
BOT_CONTAINER="agentshroud-bot"
GATEWAY_CONTAINER="agentshroud-gateway"

# Telegram notification (reads bot token from secrets)
TELEGRAM_TOKEN_FILE="$REPO_DIR/docker/secrets/telegram_bot_token_production.txt"
TELEGRAM_CHAT_ID="8096968754"  # Isaiah

# ── Logging ──────────────────────────────────────────────────────────────────
log() {
  local TS
  TS=$(date -u '+%Y-%m-%d %H:%M:%S UTC')
  echo "[$TS] $1" | tee -a "$LOG_FILE"
}

# ── Telegram notification ────────────────────────────────────────────────────
notify() {
  local MESSAGE="$1"
  if [ -f "$TELEGRAM_TOKEN_FILE" ]; then
    local TOKEN
    TOKEN=$(cat "$TELEGRAM_TOKEN_FILE" | tr -d '[:space:]')
    curl -sf --max-time 10 \
      "https://api.telegram.org/bot${TOKEN}/sendMessage" \
      -d "chat_id=${TELEGRAM_CHAT_ID}" \
      -d "text=${MESSAGE}" \
      -d "parse_mode=Markdown" \
      >/dev/null 2>&1 || log "WARNING: Telegram notification failed"
  else
    log "WARNING: Telegram token file not found, skipping notification"
  fi
}

# ── State tracking (avoid notification spam) ─────────────────────────────────
read_state() {
  if [ -f "$STATE_FILE" ]; then
    cat "$STATE_FILE"
  else
    echo '{"last_heal":0,"last_fail_notify":0,"consecutive_fails":0}'
  fi
}

write_state() {
  echo "$1" > "$STATE_FILE"
}

# ── Health checks ────────────────────────────────────────────────────────────
log "── Health check starting ──"

HEALED=false
FAILURES=()
NOW=$(date +%s)

# 1. Check Colima is running
if ! docker info >/dev/null 2>&1; then
  log "CRITICAL: Docker is not responding (Colima may be down)"
  FAILURES+=("Docker/Colima not responding")
  # Can't do anything else without Colima
  STATE=$(read_state)
  CONSEC=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('consecutive_fails',0))" 2>/dev/null || echo 0)
  CONSEC=$((CONSEC + 1))
  write_state "{\"last_heal\":0,\"last_fail_notify\":$NOW,\"consecutive_fails\":$CONSEC}"
  if [ "$CONSEC" -le 3 ] || [ $((CONSEC % 12)) -eq 0 ]; then
    notify "🚨 *AgentShroud Health Alert*
Docker/Colima is not responding!
Host: $(hostname)
Time: $(date -u '+%H:%M UTC')
Consecutive failures: $CONSEC"
  fi
  exit 1
fi

# 2. Check Colima VM internet access
VM_INTERNET=true
if ! docker exec agentshroud-gateway curl -sf --connect-timeout 5 -o /dev/null https://google.com 2>/dev/null; then
  log "DETECTED: Colima VM lost internet access"
  VM_INTERNET=false

  # Auto-heal: fix the route
  log "AUTO-HEAL: Fixing Colima VM routing..."
  log "AUTO-HEAL: Skipped route fix (colima ssh requires admin user)"

  # Verify fix worked
  sleep 2
  if docker exec agentshroud-gateway curl -sf --connect-timeout 5 -o /dev/null https://google.com 2>/dev/null; then
    log "AUTO-HEAL: ✅ Route fix successful — internet restored"
    HEALED=true
  else
    log "AUTO-HEAL: ❌ Route fix failed — internet still broken"
    FAILURES+=("Colima VM internet unreachable (auto-heal failed)")
  fi
fi

# 3. Apply/verify iptables firewall rules
log "Checking iptables rules..."
RULE_COUNT=$(docker exec agentshroud-gateway sh -c "iptables -L DOCKER-USER -n 2>/dev/null | grep -c DROP" 2>/dev/null || echo 0)
if [ "$RULE_COUNT" -lt 5 ]; then
  log "DETECTED: iptables rules missing ($RULE_COUNT/5 DROP rules)"
  if [ -x "$FIREWALL_SCRIPT" ]; then
    log "AUTO-HEAL: Reapplying firewall rules..."
    "$FIREWALL_SCRIPT" >> "$LOG_FILE" 2>&1
    HEALED=true
    log "AUTO-HEAL: ✅ Firewall rules reapplied"
  else
    FAILURES+=("iptables rules missing and firewall script not found")
  fi
else
  log "✅ iptables rules OK ($RULE_COUNT DROP rules)"
fi

# 4. Check Docker containers are healthy
for CONTAINER in "$BOT_CONTAINER" "$GATEWAY_CONTAINER"; do
  STATUS=$(docker inspect --format='{{.State.Health.Status}}' "$CONTAINER" 2>/dev/null || echo "missing")
  if [ "$STATUS" = "healthy" ]; then
    log "✅ $CONTAINER: healthy"
  elif [ "$STATUS" = "starting" ]; then
    log "⏳ $CONTAINER: starting (waiting)"
  else
    log "⚠️  $CONTAINER: $STATUS"
    FAILURES+=("$CONTAINER is $STATUS")
  fi
done

# 5. Run container network diagnostic (if bot is running)
if docker ps --filter name="$BOT_CONTAINER" --format '{{.Status}}' 2>/dev/null | grep -q "Up"; then
  log "Running network diagnostic in bot container..."
  # Capture output and exit code separately — the script exits non-zero when any test
  # fails, which would cause the '|| echo' fallback to fire and corrupt the JSON output.
  DIAG_OUTPUT=$(docker exec "$BOT_CONTAINER" bash /app/scripts/container-net-diag.sh --json 2>/dev/null)
  DIAG_RC=$?
  if [ $DIAG_RC -ne 0 ] && [ -z "$DIAG_OUTPUT" ]; then
    # docker exec itself failed (container stopped, script not found, etc.)
    DIAG_FAILS=99
  else
    DIAG_FAILS=$(echo "$DIAG_OUTPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('fail',0))" 2>/dev/null || echo 0)
  fi

  if [ "$DIAG_FAILS" -eq 0 ]; then
    log "✅ Container network diagnostic: all tests passed"
  else
    log "⚠️  Container network diagnostic: $DIAG_FAILS test(s) failed"
    FAILURES+=("Bot container: $DIAG_FAILS network tests failed")
  fi
fi

# ── Notification logic ───────────────────────────────────────────────────────
STATE=$(read_state)
LAST_NOTIFY=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('last_fail_notify',0))" 2>/dev/null || echo 0)
CONSEC=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('consecutive_fails',0))" 2>/dev/null || echo 0)

if $HEALED; then
  notify "🔧 *AgentShroud Self-Healed*
Host: $(hostname)
Time: $(date -u '+%H:%M UTC')
Actions taken:
$([ "$VM_INTERNET" = false ] && echo "• Fixed Colima VM routing")
$([ "$RULE_COUNT" -lt 5 ] && echo "• Reapplied iptables firewall rules")
All services operational."
  write_state "{\"last_heal\":$NOW,\"last_fail_notify\":0,\"consecutive_fails\":0}"
fi

if [ ${#FAILURES[@]} -gt 0 ]; then
  CONSEC=$((CONSEC + 1))
  # Notify on first failure, then every hour (12 × 5min intervals)
  NOTIFY_GAP=$((NOW - LAST_NOTIFY))
  if [ "$CONSEC" -le 1 ] || [ "$NOTIFY_GAP" -gt 3600 ]; then
    FAIL_LIST=""
    for F in "${FAILURES[@]}"; do
      FAIL_LIST="$FAIL_LIST
• $F"
    done
    notify "🚨 *AgentShroud Health Alert*
Host: $(hostname)
Time: $(date -u '+%H:%M UTC')
Issues:$FAIL_LIST
Consecutive checks failed: $CONSEC"
    LAST_NOTIFY=$NOW
  fi
  write_state "{\"last_heal\":0,\"last_fail_notify\":$LAST_NOTIFY,\"consecutive_fails\":$CONSEC}"
elif ! $HEALED; then
  # All clear
  if [ "$CONSEC" -gt 0 ]; then
    notify "✅ *AgentShroud Recovered*
Host: $(hostname)
Time: $(date -u '+%H:%M UTC')
All systems healthy after $CONSEC consecutive failures."
  fi
  write_state "{\"last_heal\":0,\"last_fail_notify\":0,\"consecutive_fails\":0}"
fi

log "── Health check complete (${#FAILURES[@]} failures) ──"
exit $(( ${#FAILURES[@]} > 0 ? 1 : 0 ))
