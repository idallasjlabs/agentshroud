#!/bin/bash
# Shared 1Password authentication helper
# Source this file, then call op_authenticate.
# On success: OP_SESSION and OP_SESSION_my are set in the calling scope.
# On failure: returns 1 (never exits, safe to source).

# Allow override for testing (default: Docker secrets mount)
OP_SECRETS_DIR="${OP_SECRETS_DIR:-/run/secrets}"

op_authenticate() {
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
    OP_SESSION=$(echo "$password" | op account add \
        --address my.1password.com \
        --email "$email" \
        --secret-key "$secret_key" \
        --signin --raw 2>/dev/null) || true

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
        export OP_SESSION_my="$OP_SESSION"
        return 0
    else
        echo "[op-auth] ERROR: Failed to authenticate with 1Password" >&2
        return 1
    fi
}
