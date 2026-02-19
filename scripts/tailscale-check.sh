#!/usr/bin/env bash
# tailscale-check.sh — Verify Tailscale connectivity and serve status
#
# Does NOT require sudo — safe to run as agentshroud-bot.
#
# Usage:
#   ./scripts/tailscale-check.sh

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

ok()   { echo -e "  ${GREEN}✓${NC} $1"; }
fail() { echo -e "  ${RED}✗${NC} $1"; ERRORS=$((ERRORS + 1)); }
warn() { echo -e "  ${YELLOW}⚠${NC} $1"; }

ERRORS=0

echo "=== Tailscale Health Check ==="
echo ""

# 1. Is tailscale installed?
if command -v tailscale &>/dev/null; then
    ok "tailscale CLI found: $(which tailscale)"
else
    fail "tailscale CLI not found in PATH"
    exit 1
fi

# 2. Is tailscaled running?
if tailscale status &>/dev/null; then
    ok "tailscaled is running"
else
    fail "tailscaled is not running (start with: sudo tailscale up)"
    exit 1
fi

# 3. Are we connected?
SELF_STATUS=$(tailscale status --self --json 2>/dev/null)
if [ -n "$SELF_STATUS" ]; then
    HOSTNAME=$(echo "$SELF_STATUS" | python3 -c "import sys,json; print(json.load(sys.stdin)['Self']['DNSName'].rstrip('.'))" 2>/dev/null || echo "unknown")
    TAILNET_IP=$(echo "$SELF_STATUS" | python3 -c "import sys,json; print(json.load(sys.stdin)['Self']['TailscaleIPs'][0])" 2>/dev/null || echo "unknown")
    ok "Connected as: ${HOSTNAME} (${TAILNET_IP})"
else
    fail "Cannot get self status"
fi

# 4. Check serve config
echo ""
echo "=== Tailscale Serve Status ==="
if tailscale serve status &>/dev/null 2>&1; then
    tailscale serve status 2>/dev/null
else
    warn "No active Tailscale serves (run: sudo ./scripts/tailscale-serve.sh start)"
fi

# 5. Check local service ports
echo ""
echo "=== Local Service Ports ==="
for port_name in "8080:Gateway" "18790:Control UI" "8050:Dashboard"; do
    PORT="${port_name%%:*}"
    NAME="${port_name##*:}"
    if ss -tlnp 2>/dev/null | grep -q ":${PORT} " || nc -z 127.0.0.1 "$PORT" 2>/dev/null; then
        ok "${NAME} listening on port ${PORT}"
    else
        warn "${NAME} not listening on port ${PORT}"
    fi
done

echo ""
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}All checks passed.${NC}"
else
    echo -e "${RED}${ERRORS} check(s) failed.${NC}"
    exit 1
fi
