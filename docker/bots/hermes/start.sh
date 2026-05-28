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

# Seed /opt/data config on first boot (idempotent)
/usr/local/bin/init-hermes-config.sh

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
exec hermes gateway run
