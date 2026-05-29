#!/command/with-contenv sh
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# AgentShroud startup wrapper for Hermes Agent.
#
# Architecture note: This runs as the s6-overlay "main program" (CMD).
# main-wrapper.sh detects it as an executable and runs:
#   exec s6-setuidgid hermes /usr/local/bin/start-hermes.sh
# The with-contenv shebang populates env from /run/s6/container_environment/
# (including secrets injected by 00-agentshroud-secrets.sh).
#
# s6-setuidgid drops uid/gid to hermes (10000) but does NOT set HOME.
# with-contenv may have HOME=/root from the container init context.
# Override explicitly so Hermes writes lock files and state to /opt/data.

set -eu

# Ensure Hermes writes runtime state to the data volume, not /root
export HOME=/opt/data
export HERMES_HOME=/opt/data
export XDG_STATE_HOME=/opt/data/.local/state
export XDG_DATA_HOME=/opt/data/.local/share
export XDG_CACHE_HOME=/opt/data/.cache

# Verify Telegram token was injected (non-fatal — gateway warns if absent)
if [ -n "${TELEGRAM_BOT_TOKEN:-}" ]; then
    echo "[hermes-startup] Telegram bot token present (${#TELEGRAM_BOT_TOKEN} chars)"
else
    echo "[hermes-startup] WARNING: TELEGRAM_BOT_TOKEN not set — Telegram channel disabled"
fi

if [ -n "${ANTHROPIC_API_KEY:-}" ]; then
    echo "[hermes-startup] Anthropic API key present"
fi

if [ -n "${API_SERVER_KEY:-}" ]; then
    echo "[hermes-startup] API server key present — OpenAI-compatible API server will be auth-gated"
else
    echo "[hermes-startup] WARNING: API_SERVER_KEY not set — API server will reject all requests"
fi


# Seed /opt/data config on first boot (idempotent)
/usr/local/bin/init-hermes-config.sh

# Telegram notification helpers — ALL traffic routes through AgentShroud gateway.
# No direct api.telegram.org calls. No hardcoded bot tokens.
_OWNER_CHAT_ID="8096968754"
_GATEWAY_TELEGRAM_BASE="${GATEWAY_OP_PROXY_URL:-http://gateway:8080}/telegram-api"

_telegram_bot_token() {
    # Token is injected into env by s6 with-contenv (from 00-agentshroud-secrets.sh).
    printf '%s' "${TELEGRAM_BOT_TOKEN:-}"
}

_telegram_send() {
    local text="$1"
    local token
    token="$(_telegram_bot_token)"
    if [ -z "$token" ]; then
        echo "[hermes-startup] ⚠ No Telegram bot token available — cannot send notification" >&2
        return 1
    fi
    # Route through AgentShroud gateway Telegram proxy (never direct to api.telegram.org).
    # X-AgentShroud-System marks this as a system notification (not LLM output) so the
    # gateway skips outbound content filtering for these admin messages.
    curl -sf --max-time 10 -X POST "${_GATEWAY_TELEGRAM_BASE}/bot${token}/sendMessage" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" \
        -d "{\"chat_id\":\"${_OWNER_CHAT_ID}\",\"text\":\"${text}\"}" \
        >/dev/null 2>&1
}

_telegram_get_me_ready() {
    local token
    token="$(_telegram_bot_token)"
    if [ -z "$token" ]; then
        return 1
    fi
    curl -sf --max-time 8 -X POST "${_GATEWAY_TELEGRAM_BASE}/bot${token}/getMe" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" \
        >/dev/null 2>&1
}

_STARTUP_NOTICE_STAMP="/tmp/.hermes-startup-notify-sent"
_STARTUP_NOTICE_COOLDOWN_SECONDS=60

# Forward TERM/INT to hermes process, send shutdown notification.
# _HERMES_PID is set after the background launch below.
trap '
    echo "[hermes-startup] Shutdown signal received"
    echo "[hermes-startup] Sending Telegram shutdown notification..."
    _telegram_send "🔴 Hermes shutting down" \
        && echo "[hermes-startup] ✓ Sent Telegram shutdown notification" \
        || echo "[hermes-startup] ⚠ Could not send Telegram shutdown notification"
    if [ -n "${_HERMES_PID:-}" ]; then
        kill "${_HERMES_PID}" 2>/dev/null || true
    fi
' TERM INT

# Wait for the gateway's /telegram-api reverse proxy to be ready before
# launching the daemon. Without this gate, a gateway restart that overlaps
# with Hermes boot causes the daemon's 30s connect window to exhaust all
# retries against a not-yet-ready gateway and give up permanently.
if [ -n "${TELEGRAM_BOT_TOKEN:-}" ]; then
    echo "[hermes-startup] Waiting for gateway Telegram proxy to be ready..."
    _i=0; _ready=0
    while [ "$_i" -lt 60 ]; do
        if curl -fsS -m 5 -o /dev/null \
             "http://gateway:8080/telegram-api/bot${TELEGRAM_BOT_TOKEN}/getMe" 2>/dev/null; then
            echo "[hermes-startup] Gateway Telegram proxy ready after ${_i}s"
            _ready=1; break
        fi
        _i=$((_i + 2)); sleep 2
    done
    [ "$_ready" -eq 1 ] || echo "[hermes-startup] WARNING: gateway Telegram proxy not ready after 60s — starting anyway (cron-only fallback)"
fi

echo "[hermes-startup] Starting Hermes Agent gateway (Telegram/Discord long-poll)..."

# Startup notification subshell — runs in background while Hermes daemon launches.
# Uses a cooldown stamp file to suppress duplicate notifications on rapid restarts.
(
    now_epoch="$(date +%s)"
    last_notice_epoch=""
    if [ -f "${_STARTUP_NOTICE_STAMP}" ]; then
        last_notice_epoch="$(cat "${_STARTUP_NOTICE_STAMP}" 2>/dev/null || true)"
    fi
    should_notify="yes"
    if [ -n "${last_notice_epoch}" ] && [ "${last_notice_epoch}" -eq "${last_notice_epoch}" ] 2>/dev/null; then
        age="$(( now_epoch - last_notice_epoch ))"
        if [ "${age}" -lt "${_STARTUP_NOTICE_COOLDOWN_SECONDS}" ]; then
            should_notify="no"
        fi
    fi
    if [ "${should_notify}" != "yes" ]; then
        echo "[hermes-startup] Startup notification suppressed (cooldown active)"
        exit 0
    fi

    printf '%s\n' "${now_epoch}" > "${_STARTUP_NOTICE_STAMP}" 2>/dev/null || true
    _telegram_send "🟡 Hermes starting" \
        && echo "[hermes-startup] ✓ Sent Telegram starting notification" \
        || echo "[hermes-startup] ⚠ Could not send Telegram starting notification"

    # Poll Telegram getMe readiness — up to 120s
    ready="no"
    for _i in $(seq 1 60); do
        if _telegram_get_me_ready; then
            ready="yes"
            break
        fi
        sleep 2
    done

    if [ "${ready}" = "yes" ]; then
        _telegram_send "🛡️ Hermes online" \
            && echo "[hermes-startup] ✓ Sent Telegram startup notification" \
            || echo "[hermes-startup] ⚠ Could not send Telegram startup notification"
    else
        _telegram_send "🟠 Hermes starting (readiness delayed)" \
            && echo "[hermes-startup] ⚠ Sent delayed startup notification" \
            || echo "[hermes-startup] ⚠ Could not send delayed startup notification"
    fi
) &

# Run Hermes in background so the TERM/INT trap above can fire on shutdown.
# (exec would replace the shell, preventing trap execution.)
hermes gateway run &
_HERMES_PID=$!
wait $_HERMES_PID
