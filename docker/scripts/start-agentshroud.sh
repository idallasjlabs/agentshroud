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
if [ -n "${GATEWAY_AUTH_TOKEN:-}" ] && [ -n "${GATEWAY_OP_PROXY_URL:-}" ]; then
    echo "[startup] Loading secrets via gateway op-proxy (${GATEWAY_OP_PROXY_URL})"

    # Load Claude OAuth token (replaces static ANTHROPIC_API_KEY)
    # Item: AgentShroud - Anthropic Claude OAuth Token (Agent Shroud Bot Credentials vault)
    ANTHROPIC_OAUTH_TOKEN="$(/usr/local/bin/op-wrapper.sh read \
        "op://Agent Shroud Bot Credentials/AgentShroud - Anthropic Claude OAuth Token/claude oath token" 2>/dev/null)" || true
    if [ -n "$ANTHROPIC_OAUTH_TOKEN" ]; then
        export ANTHROPIC_OAUTH_TOKEN
        echo "[startup] ✓ Loaded Claude OAuth token"
    else
        echo "[startup] ⚠ Could not load Claude OAuth token"
    fi

    # Load Brave Search API key
    # Item ID: 6j6ij5tzld6kobvit5tk6ufrhq (Brave Search API - agentshroud.ai@gmail.com)
    BRAVE_API_KEY="$(/usr/local/bin/op-wrapper.sh read \
        "op://Agent Shroud Bot Credentials/6j6ij5tzld6kobvit5tk6ufrhq/brave search api key" 2>/dev/null)" || true
    if [ -n "$BRAVE_API_KEY" ]; then
        export BRAVE_API_KEY
        echo "[startup] ✓ Loaded Brave Search API key"
    else
        echo "[startup] ⚠ Could not load Brave Search API key"
    fi

    # Gmail credentials intentionally not loaded at startup.
    # Loading GMAIL_APP_PASSWORD on every restart authenticates from the Docker
    # container IP, which Google flags as suspicious and locks the account.
    # Re-enable only after the Gmail accounts are recovered and a safe auth
    # strategy (e.g. OAuth2 refresh token) is in place.
else
    echo "[startup] Warning: Gateway op-proxy not configured, 1Password secrets unavailable"
fi

# Start AgentShroud gateway (powered by OpenClaw CLI)
echo "[startup] Starting AgentShroud gateway..."
exec openclaw gateway --allow-unconfigured --bind lan
