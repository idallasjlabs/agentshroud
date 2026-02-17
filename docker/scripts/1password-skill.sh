#!/bin/bash
# 1Password Skill for OpenClaw
# Allows the bot to retrieve credentials from 1Password vaults
# Usage: 1password-skill.sh <action> <args>

set -euo pipefail

# Source shared auth library (3-tier fallback, no eval)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=op-auth-common.sh
source "$SCRIPT_DIR/op-auth-common.sh"

# Reject arguments that look like option flags to prevent option injection
# into the op CLI when called programmatically by the bot or agent.
_validate_arg() {
    local name="$1" val="$2"
    if [[ "${val:-}" == -* ]]; then
        echo "[1password-skill] ERROR: Invalid $name: '$val' (must not start with '-')" >&2
        exit 1
    fi
}

# List available vaults
list_vaults() {
    op_authenticate
    op vault list --session "$OP_SESSION"
}

# List items in a vault
list_items() {
    local vault="${1:-SecureClaw Bot Credentials}"
    _validate_arg "vault" "$vault"
    op_authenticate
    op item list --vault "$vault" --session "$OP_SESSION"
}

# Get a specific field from an item
get_field() {
    local item="$1"
    local field="${2:-password}"
    local vault="${3:-SecureClaw Bot Credentials}"
    _validate_arg "item" "$item"
    _validate_arg "field" "$field"
    _validate_arg "vault" "$vault"

    op_authenticate
    op item get "$item" --vault "$vault" --fields "label=$field" --reveal --session "$OP_SESSION"
}

# Get TOTP code
get_totp() {
    local item="$1"
    local vault="${2:-SecureClaw Bot Credentials}"
    _validate_arg "item" "$item"
    _validate_arg "vault" "$vault"

    op_authenticate
    op item get "$item" --vault "$vault" --otp --session "$OP_SESSION"
}

# Main command dispatcher
ACTION="${1:-help}"

case "$ACTION" in
    list-vaults)
        list_vaults
        ;;
    list-items)
        list_items "${2:-}"
        ;;
    get-password)
        get_field "$2" "password" "${3:-SecureClaw Bot Credentials}"
        ;;
    get-username)
        get_field "$2" "username" "${3:-SecureClaw Bot Credentials}"
        ;;
    get-field)
        get_field "$2" "$3" "${4:-SecureClaw Bot Credentials}"
        ;;
    get-totp)
        get_totp "$2" "${3:-SecureClaw Bot Credentials}"
        ;;
    help|*)
        cat <<EOF
1Password Skill for OpenClaw

Usage: 1password-skill.sh <action> [args]

Actions:
  list-vaults                          List all vaults bot can access
  list-items [vault]                   List items in vault (default: SecureClaw Bot Credentials)
  get-password <item> [vault]          Get password from item
  get-username <item> [vault]          Get username from item
  get-field <item> <field> [vault]     Get specific field from item
  get-totp <item> [vault]              Get current TOTP code

Examples:
  # List vaults
  1password-skill.sh list-vaults

  # List items in default vault
  1password-skill.sh list-items

  # Get Gmail password
  1password-skill.sh get-password "Gmail - therealidallasj"

  # Get Gmail username
  1password-skill.sh get-username "Gmail - therealidallasj"

  # Get TOTP code
  1password-skill.sh get-totp "Gmail - therealidallasj"

  # Get custom field
  1password-skill.sh get-field "Gmail - therealidallasj" "openclaw bot password"
EOF
        exit 0
        ;;
esac
