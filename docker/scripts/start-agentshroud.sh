#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# AgentShroud startup wrapper - exports API keys from Docker secrets

set -euo pipefail

# Export Gateway password from secret file
# Note: OpenClaw CLI expects OPENCLAW_GATEWAY_PASSWORD env var
if [ -f "/run/secrets/gateway_password" ]; then
    export OPENCLAW_GATEWAY_PASSWORD="$(cat /run/secrets/gateway_password)"
    # FINAL: also set GATEWAY_AUTH_TOKEN so op-wrapper.sh routes through gateway
    export GATEWAY_AUTH_TOKEN="$OPENCLAW_GATEWAY_PASSWORD"
    echo "[startup] Loaded Gateway password"
else
    echo "[startup] Warning: Gateway password file not found"
fi

# Export Telegram bot token from secret file (per-host token injection)
# The apply-patches.js script reads TELEGRAM_BOT_TOKEN and injects it into openclaw.json
if [ -f "/run/secrets/telegram_bot_token" ]; then
    export TELEGRAM_BOT_TOKEN="$(cat /run/secrets/telegram_bot_token)"
    echo "[startup] Loaded Telegram bot token"
elif [ -n "${TELEGRAM_BOT_TOKEN_FILE:-}" ] && [ -f "$TELEGRAM_BOT_TOKEN_FILE" ]; then
    export TELEGRAM_BOT_TOKEN="$(cat "$TELEGRAM_BOT_TOKEN_FILE")"
    echo "[startup] Loaded Telegram bot token from $TELEGRAM_BOT_TOKEN_FILE"
fi

# Export OpenAI API key from secret file
if [ -f "/run/secrets/openai_api_key" ]; then
    export OPENAI_API_KEY="$(cat /run/secrets/openai_api_key)"
    echo "[startup] Loaded OpenAI API key"
else
    echo "[startup] Warning: OpenAI API key file not found"
fi

# FINAL: Load secrets via gateway op-proxy (bot has no direct 1Password access).
# op-wrapper.sh routes "op read" through POST /credentials/op-proxy when
# GATEWAY_AUTH_TOKEN and GATEWAY_OP_PROXY_URL are set.

# Retry wrapper for op-proxy reads — handles race condition where the bot
# restarts before the gateway's 1Password connection is fully ready.
# Usage: op_proxy_read_with_retry <label> <op-reference>
# Returns the secret value on stdout; exits non-zero only if all retries fail.
op_proxy_read_with_retry() {
    local label="$1"
    local reference="$2"
    # Cascading waits: 5s, 10s, 15s, 30s, 60s — total patience: 2 minutes before final attempt
    local delays=(5 10 15 30 60)
    local value=""

    for i in "${!delays[@]}"; do
        local attempt=$((i + 1))
        local total=$(( ${#delays[@]} + 1 ))
        value="$(/usr/local/bin/op-wrapper.sh read "$reference" 2>/dev/null)" || true
        if [ -n "$value" ]; then
            printf '%s' "$value"
            return 0
        fi
        local wait="${delays[$i]}"
        echo "[startup] ⚠ ${label}: attempt ${attempt}/${total} failed — retrying in ${wait}s" >&2
        sleep "$wait"
    done

    # Final attempt after all waits exhausted
    value="$(/usr/local/bin/op-wrapper.sh read "$reference" 2>/dev/null)" || true
    if [ -n "$value" ]; then
        printf '%s' "$value"
        return 0
    fi

    echo "[startup] ✗ ${label}: all ${total} attempts failed after 2 minutes" >&2
    return 1
}

if [ -n "${GATEWAY_AUTH_TOKEN:-}" ] && [ -n "${GATEWAY_OP_PROXY_URL:-}" ]; then
    echo "[startup] Loading secrets via gateway op-proxy (${GATEWAY_OP_PROXY_URL})"

    # Load Claude OAuth token (replaces static ANTHROPIC_API_KEY)
    # Item: AgentShroud - Anthropic Claude OAuth Token (Agent Shroud Bot Credentials vault)
    ANTHROPIC_OAUTH_TOKEN="$(op_proxy_read_with_retry "Claude OAuth token" \
        "op://Agent Shroud Bot Credentials/AgentShroud - Anthropic Claude OAuth Token/claude oath token")" || true
    if [ -n "$ANTHROPIC_OAUTH_TOKEN" ]; then
        export ANTHROPIC_OAUTH_TOKEN
        echo "[startup] ✓ Loaded Claude OAuth token"
    else
        echo "[startup] ⚠ Could not load Claude OAuth token after retries"
    fi

    # Load Brave Search API key
    # Item ID: 6j6ij5tzld6kobvit5tk6ufrhq (Brave Search API - agentshroud.ai@gmail.com)
    BRAVE_API_KEY="$(op_proxy_read_with_retry "Brave Search API key" \
        "op://Agent Shroud Bot Credentials/6j6ij5tzld6kobvit5tk6ufrhq/brave search api key")" || true
    if [ -n "$BRAVE_API_KEY" ]; then
        export BRAVE_API_KEY
        echo "[startup] ✓ Loaded Brave Search API key"
    else
        echo "[startup] ⚠ Could not load Brave Search API key after retries"
    fi

    # iCloud email credentials — loaded in background to avoid blocking startup
    # (non-critical: email features degrade gracefully without iCloud creds)
    _ICLOUD_ENV_FILE="/tmp/.icloud-env"
    (
        ICLOUD_APP_PASSWORD="$(op_proxy_read_with_retry "iCloud app password" \
            "op://Agent Shroud Bot Credentials/25ghxryyvup5wpufgfldgc2vjm/agentshroud app-specific password")" || true
        if [ -n "$ICLOUD_APP_PASSWORD" ]; then
            cat > "$_ICLOUD_ENV_FILE" << EOF
export ICLOUD_APP_PASSWORD="$ICLOUD_APP_PASSWORD"
export ICLOUD_USERNAME="agentshroud.ai@gmail.com"
export ICLOUD_EMAIL="agentshroud.ai@icloud.com"
EOF
            echo "[startup] ✓ Loaded iCloud email credentials (background)"
        else
            echo "[startup] ⚠ Could not load iCloud app-specific password after retries"
        fi
    ) &
    _ICLOUD_BG_PID=$!
else
    echo "[startup] Warning: Gateway op-proxy not configured, 1Password secrets unavailable"
fi

# Apply OpenClaw config defaults (SSH allowlist, cron jobs, agent patches, workspace brand files)
echo "[startup] Bootstrapping OpenClaw config..."
/usr/local/bin/init-openclaw-config.sh

# Wait briefly for background iCloud fetch, then source if ready
if [ -n "${_ICLOUD_BG_PID:-}" ]; then
    # Give it 3 seconds — if it's not done, gateway starts without iCloud
    for _i in 1 2 3; do
        if [ -f "${_ICLOUD_ENV_FILE:-/tmp/.icloud-env}" ]; then
            . "$_ICLOUD_ENV_FILE"
            break
        fi
        sleep 1
    done
    if [ ! -f "${_ICLOUD_ENV_FILE:-/tmp/.icloud-env}" ]; then
        echo "[startup] iCloud credentials still loading in background — gateway starting without them"
    fi
fi

# Start AgentShroud gateway (powered by OpenClaw CLI)
echo "[startup] Starting AgentShroud gateway..."
openclaw gateway --allow-unconfigured --bind lan &
OPENCLAW_PID=$!

# Telegram notification helpers — ALL traffic routes through AgentShroud gateway
# No direct api.telegram.org calls. No hardcoded bot tokens.
_OWNER_CHAT_ID="8096968754"
_GATEWAY_TELEGRAM_BASE="${GATEWAY_OP_PROXY_URL:-http://gateway:8080}/telegram-api"

_telegram_bot_token() {
    node -e "
        try {
            const c = JSON.parse(require('fs').readFileSync(
                '/home/node/.openclaw/openclaw.json', 'utf8'));
            process.stdout.write(
                (c.channels && c.channels.telegram && c.channels.telegram.botToken) || '');
        } catch(e) {}
    " 2>/dev/null
}

_telegram_send() {
    local text="$1"
    local token
    token="$(_telegram_bot_token)"
    if [ -z "$token" ]; then
        echo "[startup] ⚠ No Telegram bot token available — cannot send notification" >&2
        return 1
    fi
    # Route through AgentShroud gateway Telegram proxy (never direct to api.telegram.org)
    curl -sf --max-time 10 -X POST "${_GATEWAY_TELEGRAM_BASE}/bot${token}/sendMessage" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -d "{\"chat_id\":\"${_OWNER_CHAT_ID}\",\"text\":\"${text}\"}" \
        >/dev/null 2>&1
}

# Instance identity for notifications
_INSTANCE_LABEL="${INSTANCE_NAME:-$(hostname -s)}"
_BOT_NAME="${OPENCLAW_BOT_NAME:-agentshroud_bot}"

# Forward TERM/INT to openclaw and send shutdown notification
trap '
    echo "[startup] Shutdown signal received — sending Telegram notification..."
    _telegram_send "🔴 AgentShroud shutting down — ${_BOT_NAME} on ${_INSTANCE_LABEL}" \
        && echo "[startup] ✓ Sent Telegram shutdown notification" \
        || echo "[startup] ⚠ Could not send Telegram shutdown notification"
    kill $OPENCLAW_PID 2>/dev/null
' TERM INT

# Wait for gateway to be ready, then send Telegram startup notification
(
    # Poll health endpoint — up to 60s
    for i in $(seq 1 30); do
        if curl -sf http://localhost:18789/api/health >/dev/null 2>&1; then
            break
        fi
        sleep 2
    done

    # Give Telegram provider time to connect after gateway is ready
    sleep 5

    _telegram_send "🛡️ AgentShroud online — ${_BOT_NAME} on ${_INSTANCE_LABEL}" \
        && echo "[startup] ✓ Sent Telegram startup notification" \
        || echo "[startup] ⚠ Could not send Telegram startup notification"
) &

wait $OPENCLAW_PID
