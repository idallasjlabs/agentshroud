#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# scripts/smoke.d/test-edge-isolation.sh — LIVE network-isolation smoke test for
# the Inbound MCP Edge container (SCRUM-217). Companion to the static contract in
# gateway/tests/test_edge_network_isolation.py: that test pins the compose file,
# this one proves the running network actually behaves that way.
#
# Runs probes from INSIDE the running edge container (docker exec, using the
# image's own python — no tools are added to the image) against:
#
#   T1. Hermes API       <hermes>:8642            — by name AND by container IP
#   T2. OpenClaw         <openclaw>:18789          — by name AND by container IP
#   T3. docker-socket-proxy :2375                  — by name AND by container IP
#   T4. Internet         1.1.1.1:443               — must be unroutable (DMZ internal)
#   T5. Gateway CONNECT proxy gateway:8181         — reachable at TCP level (same
#       container as /edge/v1) but must refuse to tunnel for the DMZ subnet
#       (PROXY_ALLOWED_NETWORKS excludes it); expect any non-2xx answer
#   T6. Gateway edge door POST gateway:8080/edge/v1/rpc — MUST be reachable;
#       expect 401 (bad service token) or 503 (AGENTSHROUD_INBOUND_EDGE off)
#
# Probing by IP as well as by name matters: a DNS miss alone would "pass" a
# reachability test without proving the network blocks the connection.
#
# Requires: a running stack started with the edge (`asb up full` / profile edge).
# Read-only against every container (connect attempts and one unauthenticated
# POST); it changes no state. Intended for dev first.
#
# Container names default per account (agentshroud-bot = dev naming); override
# with EDGE_CONTAINER, HERMES_CONTAINER, OPENCLAW_CONTAINER, SOCKET_PROXY_CONTAINER.
#
# Run: bash scripts/smoke.d/test-edge-isolation.sh
# Exit 0 = pass. Exit 1 = fail. Exit 2 = precondition (edge not running).

set -euo pipefail

if [[ "${USER:-}" == "agentshroud-bot" ]]; then
    prefix="agentshroud-dev"
else
    prefix="agentshroud"
fi
EDGE_CONTAINER="${EDGE_CONTAINER:-${prefix}-mcp-edge}"
HERMES_CONTAINER="${HERMES_CONTAINER:-${prefix}-hermes-v2}"
OPENCLAW_CONTAINER="${OPENCLAW_CONTAINER:-${prefix}-openclaw}"
SOCKET_PROXY_CONTAINER="${SOCKET_PROXY_CONTAINER:-${prefix}-docker-socket-proxy}"
PROBE_TIMEOUT="${PROBE_TIMEOUT:-3}"

pass=0
fail=0

check() {
    local name="$1" condition="$2" detail="${3:-}"
    if [[ "$condition" == "true" ]]; then
        echo "  PASS  ${name}"
        pass=$((pass + 1))
    else
        echo "  FAIL  ${name}  ${detail}"
        fail=$((fail + 1))
    fi
}

if [[ "$(docker inspect -f '{{.State.Running}}' "$EDGE_CONTAINER" 2>/dev/null || true)" != "true" ]]; then
    echo "PRECONDITION: edge container '${EDGE_CONTAINER}' is not running — start the stack with the edge profile first." >&2
    exit 2
fi

# TCP connect from inside the edge. Prints "open", "refused", "timeout",
# "unresolved" or "unreachable:<errno>". Only "open" means reachable.
_tcp_probe() {
    local host="$1" port="$2"
    docker exec "$EDGE_CONTAINER" python -c '
import socket, sys
host, port, timeout = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
try:
    socket.create_connection((host, port), timeout=timeout).close()
    print("open")
except socket.gaierror:
    print("unresolved")
except ConnectionRefusedError:
    print("refused")
except (socket.timeout, TimeoutError):
    print("timeout")
except OSError as exc:
    print("unreachable:%s" % exc.errno)
' "$host" "$port" "$PROBE_TIMEOUT" 2>/dev/null || echo "exec-failed"
}

# HTTP request from inside the edge. Prints the status code, or "error:<type>".
_http_probe() {
    local method="$1" url="$2"
    docker exec "$EDGE_CONTAINER" python -c '
import sys, urllib.request, urllib.error
method, url, timeout = sys.argv[1], sys.argv[2], float(sys.argv[3])
req = urllib.request.Request(url, method=method, data=b"{}" if method == "POST" else None,
                             headers={"Content-Type": "application/json"})
try:
    print(urllib.request.urlopen(req, timeout=timeout).status)
except urllib.error.HTTPError as exc:
    print(exc.code)
except Exception as exc:
    print("error:%s" % type(exc).__name__)
' "$method" "$url" "$PROBE_TIMEOUT" 2>/dev/null || echo "exec-failed"
}

# Raw CONNECT through the gateway proxy. Prints the status line's code or "error".
_connect_probe() {
    docker exec "$EDGE_CONTAINER" python -c '
import socket, sys
timeout = float(sys.argv[1])
try:
    s = socket.create_connection(("gateway", 8181), timeout=timeout)
    s.sendall(b"CONNECT example.com:443 HTTP/1.1\r\nHost: example.com:443\r\n\r\n")
    line = s.recv(256).split(b"\r\n", 1)[0].decode("latin-1")
    s.close()
    parts = line.split()
    print(parts[1] if len(parts) > 1 else "closed")
except OSError as exc:
    print("error:%s" % type(exc).__name__)
' "$PROBE_TIMEOUT" 2>/dev/null || echo "exec-failed"
}

# Every IPv4 address a container has, across all its networks (may be empty).
_container_ips() {
    docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}} {{end}}' "$1" 2>/dev/null || true
}

# Assert a target is NOT reachable from the edge, by name and by every IP.
_assert_blocked() {
    local label="$1" container="$2" port="$3" result ip
    result="$(_tcp_probe "$container" "$port")"
    check "${label} by name (${container}:${port}) blocked" \
        "$([[ "$result" != "open" && "$result" != "exec-failed" ]] && echo true || echo false)" "got: ${result}"
    local ips
    ips="$(_container_ips "$container")"
    if [[ -z "${ips// /}" ]]; then
        echo "  NOTE  ${label}: container '${container}' not running — IP probe skipped, name probe above still counts"
        return 0
    fi
    for ip in $ips; do
        result="$(_tcp_probe "$ip" "$port")"
        check "${label} by IP (${ip}:${port}) blocked" \
            "$([[ "$result" != "open" && "$result" != "exec-failed" ]] && echo true || echo false)" "got: ${result}"
    done
}

echo "=== Inbound MCP Edge isolation (from ${EDGE_CONTAINER}) ==="

echo "T1: Hermes API"
_assert_blocked "Hermes API" "$HERMES_CONTAINER" 8642

echo "T2: OpenClaw"
_assert_blocked "OpenClaw" "$OPENCLAW_CONTAINER" 18789

echo "T3: docker-socket-proxy"
_assert_blocked "docker-socket-proxy" "$SOCKET_PROXY_CONTAINER" 2375

echo "T4: Internet"
r4="$(_tcp_probe 1.1.1.1 443)"
check "1.1.1.1:443 unreachable" \
    "$([[ "$r4" != "open" && "$r4" != "exec-failed" ]] && echo true || echo false)" "got: ${r4}"

echo "T5: Gateway CONNECT proxy refuses the DMZ"
r5="$(_connect_probe)"
check "CONNECT example.com:443 via gateway:8181 not tunnelled" \
    "$([[ ! "$r5" =~ ^2[0-9][0-9]$ && "$r5" != "exec-failed" ]] && echo true || echo false)" "got: ${r5}"

echo "T6: Gateway edge door reachable"
r6="$(_http_probe POST http://gateway:8080/edge/v1/rpc)"
check "POST gateway:8080/edge/v1/rpc answers 401 or 503" \
    "$([[ "$r6" == "401" || "$r6" == "503" ]] && echo true || echo false)" "got: ${r6}"

echo ""
echo "=== Results: ${pass} passed, ${fail} failed ==="
[[ "$fail" -eq 0 ]]
