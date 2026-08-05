#!/usr/bin/env bash
# setup-secrets.sh — Docker secrets manager for AgentShroud
#
# Subcommands:
#   store    — prompt for each secret and store in the credential backend
#   extract  — read all secrets from backend and write docker/secrets/<name>.txt
#   (none)   — backwards-compat interactive mode: prompt and write secret files directly
#
# Credential backend hierarchy (store writes to tier 1; get cascades all tiers):
#   1. macOS Keychain — dedicated agentshroud.keychain, never auto-locks (PRIMARY)
#   2. Linux secret-tool — libsecret/GNOME Keyring (PRIMARY on Linux)
#   3. 1Password CLI  — non-interactive fallback; uses "Agent Shroud Bot Credentials" vault
#   4. homedir        — ~/.agentshroud/secrets/*.txt (file fallback)
#
# Usage:
#   ./setup-secrets.sh                         # interactive, writes files directly (legacy)
#   ./setup-secrets.sh store                   # store ALL secrets in credential backend
#   ./setup-secrets.sh store --bot openclaw    # store only OpenClaw + shared secrets
#   ./setup-secrets.sh store --bot hermes      # store only Hermes + shared secrets
#   ./setup-secrets.sh extract                 # write ALL secret files from credential backend
#   ./setup-secrets.sh extract --bot openclaw  # write only OpenClaw + shared secret files
#   ./setup-secrets.sh extract --bot hermes    # write only Hermes + shared secret files
#   ./setup-secrets.sh migrate                 # one-time: pull secrets from 1Password → Keychain
#   ./setup-secrets.sh help                    # show this message

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SECRETS_DIR="${AGENTSHROUD_SECRETS_DIR:-${SCRIPT_DIR}/secrets}"

# ── Credential backend detection ──────────────────────────────────────────────
# AGENTSHROUD_SECRET_BACKEND env var always wins.
# On macOS the dedicated agentshroud.keychain is primary — it never auto-locks
# so it works over SSH without prompts. 1Password is a cascade fallback only.
SECRETS_HOME_DIR="${HOME}/.agentshroud/secrets"

detect_backend() {
    if [[ "$(uname)" == "Darwin" ]]; then
        echo "keychain"
    elif command -v secret-tool &>/dev/null; then
        echo "secretstore"
    elif [[ -d "${SECRETS_HOME_DIR}" ]]; then
        echo "homedir"
    else
        echo "prompt"
    fi
}

BACKEND="${AGENTSHROUD_SECRET_BACKEND:-$(detect_backend)}"
# 1Password vault containing AgentShroud secrets. Override with AGENTSHROUD_OP_VAULT.
# Per-host item: "AgentShroud - <hostname> [<user>]". Override with AGENTSHROUD_OP_ITEM.
OP_VAULT="${AGENTSHROUD_OP_VAULT:-Agent Shroud Bot Credentials}"

# ── macOS dedicated Keychain helpers ──────────────────────────────────────────
# Uses a separate agentshroud.keychain (never auto-locks) so SSH/headless runs
# never need a TTY or 1Password approval.
AGENTSHROUD_KC="agentshroud.keychain"
KEYCHAIN_PASS_FILE="${HOME}/.config/agentshroud/keychain.pass"

ensure_keychain() {
    [[ "$(uname)" != "Darwin" ]] && return 0
    local kc_db="${HOME}/Library/Keychains/agentshroud.keychain-db"

    # Generate a random password for the keychain on first run.
    if [[ ! -f "$KEYCHAIN_PASS_FILE" ]]; then
        mkdir -p "$(dirname "$KEYCHAIN_PASS_FILE")"
        python3 -c "import secrets; print(secrets.token_hex(32), end='')" > "$KEYCHAIN_PASS_FILE"
        chmod 600 "$KEYCHAIN_PASS_FILE"
    fi
    local kc_pass
    kc_pass="$(cat "$KEYCHAIN_PASS_FILE")"

    if [[ ! -f "$kc_db" ]]; then
        security create-keychain -p "$kc_pass" "$AGENTSHROUD_KC" 2>/dev/null
        # No -l or -u flags → keychain never auto-locks (required for headless SSH).
        security set-keychain-settings "$AGENTSHROUD_KC" 2>/dev/null
        # Append to user search list without removing existing keychains.
        local current_kcs
        current_kcs=$(security list-keychains -d user | tr -d '"' | xargs)
        # shellcheck disable=SC2086
        security list-keychains -d user -s $current_kcs "$kc_db" 2>/dev/null
        echo "  [keychain] Created ${AGENTSHROUD_KC} (never auto-locks)" >&2
    fi

    # Unlock is idempotent — safe to call when already unlocked.
    security unlock-keychain -p "$kc_pass" "$AGENTSHROUD_KC" 2>/dev/null || true
}

keychain_store() {
    local name="$1" value="$2"
    ensure_keychain
    # -U: update if exists; -A: no per-access approval (required for headless SSH).
    security add-generic-password -U -A \
        -s "agentshroud" -a "${name}" -w "${value}" \
        "${AGENTSHROUD_KC}" 2>/dev/null
}

keychain_get() {
    local name="$1"
    security find-generic-password -s "agentshroud" -a "${name}" -w \
        "${AGENTSHROUD_KC}" 2>/dev/null || true
}

# ── 1Password non-interactive fallback ────────────────────────────────────────
# op_get tries several field-label variants to handle the inconsistencies in
# the "Agent Shroud Bot Credentials" vault (e.g. openai+api_key vs openai_api_key).
op_get() {
    local name="$1"
    command -v op &>/dev/null || return 0
    command -v op &>/dev/null && op account list &>/dev/null 2>&1 || return 0
    local item="${AGENTSHROUD_OP_ITEM:-AgentShroud - $(hostname -s) [$(id -un)]}"
    local val
    # Try exact canonical name.
    val=$(op item get "$item" --vault "$OP_VAULT" --fields "$name" 2>/dev/null || true)
    [[ -n "$val" ]] && { echo "$val"; return; }
    # Try with + instead of _ (e.g. openai+api_key).
    val=$(op item get "$item" --vault "$OP_VAULT" --fields "${name//_/+}" 2>/dev/null || true)
    [[ -n "$val" ]] && { echo "$val"; return; }
    # Try with space instead of _ (e.g. "gateway password", "ssh key").
    val=$(op item get "$item" --vault "$OP_VAULT" --fields "${name//_/ }" 2>/dev/null || true)
    [[ -n "$val" ]] && echo "$val" || true
}

# ── Backend primitives ─────────────────────────────────────────────────────────
store_secret() {
    local name="$1" value="$2"
    case "$BACKEND" in
        keychain)
            keychain_store "${name}" "${value}"
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
        1password)
            # Explicit override only — never auto-detected as primary.
            op item edit "AgentShroud" "${name}[password]=${value}" --vault "$OP_VAULT" 2>/dev/null \
            || op item create \
                --category login \
                --title "AgentShroud" \
                --vault "$OP_VAULT" \
                "username=${name}" \
                "password=${value}"
            ;;
    esac
}

# get_secret cascades through all tiers: Keychain → secret-tool → 1Password → file.
# This order guarantees prompt-free reads over SSH once the Keychain is populated.
get_secret() {
    local name="$1"
    local val

    # Tier 1: macOS dedicated Keychain (always unlocked, no TTY needed).
    if [[ "$(uname)" == "Darwin" ]]; then
        ensure_keychain
        val=$(keychain_get "$name")
        [[ -n "$val" ]] && { echo "$val"; return; }
    fi

    # Tier 2: Linux secret-tool (libsecret).
    if command -v secret-tool &>/dev/null; then
        val=$(secret-tool lookup service agentshroud key "$name" 2>/dev/null || true)
        [[ -n "$val" ]] && { echo "$val"; return; }
    fi

    # Tier 3: 1Password non-interactive fallback (skipped if op not signed in).
    val=$(op_get "$name")
    [[ -n "$val" ]] && { echo "$val"; return; }

    # Tier 4: plain file fallback.
    case "$BACKEND" in
        homedir) cat "${SECRETS_HOME_DIR}/${name}.txt" 2>/dev/null || true ;;
        prompt)  cat "${SECRETS_DIR}/${name}.txt" 2>/dev/null || true ;;
    esac
}

# Extract the last non-empty line from stdin.
# Handles garbled multi-line blobs stored before the 017e7bd write-path fix —
# e.g. Keychain/homedir entries that captured TUI output (label + asterisks +
# real value) via $(read_secret_masked). The real secret is always on the last
# non-empty line; for clean single-line values the output is identical.
normalize_secret() {
    awk 'NF {last=$0} END {print last}'
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
# Format: "name|prompt|masked|optional|bot"
# masked:   yes = mask input with asterisks
# optional: yes = skip if empty (Enter to skip)
# bot:      all      = applies to all bots (shared infrastructure)
#           openclaw = applies only to OpenClaw
#           hermes   = applies only to Hermes
#
# Use --bot openclaw or --bot hermes with store/extract to limit the operation
# to a single bot's secrets plus all shared ("all") secrets.
declare -a SECRET_DEFS=(
    "anthropic_oauth_token|Claude OAuth token (sk-ant-oat01-...)|yes|no|all"
    "openai_api_key|OpenAI API key|yes|yes|all"
    "google_api_key|Google API key|yes|yes|all"
    "1password_bot_email|1Password account email|no|yes|all"
    "1password_bot_master_password|1Password master password|yes|yes|all"
    "1password_bot_secret_key|1Password secret key (A3-...)|yes|yes|all"
    "telegram_bot_token_production|Telegram bot token (production, OpenClaw)|yes|no|openclaw"
    "telegram_bot_token_marvin|Telegram bot token (marvin dev, OpenClaw)|yes|yes|openclaw"
    "telegram_bot_token_trillian|Telegram bot token (trillian dev, OpenClaw)|yes|yes|openclaw"
    "telegram_bot_token_rpi|Telegram bot token (rpi dev, OpenClaw)|yes|yes|openclaw"
    "slack_bot_token|OpenClaw Slack bot token (xoxb-...)|yes|yes|openclaw"
    "slack_signing_secret|OpenClaw Slack signing secret|yes|yes|openclaw"
    "slack_app_token|OpenClaw Slack app token (xapp-...)|yes|yes|openclaw"
    # Hermes Agent secrets (v1.1.0 — second bot)
    "hermes_telegram_bot_token|Hermes Telegram bot token (@agentshroud_hermes_bot)|yes|yes|hermes"
    "hermes_telegram_bot_token_marvin|Hermes Telegram bot token (marvin dev, @agentshroud_marvin_hermes_bot)|yes|yes|hermes"
    "slack_bot_token_hermes|Hermes Slack bot token (xoxb-...)|yes|yes|hermes"
    "slack_app_token_hermes|Hermes Slack app token (xapp-...)|yes|yes|hermes"
    "brave_api_key|Brave Search API key (shared with all bots)|yes|yes|all"
    "hermes_api_key|Hermes OpenAI API server key (random hex)|yes|yes|hermes"
    "github_pat|GitHub Personal Access Token (for Hermes GitHub MCP)|yes|yes|hermes"
)

# ── Bot filter helper ──────────────────────────────────────────────────────────
# Returns 0 (include) if the secret's bot tag matches the requested bot filter.
# BOT_FILTER="" or "all" → include everything.
# BOT_FILTER="openclaw" → include "openclaw" and "all" secrets.
# BOT_FILTER="hermes"   → include "hermes" and "all" secrets.
secret_matches_bot_filter() {
    local secret_bot="$1"
    local filter="${BOT_FILTER:-all}"
    [[ "$filter" == "all" ]] && return 0
    [[ "$secret_bot" == "all" ]] && return 0
    [[ "$secret_bot" == "$filter" ]] && return 0
    return 1
}

# ── gateway_password is auto-generated — not prompted ─────────────────────────
generate_gateway_password() {
    python3 -c "import secrets; print(secrets.token_hex(32), end='')"
}

# ── Subcommands ────────────────────────────────────────────────────────────────
cmd_store() {
    local bot_label="${BOT_FILTER:-all}"
    echo "╔═══════════════════════════════════════════╗"
    echo "║  AgentShroud — Store Secrets               ║"
    echo "║  Backend: ${BACKEND}$(printf '%*s' $((27 - ${#BACKEND})) '')║"
    [[ "$bot_label" != "all" ]] && echo "║  Bot filter: ${bot_label}$(printf '%*s' $((27 - ${#bot_label})) '')║"
    echo "╚═══════════════════════════════════════════╝"
    echo ""

    # Auto-generate gateway password
    gw_pass="$(generate_gateway_password)"
    store_secret "gateway_password" "$gw_pass"
    echo "  [stored] gateway_password (auto-generated)"

    for def in "${SECRET_DEFS[@]}"; do
        IFS='|' read -r name prompt masked optional secret_bot <<< "$def"
        # Skip secrets that don't match the bot filter
        secret_matches_bot_filter "${secret_bot:-all}" || continue
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
    local bot_label="${BOT_FILTER:-all}"
    echo "╔═══════════════════════════════════════════╗"
    echo "║  AgentShroud — Extract Secrets             ║"
    echo "║  Backend: ${BACKEND}$(printf '%*s' $((27 - ${#BACKEND})) '')║"
    [[ "$bot_label" != "all" ]] && echo "║  Bot filter: ${bot_label}$(printf '%*s' $((27 - ${#bot_label})) '')║"
    echo "╚═══════════════════════════════════════════╝"
    echo ""

    mkdir -p "${SECRETS_DIR}"

    # Build list of (name, optional) pairs. gateway_password is always required.
    declare -a extract_defs=("gateway_password|no")
    for def in "${SECRET_DEFS[@]}"; do
        IFS='|' read -r name _ _ optional secret_bot <<< "$def"
        secret_matches_bot_filter "${secret_bot:-all}" || continue
        extract_defs+=("${name}|${optional}")
    done

    ok=true
    for entry in "${extract_defs[@]}"; do
        IFS='|' read -r name optional <<< "$entry"
        value="$(get_secret "$name" | normalize_secret)"
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

cmd_migrate() {
    if [[ "$(uname)" != "Darwin" ]]; then
        echo "migrate is macOS-only (dedicated Keychain). On Linux, run 'store' to populate secret-tool." >&2
        exit 1
    fi

    local item="${AGENTSHROUD_OP_ITEM:-AgentShroud - $(hostname -s) [$(id -un)]}"
    echo "╔═══════════════════════════════════════════╗"
    echo "║  AgentShroud — Migrate Secrets to Keychain ║"
    echo "╚═══════════════════════════════════════════╝"
    echo ""
    echo "  Reading from: 1Password vault '${OP_VAULT}'"
    echo "               item '${item}'"
    echo "  Writing to:   ${AGENTSHROUD_KC} (never auto-locks)"
    echo ""
    echo "  1Password may prompt for approval once. After this migration,"
    echo "  all extract/deploy/restart runs will use the Keychain — no more prompts."
    echo ""

    ensure_keychain

    local all_names=("gateway_password")
    for def in "${SECRET_DEFS[@]}"; do
        IFS='|' read -r name _ _ _ _ <<< "$def"
        all_names+=("$name")
    done

    local migrated=0 missing=0
    for name in "${all_names[@]}"; do
        local val
        val=$(op_get "$name")
        if [[ -n "$val" ]]; then
            keychain_store "$name" "$val"
            echo "  [migrated] $name"
            migrated=$((migrated + 1))
        else
            echo "  [missing]  $name — not found in 1Password (run 'store' to add manually)"
            missing=$((missing + 1))
        fi
    done

    echo ""
    echo "Migration complete: ${migrated} migrated, ${missing} not found in 1Password."
    if [[ $missing -gt 0 ]]; then
        echo ""
        echo "For missing secrets, run: ./docker/setup-secrets.sh store"
        echo "to enter them and store directly in the Keychain."
    fi
    echo ""
    echo "From now on, './docker/setup-secrets.sh extract' runs prompt-free over SSH."
}

cmd_help() {
    cat <<'EOF'
setup-secrets.sh — Docker secrets manager for AgentShroud

Usage:
  ./setup-secrets.sh                         Interactive mode: prompt and write files directly
  ./setup-secrets.sh store                   Store ALL secrets in credential backend
  ./setup-secrets.sh store --bot openclaw    Store only OpenClaw + shared secrets
  ./setup-secrets.sh store --bot hermes      Store only Hermes + shared secrets
  ./setup-secrets.sh extract                 Extract ALL secrets → docker/secrets/*.txt
  ./setup-secrets.sh extract --bot openclaw  Extract only OpenClaw + shared secret files
  ./setup-secrets.sh extract --bot hermes    Extract only Hermes + shared secret files
  ./setup-secrets.sh migrate                 One-time: pull secrets from 1Password → Keychain
  ./setup-secrets.sh help                    Show this message

Bot values for --bot flag:
  openclaw   OpenClaw (primary bot) secrets only + shared infra secrets
  hermes     Hermes agent secrets only + shared infra secrets
  all        All secrets (default when --bot is omitted)

Credential backend (store writes to tier 1; get cascades all tiers):
  1. keychain     macOS dedicated agentshroud.keychain (never auto-locks, works over SSH)
  2. secretstore  Linux secret-tool / libsecret
  3. 1password    1Password CLI — non-interactive fallback (no biometric prompt)
  4. homedir      ~/.agentshroud/secrets/*.txt — file fallback

Override auto-detection: AGENTSHROUD_SECRET_BACKEND=keychain|secretstore|homedir|prompt
Override 1Password vault: AGENTSHROUD_OP_VAULT="Agent Shroud Bot Credentials"
Override 1Password item:  AGENTSHROUD_OP_ITEM="AgentShroud - marvin [agentshroud-bot]"

Typical first-time setup (all bots, new machine):
  1. ./setup-secrets.sh migrate    # pull from 1Password → Keychain (approve once)
  2. ./setup-secrets.sh extract    # write *.txt files Docker mounts need
  3. docker compose -f docker/docker-compose.yml up -d

First-time setup without 1Password (store directly):
  1. ./setup-secrets.sh store      # enter secrets; stored in Keychain
  2. ./setup-secrets.sh extract    # write *.txt files
  3. docker compose ... up -d

From any SSH session after migration:
  ./setup-secrets.sh extract   # prompt-free; reads from Keychain
EOF
}

# ── Dispatch ───────────────────────────────────────────────────────────────────
# Guard allows tests to `source` this script to access helpers without triggering dispatch.
if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    SUBCOMMAND="${1:-}"
    shift || true  # consume subcommand; remaining args parsed below

    # Parse optional --bot flag for store/extract subcommands.
    # Exported as BOT_FILTER so helper functions can read it.
    BOT_FILTER="all"
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --bot)
                shift
                BOT_FILTER="${1:-all}"
                case "$BOT_FILTER" in
                    openclaw|hermes|all) ;;
                    *)
                        echo "Invalid --bot value: '$BOT_FILTER'. Use: openclaw, hermes, all" >&2
                        exit 1
                        ;;
                esac
                shift
                ;;
            *)
                echo "Unknown argument: $1" >&2
                echo "Run './setup-secrets.sh help' for usage." >&2
                exit 1
                ;;
        esac
    done
    export BOT_FILTER

    case "$SUBCOMMAND" in
        store)   cmd_store ;;
        extract) cmd_extract ;;
        migrate) cmd_migrate ;;
        help|--help|-h) cmd_help ;;
        "")      cmd_interactive ;;
        *)
            echo "Unknown subcommand: $SUBCOMMAND" >&2
            echo "Run './setup-secrets.sh help' for usage." >&2
            exit 1
            ;;
    esac
fi
