#!/bin/sh
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# AgentShroud SSH-exec helper — stand-alone wrapper for both OpenClaw and Hermes.
# Routes remote SSH commands through the AgentShroud gateway /ssh/exec endpoint.
# The gateway holds the SSH key and resolves host names — no local ssh binary needed.
#
# WHY THIS WRAPPER EXISTS (the bug it fixes):
#   Both bot runtimes ship a command-safety scanner (OpenClaw's built-in npm
#   scanner; Hermes' `tirith`). When the agent runs a raw
#     curl ... -X POST http://gateway:8080/ssh/exec ...
#   the scanner sees a plain-HTTP URL passed to a downloader/executor and raises
#     "[HIGH] Plain HTTP URL in execution context"
#   forcing a Command-Approval prompt on EVERY SSH call — the feature becomes
#   unusable. http://gateway:8080 is the trusted internal Docker control-plane
#   (network `internal: true`, not internet-exposed, no MITM risk).
#
#   This wrapper moves the plain-HTTP URL OFF the agent's command line and INTO
#   a vetted, baked-in script (same pattern as agentshroud-email-send.sh). The
#   agent invokes:
#       agentshroud-ssh-exec.sh <host> "<command>" ["<reason>"] ["<cwd>"]
#   which contains no http:// URL in argv, so the scanner has nothing to flag.
#   The exemption is NARROW: only this one internal endpoint is wrapped; any
#   OTHER http:// URL the agent tries to curl still trips the scanner normally.
#
# Usage:
#   agentshroud-ssh-exec.sh marvin "uptime"
#   agentshroud-ssh-exec.sh marvin "df -h" "check disk before deploy"
#   agentshroud-ssh-exec.sh trillian "git status" "review" "/opt/repo"
#
# Approved hosts (resolved gateway-side): marvin, trillian, raspberrypi.
# Response is the gateway JSON: {"stdout":…,"stderr":…,"exit_code":…}.
#
# Exit codes:
#   0   — gateway accepted (2xx); JSON response printed to stdout
#   1   — usage error, gateway rejection (non-2xx), or network error

# Load s6 container environment (Hermes runs under s6-overlay; OpenClaw does not).
# No-op in the OpenClaw container where /run/s6 does not exist.
if [ -d /run/s6/container_environment ]; then
    set -a
    for _f in /run/s6/container_environment/*; do
        [ -f "$_f" ] && eval "$(basename "$_f")=$(cat "$_f" 2>/dev/null)" 2>/dev/null || true
    done
    set +a
fi

set -eu

_host="${1:-}"
_command="${2:-}"
_reason="${3:-}"
_cwd="${4:-}"
_gw_url="${GATEWAY_OP_PROXY_URL:-http://gateway:8080}"

if [ -z "${_host}" ] || [ -z "${_command}" ]; then
    echo "[ssh-exec] Usage: agentshroud-ssh-exec.sh <host> \"<command>\" [\"<reason>\"] [\"<cwd>\"]" >&2
    echo "[ssh-exec] Approved hosts: marvin, trillian, raspberrypi" >&2
    exit 1
fi

# Build the JSON payload with python3 so command/reason/cwd containing quotes,
# newlines, or shell metacharacters are safely encoded (never touch shell argv
# escaping). cwd is omitted from the payload when empty.
_payload_file="/tmp/.ssh-exec-payload.$$"
python3 - "${_host}" "${_command}" "${_reason}" "${_cwd}" > "${_payload_file}" <<'PYEOF'
import json, sys
host, command, reason, cwd = sys.argv[1:5]
payload = {"host": host, "command": command, "reason": reason}
if cwd:
    payload["cwd"] = cwd
json.dump(payload, sys.stdout)
PYEOF

# --noproxy gateway: HTTP_PROXY=http://gateway:8181 (EgressFilter) is set in the
# bot environment; without --noproxy the call would loop through the egress proxy
# instead of reaching the internal control-plane /ssh/exec endpoint directly.
_response="$(curl -sS --noproxy gateway --max-time 180 \
    -o /tmp/.ssh-exec-response \
    -w "%{http_code}" \
    -X POST "${_gw_url}/ssh/exec" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
    -H "X-AgentShroud-System: 1" \
    --data-binary "@${_payload_file}" \
    2>/dev/null)" || _response="000"
rm -f "${_payload_file}" 2>/dev/null || true

_body_resp="$(cat /tmp/.ssh-exec-response 2>/dev/null || true)"
rm -f /tmp/.ssh-exec-response 2>/dev/null || true

case "${_response}" in
    2*)
        printf '%s\n' "${_body_resp}"
        exit 0
        ;;
    000)
        echo "[ssh-exec] ERROR: gateway unreachable (${_gw_url})" >&2
        exit 1
        ;;
    *)
        echo "[ssh-exec] ERROR: gateway returned HTTP ${_response}: ${_body_resp}" >&2
        exit 1
        ;;
esac
