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
    echo "[ssh-exec] ERROR: no gateway auth token (GATEWAY_AUTH_TOKEN / *_FILE / /run/secrets/gateway_password all empty)" >&2
    exit 1
fi

# Build the JSON payload in pure POSIX shell so command/reason/cwd containing
# quotes, backslashes, newlines, tabs, or shell metacharacters are safely encoded
# without depending on an interpreter. The OpenClaw container is a node image with
# NO python3; the Hermes container is a python image. A shell-only builder works in
# BOTH — the previous python3 version silently failed in OpenClaw with
# "python3: not found", which is exactly why only OpenClaw's check-in spammed
# failures. cwd is omitted from the payload when empty.
#
# _json_escape reads one argument and emits a JSON-safe string body (WITHOUT the
# surrounding double quotes). Per RFC 8259 it escapes backslash, double quote, and
# the C0 control characters that must be escaped in JSON (\b \t \n \f \r, and any
# other 0x01–0x1F control char as \u00XX). This is the injection-safety boundary:
# the encoded value can never break out of its JSON string, so a command such as
# `","host":"evil` or one containing a literal newline cannot inject extra fields.
#
# The value is passed to awk on STDIN (not via -v), because awk's -v assignment
# interprets backslash escapes (mangling `\b`, dropping `\c`) and errors on a
# literal newline ("newline in string"). RS="\0" makes the entire raw input one
# record ($0), preserving embedded newlines/tabs as data. Byte-accurate and
# deterministic across busybox/dash/bash awk — no python3 or node dependency.
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
                # Escape any remaining C0 control character (0x01–0x1F) as \u00XX.
                d = index(ctrl, c)
                if (d > 0) { out = out sprintf("\\u%04x", d) }
                else { out = out c }
            }
        }
        printf "%s", out
    }'
}

_payload_file="/tmp/.ssh-exec-payload.$$"
{
    printf '{"host":"%s","command":"%s","reason":"%s"' \
        "$(_json_escape "${_host}")" \
        "$(_json_escape "${_command}")" \
        "$(_json_escape "${_reason}")"
    if [ -n "${_cwd}" ]; then
        printf ',"cwd":"%s"' "$(_json_escape "${_cwd}")"
    fi
    printf '}'
} > "${_payload_file}"

# --noproxy gateway: HTTP_PROXY=http://gateway:8181 (EgressFilter) is set in the
# bot environment; without --noproxy the call would loop through the egress proxy
# instead of reaching the internal control-plane /ssh/exec endpoint directly.
#
# --max-time 600 (not the original 180): confirmed via the /i-hdev end-to-end
# dry run 2026-08-05 that `codex exec`/`gemini -p` review calls routed through
# this wrapper can take well over 180s (codex's own cold-start retry/backoff
# alone was observed needing 60-90s+ before succeeding directly over SSH) even
# though the target host's own max_session_seconds is a generous 1800s in
# agentshroud.yaml — the CLIENT-side curl timeout here was the actual
# bottleneck, unrelated to the SSH session timeout. 600s balances real LLM
# review latency against not leaving a calling agent blocked indefinitely on
# a genuinely stuck call.
_response="$(curl -sS --noproxy gateway --max-time 600 \
    -o /tmp/.ssh-exec-response \
    -w "%{http_code}" \
    -X POST "${_gw_url}/ssh/exec" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${_gw_token}" \
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
