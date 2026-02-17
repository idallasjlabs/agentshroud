#!/bin/bash
# OpenClaw startup wrapper - exports API keys from Docker secrets

set -euo pipefail

# Export Gateway password from secret file
if [ -f "/run/secrets/gateway_password" ]; then
    export OPENCLAW_GATEWAY_PASSWORD=$(cat /run/secrets/gateway_password)
    echo "[startup] Loaded Gateway password"
else
    echo "[startup] Warning: Gateway password file not found"
fi

# Export OpenAI API key from secret file
if [ -f "/run/secrets/openai_api_key" ]; then
    export OPENAI_API_KEY=$(cat /run/secrets/openai_api_key)
    echo "[startup] Loaded OpenAI API key"
else
    echo "[startup] Warning: OpenAI API key file not found"
fi

# Export Anthropic API key from secret file
if [ -f "/run/secrets/anthropic_api_key" ]; then
    export ANTHROPIC_API_KEY=$(cat /run/secrets/anthropic_api_key)
    echo "[startup] Loaded Anthropic API key"
else
    echo "[startup] Warning: Anthropic API key file not found"
fi

# Sign in to 1Password using shared auth library (3-tier fallback)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=op-auth-common.sh
source "$SCRIPT_DIR/op-auth-common.sh"

if op_authenticate 2>/dev/null; then
    echo "[startup] ✓ Signed in to 1Password successfully"

    # Test vault access
    if op vault list --session "$OP_SESSION" >/dev/null 2>&1; then
        VAULTS=$(op vault list --session "$OP_SESSION" 2>&1 | tail -n +2 | awk '{print $2}' | tr '\n' ', ' | sed 's/,$//')
        echo "[startup] ✓ 1Password vault access confirmed"
        echo "[startup] Available vaults: $VAULTS"
    else
        echo "[startup] ⚠ Could not list vaults"
    fi

    # Load Brave Search API key from 1Password
    # Item title contains '@' which breaks op:// URIs — use item ID instead
    # Item ID: 6j6ij5tzld6kobvit5tk6ufrhq (Brave Search API - therealidallasj@gmail.com)
    BRAVE_API_KEY=$(op read --session "$OP_SESSION" \
        "op://SecureClaw Bot Credentials/6j6ij5tzld6kobvit5tk6ufrhq/brach search api key" 2>/dev/null) || true
    if [ -n "$BRAVE_API_KEY" ]; then
        export BRAVE_API_KEY
        echo "[startup] ✓ Loaded Brave Search API key"
    else
        echo "[startup] ⚠ Could not load Brave Search API key"
    fi

    # Load Gmail credentials from 1Password at startup so they survive session expiry
    # Item ID: he6wcfkfieekqkomuxdunal2xa (Gmail - therealidallasj)
    GMAIL_APP_PASSWORD=$(op read --session "$OP_SESSION" \
        "op://SecureClaw Bot Credentials/he6wcfkfieekqkomuxdunal2xa/openclaw bot password" 2>/dev/null) || true
    if [ -n "$GMAIL_APP_PASSWORD" ]; then
        export GMAIL_APP_PASSWORD
        echo "[startup] ✓ Loaded Gmail app password"
    else
        echo "[startup] ⚠ Could not load Gmail app password"
    fi

    GMAIL_USERNAME=$(op read --session "$OP_SESSION" \
        "op://SecureClaw Bot Credentials/he6wcfkfieekqkomuxdunal2xa/username" 2>/dev/null) || true
    if [ -n "$GMAIL_USERNAME" ]; then
        export GMAIL_USERNAME
        echo "[startup] ✓ Loaded Gmail username"
    else
        echo "[startup] ⚠ Could not load Gmail username"
    fi
else
    echo "[startup] Warning: 1Password credentials not found (optional)"
fi

# Start OpenClaw gateway
echo "[startup] Starting OpenClaw gateway..."
exec openclaw gateway --allow-unconfigured --bind lan
