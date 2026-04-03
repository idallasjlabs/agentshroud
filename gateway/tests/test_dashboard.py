# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for Dashboard endpoints and WebSocket activity feed"""

from __future__ import annotations

import asyncio
import time
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from gateway.ingest_api.event_bus import make_event
from gateway.ingest_api.main import app, app_state, lifespan
from gateway.ingest_api.routes.dashboard import (
    _build_activity_entries_from_contributor_logs,
    _build_activity_summary_from_contributor_logs,
    _build_egress_live_snapshot,
    _create_ws_token,
    _load_contributor_logs,
    _parse_collaborator_log_dirs,
)


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


@pytest.mark.asyncio
async def test_collaborators_endpoint_reads_configured_contributor_sources(
    client, monkeypatch, tmp_path
):
    dir_a = tmp_path / "contributors-a"
    dir_b = tmp_path / "contributors-b"
    dir_a.mkdir()
    dir_b.mkdir()
    (dir_a / "2026-03-09-111.md").write_text(
        "- 2026-03-09T12:00:00+00:00 | alice (111) | telegram | older\n"
    )
    (dir_a / "2026-03-10-111.md").write_text(
        "- 2026-03-10T12:00:00+00:00 | alice (111) | telegram | newer\n"
    )
    (dir_b / "2026-03-10-222.md").write_text(
        "- 2026-03-10T12:10:00+00:00 | bob (222) | telegram | peer\n"
    )
    monkeypatch.setenv("AGENTSHROUD_CONTRIBUTOR_LOG_DIRS", f"{dir_a},{dir_b}")

    old_tracker = getattr(app_state, "collaborator_tracker", None)
    app_state.collaborator_tracker = SimpleNamespace(
        get_activity=lambda limit=50: [],
        get_activity_summary=lambda: {
            "total_messages": 0,
            "unique_users": 0,
            "last_activity": None,
            "by_user": {},
        },
    )
    try:
        resp = await client.get(
            "/collaborators",
            headers={"Authorization": "Bearer test-token-12345"},
        )
        assert resp.status_code == 200
        data = resp.json()
        assert str(dir_a) in data["contributor_log_sources"]
        assert str(dir_b) in data["contributor_log_sources"]
        assert any(
            source.endswith("/data/bot-workspace/memory/contributors")
            for source in data["contributor_log_sources"]
        )
        assert [log["filename"] for log in data["contributor_logs"]] == [
            "2026-03-10-111.md",
            "2026-03-09-111.md",
            "2026-03-10-222.md",
        ]
        assert data["contributor_logs"][0]["source_dir"] == str(dir_a)
        assert data["contributor_logs"][-1]["source_dir"] == str(dir_b)
        assert data["activity_source"] == "contributor_logs_fallback"
        assert len(data["activity"]) == 3
        assert data["activity"][0]["username"] == "bob"
        assert data["summary"]["total_messages"] == 3
        assert data["summary"]["unique_users"] == 2
    finally:
        app_state.collaborator_tracker = old_tracker


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
        assert "privacy_access_summary" in snap["details"]
        assert "privacy_redaction_summary" in snap["details"]
        assert "pending_by_risk" in snap["details"]
        assert "pending_domain_top" in snap["details"]
        assert "pending_agent_top" in snap["details"]
        assert "pending_tool_top" in snap["details"]
        assert "pending_average_age_seconds" in snap["details"]
        assert "pending_oldest_age_seconds" in snap["details"]
        assert "pending_expiring_soon_count" in snap["details"]


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
        event = make_event(
            "privacy_policy_violation", "blocked private tool", {"tool": "gmail_send"}
        )
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


def test_parse_collaborator_log_dirs_dedupes_and_preserves_order(monkeypatch):
    monkeypatch.setenv(
        "AGENTSHROUD_CONTRIBUTOR_LOG_DIRS",
        "/tmp/a,/tmp/b,/tmp/a,,/tmp/c",
    )
    dirs = _parse_collaborator_log_dirs()
    assert dirs == [Path("/tmp/a"), Path("/tmp/b"), Path("/tmp/c")]


def test_load_contributor_logs_reads_multiple_dirs_and_dedupes(tmp_path):
    dir_a = tmp_path / "a"
    dir_b = tmp_path / "b"
    dir_a.mkdir()
    dir_b.mkdir()

    (dir_a / "2026-03-10-111.md").write_text("alice")
    (dir_b / "2026-03-10-222.md").write_text("bob")
    # duplicate filename in second dir should be skipped
    (dir_b / "2026-03-10-111.md").write_text("duplicate")

    logs = _load_contributor_logs([dir_a, dir_b])
    names = [item["filename"] for item in logs]
    assert names == ["2026-03-10-111.md", "2026-03-10-222.md"]
    assert logs[0]["content"] == "alice"
    assert logs[0]["source_dir"] == str(dir_a)
    assert logs[1]["source_dir"] == str(dir_b)


def test_build_activity_summary_from_contributor_logs():
    logs = [
        {
            "filename": "2026-03-10-111.md",
            "content": (
                "- 2026-03-10T16:33:22+00:00 | alice (111) | telegram | hello\n"
                "- 2026-03-10T16:34:22+00:00 | bob (222) | telegram | hi\n"
            ),
        },
        {
            "filename": "2026-03-10-222.md",
            "content": "- 2026-03-10T16:35:22+00:00 | alice (111) | telegram | follow-up\n",
        },
    ]
    summary = _build_activity_summary_from_contributor_logs(logs)
    assert summary["total_messages"] == 3
    assert summary["unique_users"] == 2
    assert summary["last_activity"] is not None


def test_build_activity_entries_from_contributor_logs():
    logs = [
        {
            "filename": "2026-03-10-111.md",
            "content": (
                "- 2026-03-10T16:33:22+00:00 | alice (111) | telegram | hello there\n"
                "- 2026-03-10T16:34:22+00:00 | bob (222) | telegram | hi\n"
            ),
        }
    ]
    entries = _build_activity_entries_from_contributor_logs(logs, limit=10)
    assert len(entries) == 2
    assert entries[0]["username"] == "bob"
    assert entries[0]["user_id"] == "222"
    assert entries[1]["message_preview"] == "hello there"


def test_build_activity_entries_from_contributor_logs_accepts_non_bullet_and_zulu_time():
    logs = [
        {
            "filename": "2026-03-10-raw.md",
            "content": "2026-03-10T16:35:22Z | carol (333) | telegram | weather | details",
        }
    ]
    entries = _build_activity_entries_from_contributor_logs(logs, limit=10)
    assert len(entries) == 1
    assert entries[0]["username"] == "carol"
    assert entries[0]["user_id"] == "333"
    assert entries[0]["message_preview"] == "weather | details"


def test_build_activity_summary_from_contributor_logs_accepts_non_bullet_lines():
    logs = [
        {
            "filename": "2026-03-10-raw.md",
            "content": "2026-03-10T16:35:22Z | carol (333) | telegram | hello",
        }
    ]
    summary = _build_activity_summary_from_contributor_logs(logs)
    assert summary["total_messages"] == 1
    assert summary["unique_users"] == 1


@pytest.mark.asyncio
async def test_build_egress_live_snapshot_enriches_pending_metrics(monkeypatch):
    now = time.time()

    class _ApprovalQueue:
        async def get_pending_requests(self):
            return [
                {
                    "request_id": "r1",
                    "domain": "weather.com",
                    "port": 443,
                    "agent_id": "a1",
                    "tool_name": "web_fetch",
                    "timestamp": now - 10,
                    "risk_level": "yellow",
                    "timeout_at": now + 5,
                }
            ]

        async def get_emergency_status(self):
            return {"enabled": False, "reason": ""}

    class _EgressFilter:
        def get_stats(self):
            return {"total": 1}

        def get_log(self, limit=20):
            return []

    async def _get_recent(limit=200):
        return []

    old_approval = getattr(app_state, "egress_approval_queue", None)
    old_filter = getattr(app_state, "egress_filter", None)
    old_bus = getattr(app_state, "event_bus", None)
    old_quarantine = getattr(app_state, "blocked_message_quarantine", None)
    old_outbound_quarantine = getattr(app_state, "blocked_outbound_quarantine", None)
    old_scanner_results = getattr(app_state, "scanner_results", None)
    old_scanner_history = getattr(app_state, "scanner_result_history", None)
    old_mcp_proxy = getattr(app_state, "mcp_proxy", None)
    try:
        app_state.egress_approval_queue = _ApprovalQueue()
        app_state.egress_filter = _EgressFilter()
        app_state.event_bus = SimpleNamespace(get_recent=_get_recent)
        app_state.blocked_message_quarantine = []
        app_state.blocked_outbound_quarantine = []
        app_state.scanner_results = {}
        app_state.scanner_result_history = []
        app_state.mcp_proxy = None

        snapshot = await _build_egress_live_snapshot()
        assert snapshot["pending_requests"] == 1
        assert snapshot["pending_oldest_age_seconds"] >= 9.0
        assert snapshot["pending_average_age_seconds"] >= 9.0
        assert snapshot["pending_expiring_soon_count"] == 1
        assert snapshot["pending_agent_top"] == [{"agent_id": "a1", "count": 1}]
        assert snapshot["pending_tool_top"] == [{"tool_name": "web_fetch", "count": 1}]
        assert len(snapshot["pending_items"]) == 1
        item = snapshot["pending_items"][0]
        assert item["age_seconds"] >= 9.0
        assert item["remaining_seconds"] <= 6.0
    finally:
        app_state.egress_approval_queue = old_approval
        app_state.egress_filter = old_filter
        app_state.event_bus = old_bus
        app_state.blocked_message_quarantine = old_quarantine
        app_state.blocked_outbound_quarantine = old_outbound_quarantine
        app_state.scanner_results = old_scanner_results
        app_state.scanner_result_history = old_scanner_history
        app_state.mcp_proxy = old_mcp_proxy


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
    assert "data-action" in resp.text or "data-id" in resp.text or "addEventListener" in resp.text
