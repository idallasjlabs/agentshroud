"""Tests for Dashboard endpoints and WebSocket activity feed"""

import asyncio
import json
import time
import pytest
import pytest_asyncio
from unittest.mock import patch, AsyncMock
from httpx import AsyncClient, ASGITransport

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
    from starlette.testclient import TestClient
    with patch('gateway.ingest_api.main.load_config', return_value=test_config):
        with TestClient(app) as c:
            yield c


@pytest.mark.asyncio
async def test_dashboard_serves_html(client):
    """GET /dashboard with valid cookie serves HTML"""
    resp = await client.get(
        "/dashboard",
        cookies={"dashboard_token": "test-token-12345"},
    )
    assert resp.status_code == 200
    assert "text/html" in resp.headers["content-type"]
    assert "SecureClaw" in resp.text


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
    """WebSocket /ws/activity connects and authenticates via query param"""
    with sync_client.websocket_connect("/ws/activity?token=test-token-12345") as ws:
        msg = ws.receive_json()
        assert msg["type"] == "authenticated"


def test_ws_activity_receives_events(sync_client):
    """WebSocket /ws/activity receives emitted events"""
    with sync_client.websocket_connect("/ws/activity?token=test-token-12345") as ws:
        auth_msg = ws.receive_json()
        assert auth_msg["type"] == "authenticated"

        # Emit an event through the bus
        loop = asyncio.new_event_loop()
        event = make_event("forward", "Test forward event", {"source": "api"})
        loop.run_until_complete(app_state.event_bus.emit(event))
        loop.close()

        msg = ws.receive_json()
        assert msg["type"] == "forward"
        assert msg["summary"] == "Test forward event"


def test_ws_activity_requires_auth(sync_client):
    """WebSocket /ws/activity rejects bad auth during handshake"""
    from starlette.websockets import WebSocketDisconnect
    with pytest.raises(Exception):
        with sync_client.websocket_connect("/ws/activity?token=wrong-token") as ws:
            ws.receive_json()


@pytest.mark.asyncio
async def test_dashboard_has_csp_header(client):
    """GET /dashboard includes Content-Security-Policy header"""
    resp = await client.get(
        "/dashboard",
        cookies={"dashboard_token": "test-token-12345"},
    )
    assert resp.status_code == 200
    csp = resp.headers.get("content-security-policy", "")
    assert "default-src" in csp
    assert "script-src" in csp


@pytest.mark.asyncio
async def test_dashboard_xss_prevention(client):
    """Dashboard HTML uses data attributes instead of onclick for approvals"""
    resp = await client.get(
        "/dashboard",
        cookies={"dashboard_token": "test-token-12345"},
    )
    assert "onclick" not in resp.text
    assert "data-action" in resp.text or "data-id" in resp.text or "addEventListener" in resp.text
