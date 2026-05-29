#!/usr/bin/env bash
# tailscale-serve.sh — Expose AgentShroud services over Tailscale HTTPS
#
# IMPORTANT: This script requires sudo because `tailscale serve` modifies
# the Tailscale daemon configuration. Run it as a user with sudo privileges,
# NOT as the agentshroud-bot service account.
#
# Usage:
#   sudo ./scripts/tailscale-serve.sh start   # Enable all serves
#   sudo ./scripts/tailscale-serve.sh stop    # Disable all serves
#   sudo ./scripts/tailscale-serve.sh status  # Show current serve config
#
# Services exposed:
#   :8080/      → Gateway API (port 8080)         https://<host>:8080/
#   :18789/     → Control UI (port 18789)         https://<host>:18789/
#   :9119/      → Hermes dashboard (port 9119)    https://<host>:9119/
#   :8642/      → Hermes OpenAI API (port 8642)   https://<host>:8642/v1
#   :9121/      → HCI admin proxy (port 9121)     https://<host>:9121/
#
# Note: Hermes and HCI serves (:9119/:8642/:9121) are only reachable when the
# full stack is running.  Use `asb up full` (or docker compose --profile full).

set -euo pipefail

# Require root/sudo for tailscale serve commands
if [ "$(id -u)" -ne 0 ]; then
    echo "ERROR: This script must be run with sudo."
    echo "Usage: sudo $0 {start|stop|status}"
    exit 1
fi

GATEWAY_PORT=8080
CONTROL_UI_PORT=18789
HERMES_DASH_PORT=9119
HERMES_API_PORT=8642
HCI_PORT=9121

cmd_start() {
    echo "==> Enabling Tailscale HTTPS serve for AgentShroud services..."

    echo "  → Gateway API :${GATEWAY_PORT} → http://127.0.0.1:${GATEWAY_PORT}"
    tailscale serve --bg --https=${GATEWAY_PORT} http://127.0.0.1:${GATEWAY_PORT}

    echo "  → Control UI :${CONTROL_UI_PORT} → http://127.0.0.1:${CONTROL_UI_PORT}"
    tailscale serve --bg --https=${CONTROL_UI_PORT} http://127.0.0.1:${CONTROL_UI_PORT}

    echo "  → Hermes dashboard :${HERMES_DASH_PORT} → http://127.0.0.1:${HERMES_DASH_PORT}"
    tailscale serve --bg --https=${HERMES_DASH_PORT} http://127.0.0.1:${HERMES_DASH_PORT}

    echo "  → Hermes OpenAI API :${HERMES_API_PORT} → http://127.0.0.1:${HERMES_API_PORT}"
    tailscale serve --bg --https=${HERMES_API_PORT} http://127.0.0.1:${HERMES_API_PORT}

    echo "  → HCI admin proxy :${HCI_PORT} → http://127.0.0.1:${HCI_PORT}"
    tailscale serve --bg --https=${HCI_PORT} http://127.0.0.1:${HCI_PORT}

    echo ""
    echo "==> Done. Services are now available at:"
    HOSTNAME=$(tailscale status --self --json | python3 -c "import sys,json; print(json.load(sys.stdin)['Self']['DNSName'].rstrip('.'))" 2>/dev/null || echo "<your-tailscale-hostname>")  # python3 OK here: runs on host, not in conda env
    echo "  Gateway:         https://${HOSTNAME}:${GATEWAY_PORT}/"
    echo "  Control:         https://${HOSTNAME}:${CONTROL_UI_PORT}/"
    echo "  Hermes dashboard:https://${HOSTNAME}:${HERMES_DASH_PORT}/"
    echo "  Hermes API:      https://${HOSTNAME}:${HERMES_API_PORT}/v1"
    echo "  HCI:             https://${HOSTNAME}:${HCI_PORT}/"
    echo ""
    echo "  (Hermes/HCI URLs require: asb up full)"
}

cmd_stop() {
    echo "==> Disabling Tailscale serves..."
    tailscale serve --https=${GATEWAY_PORT}    off 2>/dev/null || true
    tailscale serve --https=${CONTROL_UI_PORT} off 2>/dev/null || true
    tailscale serve --https=${HERMES_DASH_PORT} off 2>/dev/null || true
    tailscale serve --https=${HERMES_API_PORT} off 2>/dev/null || true
    tailscale serve --https=${HCI_PORT} off 2>/dev/null || true
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
