#!/usr/bin/env bash
# scripts/post-deploy-check.sh — Post-deploy smoke gate
#
# Runs automatically after `asb up` / `asb rebuild` to verify the stack
# came up cleanly. On failure, prints the failing assertion and exits 1
# so the caller knows the deploy did NOT succeed.
#
# Skip: set AGENTSHROUD_SKIP_POST_DEPLOY_CHECK=1 (emergency bypass only).
#
# Usage:
#   bash scripts/post-deploy-check.sh
#   Called automatically by: scripts/asb up | scripts/asb rebuild

set -euo pipefail

if [[ "${AGENTSHROUD_SKIP_POST_DEPLOY_CHECK:-0}" == "1" ]]; then
    echo "  [post-deploy-check] SKIPPED (AGENTSHROUD_SKIP_POST_DEPLOY_CHECK=1)"
    exit 0
fi

# Ports + project: dev bot uses 9080, prod uses 8080
if [[ "${USER:-}" == "agentshroud-bot" ]]; then
    GW_PORT="${AGENTSHROUD_GW_PORT:-9080}"
else
    GW_PORT="${AGENTSHROUD_GW_PORT:-8080}"
fi

GW_URL="http://localhost:${GW_PORT}/status"
WAIT_SECS="${AGENTSHROUD_POST_DEPLOY_WAIT:-60}"
BOT_WAIT_SECS="${AGENTSHROUD_POST_DEPLOY_BOT_WAIT:-120}"

pass=0
fail=0
errors=()

check() {
    local name="$1" condition="$2" detail="${3:-}"
    if [[ "$condition" == "true" ]]; then
        echo "  [post-deploy-check] PASS: $name"
        (( pass++ )) || true
    else
        echo "  [post-deploy-check] FAIL: $name${detail:+ ($detail)}" >&2
        errors+=("$name")
        (( fail++ )) || true
    fi
}

echo ""
echo "  [post-deploy-check] Verifying stack health..."
echo "  [post-deploy-check] Gateway: $GW_URL"
echo ""

# ── P1: Gateway /status returns 200 ──────────────────────────────────────
deadline=$(( $(date +%s) + WAIT_SECS ))
gw_ok=false
while [[ $(date +%s) -lt $deadline ]]; do
    if curl -sf "$GW_URL" > /dev/null 2>&1; then
        gw_ok=true
        break
    fi
    sleep 2
done
check "Gateway /status 200 within ${WAIT_SECS}s" \
    "$([[ "$gw_ok" == "true" ]] && echo true || echo false)"

# ── P2: Bot logs — no fatal startup errors ───────────────────────────────
# Wait a short period for the bot to start fully
sleep 5
bot_logs=""
if docker ps --format '{{.Names}}' 2>/dev/null | grep -q 'agentshroud-bot\|agentshroud-openclaw'; then
    # Allow bot to finish startup within BOT_WAIT_SECS
    started=false
    deadline=$(( $(date +%s) + BOT_WAIT_SECS ))
    while [[ $(date +%s) -lt $deadline ]]; do
        bot_logs=$(docker logs agentshroud-bot 2>&1 || docker logs agentshroud-openclaw 2>&1 || echo "")
        if [[ "$bot_logs" == *"Telegram startup notification"* || "$bot_logs" == *"Listening for"* || "$bot_logs" == *"Bot is running"* ]]; then
            started=true
            break
        fi
        sleep 3
    done

    check "Bot container started successfully within ${BOT_WAIT_SECS}s" \
        "$([[ "$started" == "true" ]] && echo true || echo false)"

    check "Bot logs: no RangeError (V8 stack overflow)" \
        "$([[ "$bot_logs" != *"RangeError: Maximum call stack size exceeded"* ]] && echo true || echo false)"

    check "Bot logs: no 'invalid_auth' (Slack token guard working)" \
        "$([[ "$bot_logs" != *"invalid_auth"* ]] && echo true || echo false)"

    check "Bot logs: no 'Failed to start CLI'" \
        "$([[ "$bot_logs" != *"Failed to start CLI"* ]] && echo true || echo false)"
else
    echo "  [post-deploy-check] SKIP: bot container not found (non-full-stack deploy?)"
fi

# ── P3: No subnet overlap in Docker networks ─────────────────────────────
network_output=$(docker network ls 2>/dev/null || echo "")
pool_error=$(docker network inspect agentshroud-internal 2>&1 || true)
check "No 'Pool overlaps' error in Docker network state" \
    "$([[ "$pool_error" != *"Pool overlaps"* ]] && echo true || echo false)"

# ── Summary ───────────────────────────────────────────────────────────────
echo ""
total=$(( pass + fail ))
echo "  [post-deploy-check] Results: ${total} checks, ${pass} passed, ${fail} failed"

if [[ "$fail" -gt 0 ]]; then
    echo ""
    echo "  [post-deploy-check] DEPLOY FAILED. Failing assertions:" >&2
    for e in "${errors[@]}"; do
        echo "    - $e" >&2
    done
    echo ""
    echo "  Investigate with:" >&2
    echo "    docker logs agentshroud-gateway 2>&1 | tail -50" >&2
    echo "    docker logs agentshroud-bot 2>&1 | tail -50" >&2
    echo "    asb status" >&2
    echo ""
    exit 1
fi

echo ""
echo "  [post-deploy-check] Stack is healthy."
echo ""
