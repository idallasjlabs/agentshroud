#!/bin/bash
# SecureClaw Kill Switch
# Emergency shutdown with optional credential revocation
#
# Usage:
#   ./killswitch.sh freeze      - Pause containers (preserve state for forensics)
#   ./killswitch.sh shutdown    - Stop containers (preserve volumes)
#   ./killswitch.sh disconnect  - Nuclear option (stop + export ledger + clear credentials)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCKER_DIR="$(dirname "$SCRIPT_DIR")"
INCIDENTS_DIR="$DOCKER_DIR/incidents"
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m'

MODE="${1:-}"

usage() {
    echo "SecureClaw Kill Switch - Emergency Shutdown"
    echo ""
    echo "Usage: $0 <mode>"
    echo ""
    echo "Modes:"
    echo "  freeze      - Pause containers immediately (preserve state for forensics)"
    echo "  shutdown    - Stop containers gracefully (preserve volumes)"
    echo "  disconnect  - Nuclear option (stop + export audit ledger + clear credentials)"
    echo ""
    echo "Examples:"
    echo "  $0 freeze      # Quick freeze for investigation"
    echo "  $0 shutdown    # Graceful shutdown"
    echo "  $0 disconnect  # Complete disconnection with credential wipe"
    exit 1
}

if [ -z "$MODE" ]; then
    usage
fi

case "$MODE" in
    freeze|shutdown|disconnect)
        ;;
    *)
        echo -e "${RED}Error:${NC} Invalid mode: $MODE"
        usage
        ;;
esac

confirm() {
    local prompt="$1"
    read -p "$(echo -e "${YELLOW}$prompt${NC} (yes/no): ")" response
    case "$response" in
        [yY][eE][sS]|[yY])
            return 0
            ;;
        *)
            echo "Aborted."
            exit 0
            ;;
    esac
}

# Mode-specific confirmation
case "$MODE" in
    freeze)
        confirm "Freeze SecureClaw containers?"
        ;;
    shutdown)
        confirm "Shutdown SecureClaw containers?"
        ;;
    disconnect)
        echo -e "${RED}WARNING: DISCONNECT MODE${NC}"
        echo "This will:"
        echo "  1. Stop all containers"
        echo "  2. Export audit ledger"
        echo "  3. Clear cached API keys from volumes"
        echo "  4. Overwrite secret files"
        echo "  5. Generate incident report"
        echo ""
        confirm "Are you ABSOLUTELY SURE you want to disconnect?"
        read -p "$(echo -e "${RED}Type 'DISCONNECT' to confirm:${NC} ")" double_confirm
        if [ "$double_confirm" != "DISCONNECT" ]; then
            echo "Aborted."
            exit 0
        fi
        ;;
esac

echo ""
echo "======================================"
echo "SecureClaw Kill Switch - $MODE"
echo "======================================"
echo ""

# Execute kill switch action
case "$MODE" in
    freeze)
        echo "[1/2] Freezing containers..."
        docker compose -f "$DOCKER_DIR/docker-compose.yml" pause
        echo -e "${GREEN}✓${NC} Containers frozen"

        echo ""
        echo "[2/2] Containers are now paused for forensic analysis"
        echo ""
        echo "To resume:  docker compose -f $DOCKER_DIR/docker-compose.yml unpause"
        echo "To inspect: docker exec openclaw-bot /bin/bash"
        echo "            docker logs openclaw-bot"
        echo ""
        ;;

    shutdown)
        echo "[1/3] Stopping containers gracefully..."
        docker compose -f "$DOCKER_DIR/docker-compose.yml" down
        echo -e "${GREEN}✓${NC} Containers stopped"

        echo ""
        echo "[2/3] Checking volumes..."
        docker volume ls | grep -E "(openclaw|gateway)" || true
        echo -e "${GREEN}✓${NC} Volumes preserved"

        echo ""
        echo "[3/3] Shutdown complete"
        echo ""
        echo "Data is preserved in Docker volumes."
        echo "To restart:  docker compose -f $DOCKER_DIR/docker-compose.yml up -d"
        echo ""
        ;;

    disconnect)
        # Create incidents directory
        mkdir -p "$INCIDENTS_DIR"

        INCIDENT_REPORT="$INCIDENTS_DIR/incident-$TIMESTAMP.md"

        echo "[1/7] Exporting audit ledger..."
        LEDGER_EXPORT="$INCIDENTS_DIR/ledger-export-$TIMESTAMP.db"

        if docker cp secureclaw-gateway:/app/data/ledger.db "$LEDGER_EXPORT" 2>/dev/null; then
            echo -e "${GREEN}✓${NC} Audit ledger exported to: $LEDGER_EXPORT"
        else
            echo -e "${YELLOW}⚠${NC} Could not export audit ledger (container may not be running)"
        fi

        echo ""
        echo "[2/7] Stopping containers..."
        docker compose -f "$DOCKER_DIR/docker-compose.yml" down
        echo -e "${GREEN}✓${NC} Containers stopped"

        echo ""
        echo "[3/7] Clearing cached credentials from volumes..."

        # Remove API keys from OpenClaw config volume
        docker run --rm -v oneclaw_openclaw-config:/data alpine sh -c \
            "find /data -type f -name '*.key' -o -name '*api*' -o -name '*token*' | xargs rm -f" 2>/dev/null || true
        echo -e "${GREEN}✓${NC} Cleared cached credentials from volumes"

        echo ""
        echo "[4/7] Overwriting secret files..."

        # Overwrite secret files (do not delete - needed for docker-compose)
        if [ -f "$DOCKER_DIR/secrets/openai_api_key.txt" ]; then
            dd if=/dev/urandom of="$DOCKER_DIR/secrets/openai_api_key.txt" bs=1 count=32 status=none
            echo "REVOKED_$(date +%s)" > "$DOCKER_DIR/secrets/openai_api_key.txt"
        fi

        if [ -f "$DOCKER_DIR/secrets/anthropic_api_key.txt" ]; then
            dd if=/dev/urandom of="$DOCKER_DIR/secrets/anthropic_api_key.txt" bs=1 count=32 status=none
            echo "REVOKED_$(date +%s)" > "$DOCKER_DIR/secrets/anthropic_api_key.txt"
        fi

        if [ -f "$DOCKER_DIR/secrets/gateway_password.txt" ]; then
            dd if=/dev/urandom of="$DOCKER_DIR/secrets/gateway_password.txt" bs=1 count=32 status=none
            echo "REVOKED_$(date +%s)" > "$DOCKER_DIR/secrets/gateway_password.txt"
        fi

        echo -e "${GREEN}✓${NC} Secret files overwritten"

        echo ""
        echo "[5/7] Generating incident report..."

        cat > "$INCIDENT_REPORT" <<EOF
# SecureClaw Security Incident Report

**Date:** $(date)
**Action:** Kill Switch - DISCONNECT
**Operator:** $(whoami)@$(hostname)

## Summary

The SecureClaw kill switch was activated in DISCONNECT mode. All containers have been stopped, credentials cleared, and audit logs exported.

## Actions Taken

1. ✓ Audit ledger exported to: \`$LEDGER_EXPORT\`
2. ✓ Containers stopped
3. ✓ Cached credentials cleared from Docker volumes
4. ✓ Secret files overwritten
5. ✓ Incident report generated

## Manual Revocation Required

You MUST manually revoke the following credentials:

### OpenAI API Key
1. Go to: https://platform.openai.com/api-keys
2. Find the key used for SecureClaw (check \`$LEDGER_EXPORT\` for recent usage)
3. Click "Revoke" to invalidate the key

### Anthropic API Key
1. Go to: https://console.anthropic.com/settings/keys
2. Find the key used for SecureClaw
3. Delete the key to invalidate it

### 1Password Session (if applicable)
1. Go to: https://my.1password.com/
2. Sign in and go to Settings > Active Sessions
3. Revoke any sessions from "therealidallasj_bot"

### Telegram Bot Token (if needed)
1. Message @BotFather on Telegram
2. Send: /revoke
3. Select: @therealidallasj_bot
4. Confirm revocation

## Next Steps

1. [ ] Investigate the reason for kill switch activation
2. [ ] Review audit ledger: \`sqlite3 $LEDGER_EXPORT\`
3. [ ] Manually revoke all API keys (see above)
4. [ ] Generate new credentials
5. [ ] Update secret files in \`docker/secrets/\`
6. [ ] Restart containers only when safe: \`docker compose -f docker/docker-compose.yml up -d\`

## Container State at Time of Disconnect

### Gateway Container
\`\`\`
$(docker inspect secureclaw-gateway 2>/dev/null || echo "Container not found")
\`\`\`

### OpenClaw Container
\`\`\`
$(docker inspect openclaw-bot 2>/dev/null || echo "Container not found")
\`\`\`

## Recent Logs

### Gateway Logs (last 50 lines)
\`\`\`
$(docker logs --tail 50 secureclaw-gateway 2>/dev/null || echo "No logs available")
\`\`\`

### OpenClaw Logs (last 50 lines)
\`\`\`
$(docker logs --tail 50 openclaw-bot 2>/dev/null || echo "No logs available")
\`\`\`

---

**Report generated:** $(date)
**Report location:** $INCIDENT_REPORT
EOF

        echo -e "${GREEN}✓${NC} Incident report generated: $INCIDENT_REPORT"

        echo ""
        echo "[6/7] System state:"
        echo "  • Containers: STOPPED"
        echo "  • Volumes: PRESERVED (but credentials cleared)"
        echo "  • Audit ledger: EXPORTED"
        echo "  • Secret files: OVERWRITTEN"
        echo ""

        echo "[7/7] MANUAL ACTIONS REQUIRED"
        echo ""
        echo -e "${RED}⚠ YOU MUST MANUALLY REVOKE API KEYS ⚠${NC}"
        echo ""
        echo "1. OpenAI:     https://platform.openai.com/api-keys"
        echo "2. Anthropic:  https://console.anthropic.com/settings/keys"
        echo "3. 1Password:  https://my.1password.com/ (Active Sessions)"
        echo "4. Telegram:   Message @BotFather -> /revoke -> @therealidallasj_bot"
        echo ""
        echo "Full incident report: $INCIDENT_REPORT"
        echo ""
        ;;
esac

echo "======================================"
echo "Kill Switch Complete"
echo "======================================"
echo ""
