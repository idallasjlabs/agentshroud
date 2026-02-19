#!/bin/bash
# Simple credential retrieval for OpenClaw bot
# Usage: get-credential <credential-name>

set -euo pipefail

ITEM="${1:-}"

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

# Fast-path: use env vars when set (avoids 1Password call entirely).
# Security trade-off: GMAIL_APP_PASSWORD and GMAIL_USERNAME live in the process
# environment for the container lifetime (set by start-openclaw.sh at boot).
# Callers MUST NOT log the return value of this script — doing so would expose
# credentials in log aggregation pipelines.
case "$ITEM" in
    gmail-app-password)
        if [ -n "${GMAIL_APP_PASSWORD:-}" ]; then
            echo "$GMAIL_APP_PASSWORD"
            exit 0
        fi
        ;;
    gmail-username)
        if [ -n "${GMAIL_USERNAME:-}" ]; then
            echo "$GMAIL_USERNAME"
            exit 0
        fi
        ;;
esac

# Source shared auth library and authenticate
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=op-auth-common.sh
source "$SCRIPT_DIR/op-auth-common.sh"

if ! op_authenticate; then
    echo "ERROR: Failed to authenticate with 1Password" >&2
    exit 1
fi

# Item ID avoids title containing '@' which breaks op:// URIs
# Item: "Gmail - therealidallasj" in vault "AgentShroud Bot Credentials"
VAULT="AgentShroud Bot Credentials"
ITEM_ID="he6wcfkfieekqkomuxdunal2xa"

case "$ITEM" in
    gmail-username)
        op read --session "$OP_SESSION" "op://$VAULT/$ITEM_ID/username"
        ;;
    gmail-password)
        op read --session "$OP_SESSION" "op://$VAULT/$ITEM_ID/password"
        ;;
    gmail-app-password)
        op read --session "$OP_SESSION" "op://$VAULT/$ITEM_ID/openclaw bot password"
        ;;
    gmail-totp)
        op item get "$ITEM_ID" --vault "$VAULT" --otp --session "$OP_SESSION"
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
