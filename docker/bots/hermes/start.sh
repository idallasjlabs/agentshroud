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

# ---------------------------------------------------------------------------
# Crash backoff escalation (Item 4)
# Track every start in a rolling 10-minute window.  More than 5 restarts
# in 600 seconds → pause 5 minutes before proceeding.  This prevents runaway
# Telegram rate-limiting during asyncio crash-loops and gives the gateway's
# getUpdates long-poll lock time to expire naturally on Telegram's servers.
# ---------------------------------------------------------------------------
_HISTORY_FILE="/opt/data/.start-history"
touch "${_HISTORY_FILE}" 2>/dev/null || true

_now_epoch="$(date +%s)"
_window_start=$(( _now_epoch - 600 ))

# Append current epoch and prune entries older than 600s (atomic via temp file)
{
    printf '%s\n' "${_now_epoch}"
    while IFS= read -r _ts; do
        [ "${_ts:-0}" -gt "${_window_start}" ] 2>/dev/null && printf '%s\n' "${_ts}"
    done < "${_HISTORY_FILE}"
} > "${_HISTORY_FILE}.tmp" && mv "${_HISTORY_FILE}.tmp" "${_HISTORY_FILE}" 2>/dev/null || true

_recent_starts="$(wc -l < "${_HISTORY_FILE}" 2>/dev/null || printf '0')"

if [ "${_recent_starts}" -gt 5 ]; then
    echo "[hermes-startup] BACKOFF: ${_recent_starts} starts in last 600s — pausing 300s to avoid Telegram rate-limit"
    # Send Telegram notice before sleeping so Isaiah knows why Hermes goes quiet.
    # (Telegram helpers not yet defined here; use raw curl with the known base URL.)
    _bt="${TELEGRAM_BOT_TOKEN:-}"
    _gw="${GATEWAY_OP_PROXY_URL:-http://gateway:8080}/telegram-api"
    if [ -n "${_bt}" ]; then
        curl -sf --max-time 10 -X POST "${_gw}/bot${_bt}/sendMessage" \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
            -H "X-AgentShroud-System: 1" \
            -d "{\"chat_id\":\"8096968754\",\"text\":\"⏸ Hermes backoff: ${_recent_starts} restarts in 10min — pausing 5min to avoid Telegram rate-limit\"}" \
            >/dev/null 2>&1 || true
    fi
    sleep 300
fi

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

_telegram_send_photo() {
    local caption="$1"
    local photo_path="${2:-/app/branding/logo.png}"
    local token
    token="$(_telegram_bot_token)"
    if [ -z "$token" ] || [ ! -f "$photo_path" ]; then
        return 1
    fi
    curl -sf --max-time 15 -X POST "${_GATEWAY_TELEGRAM_BASE}/bot${token}/sendPhoto" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" \
        -F "chat_id=${_OWNER_CHAT_ID}" \
        -F "caption=${caption}" \
        -F "photo=@${photo_path}" \
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

# ---------------------------------------------------------------------------
# Graceful Telegram session handoff (Item 3)
# Call `close` on the Telegram Bot API before killing the daemon.  This is the
# documented method for releasing a long-poll session before instance migration
# (https://core.telegram.org/bots/api#close).  Without it, the restarted
# instance hits "Conflict: terminated by other getUpdates" → 20s × 5 backoff.
# As belt-and-suspenders we also drain the in-flight poll via getUpdates
# offset=-1&timeout=0 (no-op if already expired, harmless if not).
# ---------------------------------------------------------------------------
_release_telegram_lock() {
    local token
    token="$(_telegram_bot_token)"
    [ -z "$token" ] && return 0
    curl -sf --max-time 5 -X POST \
        "${_GATEWAY_TELEGRAM_BASE}/bot${token}/close" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" >/dev/null 2>&1 || true
    # Drain in-flight getUpdates (idempotent — no-op if lock already released)
    curl -sf --max-time 3 -X POST \
        "${_GATEWAY_TELEGRAM_BASE}/bot${token}/getUpdates?offset=-1&timeout=0" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" >/dev/null 2>&1 || true
}

# ---------------------------------------------------------------------------
# Email helper (Item 8)
# Send an email to the owner via the gateway /email/send-owner endpoint.
# No SMTP credentials, no 1Password CLI, no nodemailer needed inside Hermes —
# the gateway already holds the Gmail credentials and does the actual send.
# Usage: _email_owner "Subject line" "Body text" [--html]
# ---------------------------------------------------------------------------
_email_owner() {
    local subject="$1"
    local body="$2"
    local is_html="${3:-false}"
    [ "${is_html}" = "--html" ] && is_html="true"
    local gw_url="${GATEWAY_OP_PROXY_URL:-http://gateway:8080}"
    # Escape double-quotes in subject and body for JSON embedding
    local subj_esc body_esc
    subj_esc="$(printf '%s' "${subject}" | sed 's/"/\\"/g')"
    body_esc="$(printf '%s' "${body}" | sed 's/"/\\"/g')"
    curl -sf --max-time 30 -X POST "${gw_url}/email/send-owner" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" \
        -d "{\"subject\":\"${subj_esc}\",\"body\":\"${body_esc}\",\"is_html\":${is_html}}" \
        >/dev/null 2>&1
}

# Forward TERM/INT to hermes process.
# Order: release Telegram lock first (removes getUpdates conflict on restart),
# then notify Isaiah, then SIGTERM the daemon (graceful asyncio shutdown),
# wait up to 8s for cleanup, SIGKILL if still alive.
# _HERMES_PID is set after the background launch below.
trap '
    echo "[hermes-startup] Shutdown signal received"
    _release_telegram_lock \
        && echo "[hermes-startup] ✓ Released Telegram long-poll lock" \
        || echo "[hermes-startup] ⚠ Could not release Telegram lock"
    _telegram_send "🔴 Hermes shutting down" \
        && echo "[hermes-startup] ✓ Sent Telegram shutdown notification" \
        || echo "[hermes-startup] ⚠ Could not send Telegram shutdown notification"
    if [ -n "${_HERMES_PID:-}" ]; then
        kill -TERM "${_HERMES_PID}" 2>/dev/null || true
        _w=0
        while [ "${_w}" -lt 8 ]; do
            kill -0 "${_HERMES_PID}" 2>/dev/null || break
            sleep 1; _w=$((_w + 1))
        done
        kill -KILL "${_HERMES_PID}" 2>/dev/null || true
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
        if _telegram_send_photo "🛡️ Hermes online" "/app/branding/logo.png" 2>/dev/null; then
            echo "[hermes-startup] ✓ Sent Telegram startup photo notification"
        else
            _telegram_send "🛡️ Hermes online" \
                && echo "[hermes-startup] ✓ Sent Telegram startup notification" \
                || echo "[hermes-startup] ⚠ Could not send Telegram startup notification"
        fi
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
