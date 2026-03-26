# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

import pytest
import pytest_asyncio
from types import SimpleNamespace
from unittest.mock import patch
from httpx import AsyncClient, ASGITransport

from gateway.ingest_api.main import app, lifespan, app_state
from gateway.ingest_api.event_bus import make_event


@pytest_asyncio.fixture
async def client(test_config):
    with patch("gateway.ingest_api.lifespan.load_config", return_value=test_config):
        async with lifespan(app):
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as ac:
                yield ac


@pytest.mark.asyncio
async def test_manage_egress_rules_endpoint(client, auth_headers):
    resp = await client.get("/manage/egress/rules", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "rules" in data
    assert "emergency" in data


@pytest.mark.asyncio
async def test_manage_egress_add_remove_rule_and_risk(client, auth_headers):
    add = await client.post(
        "/manage/egress/rules",
        headers=auth_headers,
        params={"domain": "example.org", "action": "allow", "mode": "permanent"},
    )
    assert add.status_code == 200
    assert add.json()["ok"] is True

    risk = await client.get(
        "/manage/egress/risk",
        headers=auth_headers,
        params={"domain": "1.2.3.4", "port": 443},
    )
    assert risk.status_code == 200
    assert risk.json()["risk_level"] == "red"

    remove = await client.delete(
        "/manage/egress/rules",
        headers=auth_headers,
        params={"domain": "example.org"},
    )
    assert remove.status_code == 200
    assert remove.json()["ok"] is True


@pytest.mark.asyncio
async def test_manage_egress_log_endpoint(client, auth_headers):
    egress = getattr(app_state, "egress_filter", None)
    assert egress is not None
    egress.check("agent-a", "https://example.com")
    resp = await client.get("/manage/egress/log", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "summary" in data
    assert "allowed" in data["summary"]
    assert "denied" in data["summary"]
    assert "count" in data
    assert "items" in data


@pytest.mark.asyncio
async def test_manage_egress_pending_endpoint_includes_summary(client, auth_headers):
    class FakeQueue:
        async def cleanup_expired(self):
            return None

        async def get_pending_requests(self):
            return [
                {
                    "request_id": "r1",
                    "domain": "example.com",
                    "agent_id": "telegram_web_fetch:100",
                    "tool_name": "web_fetch",
                    "risk_level": "yellow",
                    "timestamp": 1.0,
                    "timeout_at": 9999999999.0,
                },
                {
                    "request_id": "r2",
                    "domain": "1.2.3.4",
                    "agent_id": "telegram_web_fetch:100",
                    "tool_name": "browser",
                    "risk_level": "red",
                    "timestamp": 2.0,
                    "timeout_at": 9999999999.0,
                },
            ]

    original = app_state.egress_approval_queue
    app_state.egress_approval_queue = FakeQueue()
    try:
        resp = await client.get("/manage/egress/pending", headers=auth_headers)
        assert resp.status_code == 200
        data = resp.json()
        assert data["count"] == 2
        assert data["pending_by_risk"]["yellow"] == 1
        assert data["pending_by_risk"]["red"] == 1
        assert data["pending_domain_top"][0]["count"] >= 1
        assert data["pending_agent_top"][0]["agent_id"] == "telegram_web_fetch:100"
        assert data["pending_agent_top"][0]["count"] == 2
        assert data["pending_tool_top"][0]["count"] >= 1
        assert data["oldest_age_seconds"] >= 0
        assert data["average_age_seconds"] >= 0
        assert data["expiring_soon_count"] >= 0
        assert data["pending"][0]["age_seconds"] >= 0
        assert data["pending"][0]["remaining_seconds"] >= 0
    finally:
        app_state.egress_approval_queue = original


@pytest.mark.asyncio
async def test_manage_egress_emergency_toggle(client, auth_headers):
    on = await client.post(
        "/manage/egress/emergency-block",
        headers=auth_headers,
        params={"enabled": True, "reason": "incident"},
    )
    assert on.status_code == 200
    assert on.json()["status"]["enabled"] is True

    off = await client.post(
        "/manage/egress/emergency-block",
        headers=auth_headers,
        params={"enabled": False},
    )
    assert off.status_code == 200
    assert off.json()["status"]["enabled"] is False


@pytest.mark.asyncio
async def test_manage_soc_correlation_endpoint(client, auth_headers):
    # seed one quarantined message for correlation context
    app_state.blocked_message_quarantine = [
        {"timestamp": 1.0, "text": "blocked", "reason": "x", "source": "test"}
    ]
    resp = await client.get("/manage/soc/correlation", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "risk_score" in data
    assert "severity" in data
    assert "correlated_findings" in data
    assert "top_denied_destinations" in data
    assert "top_policy_violators" in data
    assert "scanner_findings" in data
    assert "quarantined_outbound_messages" in data
    assert "private_data_redactions" in data
    assert "scanner_recent_critical_events" in data


@pytest.mark.asyncio
async def test_manage_soc_events_endpoint(client, auth_headers):
    await app_state.event_bus.emit(
        make_event("privacy_policy_violation", "blocked private tool", {"tool": "gmail_send"}, "warning")
    )
    await app_state.event_bus.emit(
        make_event("egress_attempt", "egress checked", {"domain": "example.com"}, "info")
    )
    resp = await client.get(
        "/manage/soc/events",
        headers=auth_headers,
        params={"event_type_prefix": "privacy_", "severity": "warning"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["count"] >= 1
    assert all(str(item["type"]).startswith("privacy_") for item in data["items"])


@pytest.mark.asyncio
async def test_manage_soc_report_endpoint(client, auth_headers):
    app_state.blocked_message_quarantine = [{"message_id": "i-1", "status": "pending"}]
    app_state.blocked_outbound_quarantine = [{"message_id": "o-1", "status": "pending"}]
    app_state.scanner_results = {
        "trivy": {
            "summary": {"status": "warning", "critical": 0, "high": 1, "findings": 1},
            "result": {"mock": True},
        }
    }
    await app_state.event_bus.emit(
        make_event("scanner_result", "scan complete", {"scanner": "trivy"}, "warning")
    )
    app_state.collaborator_tracker = SimpleNamespace(
        get_activity_summary=lambda: {
            "total_messages": 2,
            "unique_users": 1,
            "last_activity": 1700000000.0,
            "by_user": {"1234": {"username": "steve", "message_count": 2, "last_active": 1700000000.0}},
        },
        get_activity=lambda limit=100: [
            {
                "timestamp": 1700000000.0,
                "user_id": "1234",
                "username": "steve",
                "message_preview": "hello",
                "source": "telegram",
            }
        ],
    )
    resp = await client.get("/manage/soc/report", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "correlation" in data
    assert "events" in data
    assert "quarantine" in data
    assert data["quarantine"]["inbound_total"] >= 1
    assert data["quarantine"]["outbound_total"] >= 1
    assert "scanner_summary" in data
    assert "privacy" in data
    assert "policy_loaded" in data["privacy"]
    assert "private_access_summary" in data["privacy"]
    assert "private_redaction_summary" in data["privacy"]
    assert "collaborator_activity" in data
    assert data["collaborator_activity"]["source"] == "tracker"
    assert data["collaborator_activity"]["summary"]["total_messages"] == 2
    assert data["collaborator_activity"]["recent"][0]["username"] == "steve"
    assert "egress_live" in data
    assert "pending_by_risk" in data["egress_live"]


@pytest.mark.asyncio
async def test_manage_soc_report_falls_back_to_contributor_logs(client, auth_headers, monkeypatch, tmp_path):
    contrib = tmp_path / "contributors"
    contrib.mkdir()
    (contrib / "2026-03-10-111.md").write_text(
        "- 2026-03-10T12:00:00+00:00 | alice (111) | telegram | hello\n"
    )
    monkeypatch.setenv("AGENTSHROUD_CONTRIBUTOR_LOG_DIRS", str(contrib))
    app_state.collaborator_tracker = None
    resp = await client.get("/manage/soc/report", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["collaborator_activity"]["source"] == "contributor_logs_fallback"
    assert data["collaborator_activity"]["summary"]["total_messages"] == 1
    assert data["collaborator_activity"]["recent"][0]["username"] == "alice"


@pytest.mark.asyncio
async def test_manage_soc_export_endpoint(client, auth_headers):
    resp = await client.get(
        "/manage/soc/export",
        headers=auth_headers,
        params={"format_type": "cef", "limit": 50},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["format"] == "cef"
    assert "record_count" in data
    assert "hash_verification" in data


@pytest.mark.asyncio
async def test_manage_soc_export_invalid_format(client, auth_headers):
    resp = await client.get(
        "/manage/soc/export",
        headers=auth_headers,
        params={"format_type": "xml"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["error"] == "invalid_format"


@pytest.mark.asyncio
async def test_quarantine_list_endpoint(client, auth_headers):
    app_state.blocked_message_quarantine = [{"timestamp": 1.0, "text": "x"}]
    resp = await client.get("/manage/quarantine/blocked-messages", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["count"] >= 1
    assert isinstance(data["items"], list)
    assert "message_id" in data["items"][0]
    assert data["items"][0]["status"] == "pending"


@pytest.mark.asyncio
async def test_quarantine_release_and_discard_flow(client, auth_headers):
    app_state.blocked_message_quarantine = [
        {"message_id": "m-1", "timestamp": 1.0, "text": "x", "status": "pending"},
        {"message_id": "m-2", "timestamp": 2.0, "text": "y", "status": "pending"},
    ]

    released = await client.post(
        "/manage/quarantine/blocked-messages/m-1/release",
        headers=auth_headers,
        params={"note": "approved for manual follow-up"},
    )
    assert released.status_code == 200
    rdata = released.json()
    assert rdata["ok"] is True
    assert rdata["item"]["status"] == "released"

    discarded = await client.post(
        "/manage/quarantine/blocked-messages/m-2/discard",
        headers=auth_headers,
        params={"note": "malicious, keep blocked"},
    )
    assert discarded.status_code == 200
    ddata = discarded.json()
    assert ddata["ok"] is True
    assert ddata["item"]["status"] == "discarded"

    pending_only = await client.get(
        "/manage/quarantine/blocked-messages",
        headers=auth_headers,
        params={"status": "pending"},
    )
    assert pending_only.status_code == 200
    pdata = pending_only.json()
    assert pdata["count"] == 0


@pytest.mark.asyncio
async def test_outbound_quarantine_endpoints(client, auth_headers):
    app_state.blocked_outbound_quarantine = [
        {"message_id": "o-1", "timestamp": 1.0, "text": "x", "status": "pending", "chat_id": "1"},
        {"message_id": "o-2", "timestamp": 2.0, "text": "y", "status": "pending", "chat_id": "2"},
    ]

    listed = await client.get("/manage/quarantine/blocked-outbound", headers=auth_headers)
    assert listed.status_code == 200
    assert listed.json()["count"] == 2

    released = await client.post(
        "/manage/quarantine/blocked-outbound/o-1/release",
        headers=auth_headers,
        params={"note": "manual resend approved"},
    )
    assert released.status_code == 200
    assert released.json()["ok"] is True
    assert released.json()["item"]["status"] == "released"

    discarded = await client.post(
        "/manage/quarantine/blocked-outbound/o-2/discard",
        headers=auth_headers,
        params={"note": "malicious output"},
    )
    assert discarded.status_code == 200
    assert discarded.json()["ok"] is True
    assert discarded.json()["item"]["status"] == "discarded"


@pytest.mark.asyncio
async def test_quarantine_summary_endpoint(client, auth_headers):
    app_state.blocked_message_quarantine = [
        {"message_id": "i-1", "status": "pending", "reason": "policy_a"},
        {"message_id": "i-2", "status": "released", "reason": "policy_a"},
    ]
    app_state.blocked_outbound_quarantine = [
        {"message_id": "o-1", "status": "pending", "reason": "sensitive_leak"},
        {"message_id": "o-2", "status": "discarded", "reason": "sensitive_leak"},
    ]
    resp = await client.get("/manage/quarantine/summary", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["inbound"]["total"] == 2
    assert data["inbound"]["pending"] == 1
    assert data["outbound"]["total"] == 2
    assert data["outbound"]["discarded"] == 1
    assert data["inbound_top_reasons"][0]["reason"] == "policy_a"
    assert data["inbound_top_reasons"][0]["count"] == 2
    assert data["outbound_top_reasons"][0]["reason"] == "sensitive_leak"
    assert data["outbound_top_reasons"][0]["count"] == 2


@pytest.mark.asyncio
async def test_manage_privacy_policy_and_audit_endpoints(client, auth_headers):
    mcp = getattr(app_state, "mcp_proxy", None)
    assert mcp is not None
    mcp.permissions.check_tool_permission("collab-user", "test", "gmail_send")
    mcp.permissions.record_private_data_redaction(
        agent_id="collab-user",
        server_name="test",
        tool_name="memory_search",
        redaction_count=2,
    )

    policy = await client.get("/manage/privacy/policy", headers=auth_headers)
    assert policy.status_code == 200
    policy_data = policy.json()
    assert "admin_private_tool_patterns" in policy_data
    assert "admin_private_data_patterns" in policy_data
    assert "policy_file" in policy_data
    assert "loaded" in policy_data["policy_file"]
    assert "path" in policy_data["policy_file"]

    audit = await client.get("/manage/privacy/audit", headers=auth_headers)
    assert audit.status_code == 200
    audit_data = audit.json()
    assert audit_data["count"] >= 1
    assert audit_data["summary"]["total"] >= 1
    assert audit_data["redaction_count"] >= 1
    assert audit_data["redaction_summary"]["total_redactions"] >= 2


@pytest.mark.asyncio
async def test_manage_scanners_summary_endpoint(client, auth_headers):
    app_state.scanner_results = {
        "trivy": {
            "summary": {"critical": 1, "high": 2, "findings": 6},
            "result": {"mock": True},
        },
        "clamav": {
            "summary": {"critical": 0, "high": 0, "findings": 0},
            "result": {"mock": True},
        },
    }
    resp = await client.get("/manage/scanners/summary", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "availability" in data
    assert "last_results" in data
    assert data["totals"]["critical"] >= 1
    assert data["totals"]["high"] >= 2


@pytest.mark.asyncio
async def test_manage_scanners_history_endpoint(client, auth_headers):
    app_state.scanner_result_history = [
        {
            "timestamp": "2026-01-01T00:00:00Z",
            "scanner": "trivy",
            "target": "fs",
            "summary": {"status": "critical", "critical": 2, "high": 0, "findings": 2},
            "result": {"mock": True},
        },
        {
            "timestamp": "2026-01-01T00:01:00Z",
            "scanner": "clamav",
            "target": "/app",
            "summary": {"status": "clean", "critical": 0, "high": 0, "findings": 0},
            "result": {"mock": True},
        },
    ]
    resp = await client.get("/manage/scanners/history", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["count"] == 2
    assert len(data["items"]) == 2

    critical_only = await client.get(
        "/manage/scanners/history",
        headers=auth_headers,
        params={"status": "critical"},
    )
    assert critical_only.status_code == 200
    cdata = critical_only.json()
    assert cdata["count"] == 1


@pytest.mark.asyncio
async def test_manage_scan_all_endpoint(client, auth_headers):
    class FakeClam:
        @staticmethod
        def run_clamscan(*_args, **_kwargs):
            return {"infected_count": 0, "error": None}

    class FakeTrivy:
        @staticmethod
        def run_trivy_scan(*_args, **_kwargs):
            return {
                "total_vulnerabilities": 1,
                "by_severity": {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 0, "LOW": 0},
                "error": None,
            }

    app_state.clamav_scanner = FakeClam()
    app_state.trivy_scanner = FakeTrivy()
    app_state.openscap_available = False

    resp = await client.post("/manage/scan/all", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "results" in data
    assert "summaries" in data
    assert "clamav" in data["results"]
    assert "trivy" in data["results"]


# ---------------------------------------------------------------------------
# V9-3: /soc/v1/scanners/recent endpoint (live app_state history)
# ---------------------------------------------------------------------------

_SOC_TEST_TOKEN = "test-token-12345"
_SOC_AUTH_HEADERS = {"Authorization": f"Bearer {_SOC_TEST_TOKEN}"}


@pytest.mark.asyncio
async def test_soc_scanners_recent_empty(client):
    """Returns empty result when scanner_result_history is empty."""
    app_state.scanner_result_history = []
    with patch("gateway.soc.auth._get_config_token", return_value=_SOC_TEST_TOKEN):
        resp = await client.get("/soc/v1/scanners/recent", headers=_SOC_AUTH_HEADERS)
    assert resp.status_code == 200
    data = resp.json()
    assert data["count"] == 0
    assert data["items"] == []
    assert data["totals"]["critical"] == 0


@pytest.mark.asyncio
async def test_soc_scanners_recent_returns_history(client):
    """Returns scanner events from app_state.scanner_result_history."""
    app_state.scanner_result_history = [
        {
            "timestamp": "2026-01-01T00:00:00Z",
            "scanner": "trivy",
            "target": "fs",
            "summary": {"status": "critical", "critical": 1, "high": 0, "findings": 1},
            "result": {},
        },
        {
            "timestamp": "2026-01-01T00:01:00Z",
            "scanner": "clamav",
            "target": "/app",
            "summary": {"status": "clean", "critical": 0, "high": 0, "findings": 0},
            "result": {},
        },
    ]
    with patch("gateway.soc.auth._get_config_token", return_value=_SOC_TEST_TOKEN):
        resp = await client.get("/soc/v1/scanners/recent", headers=_SOC_AUTH_HEADERS)
    assert resp.status_code == 200
    data = resp.json()
    assert data["count"] == 2
    assert data["totals"]["critical"] == 1
    assert data["totals"]["findings"] == 1


@pytest.mark.asyncio
async def test_soc_scanners_recent_status_filter(client):
    """Status query param filters by summary.status."""
    app_state.scanner_result_history = [
        {
            "timestamp": "2026-01-01T00:00:00Z",
            "scanner": "trivy",
            "target": "fs",
            "summary": {"status": "critical", "critical": 2, "high": 0, "findings": 2},
            "result": {},
        },
        {
            "timestamp": "2026-01-01T00:01:00Z",
            "scanner": "clamav",
            "target": "/app",
            "summary": {"status": "clean", "critical": 0, "high": 0, "findings": 0},
            "result": {},
        },
    ]
    with patch("gateway.soc.auth._get_config_token", return_value=_SOC_TEST_TOKEN):
        resp = await client.get(
            "/soc/v1/scanners/recent",
            headers=_SOC_AUTH_HEADERS,
            params={"status": "critical"},
        )
    assert resp.status_code == 200
    data = resp.json()
    assert data["count"] == 1
    assert data["items"][0]["scanner"] == "trivy"


@pytest.mark.asyncio
async def test_soc_scanners_recent_limit(client):
    """Limit param caps the number of returned items."""
    app_state.scanner_result_history = [
        {"timestamp": f"2026-01-01T00:0{i}:00Z", "scanner": "trivy",
         "summary": {"status": "clean", "critical": 0, "high": 0, "findings": 0},
         "result": {}}
        for i in range(5)
    ]
    with patch("gateway.soc.auth._get_config_token", return_value=_SOC_TEST_TOKEN):
        resp = await client.get(
            "/soc/v1/scanners/recent",
            headers=_SOC_AUTH_HEADERS,
            params={"limit": 2},
        )
    assert resp.status_code == 200
    data = resp.json()
    assert data["count"] == 2
