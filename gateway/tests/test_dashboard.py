# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for Dashboard endpoints and WebSocket activity feed"""
from __future__ import annotations


import asyncio
import pytest
import pytest_asyncio
from unittest.mock import patch
from httpx import AsyncClient, ASGITransport

from gateway.ingest_api.main import app, app_state, lifespan
from gateway.ingest_api.event_bus import make_event
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
    from starlette.testclient import TestClient

    with patch("gateway.ingest_api.lifespan.load_config", return_value=test_config):
        with TestClient(app) as c:
            yield c


@pytest.mark.asyncio
async def test_dashboard_serves_html(client):
    """GET /dashboard with valid cookie serves HTML"""
    client.cookies = {"dashboard_token": "test-token-12345"}
    resp = await client.get(
        "/dashboard",
    )
    assert resp.status_code == 200
    assert "text/html" in resp.headers["content-type"]
    assert "AgentShroud" in resp.text


@pytest.mark.asyncio
async def test_dashboard_requires_auth(client):
    """GET /dashboard without auth returns 403"""
    resp = await client.get("/dashboard")
    assert resp.status_code == 403


@pytest.mark.asyncio
async def test_dashboard_stats_endpoint(client):
    """GET /dashboard/stats returns JSON stats"""
    resp = await client.get(
        "/dashboard/stats",
        headers={"Authorization": "Bearer test-token-12345"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "total_events" in data
    assert "ledger_entries" in data
    assert "pending_approvals" in data


@pytest.mark.asyncio
async def test_dashboard_stats_requires_auth(client):
    """GET /dashboard/stats without auth returns 401"""
    resp = await client.get("/dashboard/stats")
    assert resp.status_code == 401


def test_ws_activity_connects(sync_client):
    """WebSocket /ws/activity connects and authenticates via scoped WS token"""
    ws_token = _create_ws_token()
    with sync_client.websocket_connect(f"/ws/activity?token={ws_token}") as ws:
        msg = ws.receive_json()
        assert msg["type"] == "authenticated"
        snap = ws.receive_json()
        assert snap["type"] == "egress_snapshot"


def test_ws_activity_receives_events(sync_client):
    """WebSocket /ws/activity receives emitted events"""
    ws_token = _create_ws_token()
    with sync_client.websocket_connect(f"/ws/activity?token={ws_token}") as ws:
        auth_msg = ws.receive_json()
        assert auth_msg["type"] == "authenticated"
        snap = ws.receive_json()
        assert snap["type"] == "egress_snapshot"

        # Emit an event through the bus
        loop = asyncio.new_event_loop()
        event = make_event("forward", "Test forward event", {"source": "api"})
        loop.run_until_complete(app_state.event_bus.emit(event))
        loop.close()

        msg = ws.receive_json()
        assert msg["type"] == "forward"
        assert msg["summary"] == "Test forward event"


def test_ws_egress_connects_and_snapshot(sync_client):
    """WebSocket /ws/egress connects and emits egress snapshot."""
    ws_token = _create_ws_token()
    with sync_client.websocket_connect(f"/ws/egress?token={ws_token}") as ws:
        msg = ws.receive_json()
        assert msg["type"] == "authenticated"
        snap = ws.receive_json()
        assert snap["type"] == "egress_snapshot"
        assert "details" in snap
        assert "egress_recent_log" in snap["details"]
        assert "quarantined_blocked_outbound" in snap["details"]
        assert "quarantine_summary" in snap["details"]
        assert "scanner_recent_events" in snap["details"]
        assert "recent_security_events" in snap["details"]
        assert "soc_risk" in snap["details"]
        assert "soc_summary" in snap["details"]
        assert "privacy_policy_summary" in snap["details"]


def test_ws_egress_receives_scanner_event(sync_client):
    """WebSocket /ws/egress should forward scanner_result events."""
    ws_token = _create_ws_token()
    with sync_client.websocket_connect(f"/ws/egress?token={ws_token}") as ws:
        _ = ws.receive_json()  # authenticated
        _ = ws.receive_json()  # snapshot

        loop = asyncio.new_event_loop()
        event = make_event("scanner_result", "scan done", {"scanner": "trivy"})
        loop.run_until_complete(app_state.event_bus.emit(event))
        loop.close()

        msg = ws.receive_json()
        assert msg["type"] == "scanner_result"


def test_ws_egress_receives_privacy_event(sync_client):
    """WebSocket /ws/egress should forward privacy_* events."""
    ws_token = _create_ws_token()
    with sync_client.websocket_connect(f"/ws/egress?token={ws_token}") as ws:
        _ = ws.receive_json()  # authenticated
        _ = ws.receive_json()  # snapshot

        loop = asyncio.new_event_loop()
        event = make_event("privacy_policy_violation", "blocked private tool", {"tool": "gmail_send"})
        loop.run_until_complete(app_state.event_bus.emit(event))
        loop.close()

        msg = ws.receive_json()
        assert msg["type"] == "privacy_policy_violation"


def test_ws_egress_receives_auth_event(sync_client):
    """WebSocket /ws/egress should forward auth_* events for SOC visibility."""
    ws_token = _create_ws_token()
    with sync_client.websocket_connect(f"/ws/egress?token={ws_token}") as ws:
        _ = ws.receive_json()  # authenticated
        _ = ws.receive_json()  # snapshot

        loop = asyncio.new_event_loop()
        event = make_event("auth_failed", "bad token attempt", {"path": "/ws/egress"}, "warning")
        loop.run_until_complete(app_state.event_bus.emit(event))
        loop.close()

        msg = ws.receive_json()
        assert msg["type"] == "auth_failed"


def test_ws_activity_requires_auth(sync_client):
    """WebSocket /ws/activity rejects bad auth during handshake"""
    with pytest.raises(Exception):
        with sync_client.websocket_connect("/ws/activity?token=wrong-token") as ws:
            ws.receive_json()


@pytest.mark.asyncio
async def test_dashboard_has_csp_header(client):
    """GET /dashboard includes Content-Security-Policy header"""
    client.cookies = {"dashboard_token": "test-token-12345"}
    resp = await client.get(
        "/dashboard",
    )
    assert resp.status_code == 200
    csp = resp.headers.get("content-security-policy", "")
    assert "default-src" in csp
    assert "script-src" in csp


@pytest.mark.asyncio
async def test_dashboard_xss_prevention(client):
    """Dashboard HTML uses data attributes instead of onclick for approvals"""
    client.cookies = {"dashboard_token": "test-token-12345"}
    resp = await client.get(
        "/dashboard",
    )
    assert "onclick" not in resp.text
    assert (
        "data-action" in resp.text
        or "data-id" in resp.text
        or "addEventListener" in resp.text
    )
