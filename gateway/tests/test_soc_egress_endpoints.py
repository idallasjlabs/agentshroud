# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

import pytest
import pytest_asyncio
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
    assert "count" in data
    assert "items" in data


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
    resp = await client.get("/manage/soc/report", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "correlation" in data
    assert "events" in data
    assert "quarantine" in data
    assert data["quarantine"]["inbound_total"] >= 1
    assert data["quarantine"]["outbound_total"] >= 1
    assert "scanner_summary" in data


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
        {"message_id": "i-1", "status": "pending"},
        {"message_id": "i-2", "status": "released"},
    ]
    app_state.blocked_outbound_quarantine = [
        {"message_id": "o-1", "status": "pending"},
        {"message_id": "o-2", "status": "discarded"},
    ]
    resp = await client.get("/manage/quarantine/summary", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["inbound"]["total"] == 2
    assert data["inbound"]["pending"] == 1
    assert data["outbound"]["total"] == 2
    assert data["outbound"]["discarded"] == 1


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
