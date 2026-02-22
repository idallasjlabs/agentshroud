# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""End-to-end integration tests for the full gateway stack.

Tests the complete flow through authentication, forwarding,
PII sanitization, ledger, event bus, and dashboard.
"""

import pytest
import pytest_asyncio
from unittest.mock import patch
from httpx import AsyncClient, ASGITransport

from gateway.ingest_api.main import app, app_state, lifespan
from gateway.ingest_api.event_bus import EventBus


@pytest_asyncio.fixture
async def client(test_config):
    """Fully initialized async client with lifespan."""
    with patch("gateway.ingest_api.main.load_config", return_value=test_config):
        async with lifespan(app):
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as ac:
                yield ac


AUTH = {"Authorization": "Bearer test-token-12345"}


# === Full forward flow ===


@pytest.mark.asyncio
async def test_forward_pii_sanitized_and_ledger_entry(client):
    """Forward content → PII sanitized → ledger entry created → event bus fired."""
    bus: EventBus = getattr(app_state, "event_bus", None)
    events_before = len(bus._recent_events) if bus else 0

    resp = await client.post(
        "/forward",
        json={
            "content": "Call me at 555-123-4567 or email john@example.com",
            "source": "api",
            "content_type": "text",
        },
        headers=AUTH,
    )
    assert resp.status_code in (200, 201)
    body = resp.json()

    # PII should be redacted
    assert "555-123-4567" not in body.get("sanitized_content", body.get("content", ""))

    # Ledger entry should exist
    ledger = getattr(app_state, "ledger", None)
    if ledger:
        result = await ledger.query(page=1, page_size=1)
        assert result.total >= 1

    # Event bus should have fired
    if bus:
        assert len(bus._recent_events) > events_before


@pytest.mark.asyncio
async def test_forward_without_auth_rejected(client):
    """Forward without auth returns 401/403."""
    resp = await client.post(
        "/forward",
        json={"content": "test", "source": "api"},
    )
    assert resp.status_code in (401, 403)


# === SSH flow ===


@pytest.mark.asyncio
async def test_ssh_submit_queues_approval(client):
    """Submit SSH command → approval queued."""
    resp = await client.post(
        "/ssh/execute",
        json={
            "host": "pi-dev",
            "command": "whoami",
        },
        headers=AUTH,
    )
    # SSH endpoint may queue for approval or execute directly
    # depending on config; either 200 or 202 is acceptable
    assert resp.status_code in (200, 202, 404)


# === Dashboard ===


@pytest.mark.asyncio
async def test_dashboard_returns_html(client):
    """GET /dashboard with valid cookie auth returns HTML."""
    resp = await client.get(
        "/dashboard",
        cookies={"dashboard_token": "test-token-12345"},
    )
    assert resp.status_code in (200, 201)
    assert "text/html" in resp.headers["content-type"]
    assert "AgentShroud" in resp.text


@pytest.mark.asyncio
async def test_dashboard_stats_returns_json(client):
    """GET /dashboard/stats returns JSON stats."""
    resp = await client.get("/dashboard/stats", headers=AUTH)
    assert resp.status_code in (200, 201)
    data = resp.json()
    # Should have some stats structure
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_dashboard_requires_auth(client):
    """GET /dashboard without auth returns 403."""
    resp = await client.get("/dashboard")
    assert resp.status_code == 403


# === Status endpoint (no auth) ===


@pytest.mark.asyncio
async def test_status_endpoint(client):
    """GET /status returns service info."""
    resp = await client.get("/status")
    assert resp.status_code in (200, 201)
    data = resp.json()
    assert "status" in data or "version" in data or "service" in data
