#!/usr/bin/env bash
# tailscale-serve.sh — Expose SecureClaw services over Tailscale HTTPS
#
# IMPORTANT: This script requires sudo because `tailscale serve` modifies
# the Tailscale daemon configuration. Run it as a user with sudo privileges,
# NOT as the secureclaw-bot service account.
#
# Usage:
#   sudo ./scripts/tailscale-serve.sh start   # Enable all serves
#   sudo ./scripts/tailscale-serve.sh stop    # Disable all serves
#   sudo ./scripts/tailscale-serve.sh status  # Show current serve config
#
# Services exposed:
#   /           → Gateway API (port 8080)
#   /ui         → Control UI (port 18790)
#   /dashboard  → Dashboard (port 8050)

set -euo pipefail

# Require root/sudo for tailscale serve commands
if [ "$(id -u)" -ne 0 ]; then
    echo "ERROR: This script must be run with sudo."
    echo "Usage: sudo $0 {start|stop|status}"
    exit 1
fi

GATEWAY_PORT=8080
CONTROL_UI_PORT=18790
DASHBOARD_PORT=8050

cmd_start() {
    echo "==> Enabling Tailscale HTTPS serve for SecureClaw services..."

    echo "  → Gateway API on / → http://127.0.0.1:${GATEWAY_PORT}"
    tailscale serve --bg --https=443 / http://127.0.0.1:${GATEWAY_PORT}

    echo "  → Control UI on /ui → http://127.0.0.1:${CONTROL_UI_PORT}"
    tailscale serve --bg --https=443 /ui http://127.0.0.1:${CONTROL_UI_PORT}

    echo "  → Dashboard on /dashboard → http://127.0.0.1:${DASHBOARD_PORT}"
    tailscale serve --bg --https=443 /dashboard http://127.0.0.1:${DASHBOARD_PORT}

    echo ""
    echo "==> Done. Services are now available at:"
    HOSTNAME=$(tailscale status --self --json | python3 -c "import sys,json; print(json.load(sys.stdin)['Self']['DNSName'].rstrip('.'))" 2>/dev/null || echo "<your-tailscale-hostname>")  # python3 OK here: runs on host, not in conda env
    echo "  Gateway:   https://${HOSTNAME}/"
    echo "  Control:   https://${HOSTNAME}/ui"
    echo "  Dashboard: https://${HOSTNAME}/dashboard"
}

cmd_stop() {
    echo "==> Disabling Tailscale serves..."
    tailscale serve --https=443 / off 2>/dev/null || true
    tailscale serve --https=443 /ui off 2>/dev/null || true
    tailscale serve --https=443 /dashboard off 2>/dev/null || true
    echo "==> All serves disabled."
}

cmd_status() {
    echo "==> Current Tailscale serve configuration:"
    tailscale serve status 2>/dev/null || echo "  No active serves."
    echo ""
    echo "==> Tailscale node status:"
    tailscale status --self
}

case "${1:-}" in
    start)  cmd_start ;;
    stop)   cmd_stop ;;
    status) cmd_status ;;
    *)
        echo "Usage: sudo $0 {start|stop|status}"
        exit 1
        ;;
esac
