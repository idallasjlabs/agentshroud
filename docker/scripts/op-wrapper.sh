#!/bin/bash
# Wrapper script for 1Password CLI that handles authentication
# Usage: op-wrapper.sh <op command arguments>

set -euo pipefail

if [ -f "/run/secrets/1password_bot_email" ] && [ -f "/run/secrets/1password_bot_master_password" ] && [ -f "/run/secrets/1password_bot_secret_key" ]; then
    OP_EMAIL=$(cat /run/secrets/1password_bot_email)
    OP_PASSWORD=$(cat /run/secrets/1password_bot_master_password)
    OP_SECRET_KEY=$(cat /run/secrets/1password_bot_secret_key)

    # Use --raw to get just the session token (no eval needed)
    OP_SESSION=$(echo "$OP_PASSWORD" | op account add \
        --address my.1password.com \
        --email "$OP_EMAIL" \
        --secret-key "$OP_SECRET_KEY" \
        --signin --raw 2>/dev/null || echo "")

    unset OP_PASSWORD OP_SECRET_KEY

    if [ -n "$OP_SESSION" ]; then
        op --session "$OP_SESSION" "$@"
    else
        echo "[ERROR] Failed to sign in to 1Password" >&2
        exit 1
    fi
else
    echo "[ERROR] 1Password credentials not found" >&2
    exit 1
fi
