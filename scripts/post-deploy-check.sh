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
#   bash scripts/post-deploy-check.sh --functional
#   Called automatically by: scripts/asb up | scripts/asb rebuild
#
# --functional adds F1-F4 (below): every service of the full stack must be
# running and healthy, and answer a real request. The Sunday wrapper's restore
# ladder (scripts/lib/sunday-scan.sh sunday_restore_stack) gates on it.

set -euo pipefail

FUNCTIONAL=0
for _arg in "$@"; do
    case "$_arg" in
        --functional) FUNCTIONAL=1 ;;
        *) echo "  [post-deploy-check] unknown argument: $_arg" >&2; exit 2 ;;
    esac
done

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
# 600s (was 300s): no-cache rebuilds on 2026-10-17/18 took 5 min (dev) and
# 7m03s (prod) from container start to "http server listening" -- config
# bootstrap plus `openclaw doctor --fix` -- and 300s failed both healthy deploys.
BOT_WAIT_SECS="${AGENTSHROUD_POST_DEPLOY_BOT_WAIT:-600}"

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
    HERMES_CONTAINER=$(docker ps --format '{{.Names}}' 2>/dev/null | grep -E '^agentshroud-(dev-)?hermes' | head -1)
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

    # Probed from INSIDE the container, for the same reason the :9119 check
    # above is: hermes binds its API to 127.0.0.1 in the container, and none of
    # its ports are published to the host (NetworkSettings.Ports is null for
    # 8642/9119/9120 — it runs on agentshroud-isolated). A host-side
    # `curl localhost:8642` therefore cannot succeed no matter how healthy the
    # API is, and on 2026-09-25 it reported "Hermes API :8642 reachable" as
    # FAILED while the container's OWN healthcheck — curl -fsS
    # http://127.0.0.1:8642/health, the identical URL — had it marked healthy.
    #
    # /health is the assertion. /v1/models is deliberately NOT a fallback: it
    # answers 401 without credentials, so `curl -sf` fails on a perfectly
    # working server and would only ever mask the real signal.
    hermes_api_ok=false
    if [[ -n "$HERMES_CONTAINER" ]] && \
       docker exec "$HERMES_CONTAINER" curl -sf --max-time 5 \
           "http://127.0.0.1:8642/health" > /dev/null 2>&1; then
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
# The gateway is found by its compose service label, like the OpenClaw lookup
# above: matching the literal agentshroud-gateway meant P5 never ran on dev
# (agentshroud-dev-gateway).
COMPOSE_FILE="${AGENTSHROUD_COMPOSE_FILE:-docker/docker-compose.yml}"
GATEWAY_CONTAINER=$(docker ps --filter 'label=com.docker.compose.service=gateway' --format '{{.Names}}' 2>/dev/null | head -1)
if [[ -f "$COMPOSE_FILE" ]] && [[ -n "$GATEWAY_CONTAINER" ]]; then
    # Pipe the host's compose file into the gateway container; validator runs
    # there because that's where the gateway package + deps are already installed.
    net_report=$(docker exec -i "$GATEWAY_CONTAINER" python3 -c '
import json, sys, tempfile
from gateway.security.network_validator import validate_network_security
with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False) as f:
    f.write(sys.stdin.read())
    tmp = f.name
report = validate_network_security(tmp).get_security_report()
print(json.dumps(report))
' < "$COMPOSE_FILE" 2>/dev/null || echo '{}')

    # A validator that never ran must not read as "0 critical": exec failing
    # falls back to {} above, which has no by_severity at all.
    check "Network validator ran in $GATEWAY_CONTAINER" \
        "$([[ "$net_report" == *'"by_severity"'* ]] && echo true || echo false)" \
        "no report (docker exec or the validator failed)"

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
else
    echo "  [post-deploy-check] SKIP: P5 network validator (no gateway container or no $COMPOSE_FILE)"
fi

# ── P6: Sandbox image present ─────────────────────────────────────────────
# Real functional check, not a boot-time smoke test: every check above passes
# on a container that booted fine but whose sandboxed cron jobs will fail the
# moment they actually run, because OpenClaw does not build
# openclaw-sandbox:bookworm-slim itself and does not silently substitute a
# plain debian image when it's missing (fails fast with "Sandbox image not
# found" instead). asb up/rebuild now calls _ensure_sandbox_image before this
# script runs, so this should always pass — it exists as a second, independent
# assertion in case someone runs docker-compose directly and skips asb.
if [[ -n "$BOT_CONTAINER" ]]; then
    sandbox_image_ok=false
    if docker image inspect openclaw-sandbox:bookworm-slim >/dev/null 2>&1; then
        sandbox_image_ok=true
    fi
    check "Sandbox image openclaw-sandbox:bookworm-slim present" \
        "$([[ "$sandbox_image_ok" == "true" ]] && echo true || echo false)" \
        "run: bash scripts/asb up  (auto-builds it), or scripts/asb's _ensure_sandbox_image directly"
fi

# ── P7: Configured local model actually registered in models.json ────────
# Real functional check: a container whose configured AGENTSHROUD_LOCAL_MODEL_REF
# (e.g. openai-local/nemotron-3.5-lightning-rapid) has no matching
# providers.<key>.models[] entry in OpenClaw's own models.json boots green and
# passes every check above, then fails the FIRST TIME any job actually calls
# that model with "Unknown model: <ref>" -- this is exactly the class of bug
# that shipped to prod on 2026-09-18 (models.json registration was hardcoded
# to providers.ollama regardless of the ref's actual provider prefix).
if [[ -n "$BOT_CONTAINER" ]]; then
    _local_ref=$(docker exec "$BOT_CONTAINER" sh -c 'printf "%s" "${AGENTSHROUD_LOCAL_MODEL_REF:-}"' 2>/dev/null || echo "")
    if [[ -n "$_local_ref" && "$_local_ref" == */* ]]; then
        _provider_key="${_local_ref%%/*}"
        _model_id="${_local_ref#*/}"
        model_registered=$(docker exec "$BOT_CONTAINER" sh -c '
            node -e "
              const fs = require(\"fs\");
              try {
                const cfg = JSON.parse(fs.readFileSync(\"/home/node/.openclaw/models.json\", \"utf8\"));
                const models = (cfg.providers && cfg.providers[\"'"${_provider_key}"'\"] && cfg.providers[\"'"${_provider_key}"'\"].models) || [];
                const found = models.some(m => (typeof m === \"string\" ? m : m.id) === \"'"${_model_id}"'\");
                process.stdout.write(found ? \"true\" : \"false\");
              } catch (e) {
                process.stdout.write(\"false\");
              }
            "
        ' 2>/dev/null || echo "false")
        check "Configured local model ${_local_ref} registered in models.json" \
            "$([[ "$model_registered" == "true" ]] && echo true || echo false)" \
            "providers.${_provider_key}.models[] has no entry for ${_model_id}"
    fi
fi

# ── F1-F4: functional checks (--functional only) ─────────────────────────
# The P-checks above prove the stack booted. These prove it works: the Sunday
# restore after a cut-off or failed upgrade must not call a stack "up" because
# containers exist. Each service answers a real request over the same path its
# traffic takes. Only stack-internal paths are tested: an external outage (a
# model server, Telegram) must not roll back a healthy upgrade.
if [[ "$FUNCTIONAL" == "1" ]]; then
    FUNC_WAIT_SECS="${AGENTSHROUD_FUNCTIONAL_WAIT:-180}"
    _svc_container() {
        docker ps --filter "label=com.docker.compose.service=$1" --format '{{.Names}}' 2>/dev/null | head -1
    }
    GW_CONTAINER=$(_svc_container gateway)

    # F1: the full default stack (`asb up full`) is running, and every one of
    # its containers that declares a healthcheck reports healthy. The compose
    # healthchecks are real probes (gateway /status, wazuh-agent
    # status='connected', wazuh-manager's four daemons, ...), not pgrep.
    # One deadline shared by all six, not one each: the Sunday restore runs this
    # up to three times before 08:00, so its worst case has to stay bounded.
    deadline=$(( $(date +%s) + FUNC_WAIT_SECS ))
    for _svc in gateway openclaw wazuh-manager wazuh-agent docker-socket-proxy voice-gateway; do
        _c=$(_svc_container "$_svc")
        if [[ -z "$_c" ]]; then
            check "F1: $_svc running" false "no container with com.docker.compose.service=$_svc"
            continue
        fi
        _health=""
        while :; do
            _health=$(docker inspect --format '{{if .State.Health}}{{.State.Health.Status}}{{else}}none{{end}}' "$_c" 2>/dev/null || echo "gone")
            [[ "$_health" == "healthy" || "$_health" == "none" ]] && break
            [[ $(date +%s) -ge $deadline ]] && break
            sleep 5
        done
        check "F1: $_svc ($_c) healthy" \
            "$([[ "$_health" == "healthy" || "$_health" == "none" ]] && echo true || echo false)" \
            "health=$_health within the ${FUNC_WAIT_SECS}s window"
    done
    check "F1: hermes running" \
        "$([[ -n "$HERMES_CONTAINER" ]] && echo true || echo false)" \
        "no container labelled com.agentshroud.role=hermes"

    # F2: each agent reaches the gateway over the internal network — the path
    # every model, Telegram and tool call of theirs goes through. Three tries:
    # on 2026-10-19 both agents failed this request once during a restore drill
    # (not reproducible; the gateway logged nothing), and one blip must not
    # escalate the Sunday restore to a rollback.
    for _c in "$BOT_CONTAINER" "$HERMES_CONTAINER"; do
        [[ -n "$_c" ]] || continue
        for _try in 1 2 3; do
            _code=$(docker exec "$_c" curl -s -o /dev/null -w '%{http_code}' --max-time 10 http://gateway:8080/status 2>/dev/null || true)
            [[ "$_code" == "200" ]] && break
            [[ "$_try" -lt 3 ]] && sleep 5
        done
        _code="${_code:-000}"
        check "F2: $_c -> gateway:8080/status 200" \
            "$([[ "$_code" == "200" ]] && echo true || echo false)" "http=$_code"
    done

    # F3: the gateway's resident clamd answers. Without it every scan falls
    # back to clamscan and a second ~1 GB signature DB (the 2026-10-17 OOMs).
    if [[ -n "$GW_CONTAINER" ]]; then
        _pong=$(docker exec "$GW_CONTAINER" clamdscan --ping 1 2>/dev/null || true)
        check "F3: gateway clamd answers PING" \
            "$([[ "$_pong" == *PONG* ]] && echo true || echo false)" "got='${_pong}'"
    fi

    # F4: OpenClaw's own clamd answers on its socket (no clamdscan in that
    # image, so speak the clamd protocol directly).
    if [[ -n "$BOT_CONTAINER" ]]; then
        _pong=$(docker exec "$BOT_CONTAINER" node -e '
          const s = require("net").createConnection("/tmp/clamd.ctl", () => s.write("zPING\0"));
          s.on("data", d => { process.stdout.write(d.toString()); s.end(); });
          s.on("error", () => process.exit(1));
          s.setTimeout(5000, () => process.exit(2));' 2>/dev/null || true)
        check "F4: openclaw clamd answers PING" \
            "$([[ "$_pong" == *PONG* ]] && echo true || echo false)" "got='${_pong}'"
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
    echo "    docker logs ${GATEWAY_CONTAINER:-agentshroud-gateway} 2>&1 | tail -50" >&2
    echo "    docker logs ${BOT_CONTAINER:-agentshroud-openclaw} 2>&1 | tail -50" >&2
    echo "    docker logs ${HERMES_CONTAINER:-agentshroud-hermes-v2} 2>&1 | tail -50" >&2
    echo "    asb status" >&2
    echo ""
    exit 1
fi

echo ""
echo "  [post-deploy-check] Stack is healthy."
echo ""
