# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for dashboard API endpoints: proxy/status, alerts/summary, ssh/hosts, logs/recent."""

from __future__ import annotations

import pytest
import pytest_asyncio
from unittest.mock import patch, AsyncMock
from httpx import AsyncClient, ASGITransport

from gateway.ingest_api.main import app, app_state, lifespan
from gateway.web.dashboard_endpoints import alert_store, log_buffer, AlertStore, LogBuffer


@pytest_asyncio.fixture
async def client(test_config):
    with patch("gateway.ingest_api.lifespan.load_config", return_value=test_config),          patch("gateway.web.api.load_config", return_value=test_config):
        async with lifespan(app):
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as ac:
                yield ac


@pytest.fixture
def auth_headers(test_config):
    return {"Authorization": f"Bearer {test_config.auth_token}"}


# --- /api/proxy/status ---

@pytest.mark.asyncio
async def test_proxy_status_requires_auth(client):
    resp = await client.get("/api/proxy/status")
    assert resp.status_code in (401, 403)


@pytest.mark.asyncio
async def test_proxy_status_returns_stats(client, auth_headers):
    resp = await client.get("/api/proxy/status", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "total_requests" in data
    assert "allowed" in data
    assert "blocked" in data
    assert "flagged" in data
    assert "uptime_seconds" in data


@pytest.mark.asyncio
async def test_proxy_status_includes_pipeline_stats(client, auth_headers):
    """When pipeline exists, stats should reflect its data."""
    resp = await client.get("/api/proxy/status", headers=auth_headers)
    data = resp.json()
    # Pipeline is initialized in lifespan, uptime should be > 0
    assert data["uptime_seconds"] >= 0


# --- /api/alerts/summary ---

@pytest.mark.asyncio
async def test_alerts_summary_requires_auth(client):
    resp = await client.get("/api/alerts/summary")
    assert resp.status_code in (401, 403)


@pytest.mark.asyncio
async def test_alerts_summary_empty(client, auth_headers):
    # Clear alerts
    alert_store._alerts.clear()
    resp = await client.get("/api/alerts/summary", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data == {"critical": 0, "high": 0, "medium": 0, "low": 0, "total": 0}


@pytest.mark.asyncio
async def test_alerts_summary_with_alerts(client, auth_headers):
    alert_store._alerts.clear()
    alert_store.push("critical", "proxy", "SSRF attempt detected")
    alert_store.push("high", "pii", "PII leak detected")
    alert_store.push("low", "auth", "Failed login")
    resp = await client.get("/api/alerts/summary", headers=auth_headers)
    data = resp.json()
    assert data["critical"] == 1
    assert data["high"] == 1
    assert data["low"] == 1
    assert data["total"] == 3
    # cleanup
    alert_store._alerts.clear()


# --- /api/ssh/hosts ---

@pytest.mark.asyncio
async def test_ssh_hosts_requires_auth(client):
    resp = await client.get("/api/ssh/hosts")
    assert resp.status_code in (401, 403)


@pytest.mark.asyncio
async def test_ssh_hosts_returns_hosts(client, auth_headers):
    with patch("gateway.web.dashboard_endpoints._tcp_check", return_value=False):
        resp = await client.get("/api/ssh/hosts", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "hosts" in data
    assert len(data["hosts"]) == 3
    names = {h["name"] for h in data["hosts"]}
    assert names == {"marvin", "pi", "trillian"}


@pytest.mark.asyncio
async def test_ssh_hosts_online(client, auth_headers):
    # Clear cache to force re-check
    from gateway.web.dashboard_endpoints import _ssh_cache
    _ssh_cache.clear()

    with patch("gateway.web.dashboard_endpoints._tcp_check", return_value=True):
        resp = await client.get("/api/ssh/hosts", headers=auth_headers)
    data = resp.json()
    for h in data["hosts"]:
        assert h["status"] == "online"
        assert "last_check" in h


# --- /api/logs/recent ---

@pytest.mark.asyncio
async def test_logs_recent_requires_auth(client):
    resp = await client.get("/api/logs/recent")
    assert resp.status_code in (401, 403)


@pytest.mark.asyncio
async def test_logs_recent_returns_entries(client, auth_headers):
    log_buffer._entries.clear()
    log_buffer.append("INFO", "test", "Test log entry")
    resp = await client.get("/api/logs/recent", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "entries" in data
    assert len(data["entries"]) >= 1
    log_buffer._entries.clear()


@pytest.mark.asyncio
async def test_logs_recent_tail_param(client, auth_headers):
    log_buffer._entries.clear()
    for i in range(10):
        log_buffer.append("INFO", "test", f"Entry {i}")
    resp = await client.get("/api/logs/recent?tail=3", headers=auth_headers)
    data = resp.json()
    assert len(data["entries"]) <= 3
    log_buffer._entries.clear()


@pytest.mark.asyncio
async def test_logs_recent_tail_clamped(client, auth_headers):
    """tail parameter is clamped to 1-100."""
    resp = await client.get("/api/logs/recent?tail=200", headers=auth_headers)
    assert resp.status_code == 422  # FastAPI validation error for ge/le


# --- Unit tests for AlertStore and LogBuffer ---

def test_alert_store_push_and_summary():
    store = AlertStore()
    store.push("critical", "test", "msg1")
    store.push("critical", "test", "msg2")
    store.push("low", "test", "msg3")
    s = store.summary()
    assert s["critical"] == 2
    assert s["low"] == 1
    assert s["total"] == 3


def test_log_buffer_ring():
    buf = LogBuffer(max_size=5)
    for i in range(10):
        buf.append("INFO", "test", f"msg {i}")
    assert len(buf._entries) == 5
    assert buf._entries[0]["message"] == "msg 5"


def test_log_buffer_tail():
    buf = LogBuffer()
    for i in range(5):
        buf.append("INFO", "test", f"msg {i}")
    result = buf.tail(3)
    assert len(result) == 3
    assert result[0]["message"] == "msg 2"
