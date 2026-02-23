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

    # iCloud email credentials (replaces Gmail, which is locked out)
    ICLOUD_APP_PASSWORD="$(op_proxy_read_with_retry "iCloud app password" \
        "op://AgentShroud Bot Credentials/AgentShroud - iCloud Mail [agentshroud.ai@icloud.com]/agentshroud app-specific password")" || true
    if [ -n "$ICLOUD_APP_PASSWORD" ]; then
        export ICLOUD_APP_PASSWORD
        export ICLOUD_USERNAME="agentshroud.ai@gmail.com"
        export ICLOUD_EMAIL="agentshroud.ai@icloud.com"
        echo "[startup] ✓ Loaded iCloud email credentials"
    else
        echo "[startup] ⚠ Could not load iCloud app-specific password after retries"
    fi
else
    echo "[startup] Warning: Gateway op-proxy not configured, 1Password secrets unavailable"
fi

# Apply OpenClaw config defaults (SSH allowlist, cron jobs, agent patches, workspace brand files)
echo "[startup] Bootstrapping OpenClaw config..."
/usr/local/bin/init-openclaw-config.sh

# Start AgentShroud gateway (powered by OpenClaw CLI)
echo "[startup] Starting AgentShroud gateway..."
openclaw gateway --allow-unconfigured --bind lan &
OPENCLAW_PID=$!

# Read Telegram bot token once — shared by startup and shutdown notifications
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
    [ -z "$token" ] && return 1
    curl -sf -X POST "https://api.telegram.org/bot${token}/sendMessage" \
        -H "Content-Type: application/json" \
        -d "{\"chat_id\":\"8096968754\",\"text\":\"${text}\"}" \
        >/dev/null 2>&1
}

# Forward TERM/INT to openclaw and send shutdown notification
trap '
    echo "[startup] Shutdown signal received — sending Telegram notification..."
    _telegram_send "🔴 AgentShroud bot shutting down." \
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

    _telegram_send "🛡️ AgentShroud bot online — Telegram delivery confirmed after rebuild." \
        && echo "[startup] ✓ Sent Telegram startup notification" \
        || echo "[startup] ⚠ Could not send Telegram startup notification"
) &

wait $OPENCLAW_PID
