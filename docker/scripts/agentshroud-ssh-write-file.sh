#!/bin/sh
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# AgentShroud SSH-write-file helper — stand-alone wrapper for both OpenClaw and Hermes.
# Routes remote file writes through the AgentShroud gateway /ssh/write_file endpoint.
# The gateway holds the SSH key and resolves host names — no local ssh binary needed.
#
# WHY THIS WRAPPER EXISTS (same reasoning as agentshroud-ssh-exec.sh):
#   Both bot runtimes ship a command-safety scanner (OpenClaw's built-in npm
#   scanner; Hermes' `tirith`). When the agent runs a raw
#     curl ... -X POST http://gateway:8080/ssh/write_file ...
#   the scanner sees a plain-HTTP URL passed to a downloader/executor and raises
#     "[HIGH] Plain HTTP URL in execution context"
#   forcing a Command-Approval prompt on EVERY SSH call — the feature becomes
#   unusable. http://gateway:8080 is the trusted internal Docker control-plane
#   (network `internal: true`, not internet-exposed, no MITM risk).
#
#   This wrapper moves the plain-HTTP URL OFF the agent's command line and INTO
#   a vetted, baked-in script (same pattern as agentshroud-ssh-exec.sh /
#   agentshroud-email-send.sh). The agent invokes:
#       agentshroud-ssh-write-file.sh <host> <path> ["<reason>"] < content
#   which contains no http:// URL in argv, so the scanner has nothing to flag.
#
# Content travels via STDIN, not an argv/filename argument — the caller pipes
# the file bytes in, this script base64-encodes them locally, and the encoded
# form rides inside the JSON body as `content_base64`. The remote gateway
# endpoint decodes and writes the bytes verbatim; nothing here is ever
# concatenated into a remote shell string.
#
# Usage:
#   agentshroud-ssh-write-file.sh marvin "/Users/agentshroud-bot/Development/agentshroud/notes.txt" "update notes" < notes.txt
#   printf 'hello\n' | agentshroud-ssh-write-file.sh trillian "/Users/agentshroud-bot/Development/agentshroud/hello.txt"
#
# Approved hosts (resolved gateway-side): marvin, trillian, raspberrypi.
# path MUST resolve under /Users/agentshroud-bot/Development/agentshroud (gateway-enforced).
# Response is the gateway JSON: {"request_id":…,"host":…,"path":…,"success":…,
# "bytes_written":…,"exit_code":…,"stderr":…,"duration_seconds":…,"timestamp":…,"audit_id":…}.
#
# Exit codes:
#   0   — gateway accepted (2xx) AND the remote write itself succeeded (success:true)
#   1   — usage error, gateway rejection (non-2xx), remote write failure
#         (success:false — e.g. bad path on the target host), or network error

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
_path="${2:-}"
_reason="${3:-}"
_gw_url="${GATEWAY_OP_PROXY_URL:-http://gateway:8080}"

if [ -z "${_host}" ] || [ -z "${_path}" ]; then
    echo "[ssh-write-file] Usage: agentshroud-ssh-write-file.sh <host> <path> [\"<reason>\"] < content" >&2
    echo "[ssh-write-file] Approved hosts: marvin, trillian, raspberrypi" >&2
    echo "[ssh-write-file] path must resolve under /Users/agentshroud-bot/Development/agentshroud" >&2
    exit 1
fi

# Resolve the gateway auth token (64-char control-plane password). The token was
# NEVER set as GATEWAY_AUTH_TOKEN in either bot container, so the previous curl
# sent `Authorization: Bearer ` (empty) and the gateway returned HTTP 401
# "Invalid authentication scheme. Expected 'Bearer <token>'". The token IS present
# as a Docker secret FILE at /run/secrets/gateway_password in BOTH bots, exposed
# via different *_FILE env vars:
#   OpenClaw: OPENCLAW_GATEWAY_PASSWORD_FILE=/run/secrets/gateway_password
#   Hermes:   GATEWAY_AUTH_TOKEN_FILE=/run/secrets/gateway_password
# Resolve in priority order, first non-empty wins. $(cat "$f") strips a trailing
# newline. Never send an empty Bearer — bail loudly instead.
_read_token_file() {
    _f="$1"
    if [ -n "${_f}" ] && [ -r "${_f}" ]; then
        cat "${_f}" 2>/dev/null
    fi
}

_gw_token="${GATEWAY_AUTH_TOKEN:-}"
if [ -z "${_gw_token}" ]; then
    _gw_token="$(_read_token_file "${GATEWAY_AUTH_TOKEN_FILE:-}")"
fi
if [ -z "${_gw_token}" ]; then
    _gw_token="$(_read_token_file "${OPENCLAW_GATEWAY_PASSWORD_FILE:-}")"
fi
if [ -z "${_gw_token}" ]; then
    _gw_token="$(_read_token_file "/run/secrets/gateway_password")"
fi

if [ -z "${_gw_token}" ]; then
    echo "[ssh-write-file] ERROR: no gateway auth token (GATEWAY_AUTH_TOKEN / *_FILE / /run/secrets/gateway_password all empty)" >&2
    exit 1
fi

# _json_escape reads one argument and emits a JSON-safe string body (WITHOUT the
# surrounding double quotes). Identical to the helper in agentshroud-ssh-exec.sh —
# reused verbatim rather than reinvented, per the injection-safety reasoning
# documented there: it escapes backslash, double quote, and the C0 control
# characters that must be escaped in JSON (\b \t \n \f \r, and any other
# 0x01-0x1F control char as \u00XX), so an encoded value can never break out
# of its JSON string. Used here for `path` and `reason` only — `content_base64`
# is base64 output (alphabet [A-Za-z0-9+/=]), which is always JSON-safe as-is
# and needs no escaping.
_json_escape() {
    printf '%s' "$1" | awk '
    BEGIN {
        RS = "\0"
        ctrl = sprintf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c", \
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, \
            17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    }
    {
        n = length($0)
        out = ""
        for (i = 1; i <= n; i++) {
            c = substr($0, i, 1)
            if (c == "\\") { out = out "\\\\" }
            else if (c == "\"") { out = out "\\\"" }
            else if (c == "\b") { out = out "\\b" }
            else if (c == "\t") { out = out "\\t" }
            else if (c == "\n") { out = out "\\n" }
            else if (c == "\f") { out = out "\\f" }
            else if (c == "\r") { out = out "\\r" }
            else {
                # Escape any remaining C0 control character (0x01-0x1F) as \u00XX.
                d = index(ctrl, c)
                if (d > 0) { out = out sprintf("\\u%04x", d) }
                else { out = out c }
            }
        }
        printf "%s", out
    }'
}

# Read the file content from STDIN (never a filename argument — the caller
# pipes bytes in) and base64-encode it. `base64` (not python3) is used because
# the OpenClaw container is a node image with no python3; `base64` is present
# in both the node and python base images. `tr -d '\n'` strips the encoder's
# line-wrapping (68/76-col, implementation-dependent) since content_base64
# must be a single JSON string value with no embedded literal newlines.
_content_file="/tmp/.ssh-write-content.$$"
cat > "${_content_file}"
_content_b64="$(base64 < "${_content_file}" | tr -d '\n')"
rm -f "${_content_file}" 2>/dev/null || true

_payload_file="/tmp/.ssh-write-payload.$$"
{
    printf '{"host":"%s","path":"%s","content_base64":"%s","reason":"%s"}' \
        "$(_json_escape "${_host}")" \
        "$(_json_escape "${_path}")" \
        "${_content_b64}" \
        "$(_json_escape "${_reason}")"
} > "${_payload_file}"

# --noproxy gateway: HTTP_PROXY=http://gateway:8181 (EgressFilter) is set in the
# bot environment; without --noproxy the call would loop through the egress proxy
# instead of reaching the internal control-plane /ssh/write_file endpoint directly.
_response="$(curl -sS --noproxy gateway --max-time 180 \
    -o /tmp/.ssh-write-response \
    -w "%{http_code}" \
    -X POST "${_gw_url}/ssh/write_file" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${_gw_token}" \
    -H "X-AgentShroud-System: 1" \
    --data-binary "@${_payload_file}" \
    2>/dev/null)" || _response="000"
rm -f "${_payload_file}" 2>/dev/null || true

_body_resp="$(cat /tmp/.ssh-write-response 2>/dev/null || true)"
rm -f /tmp/.ssh-write-response 2>/dev/null || true

case "${_response}" in
    2*)
        # HTTP 2xx only means the gateway ACCEPTED and processed the request —
        # per the endpoint contract a failed remote write still returns 200
        # with "success":false and diagnostic text in "stderr". Both cases must
        # be distinguished here; only success:true is a real success.
        case "${_body_resp}" in
            *'"success":true'*)
                _bytes="$(printf '%s' "${_body_resp}" | sed -n 's/.*"bytes_written":\([0-9]*\).*/\1/p')"
                echo "[ssh-write-file] OK: wrote ${_bytes:-?} bytes to ${_host}:${_path}"
                exit 0
                ;;
            *)
                echo "[ssh-write-file] ERROR: remote write failed: ${_body_resp}" >&2
                exit 1
                ;;
        esac
        ;;
    000)
        echo "[ssh-write-file] ERROR: gateway unreachable (${_gw_url})" >&2
        exit 1
        ;;
    *)
        echo "[ssh-write-file] ERROR: gateway returned HTTP ${_response}: ${_body_resp}" >&2
        exit 1
        ;;
esac
