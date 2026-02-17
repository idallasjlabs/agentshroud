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

# Sign in to 1Password (bot's personal account)
if [ -f "/run/secrets/1password_bot_email" ] && [ -f "/run/secrets/1password_bot_master_password" ] && [ -f "/run/secrets/1password_bot_secret_key" ]; then
    OP_EMAIL=$(cat /run/secrets/1password_bot_email)
    OP_PASSWORD=$(cat /run/secrets/1password_bot_master_password)
    OP_SECRET_KEY=$(cat /run/secrets/1password_bot_secret_key)

    echo "[startup] Signing in to 1Password as $OP_EMAIL..."

    # Use --raw to get just the session token (avoids dangerous eval)
    # Try adding account first (first boot); fall back to signin if already added
    mkdir -p "$HOME/.config/op"
    chmod 700 "$HOME/.config/op"
    OP_SESSION=$(echo "$OP_PASSWORD" | op account add \
        --address my.1password.com \
        --email "$OP_EMAIL" \
        --secret-key "$OP_SECRET_KEY" \
        --signin --raw 2>/dev/null) || \
    OP_SESSION=$(echo "$OP_PASSWORD" | op signin \
        --account my.1password.com \
        --raw 2>/dev/null) || \
    OP_SESSION=""

    if [ -n "$OP_SESSION" ]; then
        export OP_SESSION_my="$OP_SESSION"
        echo "[startup] ✓ Signed in to 1Password successfully"

        # Test vault access
        if op vault list --session "$OP_SESSION" >/dev/null 2>&1; then
            VAULTS=$(op vault list --session "$OP_SESSION" 2>&1 | tail -n +2 | awk '{print $2}' | tr '\n' ', ' | sed 's/,$//')
            echo "[startup] ✓ 1Password vault access confirmed"
            echo "[startup] Available vaults: $VAULTS"
        else
            echo "[startup] ⚠ Could not list vaults"
        fi
    else
        echo "[startup] ⚠ 1Password signin failed"
    fi

    # Clear sensitive data from environment
    unset OP_PASSWORD OP_SECRET_KEY
else
    echo "[startup] Warning: 1Password credentials not found (optional)"
fi

# Start OpenClaw gateway
echo "[startup] Starting OpenClaw gateway..."
exec openclaw gateway --allow-unconfigured --bind lan
