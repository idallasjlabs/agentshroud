#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# Shared 1Password authentication helper
# Source this file, then call op_authenticate.
#
# Outputs (intentional globals written to the calling scope):
#   OP_SESSION     — raw session token, valid for the current shell invocation
#   OP_SESSION_my  — same token, NOT exported; callers that need it in child
#                    processes must export it explicitly and unset before exec
#
# On success: returns 0, OP_SESSION and OP_SESSION_my are set.
# On failure: returns 1 (never exits, safe to source).

# Allow override for testing (default: Docker secrets mount)
OP_SECRETS_DIR="${OP_SECRETS_DIR:-/run/secrets}"

op_authenticate() {
    # Guard against path traversal in OP_SECRETS_DIR
    case "$OP_SECRETS_DIR" in
        *..*) echo "[op-auth] ERROR: OP_SECRETS_DIR must not contain '..'" >&2; return 1 ;;
    esac

    # Tier 1: reuse existing session if still valid
    if [ -n "${OP_SESSION_my:-}" ]; then
        if op vault list --session "$OP_SESSION_my" >/dev/null 2>&1; then
            OP_SESSION="$OP_SESSION_my"
            return 0
        fi
    fi

    # Read Docker secrets (local scope — cleared after use)
    local email password secret_key
    email=$(cat "$OP_SECRETS_DIR/1password_bot_email" 2>/dev/null || echo "")
    password=$(cat "$OP_SECRETS_DIR/1password_bot_master_password" 2>/dev/null || echo "")
    secret_key=$(cat "$OP_SECRETS_DIR/1password_bot_secret_key" 2>/dev/null || echo "")

    if [ -z "$email" ] || [ -z "$password" ]; then
        echo "[op-auth] ERROR: 1Password credentials not found in $OP_SECRETS_DIR" >&2
        return 1
    fi

    mkdir -p "$HOME/.config/op"
    chmod 700 "$HOME/.config/op"

    # Tier 2: op account add --signin --raw (first boot — account not yet registered)
    # Skip when secret_key is absent; op account add requires it and would produce a
    # misleading error rather than falling through gracefully.
    if [ -n "$secret_key" ]; then
        OP_SESSION=$(echo "$password" | op account add \
            --address my.1password.com \
            --email "$email" \
            --secret-key "$secret_key" \
            --signin --raw 2>/dev/null) || true
    fi

    # Tier 3: op signin --raw fallback (account already added on prior boot)
    if [ -z "${OP_SESSION:-}" ]; then
        OP_SESSION=$(echo "$password" | op signin \
            --account my.1password.com \
            --raw 2>/dev/null) || true
    fi

    # Clear sensitive local vars immediately
    password=""
    secret_key=""
    unset password secret_key

    if [ -n "${OP_SESSION:-}" ]; then
        # Not exported: callers export explicitly only when child processes need it,
        # and must unset before exec to avoid leaking into long-lived processes.
        OP_SESSION_my="$OP_SESSION"
        return 0
    else
        echo "[op-auth] ERROR: Failed to authenticate with 1Password" >&2
        return 1
    fi
}
