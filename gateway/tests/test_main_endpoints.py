# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Main Endpoints Integration Tests - P1 Middleware Wiring
Tests for main.py endpoint integration with middleware blocking.
"""

from __future__ import annotations

import ipaddress
import time
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from gateway.ingest_api.main import app, auth_dep
from gateway.ingest_api.middleware import MiddlewareResult


class TestForwardEndpoint:
    """Test /forward endpoint with middleware integration."""

    def test_forward_middleware_blocking(self):
        """Test that middleware can block requests with HTTP 403."""

        # Mock middleware manager to block the request
        mock_middleware = MagicMock()
        mock_middleware.process_request = AsyncMock(
            return_value=MiddlewareResult(allowed=False, reason="Test middleware block")
        )

        # Mock auth
        MagicMock()

        with (
            patch("gateway.ingest_api.routes.forward.app_state") as mock_app_state,
            patch("gateway.ingest_api.routes.forward.create_auth_dependency") as mock_auth_dep,
        ):
            mock_app_state.middleware_manager = mock_middleware
            mock_target = MagicMock()
            mock_target.name = "openclaw"
            mock_app_state.router.resolve_target = AsyncMock(return_value=mock_target)

            client = TestClient(app)

            # Mock auth dependency
            mock_auth_dep.return_value = AsyncMock()

            response = client.post(
                "/forward",
                json={"content": "test message", "content_type": "text", "source": "api"},
                headers={"Authorization": "Bearer fake-token"},
            )

            # Should return 403 when middleware blocks
            assert response.status_code == 403
            assert "Request blocked by middleware" in response.json()["detail"]

            # Verify middleware was called
            mock_middleware.process_request.assert_called_once()

    def test_forward_middleware_allowed(self):
        """Test that middleware allows requests when they pass checks."""
        # This test requires extensive mocking of the full pipeline.
        # Covered by test_e2e.py integration tests instead.
        pass

    def test_forward_middleware_error_handling(self):
        """Test that middleware errors cause requests to be blocked."""

        # Mock middleware manager to throw an exception
        mock_middleware = MagicMock()
        mock_middleware.process.side_effect = Exception("Middleware error")

        MagicMock()

        with (
            patch("gateway.ingest_api.routes.forward.app_state") as mock_app_state,
            patch("gateway.ingest_api.routes.forward.create_auth_dependency") as mock_auth_dep,
        ):
            mock_app_state.middleware_manager = mock_middleware
            mock_target = MagicMock()
            mock_target.name = "openclaw"
            mock_app_state.router.resolve_target = AsyncMock(return_value=mock_target)

            client = TestClient(app)

            # Mock auth dependency
            mock_auth_dep.return_value = AsyncMock()

            response = client.post(
                "/forward",
                json={"content": "test message", "content_type": "text", "source": "api"},
                headers={"Authorization": "Bearer fake-token"},
            )

            # Should return 500 when middleware fails
            assert response.status_code == 500
            assert "Middleware processing failed" in response.json()["detail"]


class TestStatusEndpoint:
    """Test /status endpoint."""

    def test_status_endpoint(self):
        """Test basic status endpoint functionality."""

        with patch("gateway.ingest_api.routes.health.app_state") as mock_app_state:
            import time as _time

            mock_app_state.start_time = _time.time()
            mock_app_state.ledger = MagicMock()
            mock_app_state.ledger.get_stats = AsyncMock(return_value={"total_entries": 0})
            mock_app_state.approval_queue = MagicMock()
            mock_app_state.approval_queue.get_pending = AsyncMock(return_value=[])
            mock_app_state.sanitizer = MagicMock()
            mock_app_state.sanitizer.get_mode.return_value = "presidio"

            client = TestClient(app)

            response = client.get("/status")

            # Should return 200 OK
            assert response.status_code == 200
            assert "status" in response.json()


class TestApprovalEndpoints:
    """Test approval queue endpoints."""

    def test_approval_queue_list(self):
        """Test listing pending approvals."""

        mock_approval_queue = MagicMock()
        mock_approval_queue.get_pending = AsyncMock(return_value=[])

        with patch("gateway.ingest_api.routes.approval.app_state") as mock_app_state:
            mock_app_state.approval_queue = mock_approval_queue

            client = TestClient(app)

            # Mock auth dependency
            with patch(
                "gateway.ingest_api.routes.approval.create_auth_dependency"
            ) as mock_auth_dep:
                mock_auth_dep.return_value = AsyncMock()

                response = client.get(
                    "/approve/pending", headers={"Authorization": "Bearer fake-token"}
                )

                # Should return 200 OK
                assert response.status_code == 200

    def test_approval_decision(self):
        """Test making approval decisions."""

        mock_approval_queue = MagicMock()
        mock_approval_queue.decide = AsyncMock(side_effect=KeyError("not found"))

        with patch("gateway.ingest_api.routes.approval.app_state") as mock_app_state:
            mock_app_state.approval_queue = mock_approval_queue

            client = TestClient(app)

            # Mock auth dependency
            with patch(
                "gateway.ingest_api.routes.approval.create_auth_dependency"
            ) as mock_auth_dep:
                mock_auth_dep.return_value = AsyncMock()

                response = client.post(
                    "/approve/test-id/decide",
                    json={"request_id": "test-id", "approved": True, "reason": "test approval"},
                    headers={"Authorization": "Bearer fake-token"},
                )

                # Should return 200 or 404 (not found in mock)
                assert response.status_code in (200, 404)


class TestMCPProxyEndpoint:
    """Test /mcp/proxy endpoint."""

    def test_mcp_proxy_endpoint(self):
        """Test MCP proxy endpoint basic functionality."""

        mock_mcp_proxy = MagicMock()
        mock_result = MagicMock()
        mock_result.blocked = False
        mock_result.result = {"status": "success", "result": "test result"}
        mock_mcp_proxy.process_tool_call = AsyncMock(return_value=mock_result)

        with patch("gateway.ingest_api.main.app_state") as mock_app_state:
            mock_app_state.mcp_proxy = mock_mcp_proxy

            client = TestClient(app)

            # Mock auth dependency
            with patch("gateway.ingest_api.main.create_auth_dependency") as mock_auth_dep:
                mock_auth_dep.return_value = AsyncMock()

                response = client.post(
                    "/mcp/proxy",
                    json={"server_name": "test-server", "tool_name": "test-tool", "arguments": {}},
                    headers={"Authorization": "Bearer fake-token"},
                )

                # Should return 200 OK for successful proxy request
                assert response.status_code == 200


class TestErrorHandling:
    """Test error handling across endpoints."""

    def test_404_error(self):
        """Test 404 handling for non-existent endpoints."""

        client = TestClient(app)

        response = client.get("/nonexistent")

        assert response.status_code == 404

    def test_method_not_allowed(self):
        """Test 405 handling for wrong HTTP methods."""

        client = TestClient(app)

        # Try GET on POST-only endpoint
        response = client.get("/forward")

        assert response.status_code == 405


class TestGoogleAPIProxy:
    """Regression tests for /v1beta proxy response handling."""

    def test_google_proxy_non_json_body_passthrough(self):
        """Plain-text upstream errors must not turn into gateway 500s."""
        with (
            patch("gateway.ingest_api.main.app_state") as mock_app_state,
            patch(
                "gateway.ingest_api.main._PROXY_ALLOWED_NETWORKS",
                [ipaddress.ip_network("10.254.111.0/24")],
            ),
            patch(
                "gateway.ingest_api.main._ipaddress.ip_address",
                return_value=ipaddress.ip_address("10.254.111.10"),
            ),
        ):
            mock_app_state.llm_proxy = MagicMock()
            mock_app_state.llm_proxy.proxy_messages = AsyncMock(
                return_value=(502, {"content-type": "text/plain"}, b"upstream timeout")
            )

            client = TestClient(app)
            response = client.get("/v1beta/models")

            assert response.status_code == 502
            assert "upstream timeout" in response.text

    def test_google_proxy_json_body_passthrough(self):
        """JSON upstream responses must stay JSON."""
        with (
            patch("gateway.ingest_api.main.app_state") as mock_app_state,
            patch(
                "gateway.ingest_api.main._PROXY_ALLOWED_NETWORKS",
                [ipaddress.ip_network("10.254.111.0/24")],
            ),
            patch(
                "gateway.ingest_api.main._ipaddress.ip_address",
                return_value=ipaddress.ip_address("10.254.111.10"),
            ),
        ):
            mock_app_state.llm_proxy = MagicMock()
            mock_app_state.llm_proxy.proxy_messages = AsyncMock(
                return_value=(200, {"content-type": "application/json"}, b'{"ok": true}')
            )

            client = TestClient(app)
            response = client.get("/v1beta/models")

            assert response.status_code == 200
            assert response.json() == {"ok": True}


class TestQuarantineEndpoints:
    """Test quarantine management endpoints in main.py."""

    def test_quarantine_summary_counts_inbound_and_outbound(self):
        from gateway.ingest_api import main as main_module

        app.dependency_overrides[auth_dep] = lambda: None
        try:
            main_module.app_state.blocked_message_quarantine = [
                {"status": "pending"},
                {"status": "released"},
                {"status": "discarded"},
            ]
            main_module.app_state.blocked_outbound_quarantine = [
                {"status": "pending"},
                {"status": "pending"},
                {"status": "released"},
            ]

            client = TestClient(app)
            response = client.get("/manage/quarantine/summary")
            assert response.status_code == 200
            data = response.json()
            assert data["inbound"]["total"] == 3
            assert data["inbound"]["pending"] == 1
            assert data["outbound"]["total"] == 3
            assert data["outbound"]["pending"] == 2
        finally:
            app.dependency_overrides.pop(auth_dep, None)

    def test_release_blocked_outbound_marks_item_released(self):
        from gateway.ingest_api import main as main_module

        app.dependency_overrides[auth_dep] = lambda: None
        try:
            main_module.app_state.blocked_outbound_quarantine = [
                {
                    "message_id": "msg-1",
                    "chat_id": "123",
                    "text": "blocked text",
                    "status": "pending",
                }
            ]
            main_module.app_state.event_bus = None

            client = TestClient(app)
            response = client.post("/manage/quarantine/blocked-outbound/msg-1/release")
            assert response.status_code == 200
            payload = response.json()
            assert payload["ok"] is True
            assert payload["item"]["status"] == "released"
            assert payload["item"]["released_by"] == "admin"
        finally:
            app.dependency_overrides.pop(auth_dep, None)

    def test_discard_blocked_message_not_found_returns_error(self):
        from gateway.ingest_api import main as main_module

        app.dependency_overrides[auth_dep] = lambda: None
        try:
            main_module.app_state.blocked_message_quarantine = []
            main_module.app_state.event_bus = None

            client = TestClient(app)
            response = client.post("/manage/quarantine/blocked-messages/missing/discard")
            assert response.status_code == 200
            payload = response.json()
            assert payload["ok"] is False
            assert payload["error"] == "message_not_found"
        finally:
            app.dependency_overrides.pop(auth_dep, None)


# ---------------------------------------------------------------------------
# CVE-2026-6829: hermes-dashboard path traversal guard
# ---------------------------------------------------------------------------


class TestHermesDashboardPathTraversal:
    """hermes_dashboard_proxy must reject traversal sequences before forwarding."""

    def test_dotdot_path_rejected(self):
        from gateway.ingest_api.main import _TRAVERSAL_RE

        assert _TRAVERSAL_RE.search("../../etc/passwd")

    def test_encoded_traversal_rejected(self):
        from gateway.ingest_api.main import _TRAVERSAL_RE

        assert _TRAVERSAL_RE.search("%2e%2e%2fetc%2fpasswd")

    def test_mixed_case_encoded_rejected(self):
        from gateway.ingest_api.main import _TRAVERSAL_RE

        assert _TRAVERSAL_RE.search("%2E%2E/etc/passwd")

    def test_backslash_encoded_rejected(self):
        from gateway.ingest_api.main import _TRAVERSAL_RE

        assert _TRAVERSAL_RE.search("..%5cetc%5cpasswd")

    def test_safe_path_passes(self):
        from gateway.ingest_api.main import _TRAVERSAL_RE

        assert not _TRAVERSAL_RE.search("api/workspace/files/index.html")
        assert not _TRAVERSAL_RE.search("api/conversations/list")

    @pytest.mark.asyncio
    async def test_proxy_returns_400_on_traversal(self):
        """hermes_dashboard_proxy raises HTTPException(400) for traversal in path."""
        from unittest.mock import MagicMock

        from gateway.ingest_api.main import hermes_dashboard_proxy

        mock_request = MagicMock()
        mock_request.url.query = ""

        with pytest.raises(HTTPException) as exc_info:
            await hermes_dashboard_proxy(path="../../etc/passwd", request=mock_request)

        assert exc_info.value.status_code == 400
        assert "traversal" in exc_info.value.detail.lower()

    @pytest.mark.asyncio
    async def test_proxy_returns_400_on_traversal_in_query(self):
        """hermes_dashboard_proxy raises HTTPException(400) for traversal in query string."""
        from unittest.mock import MagicMock

        from gateway.ingest_api.main import hermes_dashboard_proxy

        mock_request = MagicMock()
        mock_request.url.query = "path=../../etc/passwd"

        with pytest.raises(HTTPException) as exc_info:
            await hermes_dashboard_proxy(path="api/workspace", request=mock_request)

        assert exc_info.value.status_code == 400


class TestHermesDashboardWsProxy:
    """hermes_dashboard_ws_proxy: WebSocket counterpart of hermes_dashboard_proxy.

    Without this route, a WS-scope connection to /hermes-dashboard/{path} has
    nothing to match it (the HTTP-only @app.api_route above only handles
    http-scope requests), so a client like Hermes Conduit can log in over
    plain HTTP but silently fail to open its post-login WebSocket at
    /hermes-dashboard/api/ws.
    """

    def _mock_websocket(self, query: str = "", frames: list | None = None):
        ws = MagicMock()
        ws.url.query = query
        ws.headers = {}
        ws.accept = AsyncMock()
        ws.close = AsyncMock()
        ws.send_text = AsyncMock()
        ws.send_bytes = AsyncMock()
        # receive() yields each queued client->upstream frame, then a
        # disconnect message so _client_to_upstream's loop exits cleanly.
        incoming = list(frames or [])
        incoming.append({"type": "websocket.disconnect"})
        ws.receive = AsyncMock(side_effect=incoming)
        return ws

    @pytest.mark.asyncio
    async def test_traversal_in_path_closes_without_connecting(self):
        from gateway.ingest_api.main import hermes_dashboard_ws_proxy

        ws = self._mock_websocket()
        with patch("websockets.connect") as mock_connect:
            await hermes_dashboard_ws_proxy(ws, path="../../etc/passwd")

        ws.close.assert_awaited_once_with(code=1008)
        ws.accept.assert_not_called()
        mock_connect.assert_not_called()

    @pytest.mark.asyncio
    async def test_traversal_in_query_closes_without_connecting(self):
        from gateway.ingest_api.main import hermes_dashboard_ws_proxy

        ws = self._mock_websocket(query="ticket=../../etc/passwd")
        with patch("websockets.connect") as mock_connect:
            await hermes_dashboard_ws_proxy(ws, path="api/ws")

        ws.close.assert_awaited_once_with(code=1008)
        mock_connect.assert_not_called()

    @pytest.mark.asyncio
    async def test_connects_to_bridge_port_with_ws_scheme_and_query(self):
        """Upstream URL must be ws:// (not http://) at the bridge port, with
        the client's query string (carrying the ws-ticket) preserved."""
        from gateway.ingest_api.main import hermes_dashboard_ws_proxy

        ws = self._mock_websocket(query="ticket=abc123")

        mock_upstream = MagicMock()

        async def _empty_aiter(self):
            return
            yield  # pragma: no cover - makes this an async generator

        mock_upstream.__aiter__ = _empty_aiter
        mock_cm = AsyncMock()
        mock_cm.__aenter__.return_value = mock_upstream
        mock_cm.__aexit__.return_value = False

        with patch("websockets.connect", return_value=mock_cm) as mock_connect:
            await hermes_dashboard_ws_proxy(ws, path="api/ws")

        ws.accept.assert_awaited_once()
        called_url = mock_connect.call_args.args[0]
        assert called_url.startswith("ws://")
        assert "ticket=abc123" in called_url
        assert called_url.endswith("api/ws?ticket=abc123")

    @pytest.mark.asyncio
    async def test_relays_text_and_bytes_both_directions(self):
        from gateway.ingest_api.main import hermes_dashboard_ws_proxy

        ws = self._mock_websocket(frames=[{"type": "websocket.receive", "text": "hello-upstream"}])

        mock_upstream = MagicMock()
        mock_upstream.send = AsyncMock()

        async def _one_frame_aiter(self):
            yield "hello-client"
            yield b"\x00\x01binary"

        mock_upstream.__aiter__ = _one_frame_aiter
        mock_cm = AsyncMock()
        mock_cm.__aenter__.return_value = mock_upstream
        mock_cm.__aexit__.return_value = False

        with patch("websockets.connect", return_value=mock_cm):
            await hermes_dashboard_ws_proxy(ws, path="api/ws")

        assert any(c.args == ("hello-client",) for c in ws.send_text.await_args_list)
        assert any(c.args == (b"\x00\x01binary",) for c in ws.send_bytes.await_args_list)
        assert any(c.args == ("hello-upstream",) for c in mock_upstream.send.await_args_list)
        ws.close.assert_awaited()

    @pytest.mark.asyncio
    async def test_upstream_connect_failure_closes_gracefully(self):
        """A dead/unreachable bridge must not raise out of the route --
        it closes the client WS instead of crashing the gateway worker."""
        from gateway.ingest_api.main import hermes_dashboard_ws_proxy

        ws = self._mock_websocket()

        with patch("websockets.connect", side_effect=ConnectionRefusedError("down")):
            await hermes_dashboard_ws_proxy(ws, path="api/ws")

        ws.accept.assert_awaited_once()
        ws.close.assert_awaited()


# ---------------------------------------------------------------------------
# Scan parameter allowlist + /api/alerts localhost enforcement (quality-sweep)
# ---------------------------------------------------------------------------


class TestScanParameterAllowlists:
    """Allowlist validation on ClamAV target, Trivy scan type, OpenSCAP profile."""

    def setup_method(self):
        app.dependency_overrides[auth_dep] = lambda: None
        self.client = TestClient(app)

    def teardown_method(self):
        app.dependency_overrides.pop(auth_dep, None)

    # ClamAV target allowlist
    def test_clamav_invalid_target_returns_400(self):
        from gateway.ingest_api.main import app_state as _state

        _state.clamav_scanner = object()
        resp = self.client.post("/manage/scan/clamav?target=/etc/secrets")
        assert resp.status_code == 400
        assert "target must be one of" in resp.json()["detail"]

    def test_clamav_default_target_passes_allowlist(self):
        from gateway.ingest_api.main import app_state as _state

        _state.clamav_scanner = None
        resp = self.client.post("/manage/scan/clamav")
        assert resp.status_code == 200
        assert resp.json().get("error") == "ClamAV scanner not available"

    # Trivy scan-type allowlist
    def test_trivy_invalid_scan_type_returns_400(self):
        from gateway.ingest_api.main import app_state as _state

        _state.trivy_scanner = object()
        resp = self.client.post("/manage/scan/trivy?target=malicious")
        assert resp.status_code == 400
        assert "target must be one of" in resp.json()["detail"]

    def test_trivy_default_scan_type_passes_allowlist(self):
        from gateway.ingest_api.main import app_state as _state

        _state.trivy_scanner = None
        resp = self.client.post("/manage/scan/trivy")
        assert resp.status_code == 200
        assert resp.json().get("error") == "Trivy scanner not available"

    # OpenSCAP profile regex
    def test_openscap_invalid_profile_returns_400(self):
        resp = self.client.post("/manage/scan/openscap?profile=bad!profile")
        assert resp.status_code == 400
        assert "disallowed characters" in resp.json()["detail"]

    def test_openscap_semicolon_profile_returns_400(self):
        resp = self.client.post("/manage/scan/openscap?profile=xccdf;rm+-rf+/")
        assert resp.status_code == 400

    def test_openscap_default_profile_passes_regex(self):
        from gateway.ingest_api.main import _OPENSCAP_PROFILE_RE

        assert _OPENSCAP_PROFILE_RE.match("xccdf_org.ssgproject.content_profile_standard")


class TestAlertsLocalhostEnforcement:
    """/api/alerts must reject non-localhost callers (S1 fix)."""

    def test_alerts_rejected_from_non_localhost(self):
        client = TestClient(app)
        resp = client.post(
            "/api/alerts",
            json={"type": "security_alert", "severity": "INFO", "tool": "test"},
        )
        assert resp.status_code == 403

    @pytest.mark.asyncio
    async def test_alerts_accepted_from_localhost(self):
        """Handler returns ok=True when called from 127.0.0.1."""
        from unittest.mock import AsyncMock, MagicMock

        from gateway.ingest_api.main import receive_security_alert

        mock_request = MagicMock()
        mock_request.client.host = "127.0.0.1"
        mock_request.json = AsyncMock(
            return_value={
                "type": "security_alert",
                "severity": "INFO",
                "tool": "test",
                "message": "ok",
            }
        )

        from gateway.ingest_api.main import app_state as _state

        _state.event_bus = None

        result = await receive_security_alert(mock_request)
        assert result["ok"] is True


class TestHealthCheckDetailBotsInventory:
    """health_check_detail's per-bot inventory must key the Docker lookup by
    each bot's real resolved_container_name — not a hardcoded
    'agentshroud-{bot_id}' guess that always misses the moment a bot's
    container is renamed (hermes -> agentshroud-hermes-v2, 2026-07-18),
    silently reporting a healthy bot as "not found"."""

    @pytest.mark.asyncio
    async def test_bots_inventory_matches_the_real_container_name(self, monkeypatch):
        from types import SimpleNamespace

        from gateway.ingest_api.routes import health

        hermes_container = SimpleNamespace(
            name="agentshroud-hermes-v2",
            status="Up 2 hours (healthy)",
            image="agentshroud/hermes:latest",
        )
        fake_engine = MagicMock()
        fake_engine.ps.return_value = [hermes_container]

        fake_bot = SimpleNamespace(resolved_container_name="agentshroud-hermes-v2")
        fake_state = SimpleNamespace(
            start_time=time.time(),
            ledger=SimpleNamespace(get_stats=AsyncMock(return_value={"total": 0})),
            approval_queue=SimpleNamespace(get_pending=AsyncMock(return_value=[])),
            config=SimpleNamespace(bots={"hermes": fake_bot}, pii=SimpleNamespace(engine="regex")),
            sanitizer=SimpleNamespace(get_mode=lambda: "presidio"),
        )
        monkeypatch.setattr(health, "app_state", fake_state)
        monkeypatch.setattr("gateway.runtime.get_engine", lambda: fake_engine)

        result = await health.health_check_detail(auth=None)

        assert result.bots["hermes"]["container"] == "agentshroud-hermes-v2"
        assert result.bots["hermes"]["healthy"] is True
        assert result.bots["hermes"]["status"] == "Up 2 hours (healthy)"
