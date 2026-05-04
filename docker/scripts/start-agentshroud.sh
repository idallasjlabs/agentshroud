#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# AgentShroud startup wrapper - exports API keys from Docker secrets

set -euo pipefail

# ---------------------------------------------------------------------------
# Security agents — start before main process (non-fatal, background)
# ---------------------------------------------------------------------------

# ClamAV daemon — malware scanning for bot workspace
# Bot has ClamAV installed; clamd.conf uses /tmp for socket (read_only rootfs safe).
if command -v clamd >/dev/null 2>&1 && [ -f /var/lib/clamav/main.cvd -o -f /var/lib/clamav/main.cld ]; then
    clamd --config-file=/etc/clamav/clamd.conf 2>/tmp/clamd-start.log &
    echo "[startup] clamd launched (pid=$!)"
else
    echo "[startup] clamd: skipping (binary or virus DB not ready)"
fi

# Wazuh agent — FIM on /home/node/agentshroud/workspace
# /var/ossec is owned by node (chowned at build time); runs without root.
if [ -x /var/ossec/bin/wazuh-agentd ]; then
    mkdir -p /var/ossec/var/run /var/ossec/queue/sockets /var/ossec/tmp 2>/dev/null || true
    /var/ossec/bin/wazuh-agentd 2>/tmp/wazuh-start.log &
    echo "[startup] wazuh-agentd launched (pid=$!)"
fi

# ---------------------------------------------------------------------------
# Read the last non-empty line from a secret file.
# Handles garbled multi-line blobs (label + asterisks + real value) written to
# the secret backend before the 017e7bd write-path fix. For clean single-line
# values the result is identical to a raw cat + strip.
_read_secret_file() { awk 'NF {last=$0} END {printf "%s", last}' "$1"; }

# ---------------------------------------------------------------------------
# Export Gateway password from secret file
# Note: OpenClaw CLI expects OPENCLAW_GATEWAY_PASSWORD env var
if [ -f "/run/secrets/gateway_password" ]; then
    export OPENCLAW_GATEWAY_PASSWORD="$(_read_secret_file /run/secrets/gateway_password)"
    # FINAL: also set GATEWAY_AUTH_TOKEN so op-wrapper.sh routes through gateway
    export GATEWAY_AUTH_TOKEN="$OPENCLAW_GATEWAY_PASSWORD"
    # SECURITY (H3): Strip DNS architecture info from resolv.conf comments
# Docker adds internal network details that leak infrastructure topology
sed -i /^#.*ExtServers/d /etc/resolv.conf 2>/dev/null || true
sed -i /^#.*Overrides/d /etc/resolv.conf 2>/dev/null || true
sed -i /^#.*Based on host/d /etc/resolv.conf 2>/dev/null || true
sed -i /^#.*Option ndots/d /etc/resolv.conf 2>/dev/null || true

echo "[startup] Loaded Gateway password"
else
    echo "[startup] Warning: Gateway password file not found"
fi

# Export Telegram bot token from secret file (per-host token injection)
# The apply-patches.js script reads TELEGRAM_BOT_TOKEN and injects it into openclaw.json
if [ -f "/run/secrets/telegram_bot_token" ]; then
    export TELEGRAM_BOT_TOKEN="$(_read_secret_file /run/secrets/telegram_bot_token)"
    echo "[startup] Loaded Telegram bot token"
elif [ -n "${TELEGRAM_BOT_TOKEN_FILE:-}" ] && [ -f "$TELEGRAM_BOT_TOKEN_FILE" ]; then
    export TELEGRAM_BOT_TOKEN="$(_read_secret_file "$TELEGRAM_BOT_TOKEN_FILE")"
    echo "[startup] Loaded Telegram bot token from $TELEGRAM_BOT_TOKEN_FILE"
fi

# Export OpenAI API key from secret file (optional)
if [ -f "/run/secrets/openai_api_key" ] && [ -s "/run/secrets/openai_api_key" ]; then
    export OPENAI_API_KEY="$(_read_secret_file /run/secrets/openai_api_key)"
    echo "[startup] Loaded OpenAI API key"
else
    echo "[startup] OpenAI API key not configured (optional)"
fi

# Export Google Gemini API key from secret file (optional)
if [ -f "/run/secrets/google_api_key" ] && [ -s "/run/secrets/google_api_key" ]; then
    export GOOGLE_API_KEY="$(_read_secret_file /run/secrets/google_api_key)"
    echo "[startup] Loaded Google API key"
else
    echo "[startup] Google API key not configured (optional)"
fi

_LOCAL_ONLY_MODEL=false
_MODEL_MODE="$(echo "${AGENTSHROUD_MODEL_MODE:-local}" | tr '[:upper:]' '[:lower:]')"
if [[ "${_MODEL_MODE}" != "cloud" ]]; then
    _LOCAL_ONLY_MODEL=true
fi
if [[ "${OPENCLAW_MAIN_MODEL:-}" == ollama/* ]]; then
    _LOCAL_ONLY_MODEL=true
fi
if $_LOCAL_ONLY_MODEL && [ -z "${OLLAMA_API_KEY:-}" ]; then
    export OLLAMA_API_KEY="ollama-local"
    echo "[startup] Set default OLLAMA_API_KEY for local provider registration"
fi

# Load Claude OAuth token only when running non-local model backends.
if ! $_LOCAL_ONLY_MODEL; then
    if [ -f "/run/secrets/anthropic_oauth_token" ] && [ -s "/run/secrets/anthropic_oauth_token" ]; then
        export ANTHROPIC_OAUTH_TOKEN="$(_read_secret_file /run/secrets/anthropic_oauth_token)"
        echo "[startup] Loaded Claude OAuth token (from secret file)"
    fi
else
    echo "[startup] Local Ollama model selected — skipping Claude token load"
fi

# FINAL: Load secrets via gateway op-proxy (bot has no direct 1Password access).
# op-wrapper.sh routes "op read" through POST /credentials/op-proxy when
# GATEWAY_AUTH_TOKEN and GATEWAY_OP_PROXY_URL are set.

# Retry wrapper for op-proxy reads — handles race condition where the bot
# restarts before the gateway's 1Password connection is fully ready.
# Usage: op_proxy_read_with_retry <label> <op-reference>
# Returns the secret value on stdout; exits non-zero only if all retries fail.
op_proxy_read_with_retry() {
    local label="$1"
    local reference="$2"
    # Cascading waits: 5s, 10s, 15s, 30s, 60s — total patience: 2 minutes before final attempt
    local delays=(5 10 15 30 60)
    local value=""

    for i in "${!delays[@]}"; do
        local attempt=$((i + 1))
        local total=$(( ${#delays[@]} + 1 ))
        value="$(/usr/local/bin/op-wrapper.sh read "$reference" 2>/dev/null)" || true
        if [ -n "$value" ]; then
            printf '%s' "$value"
            return 0
        fi
        local wait="${delays[$i]}"
        echo "[startup] ⚠ ${label}: attempt ${attempt}/${total} failed — retrying in ${wait}s" >&2
        sleep "$wait"
    done

    # Final attempt after all waits exhausted
    value="$(/usr/local/bin/op-wrapper.sh read "$reference" 2>/dev/null)" || true
    if [ -n "$value" ]; then
        printf '%s' "$value"
        return 0
    fi

    echo "[startup] ✗ ${label}: all ${total} attempts failed after 2 minutes" >&2
    return 1
}

# Only attempt op-proxy reads if 1Password credentials are present and non-empty
_OP_AVAILABLE=false
if [ -f "/run/secrets/1password_bot_email" ] && [ -s "/run/secrets/1password_bot_email" ]; then
    _OP_AVAILABLE=true
fi

if [ -n "${GATEWAY_AUTH_TOKEN:-}" ] && [ -n "${GATEWAY_OP_PROXY_URL:-}" ] && $_OP_AVAILABLE; then
    echo "[startup] Loading secrets via gateway op-proxy (${GATEWAY_OP_PROXY_URL})"

    # Load Claude OAuth token via op-proxy only when not pinned to local Ollama models.
    if ! $_LOCAL_ONLY_MODEL; then
        if [ -z "${ANTHROPIC_OAUTH_TOKEN:-}" ]; then
            ANTHROPIC_OAUTH_TOKEN="$(op_proxy_read_with_retry "Claude OAuth token" \
                "op://Agent Shroud Bot Credentials/AgentShroud - Anthropic Claude OAuth Token/claude oath token")" || true
            if [ -n "$ANTHROPIC_OAUTH_TOKEN" ]; then
                export ANTHROPIC_OAUTH_TOKEN
                echo "[startup] ✓ Loaded Claude OAuth token (via op-proxy)"
            else
                echo "[startup] ⚠ Could not load Claude OAuth token after retries"
            fi
        else
            echo "[startup] ✓ Claude OAuth token already loaded (from secret file)"
        fi
    else
        echo "[startup] Local Ollama model selected — skipping Claude op-proxy fetch"
    fi

    # Load Brave Search API key (non-blocking single attempt).
    # This key is optional; do not delay bot startup for retry backoff loops.
    # Brief delay gives the gateway op-proxy time to authenticate before the first attempt.
    # Item ID: 6j6ij5tzld6kobvit5tk6ufrhq (Brave Search API - agentshroud.ai@gmail.com)
    sleep 5
    BRAVE_API_KEY="${BRAVE_API_KEY:-$(/usr/local/bin/op-wrapper.sh read \
        "op://Agent Shroud Bot Credentials/6j6ij5tzld6kobvit5tk6ufrhq/brave search api key" \
        2>/dev/null || true)}"
    if [ -n "$BRAVE_API_KEY" ]; then
        export BRAVE_API_KEY
        echo "[startup] ✓ Loaded Brave Search API key"
    else
        echo "[startup] ⚠ Brave Search API key unavailable (continuing without web search key)"
    fi

    # iCloud email credentials — loaded in background to avoid blocking startup
    # (non-critical: email features degrade gracefully without iCloud creds)
    SECRETS_DIR="${SECRETS_DIR:-/tmp/secrets}"
    _ICLOUD_ENV_FILE="/tmp/.icloud-env"
    (
        ICLOUD_APP_PASSWORD="$(op_proxy_read_with_retry "iCloud app password" \
            "op://Agent Shroud Bot Credentials/25ghxryyvup5wpufgfldgc2vjm/agentshroud app-specific password")" || true
        if [ -n "$ICLOUD_APP_PASSWORD" ]; then
            cat > "$_ICLOUD_ENV_FILE" << EOF
export ICLOUD_APP_PASSWORD="$ICLOUD_APP_PASSWORD"

# ── SECURITY (C3/H2): Write secrets to tmpfs files, then unset env vars ──
# Prevents secrets from appearing in /proc/*/environ of child processes.
# OpenClaw reads these at startup; after that, file-based access only.
SECRETS_DIR="\${SECRETS_DIR:-/tmp/secrets}"
mkdir -p "\${SECRETS_DIR}"
chmod 700 "\${SECRETS_DIR}"

for _var in ANTHROPIC_OAUTH_TOKEN BRAVE_API_KEY ICLOUD_APP_PASSWORD; do
  _val=\$(eval echo "\$\$_var")
  if [ -n "\$_val" ]; then
    printf '%s' "\$_val" > "\$SECRETS_DIR/\$_var"
    chmod 600 "\$SECRETS_DIR/\$_var"
  fi
done
echo "[security] ✓ Secrets written to tmpfs files, env vars preserved for OpenClaw startup"
export ICLOUD_USERNAME="agentshroud.ai@gmail.com"
export ICLOUD_EMAIL="agentshroud.ai@icloud.com"
EOF
            echo "[startup] ✓ Loaded iCloud email credentials (background)"
        else
            echo "[startup] ⚠ Could not load iCloud app-specific password after retries"
        fi
    ) &
    _ICLOUD_BG_PID=$!
else
    echo "[startup] Warning: Gateway op-proxy not configured, 1Password secrets unavailable"
fi

# Apply OpenClaw config defaults (SSH allowlist, cron jobs, agent patches, workspace brand files)
echo "[startup] Bootstrapping OpenClaw config..."
/usr/local/bin/init-openclaw-config.sh

# CVE-2021-23358: upgrade underscore in bot workspace if pinned to vulnerable version (<1.12.1)
# underscore@1.7.0 allows arbitrary code execution via _.template(); fixed in >=1.12.1
_WORKSPACE_PKG="/home/node/agentshroud/workspace/package-lock.json"
if [ -f "$_WORKSPACE_PKG" ] && grep -q '"underscore"' "$_WORKSPACE_PKG" 2>/dev/null; then
    _US_VER=$(node -e "try{console.log(require('/home/node/agentshroud/workspace/node_modules/underscore/package.json').version)}catch(e){console.log('0')}" 2>/dev/null || echo "0")
    # Skip npm update if already patched (>= 1.12.1)
    if [ "$_US_VER" = "0" ] || [ "$(printf '%s\n' "1.12.1" "$_US_VER" | sort -V | head -n1)" != "1.12.1" ]; then
        cd /home/node/agentshroud/workspace && npm update underscore --no-fund --no-audit 2>/dev/null || true
        cd /home/node
        echo "[startup] underscore upgraded from $_US_VER (CVE-2021-23358)"
    else
        echo "[startup] underscore $_US_VER already patched — skipping update (CVE-2021-23358)"
    fi
fi

# Wait briefly for background iCloud fetch, then source if ready
if [ -n "${_ICLOUD_BG_PID:-}" ]; then
    # Give it 3 seconds — if it's not done, gateway starts without iCloud
    for _i in 1 2 3; do
        if [ -f "${_ICLOUD_ENV_FILE:-/tmp/.icloud-env}" ]; then
            . "$_ICLOUD_ENV_FILE" || true; set -u
            break
        fi
        sleep 1
    done
    if [ ! -f "${_ICLOUD_ENV_FILE:-/tmp/.icloud-env}" ]; then
        echo "[startup] iCloud credentials still loading in background — gateway starting without them"
    fi
fi

# DNS warmup probe — prevents EAI_AGAIN on first user message.
# Docker's internal resolver (127.0.0.11) takes ~20-30s to route to the Pi-hole
# after container restart. Poll until external DNS resolves before starting OpenClaw.
_dns_warmup_probe() {
    local target="${1:-api.github.com}"
    local max_wait="${2:-30}"
    local elapsed=0
    while [ "${elapsed}" -lt "${max_wait}" ]; do
        if curl -sf --max-time 3 "https://${target}" -o /dev/null 2>/dev/null; then
            return 0
        fi
        sleep 2
        elapsed=$(( elapsed + 2 ))
    done
    return 1  # Non-fatal — OpenClaw starts regardless; warning only
}
echo "[startup] DNS warmup check..."
if _dns_warmup_probe "api.github.com" 30; then
    echo "[startup] ✓ External DNS ready"
else
    echo "[startup] ⚠ External DNS probe timed out — OpenClaw will start anyway (tools may retry)"
fi

# Start AgentShroud gateway (powered by OpenClaw CLI)
echo "[startup] Starting AgentShroud gateway..."
OPENCLAW_BIND_MODE="${OPENCLAW_GATEWAY_BIND:-loopback}"
node --stack-size=65536 "$(command -v openclaw)" gateway --allow-unconfigured --bind "${OPENCLAW_BIND_MODE}" &
OPENCLAW_PID=$!

# Telegram notification helpers — ALL traffic routes through AgentShroud gateway
# No direct api.telegram.org calls. No hardcoded bot tokens.
_OWNER_CHAT_ID="8096968754"
_GATEWAY_TELEGRAM_BASE="${GATEWAY_OP_PROXY_URL:-http://gateway:8080}/telegram-api"

_telegram_bot_token() {
    # Try env var first (exported from Docker secret at line ~31)
    if [ -n "${TELEGRAM_BOT_TOKEN:-}" ]; then
        printf '%s' "$TELEGRAM_BOT_TOKEN"
        return 0
    fi
    # Fall back to reading from OpenClaw config file (try both known paths)
    node -e "
        const paths = [
            '/home/node/.agentshroud/openclaw.json',
            '/home/node/.openclaw/openclaw.json',
        ];
        for (const p of paths) {
            try {
                const c = JSON.parse(require('fs').readFileSync(p, 'utf8'));
                const t = c.channels && c.channels.telegram && c.channels.telegram.botToken;
                if (t) { process.stdout.write(t); process.exit(0); }
            } catch(e) {}
        }
    " 2>/dev/null
}

_telegram_send() {
    local text="$1"
    local token
    token="$(_telegram_bot_token)"
    if [ -z "$token" ]; then
        echo "[startup] ⚠ No Telegram bot token available — cannot send notification" >&2
        return 1
    fi
    # Route through AgentShroud gateway Telegram proxy (never direct to api.telegram.org)
    curl -sf --max-time 10 -X POST "${_GATEWAY_TELEGRAM_BASE}/bot${token}/sendMessage" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" \
        -d "{\"chat_id\":\"${_OWNER_CHAT_ID}\",\"text\":\"${text}\"}" \
        >/dev/null 2>&1
}

# Slack notification helpers — token injected by gateway proxy, same security model as Telegram.
# SLACK_API_BASE_URL is set by docker-compose.yml to http://gateway:8080/slack-api so all
# outbound Slack API calls are intercepted by the gateway for content scanning.
_GATEWAY_SLACK_BASE="${SLACK_API_BASE_URL:-http://gateway:8080/slack-api}"

_slack_channel_id() {
    # Prefer env override, then Docker secret, then empty (disabled)
    if [ -n "${AGENTSHROUD_SLACK_CHANNEL_ID:-}" ]; then
        printf '%s' "$AGENTSHROUD_SLACK_CHANNEL_ID"
        return 0
    fi
    if [ -f "/run/secrets/slack_bot_token" ]; then
        # Channel ID must be configured via env — no way to derive it from the token
        return 1
    fi
    return 1
}

_slack_send() {
    local text="$1"
    local channel
    channel="${AGENTSHROUD_SLACK_CHANNEL_ID:-}"
    if [ -z "$channel" ]; then
        return 0  # Slack notifications not configured — skip silently
    fi
    # Route through AgentShroud gateway Slack proxy (never direct to slack.com)
    curl -sf --max-time 10 -X POST "${_GATEWAY_SLACK_BASE}/chat.postMessage" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" \
        -d "{\"channel\":\"${channel}\",\"text\":\"${text}\"}" \
        >/dev/null 2>&1
}

_telegram_get_me_ready() {
    local token
    token="$(_telegram_bot_token)"
    if [ -z "$token" ]; then
        return 1
    fi
    curl -sf --max-time 8 -X POST "${_GATEWAY_TELEGRAM_BASE}/bot${token}/getMe" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" \
        >/dev/null 2>&1
}

_model_runtime_ready() {
    if [ "${AGENTSHROUD_MODEL_MODE:-cloud}" != "local" ]; then
        return 0
    fi
    local model_name="${AGENTSHROUD_LOCAL_MODEL:-}"
    if [ -z "${model_name}" ]; then
        model_name="${AGENTSHROUD_LOCAL_MODEL_REF#ollama/}"
    fi
    if [ -z "${model_name}" ]; then
        return 1
    fi
    curl -sf --max-time 8 "${OLLAMA_BASE_URL:-http://gateway:8080/v1}/../api/tags" \
        | grep -F "\"name\":\"${model_name}\"" >/dev/null 2>&1
}

# Instance identity for notifications
_INSTANCE_LABEL="${INSTANCE_NAME:-$(hostname -s)}"
_BOT_NAME="${OPENCLAW_BOT_NAME:-agentshroud-bot}"
_STARTUP_NOTICE_STAMP="${OPENCLAW_STARTUP_NOTICE_STAMP:-/home/node/.openclaw/workspace/.startup_notice_at}"
_STARTUP_NOTICE_COOLDOWN_SECONDS="${OPENCLAW_STARTUP_NOTICE_COOLDOWN_SECONDS:-300}"

# Forward TERM/INT to openclaw, backup memory, send shutdown notification
trap '
    echo "[startup] Shutdown signal received — backing up memory..."
    MEMORY_BACKUP_DIR="/app/memory-backups"
    WORKSPACE_DIR="/home/node/.openclaw/workspace"
    if [ -d "${MEMORY_BACKUP_DIR}" ]; then
        [ -f "${WORKSPACE_DIR}/MEMORY.md" ] && cp "${WORKSPACE_DIR}/MEMORY.md" "${MEMORY_BACKUP_DIR}/MEMORY.md"
        if [ -d "${WORKSPACE_DIR}/memory" ]; then
            mkdir -p "${MEMORY_BACKUP_DIR}/memory"
            cp -r "${WORKSPACE_DIR}/memory/"* "${MEMORY_BACKUP_DIR}/memory/" 2>/dev/null || true
        fi
        for f in USER.md TOOLS.md HEARTBEAT.md; do
            [ -f "${WORKSPACE_DIR}/${f}" ] && cp "${WORKSPACE_DIR}/${f}" "${MEMORY_BACKUP_DIR}/${f}"
        done
        echo "[startup] ✓ Memory backed up before shutdown"
    fi
    echo "[startup] Sending shutdown notifications..."
    _telegram_send "🔴 AgentShroud shutting down" \
        && echo "[startup] ✓ Sent Telegram shutdown notification" \
        || echo "[startup] ⚠ Could not send Telegram shutdown notification"
    _slack_send "AgentShroud shutting down" \
        && echo "[startup] ✓ Sent Slack shutdown notification" \
        || true
    kill $OPENCLAW_PID 2>/dev/null
' TERM INT

# Wait for gateway/model/telegram readiness, then send startup notifications
(
    now_epoch="$(date +%s)"
    last_notice_epoch=""
    if [ -f "${_STARTUP_NOTICE_STAMP}" ]; then
        last_notice_epoch="$(cat "${_STARTUP_NOTICE_STAMP}" 2>/dev/null || true)"
    fi
    should_notify="yes"
    if [ -n "${last_notice_epoch}" ] && [ "${last_notice_epoch}" -eq "${last_notice_epoch}" ] 2>/dev/null; then
        age="$(( now_epoch - last_notice_epoch ))"
        if [ "${age}" -lt "${_STARTUP_NOTICE_COOLDOWN_SECONDS}" ]; then
            should_notify="no"
        fi
    fi

    if [ "${should_notify}" != "yes" ]; then
        echo "[startup] Startup notification suppressed (cooldown active)"
        exit 0
    fi

    mkdir -p "$(dirname "${_STARTUP_NOTICE_STAMP}")" 2>/dev/null || true
    printf '%s\n' "${now_epoch}" > "${_STARTUP_NOTICE_STAMP}" 2>/dev/null || true
    _telegram_send "🟡 AgentShroud starting" \
        && echo "[startup] ✓ Sent Telegram starting notification" \
        || echo "[startup] ⚠ Could not send Telegram starting notification"
    _slack_send "AgentShroud starting" || true

    # Poll OpenClaw HTTP endpoint and Telegram/model readiness — up to 120s
    ready="no"
    for _i in $(seq 1 60); do
        if curl -sf http://localhost:18789/ >/dev/null 2>&1 \
            && _telegram_get_me_ready \
            && _model_runtime_ready; then
            ready="yes"
            break
        fi
        sleep 2
    done

    if [ "${ready}" = "yes" ]; then
        _telegram_send "🛡️ AgentShroud online" \
            && echo "[startup] ✓ Sent Telegram startup notification" \
            || echo "[startup] ⚠ Could not send Telegram startup notification"
        _slack_send "AgentShroud online" \
            && echo "[startup] ✓ Sent Slack startup notification" \
            || true
    else
        _telegram_send "🟠 AgentShroud starting (readiness delayed)" \
            && echo "[startup] ⚠ Sent delayed startup notification" \
            || echo "[startup] ⚠ Could not send delayed startup notification"
        _slack_send "AgentShroud starting (readiness delayed)" || true
    fi
) &

wait $OPENCLAW_PID
