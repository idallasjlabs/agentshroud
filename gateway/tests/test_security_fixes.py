"""Tests for v0.2.0 peer review security fixes

Covers:
- CRITICAL-1: SSH StrictHostKeyChecking=yes
- CRITICAL-2: WebSocket auth during handshake (not first message)
- CRITICAL-3: Dashboard cookie-based auth with redirect
- CRITICAL-4: PII sanitization in approval queue details
"""

import asyncio
import pytest
import pytest_asyncio
from unittest.mock import patch, AsyncMock, MagicMock
from httpx import AsyncClient, ASGITransport
from starlette.testclient import TestClient

from gateway.ingest_api.main import app, app_state, lifespan
from gateway.ingest_api.event_bus import EventBus, make_event


@pytest_asyncio.fixture
async def client(test_config):
    with patch('gateway.ingest_api.main.load_config', return_value=test_config):
        async with lifespan(app):
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as ac:
                yield ac


@pytest.fixture
def sync_client(test_config):
    """Sync TestClient for WebSocket tests"""
    with patch('gateway.ingest_api.main.load_config', return_value=test_config):
        with TestClient(app) as c:
            yield c


# === CRITICAL-1: SSH StrictHostKeyChecking ===

class TestSSHStrictHostKeyChecking:
    """Verify SSH proxy uses StrictHostKeyChecking=yes, not accept-new"""

    def test_strict_host_key_checking_in_source(self):
        """Source code uses StrictHostKeyChecking=yes"""
        from gateway.ssh_proxy.proxy import SSHProxy
        import inspect
        source = inspect.getsource(SSHProxy.execute)
        assert "StrictHostKeyChecking=yes" in source
        assert "accept-new" not in source

    @pytest.mark.asyncio
    async def test_ssh_command_uses_strict_checking(self):
        """SSH execute builds command with StrictHostKeyChecking=yes"""
        from gateway.ssh_proxy.proxy import SSHProxy
        from gateway.ingest_api.ssh_config import SSHConfig, SSHHostConfig

        config = SSHConfig(
            enabled=True,
            require_approval=False,
            hosts={"testhost": SSHHostConfig(
                host="127.0.0.1", port=22, username="test",
                allowed_commands=["echo hello"],
                denied_commands=[], auto_approve_commands=["echo hello"],
                max_session_seconds=10,
            )},
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

        with patch('asyncio.create_subprocess_exec', side_effect=mock_create_subprocess):
            await proxy.execute("testhost", "echo hello")

        # Verify StrictHostKeyChecking=yes is in the command
        assert "StrictHostKeyChecking=yes" in captured_args
        assert "StrictHostKeyChecking=accept-new" not in str(captured_args)


# === CRITICAL-2: WebSocket auth during handshake ===

class TestWebSocketHandshakeAuth:
    """WebSocket endpoints must validate token during handshake, not first message"""

    def test_ws_approvals_rejects_no_token(self, sync_client):
        """WS /ws/approvals closes immediately without token"""
        from starlette.websockets import WebSocketDisconnect
        with pytest.raises(Exception):
            with sync_client.websocket_connect("/ws/approvals") as ws:
                ws.receive_json()  # Should not get here

    def test_ws_approvals_rejects_bad_token(self, sync_client):
        """WS /ws/approvals closes with bad token"""
        from starlette.websockets import WebSocketDisconnect
        with pytest.raises(Exception):
            with sync_client.websocket_connect("/ws/approvals?token=wrong") as ws:
                ws.receive_json()

    def test_ws_approvals_accepts_valid_token(self, sync_client):
        """WS /ws/approvals accepts valid token in query param"""
        with sync_client.websocket_connect("/ws/approvals?token=test-token-12345") as ws:
            msg = ws.receive_json()
            assert msg["type"] == "authenticated"

    def test_ws_activity_rejects_no_token(self, sync_client):
        """WS /ws/activity closes immediately without token"""
        from starlette.websockets import WebSocketDisconnect
        with pytest.raises(Exception):
            with sync_client.websocket_connect("/ws/activity") as ws:
                ws.receive_json()

    def test_ws_activity_rejects_bad_token(self, sync_client):
        """WS /ws/activity closes with bad token"""
        from starlette.websockets import WebSocketDisconnect
        with pytest.raises(Exception):
            with sync_client.websocket_connect("/ws/activity?token=wrong") as ws:
                ws.receive_json()

    def test_ws_activity_accepts_valid_token(self, sync_client):
        """WS /ws/activity accepts valid token in query param"""
        with sync_client.websocket_connect("/ws/activity?token=test-token-12345") as ws:
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
        resp = await client.get(
            "/dashboard",
            cookies={"dashboard_token": "test-token-12345"},
        )
        assert resp.status_code == 200
        assert "SecureClaw" in resp.text

    @pytest.mark.asyncio
    async def test_dashboard_bad_cookie_returns_403(self, client):
        """GET /dashboard with invalid cookie returns 403"""
        resp = await client.get(
            "/dashboard",
            cookies={"dashboard_token": "wrong-token"},
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
        from gateway.ssh_proxy.proxy import SSHProxy
        from gateway.ingest_api.ssh_config import SSHConfig, SSHHostConfig

        config = SSHConfig(
            enabled=True,
            require_approval=True,
            hosts={"testhost": SSHHostConfig(
                host="127.0.0.1", port=22, username="test",
                allowed_commands=["grep"],
                denied_commands=[], auto_approve_commands=[],
                max_session_seconds=30,
            )},
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
        assert "<EMAIL_ADDRESS>" in latest.description or "<EMAIL_ADDRESS>" in str(latest.details.get("command", ""))
