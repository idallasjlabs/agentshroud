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
# 300s (was 120s): the deploy's device-reset step restarts the bot moments
# before this check runs, so the bot must complete a FULL cold init (SDK
# patches, DNS warmup, readiness gate, then the Telegram notification this
# check greps for) inside the window. Observed normal boots on 2026-08-27
# took ~2.5-3 min — the 120s window false-negatived 4 separate healthy
# deploys that same day (container demonstrably healthy moments later).
BOT_WAIT_SECS="${AGENTSHROUD_POST_DEPLOY_BOT_WAIT:-300}"

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

# Resolve the OpenClaw bot container's real name. container_name is set
# literally per compose file (docker/docker-compose.yml: agentshroud-openclaw
# for prod; docker/docker-compose.agentshroud-bot.marvin.yml: agentshroud-
# marvin-openclaw for the agentshroud-bot dev account), so it can't be derived
# from $USER/$PROJECT alone — but compose always stamps the service label
# com.docker.compose.service=openclaw regardless of container_name/account, so
# match on that instead of a hardcoded literal name.
BOT_CONTAINER=$(docker ps --filter 'label=com.docker.compose.service=openclaw' --format '{{.Names}}' 2>/dev/null | head -1)

bot_logs=""
if [[ -n "$BOT_CONTAINER" ]]; then
    # Allow bot to finish startup within BOT_WAIT_SECS
    started=false
    deadline=$(( $(date +%s) + BOT_WAIT_SECS ))
    while [[ $(date +%s) -lt $deadline ]]; do
        # Docker's own healthcheck is the authoritative started signal —
        # accept it directly instead of only grepping for log markers (the
        # marker approach alone false-negatived healthy deploys whenever the
        # notification step lagged the health probe, 2026-08-27 x4).
        bot_health=$(docker inspect --format '{{if .State.Health}}{{.State.Health.Status}}{{end}}' "$BOT_CONTAINER" 2>/dev/null || echo "")
        if [[ "$bot_health" == "healthy" ]]; then
            started=true
            bot_logs=$(docker logs "$BOT_CONTAINER" 2>&1 || echo "")
            break
        fi
        bot_logs=$(docker logs "$BOT_CONTAINER" 2>&1 || echo "")
        # "Startup notification suppressed" = startup reached the notification step but
        # the anti-spam cooldown (recent restart) skipped the Telegram send — still a
        # successful start, the marker just never appears in that window.
        # "startup photo notification" = the photo path in start-agentshroud.sh, which
        # replaces the plain-text marker when a startup photo is configured.
        if [[ "$bot_logs" == *"Telegram startup notification"* || "$bot_logs" == *"Telegram startup photo notification"* || "$bot_logs" == *"Listening for"* || "$bot_logs" == *"Bot is running"* || "$bot_logs" == *"Startup notification suppressed"* ]]; then
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

# ── P3: Hermes health checks (only when hermes container is running) ─────────
# Hermes deploys via `docker run` (docker/bots/hermes/run-standalone.sh), not
# docker-compose (see that script's header comment for why), so it has no
# com.docker.compose.service label to key off like the OpenClaw bot lookup
# above. run-standalone.sh instead tags the container with its own
# com.agentshroud.role=hermes label — match on that. Fall back to the literal
# default name for containers started before that label existed (older
# `docker run`, no redeploy since); container_name itself is NOT
# account-dependent for Hermes (unlike OpenClaw's compose override), since
# run-standalone.sh hardcodes the same name regardless of $USER/account.
HERMES_CONTAINER=$(docker ps --filter 'label=com.agentshroud.role=hermes' --format '{{.Names}}' 2>/dev/null | head -1)
if [[ -z "$HERMES_CONTAINER" ]]; then
    HERMES_CONTAINER=$(docker ps --format '{{.Names}}' 2>/dev/null | grep '^agentshroud-hermes' | head -1)
fi

if [[ -n "$HERMES_CONTAINER" ]]; then
    # Hermes dashboard binds to 127.0.0.1:9119 inside the container (loopback-only).
    # Docker's published port (127.0.0.1:9119:9119) cannot forward to the container's
    # loopback, so we check from inside the container via docker exec instead.
    hermes_dash_ok=false
    deadline=$(( $(date +%s) + WAIT_SECS ))
    while [[ $(date +%s) -lt $deadline ]]; do
        if docker exec "$HERMES_CONTAINER" curl -sf --max-time 5 "http://127.0.0.1:9119/" > /dev/null 2>&1; then
            hermes_dash_ok=true
            break
        fi
        sleep 3
    done
    check "Hermes dashboard :9119 returns 200 within ${WAIT_SECS}s" \
        "$([[ "$hermes_dash_ok" == "true" ]] && echo true || echo false)"

    hermes_api_ok=false
    if curl -sf "http://localhost:8642/health" > /dev/null 2>&1 || \
       curl -sf "http://localhost:8642/v1/models" > /dev/null 2>&1; then
        hermes_api_ok=true
    fi
    check "Hermes API :8642 reachable" \
        "$([[ "$hermes_api_ok" == "true" ]] && echo true || echo false)"

    # Scope to logs since the CURRENT boot's start, first 80 lines — i.e.
    # actual startup output. The previous `tail -50` grabbed the most recent
    # lines at whatever time the check ran, so any recent cron-job runtime
    # traceback (e.g. a temporarily-down local-model backend) failed a
    # "startup" check hours after a perfectly clean startup (observed
    # 2026-08-27 running this script standalone against a healthy stack).
    hermes_started_at=$(docker inspect -f '{{.State.StartedAt}}' "$HERMES_CONTAINER" 2>/dev/null || echo "")
    if [[ -n "$hermes_started_at" ]]; then
        hermes_logs=$(docker logs --since "$hermes_started_at" "$HERMES_CONTAINER" 2>&1 | head -80 || echo "")
    else
        hermes_logs=$(docker logs "$HERMES_CONTAINER" 2>&1 | head -80 || echo "")
    fi
    check "Hermes logs: no crash on startup" \
        "$([[ "$hermes_logs" != *"Traceback (most recent call last)"* ]] && echo true || echo false)"
else
    echo "  [post-deploy-check] SKIP: hermes container not running (use 'asb up full' for full stack)"
fi

# ── P4: No subnet overlap in Docker networks ─────────────────────────────
network_output=$(docker network ls 2>/dev/null || echo "")
pool_error=$(docker network inspect agentshroud-internal 2>&1 || true)
check "No 'Pool overlaps' error in Docker network state" \
    "$([[ "$pool_error" != *"Pool overlaps"* ]] && echo true || echo false)"

# ── P5: Static compose-file network self-check ───────────────────────────
# Validates docker/docker-compose.yml against NetworkValidator's rules
# (isolated networks, exposed ports, privileged, etc.). Fails only on
# `critical` findings — high/medium are surfaced as INFO.
COMPOSE_FILE="${AGENTSHROUD_COMPOSE_FILE:-docker/docker-compose.yml}"
if [[ -f "$COMPOSE_FILE" ]] && command -v docker >/dev/null 2>&1 \
   && docker ps --format '{{.Names}}' 2>/dev/null | grep -q '^agentshroud-gateway$'; then
    # Pipe the host's compose file into the gateway container; validator runs
    # there because that's where the gateway package + deps are already installed.
    net_report=$(docker exec -i agentshroud-gateway python3 -c '
import json, sys, tempfile
from gateway.security.network_validator import validate_network_security
with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False) as f:
    f.write(sys.stdin.read())
    tmp = f.name
report = validate_network_security(tmp).get_security_report()
print(json.dumps(report))
' < "$COMPOSE_FILE" 2>/dev/null || echo '{}')

    critical_count=$(printf '%s' "$net_report" | python3 -c \
        'import json,sys; d=json.loads(sys.stdin.read() or "{}"); print(d.get("by_severity",{}).get("critical",0))' 2>/dev/null || echo "0")
    check "Network validator: 0 critical findings in $COMPOSE_FILE" \
        "$([[ "$critical_count" == "0" ]] && echo true || echo false)" \
        "saw $critical_count critical"

    high_count=$(printf '%s' "$net_report" | python3 -c \
        'import json,sys; d=json.loads(sys.stdin.read() or "{}"); print(d.get("by_severity",{}).get("high",0))' 2>/dev/null || echo "0")
    medium_count=$(printf '%s' "$net_report" | python3 -c \
        'import json,sys; d=json.loads(sys.stdin.read() or "{}"); print(d.get("by_severity",{}).get("medium",0))' 2>/dev/null || echo "0")
    if [[ "$high_count" != "0" || "$medium_count" != "0" ]]; then
        echo "  [post-deploy-check] INFO: network validator: high=$high_count medium=$medium_count (non-fatal)"
    fi
fi

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
    echo "    docker logs ${BOT_CONTAINER:-agentshroud-openclaw} 2>&1 | tail -50" >&2
    echo "    docker logs ${HERMES_CONTAINER:-agentshroud-hermes-v2} 2>&1 | tail -50" >&2
    echo "    asb status" >&2
    echo ""
    exit 1
fi

echo ""
echo "  [post-deploy-check] Stack is healthy."
echo ""
