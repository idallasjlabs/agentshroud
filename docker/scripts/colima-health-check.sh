#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# colima-health-check.sh — Periodic health check with auto-healing + notification.
#
# Designed to run via macOS crontab every 5 minutes:
#   */5 * * * * /Users/agentshroud-bot/Development/agentshroud/docker/scripts/colima-health-check.sh
#
# What it does:
#   0. Starts the Colima VM if it is stopped (the LaunchAgent cannot: see 1a)
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
# Wrapped in a function because the socket does not exist while the VM is down:
# the auto-start in step 1a must re-resolve it after `colima start` creates it.
resolve_docker_host() {
    local _owner="${SUDO_USER:-${USER:-$(id -un)}}"
    local _candidate
    for _candidate in \
        "/Users/${_owner}/.colima/default/docker.sock" \
        "/Users/agentshroud-bot/.colima/default/docker.sock" \
        "/Users/ijefferson.admin/.colima/default/docker.sock"; do
        if [ -S "$_candidate" ]; then
            export DOCKER_HOST="unix://$_candidate"
            return 0
        fi
    done
    return 1
}
resolve_docker_host || true

# ── Configuration ────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
LOG_FILE="$HOME/Library/Logs/agentshroud-health.log"
STATE_FILE="/tmp/agentshroud-health-state.json"
FIREWALL_SCRIPT="$SCRIPT_DIR/colima-firewall.sh"
DIAG_SCRIPT="$SCRIPT_DIR/container-net-diag.sh"
# Container names are env-overridable (matches gateway/security/daily_cve_report.py's
# AGENTSHROUD_GATEWAY_CONTAINER convention, commit 154262fc6) — the literal
# defaults here were wrong for this host for an unknown period: this account's
# compose override (docker/docker-compose.agentshroud-bot.marvin.yml) names
# them agentshroud-dev-openclaw / agentshroud-dev-gateway (renamed from the
# agentshroud-marvin-* scheme 2026-09-18 for dev/prod distinguishability), not
# the unprefixed names below, so every check against these was silently
# checking containers that don't exist on this host.
BOT_CONTAINER="${AGENTSHROUD_OPENCLAW_CONTAINER:-agentshroud-dev-openclaw}"
GATEWAY_CONTAINER="${AGENTSHROUD_GATEWAY_CONTAINER:-agentshroud-dev-gateway}"

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
    echo '{"consecutive_fails":0,"heal_count":0,"fail_count":0,"docker_down_count":0,"last_daily_summary":0}'
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

  # 1a. Auto-start a stopped Colima VM.
  #
  # This cron path is the only autostart that actually works on this host.
  # ~/Library/LaunchAgents/com.agentshroud.colima-autostart.plist cannot
  # cover it: a RunAtLoad LaunchAgent is bootstrapped into the Aqua domain at
  # GUI login, and this account never gets one — the console belongs to
  # ijefferson.admin and all dev work arrives over SSH (`launchctl
  # managername` reports "Background"). That plist also writes to
  # /tmp/colima-autostart.{log,err}, which admin's identically-named agent
  # creates first as ijefferson.admin:wheel 0644, so launchd could not spawn
  # this account's copy even from a GUI session. Verified live 2026-09-19:
  # the VM sat down ~20 min while this very check logged CRITICAL every 5
  # min and healed nothing.
  #
  # Gated on the account name for the same defense-in-depth reason as the
  # renice block in 1b — never boot a VM on the production account.
  COLIMA_STARTED=false
  if [ "$(whoami)" = "agentshroud-bot" ] && ! colima status >/dev/null 2>&1; then
    log "AUTO-HEAL: Colima VM is stopped — starting (typically 60-90s)..."
    # Flags mirror the LaunchAgent's so a VM created here matches the intended
    # dev shape; they are a no-op against an existing VM. timeout(1) is
    # coreutils (Homebrew, resolvable via the PATH set at the top of this
    # script) and bounds a hung start so it cannot hold the run lock for the
    # full 15-min stale-lock window.
    if timeout 300 colima start --cpu 8 --memory 10 --disk 120 --network-address >> "$LOG_FILE" 2>&1; then
      resolve_docker_host || true
      if docker info >/dev/null 2>&1; then
        COLIMA_STARTED=true
        HEALED=true
        log "AUTO-HEAL: ✅ Colima VM started — Docker is responding"
      else
        log "AUTO-HEAL: ❌ colima start reported success but Docker is still unreachable"
      fi
    else
      log "AUTO-HEAL: ❌ colima start failed or exceeded the 300s timeout"
    fi
  fi

  # 1a-bis. VM is UP but Docker is unreachable — repair the socket forward.
  #
  # Distinct failure from a stopped VM, and the common one on this host: it
  # happened four separate times on 2026-09-21 alone. lima establishes the
  # /var/run/docker.sock forward exactly once, at VM start. When the ssh
  # connection carrying that forward drops, lima re-establishes a mux for
  # `colima ssh` but never restores the socket forward — so `colima ssh` keeps
  # working (and `colima status` cheerfully reports "running") while every
  # docker call fails with "Cannot connect" or a bare EOF. Nothing self-heals
  # it; the forward stays dead until the VM is restarted.
  #
  # Verified 2026-09-21: dockerd active inside the VM with all 7 containers
  # healthy and 5.9GB free, while the host could not reach either socket path.
  # The hostagent log showed the forward set up once at 08:01:59 and no error
  # afterwards — it does not know it lost anything.
  #
  # `colima restart` is the only reliable repair, and it does bounce the
  # containers. That cost is worth paying: at this point docker is ALREADY
  # unusable, so the alternative is not "uptime", it is "an unattended run that
  # fails on its first docker call for a reason nothing in its log explains".
  # Gated on the dev account, as with the start above.
  if ! $COLIMA_STARTED && [ "$(whoami)" = "agentshroud-bot" ] \
     && colima status >/dev/null 2>&1; then
    log "DETECTED: Colima VM is running but Docker is unreachable — socket forward is dead."
    log "AUTO-HEAL: restarting Colima to re-establish the docker.sock forward..."
    if timeout 420 colima restart >> "$LOG_FILE" 2>&1; then
      resolve_docker_host || true
      if docker info >/dev/null 2>&1; then
        COLIMA_STARTED=true
        HEALED=true
        log "AUTO-HEAL: ✅ socket forward restored — Docker is responding"
      else
        log "AUTO-HEAL: ❌ colima restart completed but Docker is still unreachable"
      fi
    else
      log "AUTO-HEAL: ❌ colima restart failed or exceeded the 420s timeout"
    fi
  fi

  # When the VM came back, fall through to the remaining checks rather than
  # exiting: a freshly booted VM has no DOCKER-USER rules, so step 3's
  # firewall reapply matters most on exactly this path.
  if ! $COLIMA_STARTED; then
  STATE=$(read_state)
  CONSEC=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('consecutive_fails',0))" 2>/dev/null || echo 0)
  HEAL_COUNT=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('heal_count',0))" 2>/dev/null || echo 0)
  FAIL_COUNT=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('fail_count',0))" 2>/dev/null || echo 0)
  DOCKER_DOWN_COUNT=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('docker_down_count',0))" 2>/dev/null || echo 0)
  LAST_DAILY=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('last_daily_summary',0))" 2>/dev/null || echo 0)
  CONSEC=$((CONSEC + 1))
  DOCKER_DOWN_COUNT=$((DOCKER_DOWN_COUNT + 1))
  # Send daily summary if >24h since last one
  DAILY_GAP=$((NOW - LAST_DAILY))
  if [ "$DAILY_GAP" -gt 86400 ]; then
    CURRENT_STATUS="Docker/Colima down"
    notify "📊 *AgentShroud Daily Summary*
Host: $(hostname)
Time: $(date -u '+%H:%M UTC')
• Auto-heals: $HEAL_COUNT
• Failure events: $FAIL_COUNT
• Docker-down events: $DOCKER_DOWN_COUNT
• Status: $CURRENT_STATUS"
    LAST_DAILY=$NOW
    HEAL_COUNT=0; FAIL_COUNT=0; DOCKER_DOWN_COUNT=0
  fi
  write_state "{\"consecutive_fails\":$CONSEC,\"heal_count\":$HEAL_COUNT,\"fail_count\":$FAIL_COUNT,\"docker_down_count\":$DOCKER_DOWN_COUNT,\"last_daily_summary\":$LAST_DAILY}"
  exit 1
  fi
fi

# 1b. Enforce dev-VM CPU niceness. Self-heals every run (this script already
# runs every 5 min) instead of hooking colima's actual start — there's no
# single reliable "colima start" event to catch (no LaunchAgent, manual or
# cron-restarted), but a stale/wrong nice value gets corrected within 5 min
# either way. Owner directive 2026-08-26: this account's Colima VM must not
# compete at equal priority with the interactive/production account on the
# same physical host (marvin) until dev moves to its own hardware. +10 is a
# moderate deprioritization, not a starve — the VM still gets real CPU share
# whenever the host isn't contended, it only loses out to default-priority
# (nice 0) work when both sides are genuinely busy at once. Gated on account
# name as defense-in-depth even though this script is currently only
# cron-invoked on this account (confirmed 2026-08-26: prod/ijefferson.admin
# has no cron job calling it) — if that ever changes, this must not fire on
# the production account.
DEV_VM_NICE_TARGET=10
if [ "$(whoami)" = "agentshroud-bot" ]; then
  DEV_VM_PID=$(pgrep -u "$(whoami)" -f "Virtualization.framework.*VirtualMachine" 2>/dev/null | head -1)
  if [ -n "$DEV_VM_PID" ]; then
    CURRENT_NICE=$(ps -o nice= -p "$DEV_VM_PID" 2>/dev/null | tr -d ' ')
    if [ -n "$CURRENT_NICE" ] && [ "$CURRENT_NICE" != "$DEV_VM_NICE_TARGET" ]; then
      if renice "$DEV_VM_NICE_TARGET" -p "$DEV_VM_PID" >/dev/null 2>&1; then
        log "AUTO-HEAL: Colima VM (pid $DEV_VM_PID) reniced $CURRENT_NICE -> $DEV_VM_NICE_TARGET"
        HEALED=true
      else
        log "WARNING: renice of Colima VM (pid $DEV_VM_PID) to $DEV_VM_NICE_TARGET failed"
      fi
    fi
  else
    log "WARNING: could not find this account's Colima VM process to renice"
  fi
fi

# 2. Check Colima VM internet access and self-heal a missing default route.
# Colima's DHCP client reliably assigns eth0 an address but does not always
# install a default route (observed repeatedly 2026-09-04 through
# 2026-09-07, including on a freshly recreated VM — `ip route` has zero
# `default via` entries while a host-scope route to the DHCP-assigned
# gateway is present). `colima ssh` uses key-based auth into the VM, where
# sudo is passwordless for this user — contrary to the comment this line
# used to carry, this IS fixable from cron context, not VPN-gated.
#
# The two `docker exec` probes below use $GATEWAY_CONTAINER, not a literal
# name. They hardcoded `agentshroud-gateway` until 2026-09-19 — a container
# that does not exist on this host (it is agentshroud-dev-gateway) — so this
# entire check failed 100% of the time and logged an auto-heal failure on
# every 5-min run. Same class of bug the container-name block above already
# documents for commit 154262fc6; step 2 was simply missed by that fix.
VM_INTERNET=true
if ! docker exec "$GATEWAY_CONTAINER" curl -sf --connect-timeout 5 -o /dev/null https://google.com 2>/dev/null; then
  log "DETECTED: Colima VM internet check failed"
  HAS_DEFAULT=$(colima ssh -- sh -c "ip route show default" 2>/dev/null | tr -dc '[:print:]')
  if [ -z "$HAS_DEFAULT" ]; then
    GATEWAY=$(colima ssh -- sh -c "ip route | awk '/proto dhcp/ {print \$1; exit}'" 2>/dev/null | tr -dc '0-9.')
    IFACE=$(colima ssh -- sh -c "ip route | awk '/proto dhcp/ {print \$3; exit}'" 2>/dev/null | tr -dc '[:alnum:]')
    if [ -n "$GATEWAY" ] && [ -n "$IFACE" ]; then
      log "AUTO-HEAL: no default route on Colima VM — adding default via $GATEWAY dev $IFACE"
      colima ssh -- sudo ip route add default via "$GATEWAY" dev "$IFACE" >> "$LOG_FILE" 2>&1
    else
      log "WARNING: Colima VM has no default route and no DHCP gateway could be determined — cannot auto-heal"
    fi
  fi
  if docker exec "$GATEWAY_CONTAINER" curl -sf --connect-timeout 5 -o /dev/null https://google.com 2>/dev/null; then
    HEALED=true
    VM_INTERNET=true
    log "AUTO-HEAL: ✅ Colima VM internet access restored"
  else
    VM_INTERNET=false
    FAILURES+=("Colima VM has no internet access (auto-heal attempted)")
    log "AUTO-HEAL: ❌ Colima VM internet access still failing after default-route check"
  fi
fi

# 3. Apply/verify iptables firewall rules (check on Colima VM host, not inside container)
# The DOCKER-USER chain lives on the VM, not inside the hardened gateway container
# (which has cap_drop: ALL and no iptables binary).
#
# Both counts below run under sudo. Without it iptables exits with
# "Could not fetch rule set generation id: Permission denied (you must be
# root)" and the 2>/dev/null + `grep -c` swallows it into a literal 0 — so
# the rules read as missing even when all 5 DROPs are present and correct.
# That made step 3 reapply the firewall every 5 minutes and then report
# "did NOT restore rules (0/5)" immediately after the firewall script
# printed the 5 healthy rules it had just confirmed. Verified 2026-09-19:
# same command returns 0 without sudo and 5 with it. The 2026-08-30 recheck
# below was added to stop inflated heal counts but inherited the same
# missing sudo, so it never actually verified anything.
log "Checking iptables rules (Colima VM)..."
RULE_COUNT=$(colima ssh -- sudo sh -c "iptables -L DOCKER-USER -n 2>/dev/null | grep -c DROP || echo 0" 2>/dev/null | tail -1)
RULE_COUNT=${RULE_COUNT:-0}
# Strip any non-numeric characters (colima ssh can prepend version lines)
RULE_COUNT=$(echo "$RULE_COUNT" | tr -dc '0-9')
RULE_COUNT=${RULE_COUNT:-0}
if [ "$RULE_COUNT" -lt 5 ]; then
  log "DETECTED: iptables rules missing on Colima VM ($RULE_COUNT/5 DROP rules)"
  if [ -x "$FIREWALL_SCRIPT" ]; then
    log "AUTO-HEAL: Reapplying firewall rules..."
    "$FIREWALL_SCRIPT" >> "$LOG_FILE" 2>&1
    # Verify the reapply actually restored the rules before claiming a heal.
    # Setting HEALED=true unconditionally counted a "heal" on every 5-min
    # run even when the reapply silently did nothing in cron context —
    # inflating the daily summary to ~265 heals+failures/day (2026-08-30)
    # while masking that the rules were never actually coming back.
    RECHECK_COUNT=$(colima ssh -- sudo sh -c "iptables -L DOCKER-USER -n 2>/dev/null | grep -c DROP || echo 0" 2>/dev/null | tail -1)
    RECHECK_COUNT=$(echo "${RECHECK_COUNT:-0}" | tr -dc '0-9')
    RECHECK_COUNT=${RECHECK_COUNT:-0}
    if [ "$RECHECK_COUNT" -ge 5 ]; then
      HEALED=true
      log "AUTO-HEAL: ✅ Firewall rules reapplied and verified ($RECHECK_COUNT DROP rules)"
    else
      FAILURES+=("iptables reapply did not restore rules ($RECHECK_COUNT/5 after reapply)")
      log "AUTO-HEAL: ❌ Firewall reapply did NOT restore rules ($RECHECK_COUNT/5)"
    fi
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

  # Expected-failure baseline, re-derived live 2026-09-20 (8, was documented
  # as 5). Every one is a direct consequence of egress enforcement: the
  # container has no route off-box and reaches everything through
  # HTTP(S)_PROXY=gateway:8181, which does its own name resolution.
  #   1-2. DNS port           8.8.8.8:53 / 1.1.1.1:53 unreachable
  #   3.   DNS resolution     google.com unresolvable — Docker's embedded
  #        resolver (127.0.0.11) cannot reach its upstreams (1.1.1.1 /
  #        8.8.8.8 / 192.168.64.1). Internal names still resolve
  #        (gateway -> 172.21.0.8), which is all this container needs. The
  #        comment here asserted through 2026-09-20 that DNS resolution
  #        passes — it does not, and does not need to.
  #   4.   Gateway ping       skipped, no gateway to test
  #   5-7. TCP 8.8.8.8:443 / 8.8.8.8:53 / 1.1.1.1:443 closed/blocked
  #   8.   TCP 443 reachability  ENETUNREACH
  # Corroborated by the checks that DO pass: "Direct blocked" (direct HTTPS
  # fails without the proxy — enforcement working as designed), TCP proxy
  # gateway:8181 open, HTTP 405 and HTTPS 404 through the proxy.
  #
  # The count is compared, not just logged. This branch previously reported
  # ANY number of failures as "expected", so a genuinely new failure was
  # absorbed silently — the fake-green pattern CLAUDE.md section 2 prohibits.
  # DIAG_FAILS is also set to 99 when `docker exec` itself fails, which this
  # comparison now surfaces instead of swallowing. Override the baseline via
  # AGENTSHROUD_DIAG_EXPECTED_FAILS when the topology legitimately changes.
  DIAG_EXPECTED_FAILS="${AGENTSHROUD_DIAG_EXPECTED_FAILS:-8}"
  if [ "$DIAG_FAILS" -eq 0 ]; then
    log "✅ Container network diagnostic: all tests passed"
  elif [ "$DIAG_FAILS" -le "$DIAG_EXPECTED_FAILS" ]; then
    log "ℹ️  Container network diagnostic: $DIAG_FAILS/$DIAG_EXPECTED_FAILS expected failure(s) (egress enforcement active)"
  else
    FAILURES+=("container net diag: $DIAG_FAILS failures exceeds expected baseline of $DIAG_EXPECTED_FAILS")
    log "⚠️  Container network diagnostic: $DIAG_FAILS failures exceeds the expected baseline of $DIAG_EXPECTED_FAILS — investigate"
  fi
fi

# ── Daily summary notification logic ─────────────────────────────────────────
STATE=$(read_state)
CONSEC=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('consecutive_fails',0))" 2>/dev/null || echo 0)
HEAL_COUNT=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('heal_count',0))" 2>/dev/null || echo 0)
FAIL_COUNT=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('fail_count',0))" 2>/dev/null || echo 0)
DOCKER_DOWN_COUNT=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('docker_down_count',0))" 2>/dev/null || echo 0)
LAST_DAILY=$(echo "$STATE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('last_daily_summary',0))" 2>/dev/null || echo 0)

# Accumulate event counts — no per-event alerts
if $HEALED; then
  HEAL_COUNT=$((HEAL_COUNT + 1))
fi

if [ ${#FAILURES[@]} -gt 0 ]; then
  CONSEC=$((CONSEC + 1))
  FAIL_COUNT=$((FAIL_COUNT + 1))
else
  CONSEC=0
fi

# Send at most one summary per 24 hours
DAILY_GAP=$((NOW - LAST_DAILY))
if [ "$DAILY_GAP" -gt 86400 ]; then
  if [ ${#FAILURES[@]} -gt 0 ]; then
    CURRENT_STATUS="degraded (${#FAILURES[@]} issue(s))"
  else
    CURRENT_STATUS="healthy"
  fi
  notify "📊 *AgentShroud Daily Summary*
Host: $(hostname)
Time: $(date -u '+%H:%M UTC')
• Auto-heals: $HEAL_COUNT
• Failure events: $FAIL_COUNT
• Docker-down events: $DOCKER_DOWN_COUNT
• Status: $CURRENT_STATUS"
  LAST_DAILY=$NOW
  HEAL_COUNT=0; FAIL_COUNT=0; DOCKER_DOWN_COUNT=0
fi

write_state "{\"consecutive_fails\":$CONSEC,\"heal_count\":$HEAL_COUNT,\"fail_count\":$FAIL_COUNT,\"docker_down_count\":$DOCKER_DOWN_COUNT,\"last_daily_summary\":$LAST_DAILY}"

log "── Health check complete (${#FAILURES[@]} failures) ──"
exit $(( ${#FAILURES[@]} > 0 ? 1 : 0 ))
