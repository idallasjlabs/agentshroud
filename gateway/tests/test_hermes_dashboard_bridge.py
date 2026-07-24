# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for the Hermes dashboard bridge's HTTP header rewrite (2026-07 502/400 fix).

Hermes's dashboard binds 127.0.0.1 inside its own container and its vendor CLI
enforces Starlette TrustedHostMiddleware: any request whose Host header isn't
"127.0.0.1:<port>" gets a 400 ("Invalid Host header. Dashboard requests must use
the hostname the server was bound to."), regardless of the actual TCP source.
docker/bots/hermes/dashboard_bridge.py (the in-container relay that makes the
loopback-bound dashboard reachable from gateway — see
gateway/tests/test_security_regressions_v1_2.py::TestHermesDashboardBridgeReachability)
must rewrite the Host header to match, or every real request (which always
arrives with Host: marvin.tail240ea8.ts.net or similar) gets rejected.

The module under test lives in the Hermes image (docker/bots/hermes/dashboard_bridge.py)
and is self-contained (no gateway imports) so it works inside that image. We load it
here by file path, following the same pattern as test_hermes_model_resolver.py.
"""

from __future__ import annotations

import importlib.util
import pathlib

import pytest

_BRIDGE_PATH = (
    pathlib.Path(__file__).resolve().parents[2]
    / "docker"
    / "bots"
    / "hermes"
    / "dashboard_bridge.py"
)


@pytest.fixture(scope="module")
def bridge_module():
    if not _BRIDGE_PATH.exists():
        pytest.skip("dashboard_bridge.py not available in this environment")
    spec = importlib.util.spec_from_file_location("dashboard_bridge", _BRIDGE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestRewriteRequestHeaders:
    def test_rewrites_host_header_to_target(self, bridge_module):
        headers = b"GET /sessions HTTP/1.1\r\nHost: marvin.tail240ea8.ts.net:9119\r\nAccept: */*"
        out = bridge_module.rewrite_request_headers(headers, b"127.0.0.1:9119")
        assert b"Host: 127.0.0.1:9119" in out
        assert b"marvin.tail240ea8.ts.net" not in out

    def test_host_header_match_is_case_insensitive(self, bridge_module):
        headers = b"GET / HTTP/1.1\r\nHOST: example.com\r\nAccept: */*"
        out = bridge_module.rewrite_request_headers(headers, b"127.0.0.1:9119")
        assert b"127.0.0.1:9119" in out
        assert b"example.com" not in out

    def test_forces_connection_close_on_plain_request(self, bridge_module):
        """Forcing Connection: close makes every request single-shot per TCP
        connection, so we never need to track HTTP/1.1 keep-alive framing
        (Content-Length/chunked) just to find the next request's headers.
        """
        headers = b"GET / HTTP/1.1\r\nHost: marvin.tail240ea8.ts.net\r\nConnection: keep-alive"
        out = bridge_module.rewrite_request_headers(headers, b"127.0.0.1:9119")
        assert b"Connection: close" in out
        assert b"keep-alive" not in out

    def test_adds_connection_close_when_absent(self, bridge_module):
        headers = b"GET / HTTP/1.1\r\nHost: marvin.tail240ea8.ts.net"
        out = bridge_module.rewrite_request_headers(headers, b"127.0.0.1:9119")
        assert b"Connection: close" in out

    def test_websocket_upgrade_keeps_connection_header_untouched(self, bridge_module):
        """A WebSocket upgrade MUST keep Connection: Upgrade (not close) or the
        handshake — and the long-lived session after it — breaks.
        """
        headers = (
            b"GET /ws HTTP/1.1\r\n"
            b"Host: marvin.tail240ea8.ts.net\r\n"
            b"Connection: Upgrade\r\n"
            b"Upgrade: websocket"
        )
        out = bridge_module.rewrite_request_headers(headers, b"127.0.0.1:9119")
        assert b"Connection: Upgrade" in out
        assert b"Upgrade: websocket" in out
        assert b"127.0.0.1:9119" in out

    def test_preserves_other_headers_and_order(self, bridge_module):
        headers = (
            b"GET /sessions HTTP/1.1\r\n"
            b"Host: marvin.tail240ea8.ts.net\r\n"
            b"Accept: application/json\r\n"
            b"X-Custom: value"
        )
        out = bridge_module.rewrite_request_headers(headers, b"127.0.0.1:9119")
        lines = out.split(b"\r\n")
        assert lines[0] == b"GET /sessions HTTP/1.1"
        assert b"Accept: application/json" in lines
        assert b"X-Custom: value" in lines
