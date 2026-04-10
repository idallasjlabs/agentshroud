#!/usr/bin/env bash
# setup-secrets.sh — Docker secrets manager for AgentShroud
#
# Subcommands:
#   store    — prompt for each secret and store in the credential backend
#   extract  — read all secrets from backend and write docker/secrets/<name>.txt
#   (none)   — backwards-compat interactive mode: prompt and write secret files directly
#
# Credential backend hierarchy (auto-detected):
#   1. 1Password CLI  — cross-platform, team-friendly (primary)
#   2. macOS Keychain — fallback on macOS (security command)
#   3. Linux secret-tool — fallback on Linux (libsecret)
#   4. prompt         — write directly to secret files (no credential store)
#
# Usage:
#   ./setup-secrets.sh            # interactive, writes files directly (legacy)
#   ./setup-secrets.sh store      # store all secrets in credential backend
#   ./setup-secrets.sh extract    # write secret files from credential backend
#   ./setup-secrets.sh help       # show this message

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SECRETS_DIR="${AGENTSHROUD_SECRETS_DIR:-${SCRIPT_DIR}/secrets}"

# ── Credential backend detection ──────────────────────────────────────────────
# AGENTSHROUD_SECRET_BACKEND env var always wins.
# Auto-detection falls back to 'homedir' when stdin is not a TTY (service
# account / SSH / launchd) because macOS Keychain requires an interactive
# login session and will fail with "User interaction is not allowed".
SECRETS_HOME_DIR="${HOME}/.agentshroud/secrets"

detect_backend() {
    # macOS interactive session: prefer Keychain (fast, local, no network dependency).
    # Keychain must be unlocked — SSH sessions start with it locked; fall through to
    # 1Password if unlock fails so service accounts still work.
    if [[ "$(uname)" == "Darwin" ]] && [[ -t 0 ]]; then
        if ! security show-keychain-info ~/Library/Keychains/login.keychain-db &>/dev/null; then
            echo "  Keychain is locked. Unlocking..." >&2
            if ! security unlock-keychain ~/Library/Keychains/login.keychain-db; then
                echo "  Keychain unlock failed — trying 1Password..." >&2
                # fall through to 1Password check below
                true
            else
                echo "keychain"
                return
            fi
        else
            echo "keychain"
            return
        fi
    fi
    # Non-macOS or Keychain unavailable: prefer 1Password CLI (cross-platform, team-friendly).
    if command -v op &>/dev/null && op account list &>/dev/null 2>&1; then
        echo "1password"
    elif command -v secret-tool &>/dev/null && [[ -t 0 ]]; then
        echo "secretstore"
    elif [[ -d "${SECRETS_HOME_DIR}" ]]; then
        # Service account fallback: home-directory secrets store
        echo "homedir"
    else
        echo "prompt"
    fi
}

BACKEND="${AGENTSHROUD_SECRET_BACKEND:-$(detect_backend)}"
OP_VAULT="${AGENTSHROUD_OP_VAULT:-Private}"

# ── Backend primitives ─────────────────────────────────────────────────────────
store_secret() {
    local name="$1" value="$2"
    case "$BACKEND" in
        1password)
            op item edit "AgentShroud" "${name}[password]=${value}" --vault "$OP_VAULT" 2>/dev/null \
            || op item create \
                --category login \
                --title "AgentShroud" \
                --vault "$OP_VAULT" \
                "username=${name}" \
                "password=${value}"
            ;;
        keychain)
            security add-generic-password -U -s "agentshroud" -a "${name}" -w "${value}"
            ;;
        secretstore)
            secret-tool store --label="agentshroud-${name}" service agentshroud key "${name}" <<< "${value}"
            ;;
        homedir)
            mkdir -p "${SECRETS_HOME_DIR}"
            chmod 700 "${SECRETS_HOME_DIR}"
            printf '%s' "$value" > "${SECRETS_HOME_DIR}/${name}.txt"
            chmod 600 "${SECRETS_HOME_DIR}/${name}.txt"
            ;;
        prompt)
            mkdir -p "${SECRETS_DIR}"
            printf '%s' "$value" > "${SECRETS_DIR}/${name}.txt"
            chmod 600 "${SECRETS_DIR}/${name}.txt"
            ;;
    esac
}

get_secret() {
    local name="$1"
    case "$BACKEND" in
        1password)
            op item get "AgentShroud" --fields "${name}" 2>/dev/null || true
            ;;
        keychain)
            security find-generic-password -s "agentshroud" -a "${name}" -w 2>/dev/null || true
            ;;
        secretstore)
            secret-tool lookup service agentshroud key "${name}" 2>/dev/null || true
            ;;
        homedir)
            cat "${SECRETS_HOME_DIR}/${name}.txt" 2>/dev/null || true
            ;;
        prompt)
            cat "${SECRETS_DIR}/${name}.txt" 2>/dev/null || true
            ;;
    esac
}

# ── Masked interactive reader ──────────────────────────────────────────────────
read_secret_masked() {
    local prompt="$1" optional="${2:-}"
    local value="" char
    # All display output (prompt, asterisks, newlines) goes to /dev/tty so that
    # callers using value="$(read_secret_masked ...)" only capture the actual secret.
    echo "" > /dev/tty
    if [[ "$optional" == "optional" ]]; then
        printf "  → %s (press Enter to skip): " "$prompt" > /dev/tty
    else
        printf "  → %s: " "$prompt" > /dev/tty
    fi
    while IFS= read -r -s -n1 char; do
        if [[ "$char" == $'\0' || "$char" == $'\n' ]]; then
            break
        elif [[ "$char" == $'\177' || "$char" == $'\b' ]]; then
            if [[ ${#value} -gt 0 ]]; then
                value="${value%?}"
                printf '\b \b' > /dev/tty
            fi
        else
            value+="$char"
            printf '*' > /dev/tty
        fi
    done
    printf '\n' > /dev/tty
    if [[ -z "$value" ]]; then
        if [[ "$optional" == "optional" ]]; then
            echo "" > /dev/tty
            return
        fi
        echo "Error: value required." >&2
        exit 1
    fi
    printf '%s' "$value"
}

read_secret_plain() {
    local prompt="$1" optional="${2:-}"
    local value
    echo ""
    if [[ "$optional" == "optional" ]]; then
        read -rp "  → $prompt (press Enter to skip): " value || true
    else
        read -rp "  → $prompt: " value
        if [[ -z "$value" ]]; then
            echo "Error: value required." >&2
            exit 1
        fi
    fi
    printf '%s' "${value:-}"
}

# ── Secret definitions ─────────────────────────────────────────────────────────
# Format: "name|prompt|masked|optional"
# masked:   yes = mask input with asterisks
# optional: yes = skip if empty (Enter to skip)
declare -a SECRET_DEFS=(
    "anthropic_oauth_token|Claude OAuth token (sk-ant-oat01-...)|yes|no"
    "openai_api_key|OpenAI API key|yes|yes"
    "google_api_key|Google API key|yes|yes"
    "1password_bot_email|1Password account email|no|yes"
    "1password_bot_master_password|1Password master password|yes|yes"
    "1password_bot_secret_key|1Password secret key (A3-...)|yes|yes"
    "telegram_bot_token_production|Telegram bot token (production)|yes|no"
    "telegram_bot_token_marvin|Telegram bot token (marvin dev)|yes|yes"
    "telegram_bot_token_trillian|Telegram bot token (trillian dev)|yes|yes"
    "telegram_bot_token_rpi|Telegram bot token (rpi dev)|yes|yes"
    "slack_bot_token|Slack bot token (xoxb-...)|yes|yes"
    "slack_signing_secret|Slack signing secret|yes|yes"
    "slack_app_token|Slack app token (xapp-...)|yes|yes"
)

# ── gateway_password is auto-generated — not prompted ─────────────────────────
generate_gateway_password() {
    python3 -c "import secrets; print(secrets.token_hex(32), end='')"
}

# ── Subcommands ────────────────────────────────────────────────────────────────
cmd_store() {
    echo "╔═══════════════════════════════════════════╗"
    echo "║  AgentShroud — Store Secrets               ║"
    echo "║  Backend: ${BACKEND}$(printf '%*s' $((27 - ${#BACKEND})) '')║"
    echo "╚═══════════════════════════════════════════╝"
    echo ""

    # Auto-generate gateway password
    gw_pass="$(generate_gateway_password)"
    store_secret "gateway_password" "$gw_pass"
    echo "  [stored] gateway_password (auto-generated)"

    for def in "${SECRET_DEFS[@]}"; do
        IFS='|' read -r name prompt masked optional <<< "$def"
        if [[ "$masked" == "yes" ]]; then
            value="$(read_secret_masked "$prompt" "$optional")"
        else
            value="$(read_secret_plain "$prompt" "$optional")"
        fi
        if [[ -z "$value" && "$optional" == "yes" ]]; then
            echo "  [skipped] $name"
            continue
        fi
        store_secret "$name" "$value"
        echo "  [stored] $name"
    done

    echo ""
    echo "All secrets stored in backend: ${BACKEND}"
    echo "Run 'scripts/asb up' to start the stack (secrets extracted automatically)."
}

cmd_extract() {
    echo "╔═══════════════════════════════════════════╗"
    echo "║  AgentShroud — Extract Secrets             ║"
    echo "║  Backend: ${BACKEND}$(printf '%*s' $((27 - ${#BACKEND})) '')║"
    echo "╚═══════════════════════════════════════════╝"
    echo ""

    mkdir -p "${SECRETS_DIR}"

    # Build list of (name, optional) pairs. gateway_password is always required.
    declare -a extract_defs=("gateway_password|no")
    for def in "${SECRET_DEFS[@]}"; do
        IFS='|' read -r name _ _ optional <<< "$def"
        extract_defs+=("${name}|${optional}")
    done

    ok=true
    for entry in "${extract_defs[@]}"; do
        IFS='|' read -r name optional <<< "$entry"
        value="$(get_secret "$name")"
        if [[ -z "$value" ]]; then
            if [[ "$optional" == "yes" ]]; then
                echo "  [skipped] $name — not stored (optional)"
            else
                echo "  [missing] $name — not found in backend ${BACKEND}"
                ok=false
            fi
            continue
        fi
        out="${SECRETS_DIR}/${name}.txt"
        printf '%s' "$value" > "$out"
        chmod 600 "$out"
        echo "  [written] $out"
    done

    echo ""
    if $ok; then
        echo "All required secrets extracted to ${SECRETS_DIR}/"
        echo "Next: scripts/asb up"
    else
        echo "Some secrets were missing. Run './docker/setup-secrets.sh store' to configure them."
        echo "The stack will start in degraded mode — unconfigured features will be disabled."
        return 1
    fi
}

cmd_interactive() {
    # Backwards-compat: original behaviour — prompt and write secret files directly.
    echo "╔═══════════════════════════════════════════╗"
    echo "║  AgentShroud — Docker Secrets Setup        ║"
    echo "╚═══════════════════════════════════════════╝"
    echo ""

    mkdir -p "${SECRETS_DIR}"
    cd "${SECRETS_DIR}"

    # Auto-generate gateway password
    generate_gateway_password > gateway_password.txt
    chmod 600 gateway_password.txt
    echo "  [ok] gateway_password.txt (auto-generated)"

    echo ""
    echo "── Required secrets ──"
    for def in "${SECRET_DEFS[@]}"; do
        IFS='|' read -r name prompt masked optional <<< "$def"
        out="${name}.txt"
        if [[ "$masked" == "yes" ]]; then
            value="$(read_secret_masked "$prompt" "$optional")"
        else
            value="$(read_secret_plain "$prompt" "$optional")"
        fi
        if [[ -z "$value" && "$optional" == "yes" ]]; then
            echo "  [skipped] $out"
            continue
        fi
        printf '%s' "$value" > "$out"
        chmod 600 "$out"
        echo "  [ok] $out"
    done

    echo ""
    echo "── Validation ──"
    ok=true
    for f in anthropic_oauth_token.txt gateway_password.txt; do
        if [[ -f "$f" && -s "$f" ]]; then
            echo "  [ok] $f exists"
        else
            echo "  [MISSING] $f"
            ok=false
        fi
    done

    if $ok; then
        echo ""
        echo "All required secrets created."
        echo "Next: edit agentshroud.yaml and run docker compose up -d"
    else
        echo ""
        echo "Some secrets are missing. Re-run this script."
        exit 1
    fi
}

cmd_help() {
    cat <<'EOF'
setup-secrets.sh — Docker secrets manager for AgentShroud

Usage:
  ./setup-secrets.sh              Interactive mode: prompt and write secret files directly
  ./setup-secrets.sh store        Store all secrets in credential backend
  ./setup-secrets.sh extract      Extract secrets from backend → docker/secrets/*.txt
  ./setup-secrets.sh help         Show this message

Credential backend hierarchy (auto-detected, or set AGENTSHROUD_SECRET_BACKEND):
  1password    1Password CLI (cross-platform, team-friendly) — requires: op CLI + signed-in account
  keychain     macOS Keychain (security command)             — macOS only
  secretstore  Linux secret-tool (libsecret)                 — Linux only
  prompt       Write directly to secret files                — always available fallback

Typical first-time setup:
  1. ./setup-secrets.sh store      # enter secrets once; stored securely
  2. ./setup-secrets.sh extract    # write *.txt files Docker mounts need
  3. docker compose -f docker/docker-compose.yml up -d

On a new machine (secrets already stored in 1Password/Keychain):
  1. ./setup-secrets.sh extract    # pull from backend → local files
  2. docker compose ... up -d

Environment:
  AGENTSHROUD_SECRET_BACKEND   Override auto-detected backend (1password|keychain|secretstore|prompt)
EOF
}

# ── Dispatch ───────────────────────────────────────────────────────────────────
SUBCOMMAND="${1:-}"
case "$SUBCOMMAND" in
    store)   cmd_store ;;
    extract) cmd_extract ;;
    help|--help|-h) cmd_help ;;
    "")      cmd_interactive ;;
    *)
        echo "Unknown subcommand: $SUBCOMMAND" >&2
        echo "Run './setup-secrets.sh help' for usage." >&2
        exit 1
        ;;
esac
