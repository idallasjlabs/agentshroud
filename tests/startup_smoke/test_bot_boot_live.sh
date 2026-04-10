#!/usr/bin/env bash
# tests/startup_smoke/test_bot_boot_live.sh
#
# Live boot test: performs a full asb rebuild + asb up and inspects logs.
# Requires a working Colima VM with Docker and valid secrets.
#
# Gated by: SMOKE_LIVE=1 (skip by default — only run on self-hosted marvin runner)
#
# Usage:
#   SMOKE_LIVE=1 bash tests/startup_smoke/test_bot_boot_live.sh
#   SMOKE_LIVE=1 SMOKE_WAIT_SECS=180 bash ...   # override wait timeout
#
# Exit 0 = all assertions pass. Exit 1 = failure.

set -euo pipefail

if [[ "${SMOKE_LIVE:-0}" != "1" ]]; then
    echo "SKIP: test_bot_boot_live.sh — set SMOKE_LIVE=1 to run (requires Colima + valid secrets)"
    exit 0
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/../.." && pwd)"
WAIT_SECS="${SMOKE_WAIT_SECS:-120}"

pass=0
fail=0

check() {
    local name="$1" condition="$2" detail="${3:-}"
    if [[ "$condition" == "true" ]]; then
        echo "  PASS: $name"
        (( pass++ )) || true
    else
        echo "  FAIL: $name${detail:+ ($detail)}"
        (( fail++ )) || true
    fi
}

echo ""
echo "=== test_bot_boot_live.sh (SMOKE_LIVE=1) ==="
echo ""

# ── Rebuild + bring up ────────────────────────────────────────────────────
echo "  Rebuilding and starting stack (this takes a few minutes)..."
AGENTSHROUD_SKIP_POST_DEPLOY_CHECK=1 bash "$REPO/scripts/asb" rebuild 2>&1 | tail -20

# ── Wait for containers to start ─────────────────────────────────────────
echo "  Waiting up to ${WAIT_SECS}s for gateway to become healthy..."
deadline=$(( $(date +%s) + WAIT_SECS ))
gateway_healthy=false
while [[ $(date +%s) -lt $deadline ]]; do
    if curl -sf http://localhost:8080/status > /dev/null 2>&1; then
        gateway_healthy=true
        break
    fi
    sleep 3
done
check "L1: gateway /status returns 200 within ${WAIT_SECS}s" \
    "$([[ "$gateway_healthy" == "true" ]] && echo true || echo false)"

# ── Inspect bot logs ─────────────────────────────────────────────────────
bot_logs=$(docker logs agentshroud-bot 2>&1 || true)

check "L2: bot logs contain no RangeError (V8 stack overflow)" \
    "$([[ "$bot_logs" != *"RangeError: Maximum call stack size exceeded"* ]] && echo true || echo false)"

check "L3: bot logs contain no 'invalid_auth' (Slack token guard)" \
    "$([[ "$bot_logs" != *"invalid_auth"* ]] && echo true || echo false)"

check "L4: bot logs contain no 'Failed to start CLI'" \
    "$([[ "$bot_logs" != *"Failed to start CLI"* ]] && echo true || echo false)"

check "L5: bot logs contain no 'Pool overlaps' (subnet conflict)" \
    "$([[ "$bot_logs" != *"Pool overlaps"* ]] && echo true || echo false)"

check "L6: bot logs contain Telegram startup notification sent" \
    "$([[ "$bot_logs" == *"Sent Telegram startup notification"* ]] && echo true || echo false)"

# ── Gateway logs ─────────────────────────────────────────────────────────
gw_logs=$(docker logs agentshroud-gateway 2>&1 || true)

check "L7: gateway logs show getUpdates polling (Telegram connected)" \
    "$([[ "$gw_logs" == *"getUpdates"* ]] && echo true || echo false)"

check "L8: gateway logs contain no unhandled exception" \
    "$([[ "$gw_logs" != *"Traceback (most recent call last)"* ]] && echo true || echo false)"

# ── Verify apply-patches.js ran and set apiRoot ───────────────────────────
check "L9: bot logs show apiRoot was set by init-patch" \
    "$([[ "$bot_logs" == *"Set channels.telegram.apiRoot"* ]] && echo true || echo false)"

# ── Summary ───────────────────────────────────────────────────────────────
echo ""
total=$(( pass + fail ))
echo "${total} assertions: ${pass} passed, ${fail} failed"
echo ""

[[ "$fail" -eq 0 ]]
