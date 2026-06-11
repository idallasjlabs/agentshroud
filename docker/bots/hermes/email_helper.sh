#!/bin/sh
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# AgentShroud Hermes email helper — stand-alone script for cron and shell use.
# Routes all email through the AgentShroud gateway /email/send-owner endpoint.
# No SMTP credentials, no 1Password CLI, no nodemailer needed inside Hermes.
#
# Usage:
#   agentshroud-email-send.sh --subject "Subject line" --body "Body text"
#   agentshroud-email-send.sh --subject "Subject line" --body "HTML content" --html
#
# Exit codes:
#   0 — gateway accepted (2xx)
#   1 — gateway rejected (non-2xx) or network error

# Load s6 container environment (works in both cron/s6 context and docker exec)
if [ -d /run/s6/container_environment ]; then
    set -a
    for _f in /run/s6/container_environment/*; do
        [ -f "$_f" ] && eval "$(basename "$_f")=$(cat "$_f" 2>/dev/null)" 2>/dev/null || true
    done
    set +a
fi

set -eu

_subject=""
_body=""
_is_html="false"
_gw_url="${GATEWAY_OP_PROXY_URL:-http://gateway:8080}"

while [ "$#" -gt 0 ]; do
    case "$1" in
        --subject) _subject="$2"; shift 2 ;;
        --body)    _body="$2";    shift 2 ;;
        --html)    _is_html="true"; shift ;;
        *)
            echo "[email-send] Unknown argument: $1" >&2
            exit 1
            ;;
    esac
done

if [ -z "${_subject}" ] || [ -z "${_body}" ]; then
    echo "[email-send] ERROR: --subject and --body are required" >&2
    exit 1
fi

# Build the JSON payload with python3 — multi-line HTML bodies contain literal
# newlines, which are illegal in JSON strings (sed escaping caused gateway 422s).
_payload_file="/tmp/.email-send-payload.$$"
python3 - "${_subject}" "${_body}" "${_is_html}" > "${_payload_file}" <<'PYEOF'
import json, sys
json.dump(
    {"subject": sys.argv[1], "body": sys.argv[2], "is_html": sys.argv[3] == "true"},
    sys.stdout,
)
PYEOF

# --max-time must exceed the gateway's worst-case send (~70s: 1Password
# credential fetch + SMTP); 30s caused false timeouts and duplicate retries.
_response="$(curl -s --max-time 120 \
    -o /tmp/.email-send-response \
    -w "%{http_code}" \
    -X POST "${_gw_url}/email/send-owner" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
    -H "X-AgentShroud-System: 1" \
    --data-binary "@${_payload_file}" \
    2>/dev/null)" || _response="000"
rm -f "${_payload_file}" 2>/dev/null || true

_body_resp="$(cat /tmp/.email-send-response 2>/dev/null || true)"
rm -f /tmp/.email-send-response 2>/dev/null || true

case "${_response}" in
    2*)
        echo "[email-send] Sent (HTTP ${_response}): ${_subject}"
        exit 0
        ;;
    000)
        echo "[email-send] ERROR: gateway unreachable (${_gw_url})" >&2
        exit 1
        ;;
    *)
        echo "[email-send] ERROR: gateway returned HTTP ${_response}: ${_body_resp}" >&2
        exit 1
        ;;
esac
