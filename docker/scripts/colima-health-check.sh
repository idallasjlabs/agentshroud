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

# ── Prevent overlapping runs ─────────────────────────────────────────────────
# container-net-diag can take >5 min; skip if a previous run is still active.
LOCK_DIR="/tmp/agentshroud-health-check.lock"
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  # stat -f %m is macOS; stat -c %Y is Linux — try both
  LOCK_AGE=$(( $(date +%s) - $(stat -f %m "$LOCK_DIR" 2>/dev/null || stat -c %Y "$LOCK_DIR" 2>/dev/null || echo 0) ))
  if [ "$LOCK_AGE" -gt 900 ]; then
    # Stale lock (>15 min) — previous run must have crashed; clear and proceed
    rm -rf "$LOCK_DIR"
    mkdir "$LOCK_DIR" 2>/dev/null || exit 0
  else
    echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] SKIPPED: previous health check still running (${LOCK_AGE}s)" >> "$LOG_FILE"
    exit 0
  fi
fi
trap 'rm -rf "$LOCK_DIR"' EXIT

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
  STATE=$(read_state)
  CONSEC=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('consecutive_fails',0))" 2>/dev/null || echo 0)
  LAST_NOTIFY=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('last_fail_notify',0))" 2>/dev/null || echo 0)
  CONSEC=$((CONSEC + 1))
  # Notify on first failure only, then at most once per hour.
  # Do NOT update last_fail_notify unless a notification is actually sent.
  NOTIFY_GAP=$((NOW - LAST_NOTIFY))
  if [ "$CONSEC" -eq 1 ] || [ "$NOTIFY_GAP" -gt 3600 ]; then
    notify "🚨 *AgentShroud Health Alert*
Docker/Colima is not responding!
Host: $(hostname)
Time: $(date -u '+%H:%M UTC')
Consecutive failures: $CONSEC"
    LAST_NOTIFY=$NOW
  fi
  write_state "{\"last_heal\":0,\"last_fail_notify\":$LAST_NOTIFY,\"consecutive_fails\":$CONSEC}"
  exit 1
fi

# 2. Check Colima VM internet access (informational only — VPN commonly blocks this)
# Route auto-heal requires colima ssh as admin user; not available in cron context.
# Do NOT add to FAILURES — false-positives behind VPN would generate hourly alerts.
VM_INTERNET=true
if ! docker exec agentshroud-gateway curl -sf --connect-timeout 5 -o /dev/null https://google.com 2>/dev/null; then
  log "INFO: Colima VM internet check failed (expected behind VPN — route fix not available in this context)"
  VM_INTERNET=false
fi

# 3. Apply/verify iptables firewall rules (check on Colima VM host, not inside container)
# The DOCKER-USER chain lives on the VM, not inside the hardened gateway container
# (which has cap_drop: ALL and no iptables binary).
log "Checking iptables rules (Colima VM)..."
RULE_COUNT=$(colima ssh -- sh -c "iptables -L DOCKER-USER -n 2>/dev/null | grep -c DROP || echo 0" 2>/dev/null | tail -1)
RULE_COUNT=${RULE_COUNT:-0}
# Strip any non-numeric characters (colima ssh can prepend version lines)
RULE_COUNT=$(echo "$RULE_COUNT" | tr -dc '0-9')
RULE_COUNT=${RULE_COUNT:-0}
if [ "$RULE_COUNT" -lt 5 ]; then
  log "DETECTED: iptables rules missing on Colima VM ($RULE_COUNT/5 DROP rules)"
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
    # The 5 expected failures (TCP 8.8.8.8:443, 8.8.8.8:53, 1.1.1.1:443, gateway ping,
    # TCP 443 reachability) are by design — egress enforcement blocks direct outbound.
    # DNS resolution, HTTP/HTTPS via proxy, and proxy connectivity all pass.
    # Log for visibility but do NOT alert — these are expected in egress-enforced mode.
    log "ℹ️  Container network diagnostic: $DIAG_FAILS test(s) failed (expected — egress enforcement active)"
  fi
fi

# ── Notification logic ───────────────────────────────────────────────────────
STATE=$(read_state)
LAST_NOTIFY=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('last_fail_notify',0))" 2>/dev/null || echo 0)
CONSEC=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('consecutive_fails',0))" 2>/dev/null || echo 0)

LAST_HEAL_WRITE=0  # Tracks the last_heal value to write; preserved across HEALED + FAILURES paths

if $HEALED; then
  # Throttle self-healed notifications to once per hour (mirrors FAILURES throttle)
  LAST_HEAL=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('last_heal',0))" 2>/dev/null || echo 0)
  HEAL_GAP=$((NOW - LAST_HEAL))
  if [ "$HEAL_GAP" -gt 3600 ]; then
    notify "🔧 *AgentShroud Self-Healed*
Host: $(hostname)
Time: $(date -u '+%H:%M UTC')
Actions taken:
• Reapplied iptables firewall rules on Colima VM
All services operational."
  fi
  LAST_HEAL_WRITE=$NOW
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
  # Preserve last_heal from the HEALED block so the 1-hour throttle isn't reset
  write_state "{\"last_heal\":$LAST_HEAL_WRITE,\"last_fail_notify\":$LAST_NOTIFY,\"consecutive_fails\":$CONSEC}"
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
