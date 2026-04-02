# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for v0.2.0 peer review security fixes

Covers:
- CRITICAL-1: SSH StrictHostKeyChecking=yes
- CRITICAL-2: WebSocket auth during handshake (not first message)
- CRITICAL-3: Dashboard cookie-based auth with redirect
- CRITICAL-4: PII sanitization in approval queue details
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from starlette.testclient import TestClient
from starlette.websockets import WebSocketDisconnect

from gateway.ingest_api.main import app, app_state, lifespan
from gateway.ingest_api.routes.dashboard import _create_ws_token


@pytest_asyncio.fixture
async def client(test_config):
    with patch("gateway.ingest_api.lifespan.load_config", return_value=test_config):
        async with lifespan(app):
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as ac:
                yield ac


@pytest.fixture
def sync_client(test_config):
    """Sync TestClient for WebSocket tests"""
    with patch("gateway.ingest_api.lifespan.load_config", return_value=test_config):
        with TestClient(app) as c:
            yield c


# === CRITICAL-1: SSH StrictHostKeyChecking ===


class TestSSHStrictHostKeyChecking:
    """Verify SSH proxy uses StrictHostKeyChecking=yes, not accept-new"""

    def test_strict_host_key_checking_in_source(self):
        """Source code uses StrictHostKeyChecking=yes"""
        import inspect

        from gateway.ssh_proxy.proxy import SSHProxy

        source = inspect.getsource(SSHProxy.execute)
        assert "StrictHostKeyChecking=yes" in source
        assert "accept-new" not in source

    @pytest.mark.asyncio
    async def test_ssh_command_uses_strict_checking(self):
        """SSH execute builds command with StrictHostKeyChecking=yes"""
        from gateway.ingest_api.ssh_config import SSHConfig, SSHHostConfig
        from gateway.ssh_proxy.proxy import SSHProxy

        config = SSHConfig(
            enabled=True,
            require_approval=False,
            hosts={
                "testhost": SSHHostConfig(
                    host="127.0.0.1",
                    port=22,
                    username="test",
                    allowed_commands=["echo hello"],
                    denied_commands=[],
                    auto_approve_commands=["echo hello"],
                    max_session_seconds=10,
                )
            },
        )
        proxy = SSHProxy(config)

        # Mock subprocess to capture the args
        captured_args = []

        async def mock_create_subprocess(*args, **kwargs):
            captured_args.extend(args)
            proc = AsyncMock()
            proc.communicate = AsyncMock(return_value=(b"ok", b""))
            proc.returncode = 0
            return proc

        with patch("asyncio.create_subprocess_exec", side_effect=mock_create_subprocess):
            await proxy.execute("testhost", "echo hello")

        # Verify StrictHostKeyChecking=yes is in the command
        assert "StrictHostKeyChecking=yes" in captured_args
        assert "StrictHostKeyChecking=accept-new" not in str(captured_args)


# === CRITICAL-2: WebSocket auth during handshake ===


class TestWebSocketHandshakeAuth:
    """WebSocket endpoints must validate token during handshake, not first message"""

    def test_ws_approvals_rejects_no_token(self, sync_client):
        """WS /ws/approvals closes immediately without token"""
        with pytest.raises((WebSocketDisconnect, Exception)):
            with sync_client.websocket_connect("/ws/approvals") as ws:
                ws.receive_json()  # Should not get here

    def test_ws_approvals_rejects_bad_token(self, sync_client):
        """WS /ws/approvals closes with bad token"""
        with pytest.raises((WebSocketDisconnect, Exception)):
            with sync_client.websocket_connect("/ws/approvals?token=wrong") as ws:
                ws.receive_json()

    def test_ws_approvals_accepts_valid_token(self, sync_client):
        """WS /ws/approvals accepts valid token in query param"""
        with sync_client.websocket_connect("/ws/approvals?token=test-token-12345") as ws:
            msg = ws.receive_json()
            assert msg["type"] == "authenticated"

    def test_ws_activity_rejects_no_token(self, sync_client):
        """WS /ws/activity closes immediately without token"""
        with pytest.raises((WebSocketDisconnect, Exception)):
            with sync_client.websocket_connect("/ws/activity") as ws:
                ws.receive_json()

    def test_ws_activity_rejects_bad_token(self, sync_client):
        """WS /ws/activity closes with bad token"""
        with pytest.raises((WebSocketDisconnect, Exception)):
            with sync_client.websocket_connect("/ws/activity?token=wrong") as ws:
                ws.receive_json()

    def test_ws_activity_accepts_valid_token(self, sync_client):
        """WS /ws/activity accepts valid scoped WS token"""
        ws_token = _create_ws_token()
        with sync_client.websocket_connect(f"/ws/activity?token={ws_token}") as ws:
            msg = ws.receive_json()
            assert msg["type"] == "authenticated"


# === CRITICAL-3: Dashboard cookie-based auth ===


class TestDashboardCookieAuth:
    """Dashboard should set httpOnly cookie and redirect to clean URL"""

    @pytest.mark.asyncio
    async def test_dashboard_token_sets_cookie_and_redirects(self, client):
        """GET /dashboard?token=valid sets cookie and redirects to /dashboard"""
        resp = await client.get(
            "/dashboard?token=test-token-12345",
            follow_redirects=False,
        )
        assert resp.status_code == 302
        assert resp.headers["location"] == "/dashboard"
        # Check cookie is set
        set_cookie = resp.headers.get("set-cookie", "")
        assert "dashboard_token" in set_cookie
        assert "httponly" in set_cookie.lower()
        assert "samesite=strict" in set_cookie.lower()

    @pytest.mark.asyncio
    async def test_dashboard_cookie_auth_serves_html(self, client):
        """GET /dashboard with valid cookie serves HTML"""
        client.cookies = {"dashboard_token": "test-token-12345"}
        resp = await client.get(
            "/dashboard",
        )
        assert resp.status_code == 200
        assert "AgentShroud" in resp.text

    @pytest.mark.asyncio
    async def test_dashboard_bad_cookie_returns_403(self, client):
        """GET /dashboard with invalid cookie returns 403"""
        client.cookies = {"dashboard_token": "wrong-token"}
        resp = await client.get(
            "/dashboard",
        )
        assert resp.status_code == 403

    @pytest.mark.asyncio
    async def test_dashboard_no_auth_returns_403(self, client):
        """GET /dashboard with no auth returns 403"""
        resp = await client.get("/dashboard")
        assert resp.status_code == 403

    @pytest.mark.asyncio
    async def test_dashboard_bad_token_returns_403(self, client):
        """GET /dashboard?token=wrong returns 403"""
        resp = await client.get("/dashboard?token=wrong")
        assert resp.status_code == 403


# === CRITICAL-4: PII sanitization in approval queue ===


class TestApprovalQueuePIISanitization:
    """Approval queue details must be PII-sanitized before storage"""

    @pytest.mark.asyncio
    async def test_ssh_approval_sanitizes_command_pii(self, client):
        """SSH exec requiring approval sanitizes PII in command before storing"""
        # Configure SSH proxy to require approval
        from gateway.ingest_api.ssh_config import SSHConfig, SSHHostConfig
        from gateway.ssh_proxy.proxy import SSHProxy

        config = SSHConfig(
            enabled=True,
            require_approval=True,
            hosts={
                "testhost": SSHHostConfig(
                    host="127.0.0.1",
                    port=22,
                    username="test",
                    allowed_commands=["grep"],
                    denied_commands=[],
                    auto_approve_commands=[],
                    max_session_seconds=30,
                )
            },
        )
        app_state.ssh_proxy = SSHProxy(config)

        # Send a command containing PII (email address)
        resp = await client.post(
            "/ssh/exec",
            json={
                "host": "testhost",
                "command": "grep user@example.com",
                "reason": "Looking for user@example.com records",
            },
            headers={"Authorization": "Bearer test-token-12345"},
        )

        assert resp.status_code == 202
        data = resp.json()
        assert data["status"] == "pending_approval"

        # Verify the stored approval request has sanitized details
        pending = await app_state.approval_queue.get_pending()
        assert len(pending) >= 1
        latest = pending[-1]

        # The email should be redacted in description and details
        assert "user@example.com" not in latest.description
        assert "user@example.com" not in str(latest.details.get("command", ""))
        assert "<EMAIL_ADDRESS>" in latest.description or "<EMAIL_ADDRESS>" in str(
            latest.details.get("command", "")
        )


class TestDashboardWSToken:
    """Dashboard ws-token endpoint returns token only for cookie-authed sessions"""

    @pytest.mark.asyncio
    async def test_ws_token_with_valid_cookie(self, client):
        """GET /dashboard/ws-token with valid cookie returns token"""
        client.cookies = {"dashboard_token": "test-token-12345"}
        resp = await client.get(
            "/dashboard/ws-token",
        )
        assert resp.status_code == 200
        data = resp.json()
        assert "token" in data
        # H5 fix: ws-token now returns a scoped, short-lived WS token
        # instead of the master auth token
        assert data["token"].startswith("ws_")
        assert data["token"] != "test-token-12345"

    @pytest.mark.asyncio
    async def test_ws_token_without_cookie_returns_403(self, client):
        """GET /dashboard/ws-token without cookie returns 403"""
        resp = await client.get("/dashboard/ws-token")
        assert resp.status_code == 403

    @pytest.mark.asyncio
    async def test_ws_token_with_bad_cookie_returns_403(self, client):
        """GET /dashboard/ws-token with bad cookie returns 403"""
        client.cookies = {"dashboard_token": "wrong"}
        resp = await client.get(
            "/dashboard/ws-token",
        )
        assert resp.status_code == 403


class TestDashboardSecureCookie:
    """Dashboard cookie secure flag is dynamic based on request scheme"""

    @pytest.mark.asyncio
    async def test_cookie_not_secure_on_http(self, client):
        """Cookie secure=False on HTTP requests"""
        resp = await client.get(
            "/dashboard?token=test-token-12345",
            follow_redirects=False,
        )
        assert resp.status_code == 302
        cookie_header = resp.headers.get("set-cookie", "")
        # On HTTP, secure flag should NOT be present
        assert "; secure" not in cookie_header.lower()


# === R3: Management WS Token Scoping (R3-M2) ===


class TestManagementWSTokenScoping:
    """Management WebSocket endpoints should use scoped tokens, not master auth."""

    def test_ws_activity_rejects_master_token(self, sync_client):
        """WS /ws/activity should reject master auth token (R3-L4)"""
        with pytest.raises((WebSocketDisconnect, Exception)):
            with sync_client.websocket_connect("/ws/activity?token=test-token-12345") as ws:
                ws.receive_json()

    def test_ws_activity_rejects_empty_token(self, sync_client):
        """WS /ws/activity should reject empty token"""
        with pytest.raises((WebSocketDisconnect, Exception)):
            with sync_client.websocket_connect("/ws/activity?token=") as ws:
                ws.receive_json()

    def test_ws_activity_accepts_scoped_token(self, sync_client):
        """WS /ws/activity should accept scoped ws_ token"""
        ws_token = _create_ws_token()
        assert ws_token.startswith("ws_")
        with sync_client.websocket_connect(f"/ws/activity?token={ws_token}") as ws:
            msg = ws.receive_json()
            assert msg["type"] == "authenticated"

    def test_scoped_ws_token_is_single_use(self, sync_client):
        """Scoped WS token should be consumed after first use (single-use)"""
        ws_token = _create_ws_token()
        # First use should succeed
        with sync_client.websocket_connect(f"/ws/activity?token={ws_token}") as ws:
            msg = ws.receive_json()
            assert msg["type"] == "authenticated"
        # Second use of same token should fail
        with pytest.raises((WebSocketDisconnect, Exception)):
            with sync_client.websocket_connect(f"/ws/activity?token={ws_token}") as ws:
                ws.receive_json()


# === R3: Global Security Headers (R3-L1) ===


class TestGlobalSecurityHeaders:
    """All API responses should include basic security headers."""

    @pytest.mark.asyncio
    async def test_status_has_security_headers(self, client):
        """GET /status should include security headers"""
        resp = await client.get("/status")
        assert resp.status_code == 200
        assert resp.headers.get("X-Content-Type-Options") == "nosniff"
        assert resp.headers.get("X-Frame-Options") == "DENY"

    @pytest.mark.asyncio
    async def test_json_api_has_cache_control(self, client):
        """JSON API responses should have Cache-Control: no-store"""
        resp = await client.get("/status")
        assert resp.status_code == 200
        assert "no-store" in resp.headers.get("Cache-Control", "")


# === R3: Version Consistency (R3-M3) ===


class TestVersionConsistency:
    """Version strings should be consistent across the codebase."""

    @pytest.mark.asyncio
    async def test_status_returns_current_version(self, client):
        """GET /status should return current version"""
        resp = await client.get("/status")
        assert resp.status_code == 200
        data = resp.json()
        assert data["version"] == "1.0.0"
