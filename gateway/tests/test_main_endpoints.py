# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Main Endpoints Integration Tests - P1 Middleware Wiring
Tests for main.py endpoint integration with middleware blocking.
"""

from __future__ import annotations

import ipaddress
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from gateway.ingest_api.main import app, auth_dep
from gateway.ingest_api.middleware import MiddlewareResult
from gateway.ingest_api.models import ForwardRequest


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
        mock_auth = MagicMock()

        with (
            patch("gateway.ingest_api.routes.forward.app_state") as mock_app_state,
            patch("gateway.ingest_api.routes.forward.create_auth_dependency") as mock_auth_dep,
        ):
            mock_app_state.middleware_manager = mock_middleware

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

        mock_auth = MagicMock()

        with (
            patch("gateway.ingest_api.routes.forward.app_state") as mock_app_state,
            patch("gateway.ingest_api.routes.forward.create_auth_dependency") as mock_auth_dep,
        ):
            mock_app_state.middleware_manager = mock_middleware

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
