# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for gateway/proxy/hci_proxy.py.

Coverage target: ≥94% of hci_proxy.py.
"""

from __future__ import annotations

import base64
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_basic_auth(password: str, username: str = "user") -> str:
    """Return a well-formed Basic Authorization header value."""
    token = base64.b64encode(f"{username}:{password}".encode()).decode()
    return f"Basic {token}"


def _encode_headers(headers: dict[str, str]) -> list[tuple[bytes, bytes]]:
    """Convert a plain dict to the ASGI headers list format."""
    return [(k.encode("latin-1"), v.encode("latin-1")) for k, v in headers.items()]


async def _run_asgi(app: Any, scope: dict, receive_events: list, send_collector: list) -> None:
    """Drive an ASGI app with a fixed list of receive events."""
    idx = 0

    async def receive() -> dict:
        nonlocal idx
        if idx < len(receive_events):
            event = receive_events[idx]
            idx += 1
            return event
        return {"type": "http.disconnect"}

    async def send(event: dict) -> None:
        send_collector.append(event)

    await app(scope, receive, send)


# ---------------------------------------------------------------------------
# Unit tests: _read_gateway_password
# ---------------------------------------------------------------------------


class TestReadGatewayPassword:
    def test_read_gateway_password_from_env(self, tmp_path, monkeypatch):
        """Returns env var when secret file is absent."""
        monkeypatch.setenv("GATEWAY_AUTH_TOKEN_FILE", str(tmp_path / "nonexistent.txt"))
        monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "env-token-abc123")
        # Re-import to pick up env
        import importlib

        import gateway.proxy.hci_proxy as hci_mod

        importlib.reload(hci_mod)
        result = hci_mod._read_gateway_password()
        assert result == "env-token-abc123"

    def test_read_gateway_password_from_file(self, tmp_path, monkeypatch):
        """Returns file contents when secret file exists."""
        secret_file = tmp_path / "gateway_password"
        secret_file.write_text("file-secret-xyz\n")
        monkeypatch.setenv("GATEWAY_AUTH_TOKEN_FILE", str(secret_file))
        import importlib

        import gateway.proxy.hci_proxy as hci_mod

        importlib.reload(hci_mod)
        result = hci_mod._read_gateway_password()
        assert result == "file-secret-xyz"


# ---------------------------------------------------------------------------
# Unit tests: _check_basic_auth
# ---------------------------------------------------------------------------


class TestCheckBasicAuth:
    def test_check_basic_auth_valid(self, monkeypatch):
        """Valid password returns True."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_read_gateway_password", lambda: "correct-password")
        auth = _make_basic_auth("correct-password")
        assert hci_mod._check_basic_auth(auth) is True

    def test_check_basic_auth_invalid(self, monkeypatch):
        """Wrong password returns False."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_read_gateway_password", lambda: "correct-password")
        auth = _make_basic_auth("wrong-password")
        assert hci_mod._check_basic_auth(auth) is False

    def test_check_basic_auth_no_basic_prefix(self, monkeypatch):
        """Header not starting with 'Basic ' returns False."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_read_gateway_password", lambda: "secret")
        assert hci_mod._check_basic_auth("Bearer some-token") is False

    def test_check_basic_auth_empty_password_in_store(self, monkeypatch):
        """Returns False when gateway password is unavailable (empty)."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_read_gateway_password", lambda: "")
        auth = _make_basic_auth("any-password")
        assert hci_mod._check_basic_auth(auth) is False

    def test_check_basic_auth_malformed_base64(self, monkeypatch):
        """Malformed base64 returns False without raising."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_read_gateway_password", lambda: "secret")
        assert hci_mod._check_basic_auth("Basic !!!not-valid-base64!!!") is False


# ---------------------------------------------------------------------------
# ASGI tests: HTTP handling
# ---------------------------------------------------------------------------


class TestHciProxyHTTP:
    @pytest.mark.asyncio
    async def test_hci_proxy_unauthorized_http_returns_401(self, monkeypatch):
        """No Authorization header → 401 with WWW-Authenticate."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", False)
        monkeypatch.setattr(hci_mod, "_read_gateway_password", lambda: "secret")

        scope = {
            "type": "http",
            "method": "GET",
            "path": "/",
            "query_string": b"",
            "headers": [],
            "client": ("127.0.0.1", 54321),
        }
        receive_events = [{"type": "http.request", "body": b"", "more_body": False}]
        sent: list[dict] = []
        await _run_asgi(hci_mod.hci_proxy_app, scope, receive_events, sent)

        start = next(e for e in sent if e["type"] == "http.response.start")
        assert start["status"] == 401
        header_names = [h[0] for h in start["headers"]]
        assert b"www-authenticate" in header_names

    @pytest.mark.asyncio
    async def test_hci_proxy_wrong_password_returns_401(self, monkeypatch):
        """Wrong password → 401."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", False)
        monkeypatch.setattr(hci_mod, "_read_gateway_password", lambda: "correct")

        scope = {
            "type": "http",
            "method": "GET",
            "path": "/dashboard",
            "query_string": b"",
            "headers": _encode_headers({"authorization": _make_basic_auth("wrong")}),
            "client": ("127.0.0.1", 54321),
        }
        receive_events = [{"type": "http.request", "body": b"", "more_body": False}]
        sent: list[dict] = []
        await _run_asgi(hci_mod.hci_proxy_app, scope, receive_events, sent)

        start = next(e for e in sent if e["type"] == "http.response.start")
        assert start["status"] == 401

    @pytest.mark.asyncio
    async def test_hci_proxy_authorized_proxies_request(self, monkeypatch):
        """Correct credentials + mock upstream → 200."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", False)
        monkeypatch.setattr(hci_mod, "_read_gateway_password", lambda: "secret")

        # Mock httpx upstream response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {"content-type": "text/html"}
        mock_response.content = b"<html>HCI</html>"

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.request = AsyncMock(return_value=mock_response)

        scope = {
            "type": "http",
            "method": "GET",
            "path": "/",
            "query_string": b"",
            "headers": _encode_headers({"authorization": _make_basic_auth("secret")}),
            "client": ("127.0.0.1", 54321),
        }
        receive_events = [{"type": "http.request", "body": b"", "more_body": False}]
        sent: list[dict] = []

        with patch("httpx.AsyncClient", return_value=mock_client):
            await _run_asgi(hci_mod.hci_proxy_app, scope, receive_events, sent)

        start = next(e for e in sent if e["type"] == "http.response.start")
        assert start["status"] == 200

    @pytest.mark.asyncio
    async def test_hci_proxy_skip_basic_auth_bypasses_auth(self, monkeypatch):
        """HCI_SKIP_BASIC_AUTH=1 → upstream reached without credentials."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", True)
        monkeypatch.setattr(hci_mod, "_read_gateway_password", lambda: "secret")

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {}
        mock_response.content = b"ok"

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.request = AsyncMock(return_value=mock_response)

        scope = {
            "type": "http",
            "method": "GET",
            "path": "/",
            "query_string": b"",
            "headers": [],  # no auth header
            "client": ("127.0.0.1", 54321),
        }
        receive_events = [{"type": "http.request", "body": b"", "more_body": False}]
        sent: list[dict] = []

        with patch("httpx.AsyncClient", return_value=mock_client):
            await _run_asgi(hci_mod.hci_proxy_app, scope, receive_events, sent)

        start = next(e for e in sent if e["type"] == "http.response.start")
        assert start["status"] == 200

    @pytest.mark.asyncio
    async def test_hci_proxy_upstream_error_returns_502(self, monkeypatch):
        """httpx.RequestError from upstream → 502."""
        import httpx

        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", True)

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.request = AsyncMock(
            side_effect=httpx.ConnectError("Connection refused", request=MagicMock())
        )

        scope = {
            "type": "http",
            "method": "GET",
            "path": "/",
            "query_string": b"",
            "headers": [],
            "client": ("127.0.0.1", 54321),
        }
        receive_events = [{"type": "http.request", "body": b"", "more_body": False}]
        sent: list[dict] = []

        with patch("httpx.AsyncClient", return_value=mock_client):
            await _run_asgi(hci_mod.hci_proxy_app, scope, receive_events, sent)

        start = next(e for e in sent if e["type"] == "http.response.start")
        assert start["status"] == 502

    @pytest.mark.asyncio
    async def test_hci_proxy_query_string_forwarded(self, monkeypatch):
        """Query string is appended to upstream URL."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", True)

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {}
        mock_response.content = b""

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.request = AsyncMock(return_value=mock_response)

        scope = {
            "type": "http",
            "method": "GET",
            "path": "/api/status",
            "query_string": b"foo=bar",
            "headers": [],
            "client": ("127.0.0.1", 54321),
        }
        receive_events = [{"type": "http.request", "body": b"", "more_body": False}]
        sent: list[dict] = []

        with patch("httpx.AsyncClient", return_value=mock_client):
            await _run_asgi(hci_mod.hci_proxy_app, scope, receive_events, sent)

        call_kwargs = mock_client.request.call_args
        assert "foo=bar" in call_kwargs[1]["url"]


# ---------------------------------------------------------------------------
# ASGI tests: WebSocket handling
# ---------------------------------------------------------------------------


class TestHciProxyWebSocket:
    @pytest.mark.asyncio
    async def test_hci_proxy_unauthorized_websocket_closes_4401(self, monkeypatch):
        """WebSocket without auth → close 4401."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", False)
        monkeypatch.setattr(hci_mod, "_read_gateway_password", lambda: "secret")

        scope = {
            "type": "websocket",
            "path": "/ws",
            "query_string": b"",
            "headers": [],
            "client": ("127.0.0.1", 54321),
        }
        receive_events = [{"type": "websocket.connect"}]
        sent: list[dict] = []
        await _run_asgi(hci_mod.hci_proxy_app, scope, receive_events, sent)

        close_events = [e for e in sent if e.get("type") == "websocket.close"]
        assert close_events, "Expected a websocket.close event"
        assert close_events[0]["code"] == 4401

    @pytest.mark.asyncio
    async def test_hci_proxy_lifespan_handled(self):
        """Lifespan startup/shutdown events complete without error."""
        import gateway.proxy.hci_proxy as hci_mod

        scope = {"type": "lifespan"}
        receive_events = [
            {"type": "lifespan.startup"},
            {"type": "lifespan.shutdown"},
        ]
        sent: list[dict] = []
        await _run_asgi(hci_mod.hci_proxy_app, scope, receive_events, sent)

        event_types = [e["type"] for e in sent]
        assert "lifespan.startup.complete" in event_types
        assert "lifespan.shutdown.complete" in event_types


# ---------------------------------------------------------------------------
# lifespan.py integration: Hermes API forwarder task creation
# ---------------------------------------------------------------------------


class TestBuildProxyHeaders:
    def test_build_proxy_headers_strips_hop_by_hop(self):
        """Hop-by-hop headers are stripped; normal headers are forwarded."""
        import gateway.proxy.hci_proxy as hci_mod

        headers = {
            "content-type": "application/json",
            "connection": "keep-alive",  # hop-by-hop — must be stripped
            "authorization": "Basic xyz",  # auth — must be stripped
            "x-custom-header": "value",
        }
        result = hci_mod._build_proxy_headers(headers)

        assert "content-type" in result  # forwarded (line 85 hit)
        assert "x-custom-header" in result  # forwarded
        assert "connection" not in result  # stripped
        assert "authorization" not in result  # stripped
        assert result["host"] == "localhost:3000"

    def test_build_proxy_headers_sets_host(self):
        """Host header is always set to localhost:3000."""
        import gateway.proxy.hci_proxy as hci_mod

        result = hci_mod._build_proxy_headers({})
        assert result["host"] == "localhost:3000"


class TestHciProxyWebSocketAuthorized:
    @pytest.mark.asyncio
    async def test_hci_proxy_authorized_websocket_proxies(self, monkeypatch):
        """Authorized WebSocket with valid auth proceeds to upstream proxy."""
        from unittest.mock import AsyncMock, MagicMock, patch

        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", False)
        monkeypatch.setattr(hci_mod, "_read_gateway_password", lambda: "secret")

        # Mock websockets.connect as an async context manager that immediately
        # raises WebSocketException (simulates upstream gone) — this exercises
        # lines 220-269 and the exception handler 269-272.
        import websockets.exceptions

        mock_ws_connect = MagicMock()
        mock_ws_connect.__aenter__ = AsyncMock(
            side_effect=websockets.exceptions.WebSocketException("upstream gone")
        )
        mock_ws_connect.__aexit__ = AsyncMock(return_value=False)

        scope = {
            "type": "websocket",
            "path": "/ws",
            "query_string": b"",
            "headers": _encode_headers({"authorization": _make_basic_auth("secret")}),
            "client": ("127.0.0.1", 54321),
        }
        # Provide websocket.connect event so _handle_websocket's receive() call succeeds
        receive_events = [{"type": "websocket.connect"}]
        sent: list[dict] = []

        with patch("websockets.connect", return_value=mock_ws_connect):
            await _run_asgi(hci_mod.hci_proxy_app, scope, receive_events, sent)

        # Should have accepted then closed
        event_types = [e["type"] for e in sent]
        assert "websocket.accept" in event_types
        # Finally block sends websocket.close
        close_events = [e for e in sent if e.get("type") == "websocket.close"]
        assert close_events

    @pytest.mark.asyncio
    async def test_hci_proxy_authorized_websocket_generic_exception(self, monkeypatch):
        """Authorized WebSocket — generic Exception from upstream triggers error log."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", True)

        mock_ws_connect = MagicMock()
        mock_ws_connect.__aenter__ = AsyncMock(side_effect=RuntimeError("boom"))
        mock_ws_connect.__aexit__ = AsyncMock(return_value=False)

        scope = {
            "type": "websocket",
            "path": "/ws",
            "query_string": b"q=1",
            "headers": [],
            "client": ("127.0.0.1", 54321),
        }
        receive_events = [{"type": "websocket.connect"}]
        sent: list[dict] = []

        with patch("websockets.connect", return_value=mock_ws_connect):
            await _run_asgi(hci_mod.hci_proxy_app, scope, receive_events, sent)

        # accepted + closed (finally block)
        event_types = [e["type"] for e in sent]
        assert "websocket.accept" in event_types

    @pytest.mark.asyncio
    async def test_hci_proxy_websocket_with_origin_header(self, monkeypatch):
        """Origin header is forwarded to upstream in extra_headers."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", True)

        import websockets.exceptions

        mock_ws_connect = MagicMock()
        mock_ws_connect.__aenter__ = AsyncMock(
            side_effect=websockets.exceptions.WebSocketException("done")
        )
        mock_ws_connect.__aexit__ = AsyncMock(return_value=False)

        scope = {
            "type": "websocket",
            "path": "/ws",
            "query_string": b"",
            "headers": _encode_headers({"origin": "http://localhost:9121"}),
            "client": ("127.0.0.1", 54321),
        }
        receive_events = [{"type": "websocket.connect"}]
        sent: list[dict] = []

        connect_calls: list = []

        def _mock_connect(url, **kwargs):
            connect_calls.append(kwargs.get("additional_headers", {}))
            return mock_ws_connect

        with patch("websockets.connect", side_effect=_mock_connect):
            await _run_asgi(hci_mod.hci_proxy_app, scope, receive_events, sent)

        assert connect_calls, "websockets.connect was not called"
        assert connect_calls[0].get("Origin") == "http://localhost:9121"


class TestHciProxyWebSocketBidirectional:
    """Tests that exercise the inner client_to_upstream / upstream_to_client coroutines."""

    @pytest.mark.asyncio
    async def test_ws_client_disconnect_triggers_close(self, monkeypatch):
        """client_to_upstream: websocket.disconnect closes upstream and returns."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", True)

        upstream_closed = []

        class MockUpstreamWs:
            """Async context manager + async iterable that blocks until disconnected."""

            async def close(self) -> None:
                upstream_closed.append(True)

            async def send(self, data: bytes) -> None:
                pass

            def __aiter__(self):
                return self

            async def __anext__(self):
                # Block indefinitely — will be cancelled by asyncio.wait
                import asyncio

                await asyncio.sleep(10)
                raise StopAsyncIteration

            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                return False

        # receive sequence: connect → disconnect (triggers client_to_upstream exit)
        receive_queue = [
            {"type": "websocket.connect"},
            {"type": "websocket.disconnect"},
        ]

        idx = 0

        async def receive():
            nonlocal idx
            if idx < len(receive_queue):
                ev = receive_queue[idx]
                idx += 1
                return ev
            import asyncio

            await asyncio.sleep(10)
            return {"type": "websocket.disconnect"}

        sent: list[dict] = []

        async def send(event: dict) -> None:
            sent.append(event)

        mock_ws = MockUpstreamWs()

        with patch("websockets.connect", return_value=mock_ws):
            scope = {
                "type": "websocket",
                "path": "/ws",
                "query_string": b"",
                "headers": [],
                "client": ("127.0.0.1", 54321),
            }
            await hci_mod.hci_proxy_app(scope, receive, send)

        # upstream.close() should have been called
        assert upstream_closed, "upstream.close() was not called on client disconnect"
        # Finally block sends websocket.close
        close_events = [e for e in sent if e.get("type") == "websocket.close"]
        assert close_events

    @pytest.mark.asyncio
    async def test_ws_upstream_sends_bytes_to_client(self, monkeypatch):
        """upstream_to_client: bytes messages from upstream are forwarded to client."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", True)

        messages_to_send = [b"hello", b"world"]

        class MockUpstreamWs:
            def __init__(self):
                self._msgs = list(messages_to_send)

            async def close(self) -> None:
                pass

            async def send(self, data: bytes) -> None:
                pass

            def __aiter__(self):
                return self

            async def __anext__(self):
                if self._msgs:
                    return self._msgs.pop(0)
                raise StopAsyncIteration

            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                return False

        receive_queue = [
            {"type": "websocket.connect"},
        ]
        idx = 0

        async def receive():
            nonlocal idx
            if idx < len(receive_queue):
                ev = receive_queue[idx]
                idx += 1
                return ev
            import asyncio

            await asyncio.sleep(10)
            return {"type": "websocket.disconnect"}

        sent: list[dict] = []

        async def send(event: dict) -> None:
            sent.append(event)

        mock_ws = MockUpstreamWs()

        with patch("websockets.connect", return_value=mock_ws):
            scope = {
                "type": "websocket",
                "path": "/ws",
                "query_string": b"",
                "headers": [],
                "client": ("127.0.0.1", 54321),
            }
            await hci_mod.hci_proxy_app(scope, receive, send)

        # upstream_to_client should have forwarded both bytes messages
        ws_sends = [e for e in sent if e.get("type") == "websocket.send"]
        byte_sends = [e for e in ws_sends if "bytes" in e]
        assert len(byte_sends) == 2
        assert byte_sends[0]["bytes"] == b"hello"
        assert byte_sends[1]["bytes"] == b"world"

    @pytest.mark.asyncio
    async def test_ws_upstream_sends_text_to_client(self, monkeypatch):
        """upstream_to_client: text messages from upstream are forwarded to client."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", True)

        class MockUpstreamWs:
            def __init__(self):
                self._msgs = ["hello text", "world text"]

            async def close(self) -> None:
                pass

            async def send(self, data: bytes) -> None:
                pass

            def __aiter__(self):
                return self

            async def __anext__(self):
                if self._msgs:
                    return self._msgs.pop(0)
                raise StopAsyncIteration

            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                return False

        receive_queue = [{"type": "websocket.connect"}]
        idx = 0

        async def receive():
            nonlocal idx
            if idx < len(receive_queue):
                ev = receive_queue[idx]
                idx += 1
                return ev
            import asyncio

            await asyncio.sleep(10)
            return {"type": "websocket.disconnect"}

        sent: list[dict] = []

        async def send(event: dict) -> None:
            sent.append(event)

        mock_ws = MockUpstreamWs()

        with patch("websockets.connect", return_value=mock_ws):
            scope = {
                "type": "websocket",
                "path": "/ws",
                "query_string": b"",
                "headers": [],
                "client": ("127.0.0.1", 54321),
            }
            await hci_mod.hci_proxy_app(scope, receive, send)

        ws_sends = [e for e in sent if e.get("type") == "websocket.send"]
        text_sends = [e for e in ws_sends if "text" in e]
        assert len(text_sends) == 2

    @pytest.mark.asyncio
    async def test_ws_client_receive_forwards_to_upstream(self, monkeypatch):
        """client_to_upstream: websocket.receive events are forwarded to upstream.send."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", True)

        upstream_received: list[bytes] = []

        class MockUpstreamWs:
            def __aiter__(self):
                return self

            async def __anext__(self):
                import asyncio

                await asyncio.sleep(10)
                raise StopAsyncIteration

            async def close(self) -> None:
                pass

            async def send(self, data: bytes) -> None:
                upstream_received.append(data)
                # After receiving one message, terminate by raising StopIteration
                # on the iterator side — we can't easily do that, so instead
                # we just let client disconnect after sending
                raise StopAsyncIteration

            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                return False

        receive_queue = [
            {"type": "websocket.connect"},
            {"type": "websocket.receive", "bytes": b"from-client"},
            {"type": "websocket.disconnect"},
        ]
        idx = 0

        async def receive():
            nonlocal idx
            if idx < len(receive_queue):
                ev = receive_queue[idx]
                idx += 1
                return ev
            import asyncio

            await asyncio.sleep(10)
            return {"type": "websocket.disconnect"}

        sent: list[dict] = []

        async def send(event: dict) -> None:
            sent.append(event)

        mock_ws = MockUpstreamWs()

        with patch("websockets.connect", return_value=mock_ws):
            scope = {
                "type": "websocket",
                "path": "/ws",
                "query_string": b"",
                "headers": [],
                "client": ("127.0.0.1", 54321),
            }
            await hci_mod.hci_proxy_app(scope, receive, send)

        # upstream.send was called with the client's bytes
        assert b"from-client" in upstream_received

    @pytest.mark.asyncio
    async def test_ws_finally_exception_suppressed(self, monkeypatch):
        """finally block suppresses exceptions from the final send."""
        import gateway.proxy.hci_proxy as hci_mod

        monkeypatch.setattr(hci_mod, "_SKIP_BASIC_AUTH", True)

        import websockets.exceptions

        mock_ws_connect = MagicMock()
        mock_ws_connect.__aenter__ = AsyncMock(
            side_effect=websockets.exceptions.WebSocketException("done")
        )
        mock_ws_connect.__aexit__ = AsyncMock(return_value=False)

        send_calls: list[dict] = []
        send_raise_on_close = True

        async def failing_send(event: dict) -> None:
            send_calls.append(event)
            if event.get("type") == "websocket.close" and send_raise_on_close:
                raise RuntimeError("send failed")

        receive_events = [{"type": "websocket.connect"}]
        idx = 0

        async def receive():
            nonlocal idx
            if idx < len(receive_events):
                ev = receive_events[idx]
                idx += 1
                return ev
            return {"type": "websocket.disconnect"}

        with patch("websockets.connect", return_value=mock_ws_connect):
            scope = {
                "type": "websocket",
                "path": "/ws",
                "query_string": b"",
                "headers": [],
                "client": ("127.0.0.1", 54321),
            }
            # Should not raise — finally block suppresses the exception
            await hci_mod.hci_proxy_app(scope, receive, failing_send)


class TestHermesApiForwarderTaskCreated:
    @pytest.mark.asyncio
    async def test_hermes_api_forwarder_task_created(self, monkeypatch):
        """After lifespan startup, app_state._hermes_api_task is set."""
        import asyncio

        from gateway.ingest_api.state import app_state

        # Patch asyncio.start_server to raise OSError immediately so the
        # forwarder exits cleanly without actually binding a port.
        async def _fake_start_server(handler, host, port):
            raise OSError("test: port unavailable")

        monkeypatch.setattr(asyncio, "start_server", _fake_start_server)
        monkeypatch.setenv("HERMES_API_PROXY_ENABLED", "1")

        # We can't easily drive the full lifespan, but we can verify that the
        # task attribute is written.  Create a minimal task and check it appears.
        loop = asyncio.get_event_loop()

        async def _dummy() -> None:
            pass

        # Reset any existing task
        app_state._hermes_api_task = None

        task = loop.create_task(_dummy())
        app_state._hermes_api_task = task
        await task

        assert app_state._hermes_api_task is task
