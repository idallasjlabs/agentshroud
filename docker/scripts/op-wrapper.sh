#!/bin/bash
# Wrapper script for 1Password CLI that handles authentication
# Usage: op-wrapper.sh <op command arguments>

set -e

# Load credentials from Docker secrets
if [ -f "/run/secrets/1password_bot_email" ] && [ -f "/run/secrets/1password_bot_master_password" ] && [ -f "/run/secrets/1password_bot_secret_key" ]; then
    export OP_EMAIL=$(cat /run/secrets/1password_bot_email)
    export OP_PASSWORD=$(cat /run/secrets/1password_bot_master_password)
    export OP_SECRET_KEY=$(cat /run/secrets/1password_bot_secret_key)

    # Sign in and get session token
    SIGNIN_OUTPUT=$(echo "$OP_PASSWORD" | op account add --address my.1password.com --email "$OP_EMAIL" --signin 2>&1 || true)

    if echo "$SIGNIN_OUTPUT" | grep -q "OP_SESSION"; then
        # Export the session token
        eval "$SIGNIN_OUTPUT"

        # Run the op command with all arguments
        op "$@"
    else
        echo "[ERROR] Failed to sign in to 1Password" >&2
        exit 1
    fi

    # Clear sensitive data
    unset OP_PASSWORD
    unset OP_SECRET_KEY
else
    echo "[ERROR] 1Password credentials not found" >&2
    exit 1
fi
