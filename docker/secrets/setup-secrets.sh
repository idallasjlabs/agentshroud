#!/usr/bin/env bash
# setup-secrets.sh — Interactive Docker secrets creator for AgentShroud
# Generates all required secret files for docker-compose.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "╔═══════════════════════════════════════╗"
echo "║  AgentShroud — Docker Secrets Setup    ║"
echo "╚═══════════════════════════════════════╝"
echo ""

read_secret() {
    local prompt="$1" file="$2" optional="${3:-}"
    if [[ "$optional" == "optional" ]]; then
        read -rp "$prompt (press Enter to skip): " value
        [[ -z "$value" ]] && return
    else
        read -rp "$prompt: " value
        if [[ -z "$value" ]]; then
            echo "Error: value required." >&2
            exit 1
        fi
    fi
    printf %s "$value" > "$file"
    chmod 600 "$file"
    echo "  ✅ $file"
}

# Like read_secret but masks input with asterisks as you type
read_secret_masked() {
    local prompt="$1" file="$2" optional="${3:-}"
    local value="" char
    if [[ "$optional" == "optional" ]]; then
        printf "%s (press Enter to skip): " "$prompt"
    else
        printf "%s: " "$prompt"
    fi
    while IFS= read -r -s -n1 char; do
        if [[ "$char" == $'\0' || "$char" == $'\n' ]]; then
            break
        elif [[ "$char" == $'\177' || "$char" == $'\b' ]]; then
            if [[ ${#value} -gt 0 ]]; then
                value="${value%?}"
                printf '\b \b'
            fi
        else
            value+="$char"
            printf '*'
        fi
    done
    printf '\n'
    if [[ -z "$value" ]]; then
        [[ "$optional" == "optional" ]] && return
        echo "Error: value required." >&2
        exit 1
    fi
    printf %s "$value" > "$file"
    chmod 600 "$file"
    echo "  ✅ $file"
}

# Required secrets
echo "── Required secrets ──"
read_secret_masked "Claude OAuth token (sk-ant-oat01-...)" "anthropic_oauth_token.txt"
read_secret "OpenAI API key" "openai_api_key.txt" optional

# Auto-generate gateway password
python3 -c "import secrets; print(secrets.token_hex(32), end='')" > gateway_password.txt
chmod 600 gateway_password.txt
echo "  ✅ gateway_password.txt (auto-generated)"

# Optional 1Password secrets
echo ""
echo "── 1Password secrets (optional) ──"
read_secret "1Password bot email" "1password_bot_email.txt" optional
read_secret "1Password bot master password" "1password_bot_master_password.txt" optional
read_secret "1Password bot secret key" "1password_bot_secret_key.txt" optional

# Validate
echo ""
echo "── Validation ──"
ok=true
for f in anthropic_oauth_token.txt gateway_password.txt; do
    if [[ -f "$f" && -s "$f" ]]; then
        echo "  ✅ $f exists"
    else
        echo "  ❌ $f missing or empty"
        ok=false
    fi
done

if $ok; then
    echo ""
    echo "All required secrets created. Gateway password:"
    echo "  $(cat gateway_password.txt)"
    echo ""
    echo "Next: edit agentshroud.yaml and run docker compose up -d"
else
    echo ""
    echo "Some secrets are missing. Re-run this script."
    exit 1
fi
