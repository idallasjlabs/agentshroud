#!/bin/bash
# OpenClaw startup wrapper - exports API keys from Docker secrets

set -e

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
    export OP_EMAIL=$(cat /run/secrets/1password_bot_email)
    export OP_PASSWORD=$(cat /run/secrets/1password_bot_master_password)
    export OP_SECRET_KEY=$(cat /run/secrets/1password_bot_secret_key)

    echo "[startup] Signing in to 1Password as $OP_EMAIL..."

    # Add account and sign in, capturing the session token
    SIGNIN_OUTPUT=$(echo "$OP_PASSWORD" | op account add --address my.1password.com --email "$OP_EMAIL" --signin 2>&1)

    if echo "$SIGNIN_OUTPUT" | grep -q "OP_SESSION"; then
        echo "[startup] ✓ Signed in to 1Password successfully"

        # Export the session token
        eval "$SIGNIN_OUTPUT"

        # Test vault access and list available vaults
        VAULTS=$(op vault list 2>&1)
        if [ $? -eq 0 ]; then
            echo "[startup] ✓ 1Password vault access confirmed"
            echo "[startup] Available vaults: $(echo "$VAULTS" | tail -n +2 | awk '{print $2}' | tr '\n' ', ' | sed 's/,$//')"
        else
            echo "[startup] ⚠ Could not list vaults"
        fi
    else
        echo "[startup] ⚠ 1Password signin failed: $SIGNIN_OUTPUT"
    fi

    # Clear sensitive data from environment
    unset OP_PASSWORD
    unset OP_SECRET_KEY
else
    echo "[startup] Warning: 1Password credentials not found (optional)"
fi

# Start OpenClaw gateway
echo "[startup] Starting OpenClaw gateway..."
exec openclaw gateway --allow-unconfigured --bind lan
