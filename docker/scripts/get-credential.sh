#!/bin/bash
# Simple credential retrieval for OpenClaw bot
# Usage: get-credential <credential-name>

set -e

ITEM="$1"

if [ -z "$ITEM" ]; then
    echo "Usage: get-credential <credential-name>"
    echo ""
    echo "Available credentials:"
    echo "  - gmail-username"
    echo "  - gmail-password"
    echo "  - gmail-app-password"
    echo "  - gmail-totp"
    exit 1
fi

# Authenticate with 1Password
authenticate() {
    export OP_EMAIL=$(cat /run/secrets/1password_bot_email 2>/dev/null || echo "")
    export OP_PASSWORD=$(cat /run/secrets/1password_bot_master_password 2>/dev/null || echo "")
    export OP_SECRET_KEY=$(cat /run/secrets/1password_bot_secret_key 2>/dev/null || echo "")

    SIGNIN_OUTPUT=$(echo "$OP_PASSWORD" | op account add --address my.1password.com --email "$OP_EMAIL" --signin 2>&1 || true)
    if echo "$SIGNIN_OUTPUT" | grep -q "OP_SESSION"; then
        eval "$SIGNIN_OUTPUT"
    else
        echo "ERROR: Failed to authenticate with 1Password" >&2
        exit 1
    fi
    unset OP_PASSWORD OP_SECRET_KEY
}

authenticate

VAULT="SecureClaw Bot Credentials"
ITEM_NAME="Gmail - therealidallasj"

case "$ITEM" in
    gmail-username)
        op item get "$ITEM_NAME" --vault "$VAULT" --fields label=username --reveal
        ;;
    gmail-password)
        op item get "$ITEM_NAME" --vault "$VAULT" --fields label=password --reveal
        ;;
    gmail-app-password)
        op item get "$ITEM_NAME" --vault "$VAULT" --fields label="openclaw bot password" --reveal
        ;;
    gmail-totp)
        op item get "$ITEM_NAME" --vault "$VAULT" --otp
        ;;
    list)
        echo "Available credentials in $VAULT:"
        op item list --vault "$VAULT"
        ;;
    *)
        echo "Unknown credential: $ITEM" >&2
        echo "Run 'get-credential' with no arguments to see available credentials" >&2
        exit 1
        ;;
esac
