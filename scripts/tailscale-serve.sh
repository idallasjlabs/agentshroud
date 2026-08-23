#!/usr/bin/env bash
# tailscale-serve.sh — Expose AgentShroud services over Tailscale HTTPS
#
# IMPORTANT: This script requires sudo because `tailscale serve` modifies
# the Tailscale daemon configuration. Run it as a user with sudo privileges,
# NOT as the agentshroud-bot service account.
#
# Usage:
#   sudo ./scripts/tailscale-serve.sh start    # Enable the 5 core AgentShroud serves
#   sudo ./scripts/tailscale-serve.sh stop     # Disable the 5 core AgentShroud serves
#   sudo ./scripts/tailscale-serve.sh status   # Show current serve config
#   sudo ./scripts/tailscale-serve.sh persist  # One-shot: fix the dual-tailscaled-daemon
#                                               # conflict (standardize on the Homebrew
#                                               # LaunchDaemon so it survives reboots),
#                                               # reconnect if needed, and re-apply the
#                                               # 5 core AgentShroud serves. Re-run this
#                                               # after any reboot, `brew upgrade tailscale`,
#                                               # or macOS update. Only touches the 5
#                                               # AgentShroud ports below — leaves any other
#                                               # serve config (e.g. from other local
#                                               # projects) untouched.
#
# Services exposed:
#   :8080/      → Gateway API (port 8080)          https://<host>:8080/
#   :18789/     → Control UI (port 18789)           https://<host>:18789/
#   :9119/      → Hermes dashboard (port 9119)      https://<host>:9119/
#   :8642/      → Hermes OpenAI API (port 8642)     https://<host>:8642/v1
#   :8765/      → Voice Gateway WS (port 8765)      wss://<host>:8765/voice (tailnet peers)
#   /voice      → ESP32-S3-BOX-3 voice terminal     wss://<host>/voice (public Funnel)
#   /health     → Voice Gateway health check         https://<host>/health (public Funnel —
#                 lets external uptime monitors (e.g. UptimeRobot) check liveness without a
#                 tailnet client; /voice itself is a WebSocket route and always 404s to a
#                 plain HTTP GET, so it can't be used for that)
#
# ⚠️  TEMPORARY (2026-07-27): the ESP32's current firmware is hardcoded
# (CONFIG_VT_VG_WS_URL, compile-time) to the Funnel URL above and has no
# on-device Tailscale client — Funnel is back on ONLY as a stopgap until the
# firmware is rebuilt for LAN-only (or another non-public path) and reflashed.
# Owner's stated end-state is NO Funnel / no public exposure at all — once the
# firmware fix ships and is confirmed working, remove the `tailscale funnel`
# line in cmd_start below and restore the "actively turn Funnel off" guard
# that was here before. Don't remove Funnel again without checking the
# firmware has actually been updated first, or this breaks the device exactly
# like it did on 2026-07-27.
#
# Note: Hermes/Voice-Gateway serves are only reachable when the relevant
# profile is running. Use `asb up voice` or `asb up full`.

set -euo pipefail

# Require root/sudo for tailscale serve commands
if [ "$(id -u)" -ne 0 ]; then
    echo "ERROR: This script must be run with sudo."
    echo "Usage: sudo $0 {start|stop|status|persist}"
    exit 1
fi

GATEWAY_PORT=8080
CONTROL_UI_PORT=18789
HERMES_DASH_PORT=9119
HERMES_API_PORT=8642
VOICE_GATEWAY_PORT=8765

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

    echo "  → Voice Gateway WS :${VOICE_GATEWAY_PORT} → http://127.0.0.1:${VOICE_GATEWAY_PORT}"
    tailscale serve --bg --https=${VOICE_GATEWAY_PORT} http://127.0.0.1:${VOICE_GATEWAY_PORT}

    # TEMPORARY (2026-07-27) — see header note. Remove once ESP32 firmware no
    # longer depends on this Funnel URL, and restore
    # `tailscale funnel --https=443 off` here instead.
    echo "  → ESP32 voice Funnel :443/voice → http://127.0.0.1:${VOICE_GATEWAY_PORT}/voice"
    tailscale funnel --bg --set-path=/voice "http://127.0.0.1:${VOICE_GATEWAY_PORT}/voice"

    echo "  → Uptime monitor Funnel :443/health → http://127.0.0.1:${VOICE_GATEWAY_PORT}/health"
    tailscale funnel --bg --set-path=/health "http://127.0.0.1:${VOICE_GATEWAY_PORT}/health"

    echo ""
    echo "==> Done. Services are now available at:"
    HOSTNAME=$(tailscale status --self --json | python3 -c "import sys,json; print(json.load(sys.stdin)['Self']['DNSName'].rstrip('.'))" 2>/dev/null || echo "<your-tailscale-hostname>")  # python3 OK here: runs on host, not in conda env
    echo "  Gateway:         https://${HOSTNAME}:${GATEWAY_PORT}/"
    echo "  Control:         https://${HOSTNAME}:${CONTROL_UI_PORT}/"
    echo "  Hermes dashboard:https://${HOSTNAME}:${HERMES_DASH_PORT}/"
    echo "  Hermes API:      https://${HOSTNAME}:${HERMES_API_PORT}/v1"
    echo "  Voice Gateway:   wss://${HOSTNAME}:${VOICE_GATEWAY_PORT}/voice"
    echo "  ESP32 voice:     wss://${HOSTNAME}/voice  (public Funnel — TEMPORARY, see header note)"
    echo "  Uptime monitor:  https://${HOSTNAME}/health  (public Funnel)"
    echo ""
    echo "  (Hermes/Voice-Gateway URLs require: asb up voice|full)"
}

cmd_stop() {
    echo "==> Disabling Tailscale serves..."
    tailscale serve --https=${GATEWAY_PORT}      off 2>/dev/null || true
    tailscale serve --https=${CONTROL_UI_PORT}   off 2>/dev/null || true
    tailscale serve --https=${HERMES_DASH_PORT}  off 2>/dev/null || true
    tailscale serve --https=${HERMES_API_PORT}   off 2>/dev/null || true
    tailscale serve --https=${VOICE_GATEWAY_PORT} off 2>/dev/null || true
    tailscale funnel --https=443 off 2>/dev/null || true
    echo "==> All serves disabled."
}

cmd_status() {
    echo "==> Current Tailscale serve configuration:"
    tailscale serve status 2>/dev/null || echo "  No active serves."
    echo ""
    echo "==> Tailscale node status:"
    tailscale status --self
}

# Standardizes on the Homebrew `brew services` LaunchDaemon so tailscaled
# survives reboots deterministically. Some macOS setups end up with a second,
# self-installed system LaunchDaemon (com.tailscale.tailscaled.plist) that
# wins the race for the TUN/socket at boot and leaves the Homebrew daemon
# crash-looping in the background — removing it here is what makes this
# idempotent to re-run after upgrades.
cmd_persist() {
    echo "==> Persisting Tailscale across reboots/updates (canonical daemon: Homebrew)..."

    SYSTEM_DAEMON_PLIST="/Library/LaunchDaemons/com.tailscale.tailscaled.plist"
    if [ -f "$SYSTEM_DAEMON_PLIST" ]; then
        echo "  → Removing self-installed system tailscaled daemon (backup kept in /tmp)..."
        cp -p "$SYSTEM_DAEMON_PLIST" "/tmp/com.tailscale.tailscaled.plist.bak.$$" 2>/dev/null || true
        launchctl bootout system/com.tailscale.tailscaled 2>/dev/null || true
        rm -f "$SYSTEM_DAEMON_PLIST"
    else
        echo "  → Self-installed system daemon already absent."
    fi

    echo "  → Enabling Homebrew tailscaled LaunchDaemon..."
    launchctl bootstrap system /Library/LaunchDaemons/homebrew.mxcl.tailscale.plist 2>/dev/null || true
    launchctl enable system/homebrew.mxcl.tailscale 2>/dev/null || true
    launchctl kickstart -k system/homebrew.mxcl.tailscale 2>/dev/null || true

    echo "  → Waiting for tailscaled to become available..."
    ATTEMPTS=0
    until tailscale status &>/dev/null; do
        ATTEMPTS=$((ATTEMPTS + 1))
        if [ "$ATTEMPTS" -ge 20 ]; then
            echo "ERROR: tailscaled did not become available after ${ATTEMPTS}s." >&2
            exit 1
        fi
        sleep 1
    done

    BACKEND_STATE=$(tailscale status --json 2>/dev/null | python3 -c "import sys,json; print(json.load(sys.stdin).get('BackendState',''))" 2>/dev/null || echo "")  # python3 OK here: runs on host, not in conda env
    if [ "$BACKEND_STATE" != "Running" ]; then
        echo "  → Backend state is '${BACKEND_STATE:-unknown}', bringing Tailscale up..."
        tailscale up
    else
        echo "  → Already connected (BackendState=Running)."
    fi

    cmd_start

    echo ""
    echo "==> Verification:"
    tailscale status --self
    DAEMON_COUNT=$(pgrep -x tailscaled | wc -l | tr -d ' ')
    if [ "$DAEMON_COUNT" -eq 1 ]; then
        echo "  ✓ Exactly one tailscaled process running (PID $(pgrep -x tailscaled))."
    else
        echo "  ⚠ WARNING: ${DAEMON_COUNT} tailscaled processes running (expected 1)." >&2
    fi
    echo ""
    echo "==> Tailscale is now persistent via the Homebrew LaunchDaemon."
    echo "    After any future reboot, 'brew upgrade tailscale', or macOS update, just re-run:"
    echo "      sudo $0 persist"
}

case "${1:-}" in
    start)   cmd_start ;;
    stop)    cmd_stop ;;
    status)  cmd_status ;;
    persist) cmd_persist ;;
    *)
        echo "Usage: sudo $0 {start|stop|status|persist}"
        exit 1
        ;;
esac
