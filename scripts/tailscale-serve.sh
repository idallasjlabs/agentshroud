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
#   ./scripts/tailscale-serve.sh edge-funnel [plan]   # Inbound MCP Edge: print what WOULD be
#                                               # exposed publicly (default; no sudo, no
#                                               # tailscale calls, changes nothing)
#   sudo ./scripts/tailscale-serve.sh edge-funnel on --yes-expose-publicly
#   sudo ./scripts/tailscale-serve.sh edge-funnel off     # Funnel off on the edge port only
#   sudo ./scripts/tailscale-serve.sh edge-funnel status  # read-only
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
#   :9119/      → Hermes dashboard (direct forwarder) https://<host>:9119/
#                 2026-10-16: RESTORED to proxy 127.0.0.1:9119 (the gateway container's
#                 published TCP forwarder to Hermes) — the owner's working config from
#                 before 2026-10-08; the gateway-route variant below is what Funnel
#                 /hermes uses. Owner directive: keep this exactly as it worked.
#   /hermes     → Hermes dashboard via gateway        https://<host>/hermes (public Funnel, for Conduit iOS)
#                 (proxies to gateway:8080/hermes-dashboard/, NOT directly to
#                 Hermes port 9119 -- Hermes is on agentshroud-isolated
#                 [internal:true] specifically so it can't be reached except
#                 through the gateway's reverse proxy, which applies the same
#                 audit/security middleware as every other gateway route.
#                 2026-10-08: this used to proxy straight to 127.0.0.1:9119,
#                 bypassing that isolation boundary entirely -- found and
#                 fixed after the owner asked "shouldn't I connect through
#                 AgentShroud?" while setting up the Hermes Conduit iOS app.)
#   /           → Hermes dashboard via gateway        https://<host>/ (public Funnel; Conduit's
#                 WKWebView bridge fetches root-relative paths, so /hermes alone 404s on refresh.
#                 2026-10-17. Longest-prefix match keeps /voice and /health intact.)
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

# ── Inbound MCP Edge Funnel (SCRUM-215/217) ──────────────────────────────────
# PUBLIC INTERNET exposure of the agentshroud-mcp-edge container for hosted
# agents (Claude Duet, Poke, Gemini Spark, OpenAI Dots). Kept apart from
# start/stop: `start` never enables it and `stop` never disables it, and
# `edge-funnel off` never touches :443 (voice/Hermes Funnels).
# Path: Funnel :EDGE_FUNNEL_PORT → http://127.0.0.1:EDGE_LOCAL_PORT (the
# gateway's published TCP forwarder) → agentshroud-mcp-edge:8443.
# Prod: 8443 → 8443. Dev (agentshroud-bot): EDGE_FUNNEL_PORT=10000
# EDGE_LOCAL_PORT=9443 — Funnel serves only 443/8443/10000 and prod owns 443
# and 8443 on this node. The edge rejects every path not listed below with a
# 404 (gateway/inbound_edge/edge_app.py _EXACT_PATHS); Funnel is additionally
# limited to the same paths so nothing else is even routed.
EDGE_FUNNEL_PORT="${EDGE_FUNNEL_PORT:-8443}"
EDGE_LOCAL_PORT="${EDGE_LOCAL_PORT:-8443}"
EDGE_PATHS=(/mcp /.well-known/ /authorize /token /register /revoke /oauth/consent /healthz)

edge_validate_ports() {
    case "$EDGE_FUNNEL_PORT" in
        8443|10000) ;;
        *) echo "ERROR: EDGE_FUNNEL_PORT must be 8443 or 10000 (got '${EDGE_FUNNEL_PORT}'); 443 is reserved for the existing voice/Hermes Funnels." >&2
           exit 1 ;;
    esac
    case "$EDGE_LOCAL_PORT" in
        ''|*[!0-9]*) echo "ERROR: EDGE_LOCAL_PORT must be a port number (got '${EDGE_LOCAL_PORT}')." >&2; exit 1 ;;
    esac
}

edge_funnel_plan() {
    echo "==> Inbound MCP Edge Funnel — PLAN ONLY (nothing is changed)"
    echo ""
    echo "  Funnel port ${EDGE_FUNNEL_PORT} → http://127.0.0.1:${EDGE_LOCAL_PORT} (gateway forwarder → agentshroud-mcp-edge:8443)"
    echo "  Paths that would be exposed:"
    local p
    for p in "${EDGE_PATHS[@]}"; do
        case "$p" in
            */) echo "    https://<host>:${EDGE_FUNNEL_PORT}${p}*" ;;
            *)  echo "    https://<host>:${EDGE_FUNNEL_PORT}${p}" ;;
        esac
    done
    echo ""
    echo "  !! WARNING: this is PUBLIC INTERNET exposure. Anyone on the internet can"
    echo "  !! reach these paths; the edge's OAuth 2.1 + owner enrollment code and the"
    echo "  !! gateway's policy pipeline are the only gates."
    echo ""
    echo "  Prerequisites (verify every one before 'on'):"
    echo "    1. Gateway runs with AGENTSHROUD_INBOUND_EDGE=1 and an https"
    echo "       AGENTSHROUD_EDGE_PUBLIC_URL equal to https://<host>:${EDGE_FUNNEL_PORT}"
    echo "    2. config/inbound-edge/descriptors.manifest.json is signed"
    echo "       (descriptors.manifest.sig + descriptors.pub.pem present and verifying)"
    echo "    3. At least one vendor in config/inbound-edge/vendors/*.yaml has enabled: true"
    echo "    4. Secrets edge_signing_key and edge_gateway_token are provisioned"
    echo "       (docker/setup-secrets.sh edge-init)"
    echo ""
    echo "  To apply: sudo $0 edge-funnel on --yes-expose-publicly"
}

edge_require_root() {
    if [ "$(id -u)" -ne 0 ]; then
        echo "ERROR: this edge-funnel action changes tailscale state and must be run with sudo." >&2
        exit 1
    fi
}

# Prints the handler paths served on <port>, one per line, prefixed with
# "funnel " when Funnel is allowed for that host:port. Read-only.
edge_port_handlers() {
    local port="$1"
    { tailscale serve status --json 2>/dev/null || echo '{}'; } | python3 -c '
import json, sys
port = sys.argv[1]
cfg = json.load(sys.stdin) or {}
funnel = {k for k, v in (cfg.get("AllowFunnel") or {}).items() if v}
for hostport, web in (cfg.get("Web") or {}).items():
    if hostport.rsplit(":", 1)[-1] != port:
        continue
    tag = "funnel " if hostport in funnel else ""
    for path in sorted((web or {}).get("Handlers") or {}):
        print(tag + path)
' "$port"  # python3 OK here: runs on host, not in conda env
}

edge_funnel_on() {
    local confirmed=0 arg
    for arg in "$@"; do
        [ "$arg" = "--yes-expose-publicly" ] && confirmed=1
    done
    if [ "$confirmed" -ne 1 ]; then
        echo "REFUSED: 'edge-funnel on' exposes the Inbound MCP Edge to the PUBLIC INTERNET." >&2
        echo "Review the plan, then re-run with --yes-expose-publicly:" >&2
        echo "" >&2
        edge_funnel_plan >&2
        exit 2
    fi
    edge_require_root
    echo "==> Enabling PUBLIC Funnel :${EDGE_FUNNEL_PORT} for the Inbound MCP Edge..."
    local before443 after443 served p missing=0
    before443="$(edge_port_handlers 443)"
    for p in "${EDGE_PATHS[@]}"; do
        echo "  → Funnel :${EDGE_FUNNEL_PORT}${p} → http://127.0.0.1:${EDGE_LOCAL_PORT}${p}"
        tailscale funnel --bg --https="${EDGE_FUNNEL_PORT}" --set-path="${p}" "http://127.0.0.1:${EDGE_LOCAL_PORT}${p}"
    done

    # Prove the outcome, not the steps: every path must now be a Funnel handler
    # on the edge port, and :443 must be exactly as it was.
    served="$(edge_port_handlers "${EDGE_FUNNEL_PORT}")"
    for p in "${EDGE_PATHS[@]}"; do
        if ! printf '%s\n' "$served" | grep -qxF "funnel ${p}"; then
            echo "  ✗ not served via Funnel: :${EDGE_FUNNEL_PORT}${p}" >&2
            missing=1
        fi
    done
    after443="$(edge_port_handlers 443)"
    if [ "$before443" != "$after443" ]; then
        echo "  ✗ :443 handlers changed while enabling the edge Funnel — investigate now." >&2
        missing=1
    fi
    if [ "$missing" -ne 0 ]; then
        echo "FAILED: edge Funnel state does not match the plan." >&2
        exit 1
    fi
    echo "==> Edge Funnel ON: ${#EDGE_PATHS[@]} paths public on :${EDGE_FUNNEL_PORT}; :443 unchanged."
}

edge_funnel_off() {
    edge_require_root
    echo "==> Disabling Funnel :${EDGE_FUNNEL_PORT} (Inbound MCP Edge); :443 is not touched..."
    local before443 after443 remaining
    before443="$(edge_port_handlers 443)"
    tailscale funnel --https="${EDGE_FUNNEL_PORT}" off
    remaining="$(edge_port_handlers "${EDGE_FUNNEL_PORT}" | grep '^funnel ' || true)"
    after443="$(edge_port_handlers 443)"
    if [ -n "$remaining" ]; then
        echo "FAILED: still public on :${EDGE_FUNNEL_PORT}:" >&2
        echo "$remaining" >&2
        exit 1
    fi
    if [ "$before443" != "$after443" ]; then
        echo "FAILED: :443 handlers changed while disabling the edge Funnel — investigate now." >&2
        exit 1
    fi
    echo "==> Edge Funnel OFF: nothing public on :${EDGE_FUNNEL_PORT}; :443 unchanged."
}

edge_funnel_status() {
    echo "==> Funnel status (read-only):"
    tailscale funnel status 2>/dev/null || echo "  No active Funnel."
    echo ""
    echo "==> Handlers on edge port :${EDGE_FUNNEL_PORT}:"
    edge_port_handlers "${EDGE_FUNNEL_PORT}" | sed 's/^/  /'
}

# edge-funnel is dispatched before the global sudo gate: `plan` (the default)
# is pure output and must be runnable without privileges.
if [ "${1:-}" = "edge-funnel" ]; then
    shift
    edge_validate_ports
    action="${1:-plan}"
    if [ $# -gt 0 ]; then shift; fi
    case "$action" in
        plan)   edge_funnel_plan ;;
        on)     edge_funnel_on "$@" ;;
        off)    edge_funnel_off ;;
        status) edge_funnel_status ;;
        *)
            echo "Usage: $0 edge-funnel {plan|on --yes-expose-publicly|off|status}" >&2
            exit 1
            ;;
    esac
    exit 0
fi

# Require root/sudo for tailscale serve commands
if [ "$(id -u)" -ne 0 ]; then
    echo "ERROR: This script must be run with sudo."
    echo "Usage: sudo $0 {start|stop|status|persist}"
    echo "       $0 edge-funnel {plan|on --yes-expose-publicly|off|status}"
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

    echo "  → Hermes dashboard :${HERMES_DASH_PORT} → http://127.0.0.1:${HERMES_DASH_PORT} (gateway TCP forwarder → Hermes; restored 2026-10-16, see header note)"
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

    # 2026-10-16 (owner decision): Hermes dashboard also published via Funnel so the
    # Hermes Conduit iOS app works from devices whose DNS resolves *.ts.net publicly
    # (public DNS points at Funnel ingress, which only carries :443). Public internet
    # exposure, protected by the dashboard password + the gateway's middleware.
    echo "  → Hermes dashboard Funnel :443/hermes → http://127.0.0.1:${GATEWAY_PORT}/hermes-dashboard/"
    tailscale funnel --bg --set-path=/hermes "http://127.0.0.1:${GATEWAY_PORT}/hermes-dashboard/"
    # 2026-10-17: Conduit's dashboard bridge issues ROOT-relative fetches
    # (fetch("/api/auth/ws-ticket") from a WKWebView), so a sub-path alone breaks
    # every session refresh with a bare Funnel 404. Serve matches the longest
    # prefix, so /voice and /health above still win; everything else is the
    # dashboard. Conduit URL: https://<host> (no path). Same upstream as /hermes.
    echo "  → Hermes dashboard Funnel :443/ → http://127.0.0.1:${GATEWAY_PORT}/hermes-dashboard/"
    tailscale funnel --bg --set-path=/ "http://127.0.0.1:${GATEWAY_PORT}/hermes-dashboard/"

    echo "  → Uptime monitor Funnel :443/health → http://127.0.0.1:${VOICE_GATEWAY_PORT}/health"
    tailscale funnel --bg --set-path=/health "http://127.0.0.1:${VOICE_GATEWAY_PORT}/health"

    echo ""
    echo "==> Done. Services are now available at:"
    HOSTNAME=$(tailscale status --self --json | python3 -c "import sys,json; print(json.load(sys.stdin)['Self']['DNSName'].rstrip('.'))" 2>/dev/null || echo "<your-tailscale-hostname>")  # python3 OK here: runs on host, not in conda env
    echo "  Gateway:         https://${HOSTNAME}:${GATEWAY_PORT}/"
    echo "  Control:         https://${HOSTNAME}:${CONTROL_UI_PORT}/"
    echo "  Hermes dashboard:https://${HOSTNAME}:${HERMES_DASH_PORT}/  (tailnet)"
    echo "  Hermes dashboard:https://${HOSTNAME}/hermes  (public Funnel — Conduit iOS)"
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
