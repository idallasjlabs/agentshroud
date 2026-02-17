#!/bin/bash
# Simple credential retrieval for OpenClaw bot
# Usage: get-credential <credential-name>

set -euo pipefail

ITEM="$1"

if [ -z "${ITEM:-}" ]; then
    echo "Usage: get-credential <credential-name>"
    echo ""
    echo "Available credentials:"
    echo "  - gmail-username"
    echo "  - gmail-password"
    echo "  - gmail-app-password"
    echo "  - gmail-totp"
    exit 1
fi

# Authenticate with 1Password using --raw (no eval)
authenticate() {
    local email password secret_key
    email=$(cat /run/secrets/1password_bot_email 2>/dev/null || echo "")
    password=$(cat /run/secrets/1password_bot_master_password 2>/dev/null || echo "")
    secret_key=$(cat /run/secrets/1password_bot_secret_key 2>/dev/null || echo "")

    if [ -z "$email" ] || [ -z "$password" ]; then
        echo "ERROR: 1Password credentials not found" >&2
        exit 1
    fi

    OP_SESSION=$(echo "$password" | op account add \
        --address my.1password.com \
        --email "$email" \
        --secret-key "$secret_key" \
        --signin --raw 2>/dev/null || echo "")

    unset password secret_key

    if [ -z "$OP_SESSION" ]; then
        echo "ERROR: Failed to authenticate with 1Password" >&2
        exit 1
    fi
}

authenticate

VAULT="SecureClaw Bot Credentials"
ITEM_NAME="Gmail - therealidallasj"

case "$ITEM" in
    gmail-username)
        op item get "$ITEM_NAME" --vault "$VAULT" --fields label=username --reveal --session "$OP_SESSION"
        ;;
    gmail-password)
        op item get "$ITEM_NAME" --vault "$VAULT" --fields label=password --reveal --session "$OP_SESSION"
        ;;
    gmail-app-password)
        op item get "$ITEM_NAME" --vault "$VAULT" --fields label="openclaw bot password" --reveal --session "$OP_SESSION"
        ;;
    gmail-totp)
        op item get "$ITEM_NAME" --vault "$VAULT" --otp --session "$OP_SESSION"
        ;;
    list)
        echo "Available credentials in $VAULT:"
        op item list --vault "$VAULT" --session "$OP_SESSION"
        ;;
    *)
        echo "Unknown credential: $ITEM" >&2
        exit 1
        ;;
esac
