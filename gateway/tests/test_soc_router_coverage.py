# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Coverage tests for gateway/soc/router.py — SCL REST endpoints.

Strategy: a standalone FastAPI app with only the SOC router mounted, the
``get_caller`` dependency overridden with a deterministic FakeCaller, and
``soc_router._app_state`` monkeypatched to a per-test SimpleNamespace so every
handler branch (present / absent / raising backing module) is reachable without
real Docker, network, or Telegram access.
"""

from __future__ import annotations

import asyncio
import http.client
import json
import logging
import urllib.error
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from starlette.testclient import TestClient

import gateway.soc.router as soc_router
from gateway.security.rbac_config import Role
from gateway.soc.auth import get_caller

# ---------------------------------------------------------------------------
# Fakes & fixtures
# ---------------------------------------------------------------------------


class FakeCaller:
    """Stands in for SCLCaller: RBAC require() is a no-op, owner is switchable."""

    def __init__(self, user_id="owner-1", owner=True, group_admin=False):
        self.user_id = user_id
        self.role = Role.OWNER if owner else Role.COLLABORATOR
        self._owner = owner
        self._group_admin = group_admin

    def require(self, action, resource):
        return None

    def is_owner(self):
        return self._owner

    def is_group_admin(self, group_id):
        return self._group_admin


class FakeAuditStore:
    def __init__(self, entries):
        self._entries = entries

    async def get_recent_entries(self, limit=100):
        return self._entries[:limit]


class _Svc:
    def __init__(self, name, status="running", health="healthy", image="img"):
        self.name = name
        self.status = SimpleNamespace(value=status)
        self.health = SimpleNamespace(value=health)
        self.image = image

    def model_dump(self):
        return {"name": self.name, "status": self.status.value, "image": self.image}


def _make_service_manager(services=None, logs=None, results=None):
    services = services or []
    logs = logs if logs is not None else ["log line"]
    results = results or {}

    class _Mgr:
        def __init__(self, engine=None):
            pass

        def list_services(self):
            return services

        async def get_logs(self, name, tail=50, module_filter=""):
            return logs

        async def start_service(self, name):
            return results.get("start", True)

        async def stop_service(self, name):
            return results.get("stop", True)

        async def restart_service(self, name):
            return results.get("restart", True)

        async def update_service(self, name):
            return results.get("update", True)

    return _Mgr


class FakeGroup:
    def __init__(self, name="Team", members=None, admin=None, collab_mode="local_only"):
        self.name = name
        self.members = members if members is not None else []
        self.admin = admin
        self.collab_mode = collab_mode

    def model_dump(self):
        return {
            "name": self.name,
            "members": list(self.members),
            "admin": self.admin,
            "collab_mode": self.collab_mode,
        }


@pytest.fixture
def holder():
    return {"caller": FakeCaller()}


@pytest.fixture
def state(monkeypatch):
    ns = SimpleNamespace()
    monkeypatch.setattr(soc_router, "_app_state", lambda: ns)
    return ns


@pytest.fixture
async def client(holder, state):
    app = FastAPI()
    app.include_router(soc_router.router)
    app.dependency_overrides[get_caller] = lambda: holder["caller"]
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


OWNER = FakeCaller()
NON_OWNER = FakeCaller(user_id="55555", owner=False)


# ---------------------------------------------------------------------------
# Helpers: _log_audit / _risk_level_label / _file_hash
# ---------------------------------------------------------------------------


async def test_log_audit_appends_to_audit_store(monkeypatch):
    store = SimpleNamespace(append=AsyncMock())
    monkeypatch.setattr(soc_router, "_app_state", lambda: SimpleNamespace(audit_store=store))
    soc_router._log_audit(OWNER, "test cmd", target="t1", details={"k": "v"})
    await asyncio.sleep(0)
    store.append.assert_awaited()
    entry = store.append.await_args.args[0]
    assert entry["command"] == "test cmd"
    assert entry["target"] == "t1"
    assert entry["actor_id"] == "owner-1"


async def test_log_audit_survives_app_state_failure(monkeypatch):
    def _boom():
        raise RuntimeError("state unavailable")

    monkeypatch.setattr(soc_router, "_app_state", _boom)
    # Must not raise — audit logging is best-effort
    soc_router._log_audit(OWNER, "cmd", target="t")


def test_risk_level_label_boundaries():
    assert soc_router._risk_level_label(70) == "critical"
    assert soc_router._risk_level_label(40) == "high"
    assert soc_router._risk_level_label(20) == "medium"
    assert soc_router._risk_level_label(19) == "low"
    assert soc_router._risk_level_label(0) == "low"


def test_file_hash_existing_and_missing():
    h = soc_router._file_hash("soc.js")
    assert len(h) == 8 and h != "0"
    assert soc_router._file_hash("definitely-not-a-file.xyz") == "0"


# ---------------------------------------------------------------------------
# Auth endpoints
# ---------------------------------------------------------------------------


async def test_auth_login_no_configured_token(client, monkeypatch):
    monkeypatch.delenv("AGENTSHROUD_GATEWAY_PASSWORD", raising=False)
    monkeypatch.delenv("OPENCLAW_GATEWAY_PASSWORD", raising=False)
    resp = await client.post("/soc/v1/auth/login", json={"token": "anything"})
    assert resp.status_code == 401
    assert resp.json()["code"] == "UNAUTHORIZED"


async def test_auth_login_wrong_token(client, monkeypatch):
    monkeypatch.setenv("AGENTSHROUD_GATEWAY_PASSWORD", "correct-token")
    resp = await client.post("/soc/v1/auth/login", json={"token": "wrong"})
    assert resp.status_code == 401


async def test_auth_login_success_sets_secure_cookie(client, monkeypatch):
    monkeypatch.setenv("AGENTSHROUD_GATEWAY_PASSWORD", "correct-token")
    monkeypatch.delenv("AGENTSHROUD_DEV_MODE", raising=False)
    resp = await client.post("/soc/v1/auth/login", json={"token": "correct-token"})
    assert resp.status_code == 200
    assert resp.json()["ok"] is True
    cookie = resp.headers["set-cookie"]
    assert "soc_session=" in cookie
    assert "Secure" in cookie
    assert "HttpOnly" in cookie


async def test_auth_login_dev_mode_omits_secure_flag(client, monkeypatch):
    monkeypatch.setenv("AGENTSHROUD_GATEWAY_PASSWORD", "correct-token")
    monkeypatch.setenv("AGENTSHROUD_DEV_MODE", "1")
    resp = await client.post("/soc/v1/auth/login", json={"token": "correct-token"})
    assert resp.status_code == 200
    assert "Secure" not in resp.headers["set-cookie"]


async def test_auth_ws_token(client):
    resp = await client.post("/soc/v1/auth/ws-token")
    assert resp.status_code == 200
    data = resp.json()
    assert data["ttl_seconds"] == 300
    assert len(data["token"]) == 64


# ---------------------------------------------------------------------------
# Security endpoints
# ---------------------------------------------------------------------------

_ENTRIES = [
    SimpleNamespace(
        timestamp="2026-01-01T00:00:00Z",
        details={"agent_id": "botA:1"},
        event_type="egress_denied",
        source_module="egress_filter",
        severity="high",
        entry_hash="h1",
        prev_hash="p1",
    ),
    SimpleNamespace(
        timestamp="2026-01-01T00:01:00Z",
        details={"agent_id": "botB"},
        event_type="prompt_blocked",
        source_module="prompt_guard",
        severity="info",
        entry_hash="h2",
        prev_hash="h1",
    ),
]


async def test_security_events_with_filters(client, state):
    state.audit_store = FakeAuditStore(_ENTRIES)
    resp = await client.get("/soc/v1/security/events")
    assert resp.status_code == 200
    assert len(resp.json()) == 2

    high_only = await client.get("/soc/v1/security/events", params={"severity": "high"})
    assert [e["event_type"] for e in high_only.json()] == ["egress_denied"]

    bot_a = await client.get("/soc/v1/security/events", params={"bot_id": "botA"})
    assert len(bot_a.json()) == 1
    assert bot_a.json()[0]["agent_id"] == "botA:1"


async def test_security_events_no_store(client):
    resp = await client.get("/soc/v1/security/events")
    assert resp.status_code == 200
    assert resp.json() == []


async def test_security_alerts_with_dispatcher(client, state):
    state.alert_dispatcher = SimpleNamespace(
        get_recent_alerts=lambda limit=50: [
            {"event_type": "anomaly", "severity": "high", "summary": "spike"},
            "not-a-dict",
        ]
    )
    resp = await client.get("/soc/v1/security/alerts")
    assert resp.status_code == 200
    alerts = resp.json()
    assert len(alerts) == 1
    assert alerts[0]["event_type"] == "anomaly"
    assert alerts[0]["summary"] == "spike"


async def test_security_alerts_dispatcher_raises(client, state):
    def _boom(limit=50):
        raise RuntimeError("dispatch error")

    state.alert_dispatcher = SimpleNamespace(get_recent_alerts=_boom)
    resp = await client.get("/soc/v1/security/alerts")
    assert resp.status_code == 200
    assert resp.json() == []


async def test_security_alerts_no_dispatcher(client):
    resp = await client.get("/soc/v1/security/alerts")
    assert resp.json() == []


async def test_correlation_via_engine(client, state):
    state.soc_correlation = SimpleNamespace(
        get_summary=lambda: {"status": "ok", "risk_score": 5, "signals": []}
    )
    resp = await client.get("/soc/v1/security/correlation")
    assert resp.json() == {"status": "ok", "risk_score": 5, "signals": []}


async def test_correlation_fallback_builder(client, monkeypatch):
    import gateway.security.soc_correlation as corr_mod

    monkeypatch.setattr(
        corr_mod,
        "build_correlation_summary",
        lambda app: SimpleNamespace(to_dict=lambda: {"status": "fallback", "risk_score": 1}),
    )
    resp = await client.get("/soc/v1/security/correlation")
    assert resp.json()["status"] == "fallback"


async def test_correlation_unavailable_on_error(client, monkeypatch):
    import gateway.security.soc_correlation as corr_mod

    def _boom(app):
        raise RuntimeError("no signals")

    monkeypatch.setattr(corr_mod, "build_correlation_summary", _boom)
    resp = await client.get("/soc/v1/security/correlation")
    assert resp.json() == {"status": "unavailable", "risk_score": 0, "signals": []}


async def test_risk_via_engine_critical(client, state):
    state.soc_correlation = SimpleNamespace(get_risk_score=lambda: 75)
    resp = await client.get("/soc/v1/security/risk")
    data = resp.json()
    assert data["risk_score"] == 75
    assert data["level"] == "critical"
    assert "updated_at" in data


async def test_risk_fallback_builder(client, monkeypatch):
    import gateway.security.soc_correlation as corr_mod

    monkeypatch.setattr(
        corr_mod, "build_correlation_summary", lambda app: SimpleNamespace(risk_score=25)
    )
    resp = await client.get("/soc/v1/security/risk")
    assert resp.json()["risk_score"] == 25
    assert resp.json()["level"] == "medium"


async def test_risk_defaults_low_on_error(client, monkeypatch):
    import gateway.security.soc_correlation as corr_mod

    def _boom(app):
        raise RuntimeError("nope")

    monkeypatch.setattr(corr_mod, "build_correlation_summary", _boom)
    resp = await client.get("/soc/v1/security/risk")
    assert resp.json()["risk_score"] == 0
    assert resp.json()["level"] == "low"


async def test_risk_summary(client, monkeypatch):
    import gateway.security.soc_correlation as corr_mod

    summary = SimpleNamespace(
        risk_score=42,
        severity="high",
        operator_summary=["3 denied egress attempts"],
        per_user_risk=[{"user_id": "u1", "score": 10}],
        correlated_findings=[
            {"type": "generated_at", "timestamp": "2026-06-12T00:00:00Z"},
            {"type": "egress_denied", "count": 3},
        ],
    )
    monkeypatch.setattr(corr_mod, "build_correlation_summary", lambda app: summary)
    resp = await client.get("/soc/v1/security/risk/summary")
    data = resp.json()
    assert data["risk_score"] == 42
    assert data["severity"] == "high"
    assert data["generated_at"] == "2026-06-12T00:00:00Z"
    assert data["correlated_findings"] == [{"type": "egress_denied", "count": 3}]


async def test_risk_summary_fallback_on_error(client, monkeypatch):
    import gateway.security.soc_correlation as corr_mod

    def _boom(app):
        raise RuntimeError("no data")

    monkeypatch.setattr(corr_mod, "build_correlation_summary", _boom)
    resp = await client.get("/soc/v1/security/risk/summary")
    data = resp.json()
    assert data["risk_score"] == 0
    assert data["operator_summary"] == ["Risk summary unavailable"]


async def test_audit_export_cef(client, state):
    state.audit_exporter = SimpleNamespace(export=AsyncMock(return_value="cef-payload"))
    resp = await client.get("/soc/v1/security/audit/export", params={"format": "cef"})
    assert resp.status_code == 200
    assert resp.text == "cef-payload"
    assert resp.headers["content-type"].startswith("text/plain")
    assert 'filename="audit.cef"' in resp.headers["content-disposition"]


async def test_audit_export_json_dict_payload(client, state):
    state.audit_exporter = SimpleNamespace(export=AsyncMock(return_value={"records": [1, 2]}))
    resp = await client.get("/soc/v1/security/audit/export")
    assert resp.status_code == 200
    assert json.loads(resp.text) == {"records": [1, 2]}


async def test_audit_export_unavailable(client):
    resp = await client.get("/soc/v1/security/audit/export")
    assert resp.status_code == 503
    assert resp.json()["code"] == "UNAVAILABLE"


async def test_audit_export_exporter_raises(client, state):
    state.audit_exporter = SimpleNamespace(export=AsyncMock(side_effect=RuntimeError("disk")))
    resp = await client.get("/soc/v1/security/audit/export")
    assert resp.status_code == 503


async def test_audit_verify_chain_valid(client, state):
    state.pipeline = SimpleNamespace(verify_audit_chain=lambda: (True, "chain intact"))
    resp = await client.post("/soc/v1/security/audit/verify")
    assert resp.json() == {"valid": True, "message": "chain intact"}


async def test_audit_verify_chain_unavailable(client):
    resp = await client.post("/soc/v1/security/audit/verify")
    assert resp.json() == {"valid": False, "message": "Audit chain not available"}


async def test_audit_verify_chain_raises(client, state):
    def _boom():
        raise RuntimeError("hash mismatch read error")

    state.pipeline = SimpleNamespace(verify_audit_chain=_boom)
    resp = await client.post("/soc/v1/security/audit/verify")
    assert resp.json()["valid"] is False


# ---------------------------------------------------------------------------
# Egress endpoints
# ---------------------------------------------------------------------------


async def test_egress_pending_with_bot_filter(client, state):
    state.egress_approval_queue = SimpleNamespace(
        get_pending_requests=AsyncMock(
            return_value=[{"agent_id": "botA", "domain": "a.com"}, {"agent_id": "botB"}]
        )
    )
    resp = await client.get("/soc/v1/egress/pending")
    assert len(resp.json()) == 2
    filtered = await client.get("/soc/v1/egress/pending", params={"bot_id": "botA"})
    assert [r["agent_id"] for r in filtered.json()] == ["botA"]


async def test_egress_pending_non_list_and_missing(client, state):
    resp = await client.get("/soc/v1/egress/pending")
    assert resp.json() == []
    state.egress_approval_queue = SimpleNamespace(
        get_pending_requests=AsyncMock(return_value={"unexpected": "dict"})
    )
    resp = await client.get("/soc/v1/egress/pending")
    assert resp.json() == []


async def test_egress_pending_queue_raises(client, state):
    state.egress_approval_queue = SimpleNamespace(
        get_pending_requests=AsyncMock(side_effect=RuntimeError("db locked"))
    )
    resp = await client.get("/soc/v1/egress/pending")
    assert resp.json() == []


async def test_egress_rules_source_tagging(client, state):
    state.egress_approval_queue = SimpleNamespace(
        get_all_rules=AsyncMock(
            return_value={
                "permanent_rules": [
                    {"domain": "a.com", "action": "allow"},
                    {"domain": "b.com", "action": "deny"},
                ],
                "session_rules": [{"domain": "s.com"}],
            }
        ),
        _permanent_rules={"a.com": SimpleNamespace(source="preloaded")},
    )
    resp = await client.get("/soc/v1/egress/rules")
    data = resp.json()
    by_domain = {r["domain"]: r for r in data["permanent_rules"]}
    assert by_domain["a.com"]["source"] == "preloaded"
    assert by_domain["b.com"]["source"] == "user"
    assert data["session_rules"] == [{"domain": "s.com"}]


async def test_egress_rules_fallback_empty(client, state):
    resp = await client.get("/soc/v1/egress/rules")
    assert resp.json() == {"permanent_rules": [], "session_rules": []}
    state.egress_approval_queue = SimpleNamespace(
        get_all_rules=AsyncMock(side_effect=RuntimeError("boom")), _permanent_rules={}
    )
    resp = await client.get("/soc/v1/egress/rules")
    assert resp.json() == {"permanent_rules": [], "session_rules": []}


async def test_egress_log_filters_egress_events(client, state):
    state.audit_store = FakeAuditStore(_ENTRIES)
    resp = await client.get("/soc/v1/egress/log")
    events = resp.json()
    assert len(events) == 1
    assert events[0]["event_type"] == "egress_denied"
    filtered = await client.get("/soc/v1/egress/log", params={"bot_id": "nope"})
    assert filtered.json() == []


async def test_egress_approve_mode_mapping(client, state):
    from gateway.security.egress_approval import ApprovalMode

    approve = AsyncMock()
    state.egress_approval_queue = SimpleNamespace(approve=approve)
    resp = await client.post("/soc/v1/egress/r-1/approve", json={"mode": "permanent"})
    assert resp.json() == {
        "ok": True,
        "request_id": "r-1",
        "action": "approved",
        "mode": "permanent",
    }
    assert approve.await_args.kwargs["mode"] is ApprovalMode.PERMANENT

    resp = await client.post("/soc/v1/egress/r-2/approve", json={"mode": "4h"})
    assert resp.json()["ok"] is True
    assert approve.await_args.kwargs["mode"] is ApprovalMode.SESSION

    resp = await client.post("/soc/v1/egress/r-3/approve", json={"mode": "bogus"})
    assert approve.await_args.kwargs["mode"] is ApprovalMode.ONCE


async def test_egress_approve_missing_or_raises(client, state):
    resp = await client.post("/soc/v1/egress/r-1/approve", json={"mode": "once"})
    assert resp.json()["ok"] is False
    state.egress_approval_queue = SimpleNamespace(approve=AsyncMock(side_effect=KeyError("r-1")))
    resp = await client.post("/soc/v1/egress/r-1/approve", json={"mode": "once"})
    assert resp.json()["ok"] is False


async def test_egress_deny(client, state):
    deny = MagicMock()
    state.egress_approval_queue = SimpleNamespace(deny=deny)
    resp = await client.post("/soc/v1/egress/r-9/deny")
    assert resp.json() == {"ok": True, "request_id": "r-9", "action": "denied"}
    assert deny.call_args.kwargs["decided_by"] == "owner-1"


async def test_egress_deny_missing_queue(client):
    resp = await client.post("/soc/v1/egress/r-9/deny")
    assert resp.json()["ok"] is False


async def test_egress_rule_override_scoped(client, state):
    add_rule = AsyncMock(return_value=True)
    state.egress_approval_queue = SimpleNamespace(add_rule=add_rule)
    resp = await client.post(
        "/soc/v1/egress/rules/override",
        json={
            "domain": "evil.example",
            "action": "deny",
            "mode": "session",
            "scope": {"kind": "user", "user_ids": ["u1"], "group_ids": []},
        },
    )
    data = resp.json()
    assert data["ok"] is True
    assert data["scope"]["kind"] == "user"
    assert add_rule.await_count == 1

    # Default (no scope) → "all"
    resp = await client.post(
        "/soc/v1/egress/rules/override", json={"domain": "ok.example", "action": "allow"}
    )
    assert resp.json()["scope"]["kind"] == "all"
    assert resp.json()["mode"] == "permanent"


async def test_egress_rule_override_no_queue(client):
    resp = await client.post(
        "/soc/v1/egress/rules/override", json={"domain": "x.com", "action": "deny"}
    )
    assert resp.json() == {"ok": False, "error": "Egress approval queue not available"}


async def test_egress_rule_remove(client, state):
    state.egress_approval_queue = SimpleNamespace(remove_rule=AsyncMock(return_value=True))
    resp = await client.delete("/soc/v1/egress/rules/x.com")
    assert resp.json() == {"ok": True, "domain": "x.com", "action": "removed"}


async def test_egress_rule_remove_no_queue(client):
    resp = await client.delete("/soc/v1/egress/rules/x.com")
    assert resp.json()["ok"] is False


async def test_egress_history_with_bot_filter(client, state):
    state.egress_approval_queue = SimpleNamespace(
        get_decision_log=AsyncMock(
            return_value=[{"agent_id": "botA", "id": "1"}, {"agent_id": "botB", "id": "2"}]
        )
    )
    resp = await client.get("/soc/v1/egress/history")
    assert len(resp.json()) == 2
    filtered = await client.get("/soc/v1/egress/history", params={"bot_id": "botB"})
    assert [d["id"] for d in filtered.json()] == ["2"]


async def test_egress_history_no_queue(client):
    resp = await client.get("/soc/v1/egress/history")
    assert resp.json() == []


async def test_egress_history_revoke(client, state):
    state.egress_approval_queue = SimpleNamespace(revoke_decision=AsyncMock(return_value=True))
    resp = await client.post("/soc/v1/egress/history/e-1/revoke")
    assert resp.json() == {"ok": True, "entry_id": "e-1"}


async def test_egress_history_revoke_no_queue(client):
    resp = await client.post("/soc/v1/egress/history/e-1/revoke")
    assert resp.json()["ok"] is False


async def test_emergency_block_requires_confirmation(client):
    resp = await client.post("/soc/v1/egress/emergency-block", json={"confirm": False})
    assert resp.status_code == 409
    body = resp.json()
    assert body["action"] == "block egress"
    assert body["target"] == "all"


async def test_emergency_block_confirmed(client, state):
    ef = MagicMock()
    state.egress_filter = ef
    resp = await client.post(
        "/soc/v1/egress/emergency-block", json={"confirm": True, "reason": "incident-7"}
    )
    assert resp.json() == {"ok": True, "action": "emergency_block", "reason": "incident-7"}
    ef.emergency_block.assert_called_once_with(reason="incident-7")


async def test_emergency_block_filter_raises_still_ok(client, state):
    state.egress_filter = SimpleNamespace(
        emergency_block=MagicMock(side_effect=RuntimeError("fail"))
    )
    resp = await client.post("/soc/v1/egress/emergency-block", json={"confirm": True})
    assert resp.json()["ok"] is True


# ---------------------------------------------------------------------------
# Service endpoints
# ---------------------------------------------------------------------------


async def test_list_services_and_bot_filter(client, state, monkeypatch):
    svcs = [_Svc("agentshroud-openclaw"), _Svc("agentshroud-gateway", image="gw-img")]
    monkeypatch.setattr("gateway.soc.services.ServiceManager", _make_service_manager(svcs))
    resp = await client.get("/soc/v1/services")
    assert len(resp.json()) == 2

    # bot filter — match by hostname substring
    state.config = SimpleNamespace(
        bots={"openclaw": SimpleNamespace(hostname="agentshroud-openclaw", image="")}
    )
    resp = await client.get("/soc/v1/services", params={"bot_id": "openclaw"})
    assert [s["name"] for s in resp.json()] == ["agentshroud-openclaw"]

    # unknown bot → unfiltered
    resp = await client.get("/soc/v1/services", params={"bot_id": "ghost"})
    assert len(resp.json()) == 2


async def test_service_logs(client, monkeypatch):
    monkeypatch.setattr(
        "gateway.soc.services.ServiceManager", _make_service_manager(logs=["a", "b"])
    )
    resp = await client.get("/soc/v1/services/gw/logs", params={"tail": 2})
    assert resp.json() == {"service": "gw", "lines": ["a", "b"]}


async def test_service_start(client, monkeypatch):
    monkeypatch.setattr(
        "gateway.soc.services.ServiceManager", _make_service_manager(results={"start": True})
    )
    resp = await client.post("/soc/v1/services/gw/start")
    assert resp.json() == {"ok": True, "service": "gw", "action": "start"}


async def test_service_stop_confirmation_then_stop(client, monkeypatch):
    monkeypatch.setattr(
        "gateway.soc.services.ServiceManager", _make_service_manager(results={"stop": False})
    )
    resp = await client.post("/soc/v1/services/gw/stop", json={"confirm": False})
    assert resp.status_code == 409
    resp = await client.post("/soc/v1/services/gw/stop", json={"confirm": True})
    assert resp.json() == {"ok": False, "service": "gw", "action": "stop"}


async def test_service_restart(client, monkeypatch):
    monkeypatch.setattr(
        "gateway.soc.services.ServiceManager", _make_service_manager(results={"restart": True})
    )
    resp = await client.post("/soc/v1/services/gw/restart", json={"confirm": False})
    assert resp.status_code == 409
    resp = await client.post("/soc/v1/services/gw/restart", json={"confirm": True})
    assert resp.json()["ok"] is True


async def test_service_update(client, monkeypatch):
    monkeypatch.setattr(
        "gateway.soc.services.ServiceManager", _make_service_manager(results={"update": True})
    )
    resp = await client.post("/soc/v1/services/gw/update", json={"confirm": False})
    assert resp.status_code == 409
    resp = await client.post("/soc/v1/services/gw/update", json={"confirm": True})
    assert resp.json()["action"] == "update"


async def test_services_rebuild(client):
    resp = await client.post("/soc/v1/services/rebuild", json={"confirm": False})
    assert resp.status_code == 409
    resp = await client.post("/soc/v1/services/rebuild", json={"confirm": True})
    assert resp.json()["ok"] is True
    assert resp.json()["action"] == "rebuild"


# ---------------------------------------------------------------------------
# Kill switch endpoints
# ---------------------------------------------------------------------------


async def test_killswitch_freeze(client, state):
    resp = await client.post("/soc/v1/killswitch/freeze", json={"confirm": False})
    assert resp.status_code == 409
    monitor = MagicMock()
    state.killswitch_monitor = monitor
    resp = await client.post("/soc/v1/killswitch/freeze", json={"confirm": True})
    assert resp.json() == {"ok": True, "action": "freeze"}
    monitor.trigger_freeze.assert_called_once()


async def test_killswitch_shutdown(client, state):
    resp = await client.post("/soc/v1/killswitch/shutdown", json={"confirm": False})
    assert resp.status_code == 409
    monitor = MagicMock()
    state.killswitch_monitor = monitor
    resp = await client.post("/soc/v1/killswitch/shutdown", json={"confirm": True})
    assert resp.json() == {"ok": True, "action": "shutdown"}
    monitor.trigger_shutdown.assert_called_once()


async def test_killswitch_disconnect_owner_gate(client, holder, state):
    holder["caller"] = NON_OWNER
    resp = await client.post("/soc/v1/killswitch/disconnect", json={"confirm": True, "force": True})
    assert resp.status_code == 403

    holder["caller"] = OWNER
    resp = await client.post(
        "/soc/v1/killswitch/disconnect", json={"confirm": True, "force": False}
    )
    assert resp.status_code == 409

    monitor = MagicMock()
    state.killswitch_monitor = monitor
    resp = await client.post("/soc/v1/killswitch/disconnect", json={"confirm": True, "force": True})
    assert resp.json() == {"ok": True, "action": "disconnect"}
    monitor.trigger_disconnect.assert_called_once()


# ---------------------------------------------------------------------------
# Contributor / user management
# ---------------------------------------------------------------------------


def _fake_contributor_manager(record):
    class _Mgr:
        def __init__(self, rbac_config=None, teams_config=None, activity_tracker=None):
            pass

        def list_contributors(self):
            return [record] if record else []

        def get_contributor(self, user_id):
            return record

    return _Mgr


async def test_list_users(client, monkeypatch):
    rec = SimpleNamespace(model_dump=lambda: {"user_id": "u1", "role": "collaborator"})
    monkeypatch.setattr(
        "gateway.soc.contributors.ContributorManager", _fake_contributor_manager(rec)
    )
    resp = await client.get("/soc/v1/users")
    assert resp.json() == [{"user_id": "u1", "role": "collaborator"}]


async def test_get_user_found_and_missing(client, monkeypatch):
    rec = SimpleNamespace(model_dump=lambda: {"user_id": "u1"})
    monkeypatch.setattr(
        "gateway.soc.contributors.ContributorManager", _fake_contributor_manager(rec)
    )
    resp = await client.get("/soc/v1/users/u1")
    assert resp.json() == {"user_id": "u1"}

    monkeypatch.setattr(
        "gateway.soc.contributors.ContributorManager", _fake_contributor_manager(None)
    )
    resp = await client.get("/soc/v1/users/ghost")
    assert resp.status_code == 404


async def test_update_display_name(client, holder):
    holder["caller"] = NON_OWNER
    resp = await client.put("/soc/v1/users/u1/display-name", json={"display_name": "Al"})
    assert resp.status_code == 403
    holder["caller"] = OWNER
    resp = await client.put("/soc/v1/users/u1/display-name", json={"display_name": "Al"})
    assert resp.json()["ok"] is True
    assert resp.json()["display_name"] == "Al"


async def test_add_collaborator(client, holder, monkeypatch):
    persisted = []
    monkeypatch.setattr(
        "gateway.security.rbac_config.persist_approved_collaborator", persisted.append
    )
    holder["caller"] = NON_OWNER
    resp = await client.post("/soc/v1/users/collaborator", json={"user_id": "777"})
    assert resp.status_code == 403
    assert persisted == []

    holder["caller"] = OWNER
    resp = await client.post("/soc/v1/users/collaborator", json={"user_id": "777"})
    assert resp.json() == {"ok": True, "user_id": "777", "action": "added"}
    assert persisted == ["777"]


async def test_revoke_collaborator(client, holder):
    holder["caller"] = NON_OWNER
    resp = await client.delete("/soc/v1/users/777/collaborator")
    assert resp.status_code == 403
    holder["caller"] = OWNER
    resp = await client.delete("/soc/v1/users/777/collaborator")
    assert resp.json()["action"] == "revoked"


_ACTIVITY = [
    {
        "timestamp": 3.0,
        "user_id": "u1",
        "username": "alice",
        "source": "telegram:openclaw",
        "is_owner": False,
        "direction": "inbound",
        "message_preview": "hi",
        "correlation_id": "c1",
    },
    {
        "timestamp": 4.0,
        "user_id": "u1",
        "username": "alice",
        "source": "telegram:openclaw",
        "is_owner": False,
        "direction": "outbound",
        "message_preview": "hello back",
        "correlation_id": "c1",
    },
    {
        "timestamp": 5.0,
        "user_id": "u2",
        "username": "bob",
        "source": "telegram:hermes",
        "is_owner": True,
        "direction": "inbound",
        "message_preview": "status?",
    },
    {
        "timestamp": 6.0,
        "user_id": "u2",
        "username": "bob",
        "source": "telegram:hermes",
        "is_owner": True,
        "direction": "outbound",
        "message_preview": "all green",
        "correlation_id": "c2",
    },
]


async def test_collaborator_activity_no_tracker(client):
    resp = await client.get("/soc/v1/collaborators/activity")
    data = resp.json()
    assert data["tracker_available"] is False
    assert data["entries"] == []


async def test_collaborator_activity_pairing(client, state):
    state.collaborator_tracker = SimpleNamespace(
        get_activity=lambda since=0.0, limit=0: list(_ACTIVITY)
    )
    resp = await client.get("/soc/v1/collaborators/activity")
    data = resp.json()
    assert data["total"] == 4
    assert data["total_unfiltered"] == 4
    paired = data["paired_entries"]
    # 2 correlation pairs + 1 unpaired = 3, sorted newest first
    assert len(paired) == 3
    assert paired[0]["correlation_id"] == "c2"
    assert paired[0]["response_preview"] == "all green"
    assert paired[0]["query_preview"] is None
    pair_c1 = next(p for p in paired if p["correlation_id"] == "c1")
    assert pair_c1["query_preview"] == "hi"
    assert pair_c1["response_preview"] == "hello back"
    unpaired = next(p for p in paired if p["correlation_id"] is None)
    assert unpaired["query_preview"] == "status?"


async def test_collaborator_activity_filters(client, state):
    state.collaborator_tracker = SimpleNamespace(
        get_activity=lambda since=0.0, limit=0: list(_ACTIVITY)
    )
    by_user = await client.get("/soc/v1/collaborators/activity", params={"user_id": "u1"})
    assert by_user.json()["total"] == 2

    inbound = await client.get("/soc/v1/collaborators/activity", params={"direction": "inbound"})
    assert inbound.json()["total"] == 2

    owners = await client.get("/soc/v1/collaborators/activity", params={"is_owner": "true"})
    assert owners.json()["total"] == 2

    search = await client.get("/soc/v1/collaborators/activity", params={"search": "bob"})
    assert search.json()["total"] == 2

    bots = await client.get("/soc/v1/collaborators/activity", params={"bot_id": "hermes"})
    assert bots.json()["total"] == 2
    assert bots.json()["total_unfiltered"] == 4

    page = await client.get("/soc/v1/collaborators/activity", params={"offset": 1, "limit": 1})
    assert len(page.json()["entries"]) == 1
    assert len(page.json()["paired_entries"]) == 1


async def test_set_user_role_invalid(client):
    resp = await client.put("/soc/v1/users/777/role", json={"role": "supreme-leader"})
    assert resp.status_code == 400
    assert resp.json()["detail"]["code"] == "VALIDATION_ERROR"


async def test_set_user_role_non_owner_denied(client, holder):
    # caller user_id 55555 is a viewer in RBACConfig → SET_ROLE denied
    holder["caller"] = FakeCaller(user_id="55555", owner=False)
    resp = await client.put("/soc/v1/users/777/role", json={"role": "admin"})
    assert resp.status_code == 403
    assert resp.json()["detail"]["code"] == "PERMISSION_DENIED"


async def test_set_user_role_owner_success(client, holder, monkeypatch):
    monkeypatch.setenv("AGENTSHROUD_OWNER_USER_ID", "990001122")
    holder["caller"] = FakeCaller(user_id="990001122")
    resp = await client.put("/soc/v1/users/777/role", json={"role": "admin"})
    assert resp.json() == {"ok": True, "user_id": "777", "role": "admin"}


async def test_set_user_collab_mode(client, state, monkeypatch):
    calls = []
    monkeypatch.setattr(
        "gateway.security.group_config.persist_user_collab_mode",
        lambda uid, mode: calls.append((uid, mode)),
    )
    resp = await client.put("/soc/v1/users/777/mode", json={"mode": "yolo"})
    assert resp.status_code == 400

    teams = SimpleNamespace(user_overrides={})
    state.config = SimpleNamespace(teams=teams)
    resp = await client.put("/soc/v1/users/777/mode", json={"mode": "full_access"})
    assert resp.json() == {"ok": True, "user_id": "777", "mode": "full_access"}
    assert teams.user_overrides["777"]["collab_mode"] == "full_access"
    assert calls == [("777", "full_access")]


# ---------------------------------------------------------------------------
# Groups
# ---------------------------------------------------------------------------


async def test_list_groups_empty_and_populated(client, state):
    resp = await client.get("/soc/v1/groups")
    assert resp.json() == []
    state.config = SimpleNamespace(teams=SimpleNamespace(groups={"g1": FakeGroup(name="Ops")}))
    resp = await client.get("/soc/v1/groups")
    assert resp.json()[0]["id"] == "g1"
    assert resp.json()[0]["name"] == "Ops"


async def test_get_group(client, state):
    resp = await client.get("/soc/v1/groups/g1")
    assert resp.status_code == 404
    state.config = SimpleNamespace(teams=SimpleNamespace(groups={"g1": FakeGroup(name="Ops")}))
    resp = await client.get("/soc/v1/groups/g1")
    assert resp.json()["id"] == "g1"


async def test_create_group_paths(client, holder, state, monkeypatch):
    created = []
    monkeypatch.setattr(
        "gateway.security.group_config.persist_group_create",
        lambda *a: created.append(a),
    )
    holder["caller"] = NON_OWNER
    resp = await client.post("/soc/v1/groups", json={"group_id": "g2", "name": "Eng"})
    assert resp.status_code == 403

    holder["caller"] = OWNER
    # teams config unavailable
    resp = await client.post("/soc/v1/groups", json={"group_id": "g2", "name": "Eng"})
    assert resp.status_code == 503

    teams = SimpleNamespace(groups={"g1": FakeGroup()})
    state.config = SimpleNamespace(teams=teams)
    # conflict
    resp = await client.post("/soc/v1/groups", json={"group_id": "g1", "name": "Dup"})
    assert resp.status_code == 409

    # success
    resp = await client.post(
        "/soc/v1/groups",
        json={"group_id": "g2", "name": "Eng", "members": ["u1"], "collab_mode": "full_access"},
    )
    data = resp.json()
    assert data["ok"] is True
    assert "g2" in teams.groups
    assert teams.groups["g2"].members == ["u1"]
    assert created[0][0] == "g2"


async def test_delete_group_paths(client, holder, state, monkeypatch):
    deleted = []
    monkeypatch.setattr("gateway.security.group_config.persist_group_delete", deleted.append)
    holder["caller"] = NON_OWNER
    resp = await client.delete("/soc/v1/groups/g1")
    assert resp.status_code == 403

    holder["caller"] = OWNER
    resp = await client.delete("/soc/v1/groups/g1")
    assert resp.status_code == 404

    teams = SimpleNamespace(groups={"g1": FakeGroup()})
    state.config = SimpleNamespace(teams=teams)
    resp = await client.delete("/soc/v1/groups/g1")
    assert resp.json()["action"] == "deleted"
    assert teams.groups == {}
    assert deleted == ["g1"]


async def test_add_group_member_paths(client, holder, state, monkeypatch):
    added = []
    monkeypatch.setattr(
        "gateway.security.group_config.persist_group_member_add",
        lambda gid, uid: added.append((gid, uid)),
    )
    holder["caller"] = NON_OWNER
    resp = await client.post("/soc/v1/groups/g1/members", json={"user_id": "u9"})
    assert resp.status_code == 403

    # group admin (non-owner) allowed
    holder["caller"] = FakeCaller(user_id="adm", owner=False, group_admin=True)
    resp = await client.post("/soc/v1/groups/g1/members", json={"user_id": "u9"})
    assert resp.status_code == 404  # passes auth gate, group missing

    group = FakeGroup(members=["u9"])
    state.config = SimpleNamespace(teams=SimpleNamespace(groups={"g1": group}))
    resp = await client.post("/soc/v1/groups/g1/members", json={"user_id": "u9"})
    assert resp.json()["action"] == "added"
    assert group.members == ["u9"]  # no duplicate appended

    resp = await client.post("/soc/v1/groups/g1/members", json={"user_id": "u10"})
    assert group.members == ["u9", "u10"]
    assert ("g1", "u10") in added


async def test_remove_group_member_paths(client, holder, state, monkeypatch):
    removed = []
    monkeypatch.setattr(
        "gateway.security.group_config.persist_group_member_remove",
        lambda gid, uid: removed.append((gid, uid)),
    )
    holder["caller"] = NON_OWNER
    resp = await client.delete("/soc/v1/groups/g1/members/u9")
    assert resp.status_code == 403

    holder["caller"] = OWNER
    resp = await client.delete("/soc/v1/groups/g1/members/u9")
    assert resp.status_code == 404

    group = FakeGroup(members=["u9"])
    state.config = SimpleNamespace(teams=SimpleNamespace(groups={"g1": group}))
    resp = await client.delete("/soc/v1/groups/g1/members/u9")
    assert resp.json()["action"] == "removed"
    assert group.members == []
    assert removed == [("g1", "u9")]


async def test_rename_group_paths(client, holder, state):
    holder["caller"] = NON_OWNER
    resp = await client.put("/soc/v1/groups/g1/name", json={"name": "X"})
    assert resp.status_code == 403

    holder["caller"] = OWNER
    resp = await client.put("/soc/v1/groups/g1/name", json={"name": "   "})
    assert resp.status_code == 400

    resp = await client.put("/soc/v1/groups/g1/name", json={"name": "X"})
    assert resp.status_code == 404

    group = FakeGroup(name="Old")
    state.config = SimpleNamespace(teams=SimpleNamespace(groups={"g1": group}))
    resp = await client.put("/soc/v1/groups/g1/name", json={"name": "New"})
    assert resp.json() == {"ok": True, "group_id": "g1", "name": "New"}
    assert group.name == "New"


async def test_set_group_mode_paths(client, holder, state, monkeypatch):
    calls = []
    monkeypatch.setattr(
        "gateway.security.group_config.persist_group_collab_mode",
        lambda gid, mode: calls.append((gid, mode)),
    )
    holder["caller"] = NON_OWNER
    resp = await client.put("/soc/v1/groups/g1/mode", json={"collab_mode": "full_access"})
    assert resp.status_code == 403

    holder["caller"] = OWNER
    resp = await client.put("/soc/v1/groups/g1/mode", json={"collab_mode": "bogus"})
    assert resp.status_code == 400

    resp = await client.put("/soc/v1/groups/g1/mode", json={"collab_mode": "full_access"})
    assert resp.status_code == 404

    group = FakeGroup()
    state.config = SimpleNamespace(teams=SimpleNamespace(groups={"g1": group}))
    resp = await client.put("/soc/v1/groups/g1/mode", json={"collab_mode": "full_access"})
    assert resp.json()["collab_mode"] == "full_access"
    assert group.collab_mode == "full_access"
    assert calls == [("g1", "full_access")]


# ---------------------------------------------------------------------------
# Delegation
# ---------------------------------------------------------------------------


async def test_list_delegations(client, state):
    resp = await client.get("/soc/v1/delegation")
    assert resp.json() == []
    mgr = MagicMock()
    mgr.get_active_delegations.return_value = [SimpleNamespace(to_dict=lambda: {"id": "d1"})]
    state.delegation_manager = mgr
    resp = await client.get("/soc/v1/delegation")
    assert resp.json() == [{"id": "d1"}]
    mgr.cleanup_expired.assert_called_once()


async def test_create_delegation_paths(client, holder, state):
    holder["caller"] = NON_OWNER
    resp = await client.post("/soc/v1/delegation", json={"delegatee_id": "u1"})
    assert resp.status_code == 403

    holder["caller"] = OWNER
    resp = await client.post("/soc/v1/delegation", json={"delegatee_id": "u1"})
    assert resp.status_code == 503

    mgr = MagicMock()
    mgr.delegate.return_value = SimpleNamespace(
        to_dict=lambda: {"delegatee_id": "u1", "privilege": "egress_approval"}
    )
    state.delegation_manager = mgr
    resp = await client.post(
        "/soc/v1/delegation", json={"delegatee_id": "u1", "privilege": "not-a-privilege"}
    )
    assert resp.status_code == 400

    resp = await client.post(
        "/soc/v1/delegation",
        json={"delegatee_id": "u1", "privilege": "egress_approval", "duration_hours": 2.0},
    )
    assert resp.json()["delegatee_id"] == "u1"
    assert mgr.delegate.call_args.kwargs["duration_hours"] == 2.0


async def test_revoke_delegation_paths(client, holder, state):
    holder["caller"] = NON_OWNER
    resp = await client.delete("/soc/v1/delegation/u1")
    assert resp.status_code == 403

    holder["caller"] = OWNER
    resp = await client.delete("/soc/v1/delegation/u1")
    assert resp.status_code == 503

    mgr = MagicMock()
    mgr.revoke.return_value = True
    mgr.revoke_all_for_user.return_value = 2
    state.delegation_manager = mgr

    resp = await client.delete("/soc/v1/delegation/u1", params={"privilege": "bogus"})
    assert resp.status_code == 400

    resp = await client.delete("/soc/v1/delegation/u1", params={"privilege": "egress_approval"})
    assert resp.json() == {"ok": True, "delegatee_id": "u1", "revoked_count": 1}

    mgr.revoke.return_value = False
    resp = await client.delete("/soc/v1/delegation/u1", params={"privilege": "egress_approval"})
    assert resp.json()["ok"] is False

    resp = await client.delete("/soc/v1/delegation/u1")
    assert resp.json() == {"ok": True, "delegatee_id": "u1", "revoked_count": 2}


# ---------------------------------------------------------------------------
# Tool ACL / shared memory / privacy
# ---------------------------------------------------------------------------


async def test_tool_acl(client, state):
    resp = await client.get("/soc/v1/tool-acl/u1")
    assert resp.json()["note"] == "ToolACLEnforcer not initialized"
    state.tool_acl_enforcer = SimpleNamespace(
        get_allowed_tools=lambda eid: ["web_fetch"],
        get_denied_tools=lambda eid: ["shell"],
    )
    resp = await client.get("/soc/v1/tool-acl/u1")
    assert resp.json() == {"entity_id": "u1", "allowed": ["web_fetch"], "denied": ["shell"]}


async def test_group_memory_read(client, state, monkeypatch):
    resp = await client.get("/soc/v1/shared-memory/groups/g1")
    assert resp.json()["note"] == "SessionManager not initialized"

    class FakeSMM:
        def __init__(self, sm):
            pass

        def get_group_memory(self, gid):
            return "shared notes"

    state.session_manager = object()
    monkeypatch.setattr("gateway.security.shared_memory.SharedMemoryManager", FakeSMM)
    resp = await client.get("/soc/v1/shared-memory/groups/g1")
    assert resp.json() == {"group_id": "g1", "memory": "shared notes", "length": 12}


async def test_group_memory_clear(client, holder, state, tmp_path):
    holder["caller"] = NON_OWNER
    resp = await client.delete("/soc/v1/shared-memory/groups/g1")
    assert resp.status_code == 403

    holder["caller"] = OWNER
    resp = await client.delete("/soc/v1/shared-memory/groups/g1")
    assert resp.json()["ok"] is False

    mem_file = tmp_path / "memory.md"
    mem_file.write_text("old content", encoding="utf-8")
    state.session_manager = SimpleNamespace(
        get_or_create_group_session=lambda gid: SimpleNamespace(memory_file=mem_file)
    )
    resp = await client.delete("/soc/v1/shared-memory/groups/g1")
    assert resp.json() == {"ok": True, "group_id": "g1"}
    assert mem_file.read_text(encoding="utf-8") == ""


async def test_group_memory_clear_error(client, state):
    def _boom(gid):
        raise RuntimeError("fs error")

    state.session_manager = SimpleNamespace(get_or_create_group_session=_boom)
    resp = await client.delete("/soc/v1/shared-memory/groups/g1")
    assert resp.status_code == 500
    assert resp.json()["detail"]["code"] == "INTERNAL_ERROR"


async def test_privacy_policies(client, state):
    resp = await client.get("/soc/v1/privacy")
    assert resp.json()["note"] == "PrivacyPolicyEnforcer not initialized"

    state.privacy_enforcer = SimpleNamespace(
        _policy=SimpleNamespace(
            audit_access_attempts=True,
            alert_on_private_access=False,
            services={
                "gmail": SimpleNamespace(
                    privacy=SimpleNamespace(value="private"),
                    allowed_groups=["ops"],
                    description="mail",
                )
            },
        )
    )
    resp = await client.get("/soc/v1/privacy")
    data = resp.json()
    assert data["audit_access_attempts"] is True
    assert data["services"]["gmail"]["privacy"] == "private"
    assert data["services"]["gmail"]["allowed_groups"] == ["ops"]


# ---------------------------------------------------------------------------
# Approvals
# ---------------------------------------------------------------------------


async def test_approvals_pending(client, state):
    resp = await client.get("/soc/v1/approvals/pending")
    assert resp.json() == []
    state.approval_queue = SimpleNamespace(
        get_pending_items=lambda: [{"id": "a1"}, SimpleNamespace(id="a2")]
    )
    resp = await client.get("/soc/v1/approvals/pending")
    assert resp.json() == [{"id": "a1"}, {"id": "a2"}]


async def test_approvals_approve_and_deny(client, state):
    aq = SimpleNamespace(approve=AsyncMock(), deny=AsyncMock())
    state.approval_queue = aq
    resp = await client.post("/soc/v1/approvals/a1/approve", json={"reason": ""})
    assert resp.json() == {"ok": True, "approval_id": "a1", "action": "approved"}
    assert aq.approve.await_args.kwargs["approver"] == "owner-1"

    resp = await client.post("/soc/v1/approvals/a1/deny", json={"reason": "nope"})
    assert resp.json() == {"ok": True, "approval_id": "a1", "action": "denied"}
    assert aq.deny.await_args.kwargs["reason"] == "nope"


async def test_approvals_missing_queue(client):
    resp = await client.post("/soc/v1/approvals/a1/approve", json={"reason": ""})
    assert resp.json()["ok"] is False
    resp = await client.post("/soc/v1/approvals/a1/deny", json={"reason": ""})
    assert resp.json()["ok"] is False


async def test_approvals_approve_raises(client, state):
    state.approval_queue = SimpleNamespace(approve=AsyncMock(side_effect=KeyError("a1")))
    resp = await client.post("/soc/v1/approvals/a1/approve", json={"reason": ""})
    assert resp.json()["ok"] is False


# ---------------------------------------------------------------------------
# Observability / modules / config
# ---------------------------------------------------------------------------


async def test_health_healthy_and_degraded(client, monkeypatch):
    monkeypatch.setattr(
        "gateway.soc.services.ServiceManager",
        _make_service_manager([_Svc("gw", status="running"), _Svc("bot", status="standby")]),
    )
    resp = await client.get("/soc/v1/health")
    assert resp.json()["status"] == "healthy"

    monkeypatch.setattr(
        "gateway.soc.services.ServiceManager",
        _make_service_manager([_Svc("gw", status="stopped", health="unhealthy")]),
    )
    resp = await client.get("/soc/v1/health")
    data = resp.json()
    assert data["status"] == "degraded"
    assert data["services"][0]["health"] == "unhealthy"


async def test_get_modules_unavailable(client):
    resp = await client.get("/soc/v1/modules")
    mods = resp.json()
    assert len(mods) == 10
    assert all(m["available"] is False for m in mods)
    assert all(m["mode"] == "enforce" for m in mods)
    assert mods[0]["description"]


async def test_get_modules_modes(client, state):
    state.sanitizer = SimpleNamespace(config=SimpleNamespace(mode="monitor"))
    state.prompt_guard = SimpleNamespace(mode="disabled")
    resp = await client.get("/soc/v1/security/modules")
    by_name = {m["name"]: m for m in resp.json()}
    assert by_name["sanitizer"] == {
        "name": "sanitizer",
        "available": True,
        "mode": "monitor",
        "description": soc_router._MODULE_DESCRIPTIONS["sanitizer"],
    }
    assert by_name["prompt_guard"]["mode"] == "disabled"


async def test_llm_failover_stats(client, state):
    resp = await client.get("/soc/v1/llm/failover")
    assert resp.json() == {"available": False, "succeeded": 0, "failed": 0, "active": False}

    state.llm_proxy = SimpleNamespace(
        get_stats=lambda: {
            "failover_quota_succeeded": 3,
            "failover_quota_failed": 1,
            "failover_active": True,
            "failover_last_provider": "ollama",
            "failover_last_event": "quota",
        },
        _get_local_model=lambda: "qwen3:14b",
    )
    resp = await client.get("/soc/v1/llm/failover")
    data = resp.json()
    assert data["available"] is True
    assert data["succeeded"] == 3
    assert data["local_model"] == "qwen3:14b"


async def test_set_module_mode_paths(client, state):
    resp = await client.put("/soc/v1/security/modules/sanitizer/mode", json={"mode": "yolo"})
    assert resp.status_code == 400

    resp = await client.put("/soc/v1/security/modules/sanitizer/mode", json={"mode": "monitor"})
    assert resp.status_code == 404

    cfg = SimpleNamespace(mode="enforce")
    state.sanitizer = SimpleNamespace(config=cfg)
    resp = await client.put("/soc/v1/security/modules/sanitizer/mode", json={"mode": "monitor"})
    assert resp.json() == {"ok": True, "name": "sanitizer", "mode": "monitor"}
    assert cfg.mode == "monitor"

    obj = SimpleNamespace(mode="enforce")
    state.egress_filter = obj
    resp = await client.put(
        "/soc/v1/security/modules/egress_filter/mode", json={"mode": "disabled"}
    )
    assert resp.json()["ok"] is True
    assert obj.mode == "disabled"

    state.mcp_proxy = object()  # no config, no mode attribute
    resp = await client.put("/soc/v1/security/modules/mcp_proxy/mode", json={"mode": "monitor"})
    assert resp.status_code == 400
    assert resp.json()["detail"]["code"] == "NOT_SUPPORTED"


async def test_list_bots_default_and_configured(client, state):
    resp = await client.get("/soc/v1/bots")
    assert resp.json() == [
        {"id": "openclaw", "name": "OpenClaw", "hostname": "agentshroud-openclaw", "default": True}
    ]
    state.config = SimpleNamespace(
        bots={
            "hermes": SimpleNamespace(name="Hermes", hostname="agentshroud-hermes", default=False)
        }
    )
    resp = await client.get("/soc/v1/bots")
    assert resp.json() == [
        {"id": "hermes", "name": "Hermes", "hostname": "agentshroud-hermes", "default": False}
    ]


async def test_get_config_variants(client, state):
    resp = await client.get("/soc/v1/config")
    assert resp.json() == {}

    state.config = SimpleNamespace(
        bind="0.0.0.0",
        port=8080,
        log_level="INFO",
        bots={
            "hermes": SimpleNamespace(
                name="Hermes",
                hostname="agentshroud-hermes",
                port=8642,
                image="img:1",
                egress_domains=["x.com"],
            )
        },
        teams=None,
    )
    resp = await client.get("/soc/v1/config")
    data = resp.json()
    assert data["port"] == 8080
    assert data["bots"]["hermes"]["hostname"] == "agentshroud-hermes"
    assert data["teams_enabled"] is False

    resp = await client.get("/soc/v1/config", params={"bot_id": "ghost"})
    assert resp.json() == {"error": "bot not found: ghost"}

    resp = await client.get("/soc/v1/config", params={"bot_id": "hermes"})
    assert resp.json()["image"] == "img:1"
    assert resp.json()["egress_domains"] == ["x.com"]


async def test_set_log_level(client):
    resp = await client.put("/soc/v1/config/log-level", json={"level": "verbose"})
    assert resp.status_code == 400

    root = logging.getLogger()
    shroud = logging.getLogger("agentshroud")
    orig_root, orig_shroud = root.level, shroud.level
    try:
        resp = await client.put("/soc/v1/config/log-level", json={"level": "warning"})
        assert resp.json() == {"ok": True, "level": "WARNING"}
        assert root.level == logging.WARNING
        assert shroud.level == logging.WARNING
    finally:
        root.setLevel(orig_root)
        shroud.setLevel(orig_shroud)


async def test_config_integrity_acknowledge(client, holder, state):
    holder["caller"] = NON_OWNER
    resp = await client.post("/soc/v1/config-integrity/acknowledge")
    assert resp.status_code == 403

    holder["caller"] = OWNER
    resp = await client.post("/soc/v1/config-integrity/acknowledge")
    assert resp.json()["status"] == "skipped"

    monitor = MagicMock()
    state.config_integrity = monitor
    resp = await client.post("/soc/v1/config-integrity/acknowledge")
    assert resp.json()["status"] == "ok"
    monitor.reset_baseline.assert_called_once()


# ---------------------------------------------------------------------------
# Scanners / scans / scorecard / SBOM / CVE
# ---------------------------------------------------------------------------


async def test_run_scanner_validation_and_launch(client, monkeypatch):
    resp = await client.post("/soc/v1/scan/nmap")
    assert resp.status_code == 400

    launch = AsyncMock()
    monkeypatch.setattr(soc_router, "_launch_scan_background", launch)
    resp = await client.post("/soc/v1/scan/trivy")
    assert resp.json()["ok"] is True
    assert resp.json()["status"] == "initiated"
    launch.assert_awaited_once_with("trivy")


async def test_launch_scan_background_success(monkeypatch):
    proc = SimpleNamespace(wait=AsyncMock(return_value=0))
    create = AsyncMock(return_value=proc)
    monkeypatch.setattr(asyncio, "create_subprocess_exec", create)
    await soc_router._launch_scan_background("sbom")
    await asyncio.sleep(0)
    assert proc.wait.await_count == 1
    args = create.await_args.args
    assert args[0] == soc_router._SECURITY_SCAN_SCRIPT
    assert args[1] == "--sbom"


async def test_launch_scan_background_exec_failure(monkeypatch):
    monkeypatch.setattr(
        asyncio, "create_subprocess_exec", AsyncMock(side_effect=OSError("missing script"))
    )
    # Must not raise — fire-and-forget semantics
    await soc_router._launch_scan_background("all")


async def test_scan_results(client, state):
    resp = await client.get("/soc/v1/scan/results")
    assert resp.json() == []
    state.trivy_scanner = SimpleNamespace(get_last_results=lambda: {"vulns": 1})
    resp = await client.get("/soc/v1/scan/results")
    assert resp.json() == [{"scanner": "trivy", "results": {"vulns": 1}}]
    state.trivy_scanner = SimpleNamespace(get_last_results=lambda: None)
    resp = await client.get("/soc/v1/scan/results")
    assert resp.json() == []


async def test_scanners_aggregate(client, state, monkeypatch):
    monkeypatch.setattr(
        "gateway.security.scanner_integration.aggregate_results",
        lambda: {"scanners": {"trivy": {}}, "totals": {"critical": 0}},
    )
    resp = await client.get("/soc/v1/scanners")
    assert resp.json()["scanners"] == {"trivy": {}}

    state.config = SimpleNamespace(bots={"hermes": SimpleNamespace(image="img:1")})
    state.scanner_results = {"trivy:image:img:1": {"summary": {"critical": 2}}}
    resp = await client.get("/soc/v1/scanners", params={"bot_id": "hermes"})
    data = resp.json()
    assert data["bot_id"] == "hermes"
    assert data["bot_image"] == {"critical": 2}


async def test_scanners_aggregate_error(client, monkeypatch):
    def _boom():
        raise RuntimeError("volume unreadable")

    monkeypatch.setattr("gateway.security.scanner_integration.aggregate_results", _boom)
    resp = await client.get("/soc/v1/scanners")
    data = resp.json()
    assert data["status"] == "error"
    assert data["totals"]["critical"] == 0


async def test_scanners_recent(client, state):
    resp = await client.get("/soc/v1/scanners/recent")
    assert resp.json() == {
        "count": 0,
        "totals": {"critical": 0, "high": 0, "findings": 0},
        "items": [],
    }

    state.scanner_result_history = [
        {"summary": {"status": "critical", "critical": 1, "high": 2, "findings": 3}},
        {"summary": {"status": "clean", "critical": 0, "high": 0, "findings": 0}},
    ]
    resp = await client.get("/soc/v1/scanners/recent")
    data = resp.json()
    assert data["count"] == 2
    assert data["totals"] == {"critical": 1, "high": 2, "findings": 3}

    resp = await client.get("/soc/v1/scanners/recent", params={"status": "critical"})
    assert resp.json()["count"] == 1

    resp = await client.get("/soc/v1/scanners/recent", params={"limit": 1})
    assert resp.json()["count"] == 1


async def test_scorecard_global_bot_and_error(client, state, monkeypatch):
    monkeypatch.setattr(
        "gateway.security.scanner_integration.compute_scorecard",
        lambda: {"totals": {"score": 48}},
    )
    monkeypatch.setattr(
        "gateway.security.scanner_integration.compute_bot_scorecard",
        lambda bot_id, app: {"bot_id": bot_id, "totals": {"score": 30}},
    )
    resp = await client.get("/soc/v1/scorecard")
    assert resp.json()["totals"]["score"] == 48

    resp = await client.get("/soc/v1/scorecard", params={"bot_id": "hermes"})
    assert resp.json()["bot_id"] == "hermes"

    def _boom():
        raise RuntimeError("missing reports")

    monkeypatch.setattr("gateway.security.scanner_integration.compute_scorecard", _boom)
    resp = await client.get("/soc/v1/scorecard")
    assert resp.json()["overall_maturity"] == "Not Started"


async def test_sbom_paths(client, monkeypatch):
    monkeypatch.setattr("gateway.security.scanner_integration.get_sbom", lambda: None)
    resp = await client.get("/soc/v1/sbom")
    assert resp.status_code == 404

    monkeypatch.setattr(
        "gateway.security.scanner_integration.get_sbom", lambda: {"spdxVersion": "SPDX-2.3"}
    )
    resp = await client.get("/soc/v1/sbom")
    assert resp.json() == {"spdxVersion": "SPDX-2.3"}

    def _boom():
        raise RuntimeError("corrupt sbom")

    monkeypatch.setattr("gateway.security.scanner_integration.get_sbom", _boom)
    resp = await client.get("/soc/v1/sbom")
    assert resp.status_code == 503


async def test_trivy_summary(client, monkeypatch):
    monkeypatch.setattr(
        "gateway.security.scanner_integration.get_trivy_summary",
        lambda: {"tool": "trivy", "findings": 4},
    )
    resp = await client.get("/soc/v1/trivy")
    assert resp.json()["findings"] == 4

    def _boom():
        raise RuntimeError("no report")

    monkeypatch.setattr("gateway.security.scanner_integration.get_trivy_summary", _boom)
    resp = await client.get("/soc/v1/trivy")
    assert resp.json()["status"] == "error"


async def test_agent_cves_known_and_unknown(client):
    resp = await client.get("/soc/v1/agent-cves")
    data = resp.json()
    assert "error" not in data  # openclaw registry exists
    resp = await client.get("/soc/v1/agent-cves", params={"bot_id": "ghostbot"})
    assert resp.json() == {"error": "unknown bot_id: ghostbot"}


async def test_agent_cves_registry_error(client, monkeypatch):
    def _boom(bot_id="openclaw"):
        raise RuntimeError("registry corrupt")

    monkeypatch.setattr("gateway.security.agent_cve_registry.get_agent_cve_summary", _boom)
    resp = await client.get("/soc/v1/agent-cves")
    assert resp.json() == {"error": "registry corrupt"}


async def test_cve_report_queued(client, monkeypatch):
    sent = AsyncMock(return_value=True)
    monkeypatch.setattr("gateway.security.daily_cve_report.run_and_send_cve_report", sent)
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "tok-x")
    monkeypatch.setenv("TELEGRAM_API_BASE_URL", "https://tg.local/")
    resp = await client.post("/soc/v1/cve-report")
    assert resp.json()["status"] == "queued"
    await asyncio.sleep(0.01)
    sent.assert_awaited_once()
    assert sent.await_args.kwargs["bot_token"] == "tok-x"
    assert sent.await_args.kwargs["base_url"] == "https://tg.local"


async def test_cve_report_error(client, monkeypatch):
    monkeypatch.delenv("TELEGRAM_BOT_TOKEN", raising=False)

    def _boom(name):
        raise RuntimeError("secret store offline")

    monkeypatch.setattr("gateway.utils.secrets.read_secret", _boom)
    resp = await client.post("/soc/v1/cve-report")
    assert resp.json()["status"] == "error"


# ---------------------------------------------------------------------------
# Updates / upgrade / rollback
# ---------------------------------------------------------------------------


def test_fetch_latest_release_success():
    body = json.dumps(
        {"tag_name": "v9.9.9", "html_url": "https://gh/rel", "body": "notes"}
    ).encode()
    cm = MagicMock()
    cm.__enter__.return_value.read.return_value = body
    with patch("urllib.request.urlopen", return_value=cm):
        result = soc_router._fetch_latest_release()
    assert result == {"tag_name": "v9.9.9", "html_url": "https://gh/rel", "body": "notes"}


def test_fetch_latest_release_error():
    with patch("urllib.request.urlopen", side_effect=urllib.error.URLError("offline")):
        result = soc_router._fetch_latest_release()
    assert "error" in result


async def test_get_updates_variants(client, monkeypatch):
    monkeypatch.setattr(soc_router, "_fetch_latest_release", lambda: {"error": "offline"})
    resp = await client.get("/soc/v1/updates")
    assert resp.json()["check_error"] == "offline"
    assert resp.json()["available"] == []

    monkeypatch.setattr(
        soc_router,
        "_fetch_latest_release",
        lambda: {"tag_name": f"v{soc_router._CURRENT_VERSION}", "html_url": "u", "body": ""},
    )
    resp = await client.get("/soc/v1/updates")
    assert resp.json()["available"] == []

    monkeypatch.setattr(
        soc_router,
        "_fetch_latest_release",
        lambda: {"tag_name": "v999.0.0", "html_url": "https://gh/rel", "body": "big"},
    )
    resp = await client.get("/soc/v1/updates")
    data = resp.json()
    assert data["latest_version"] == "999.0.0"
    assert data["available"][0]["url"] == "https://gh/rel"


async def test_ssh_compose_no_host(monkeypatch):
    monkeypatch.delenv("AGENTSHROUD_COMPOSE_HOST", raising=False)
    rc, out, err = await soc_router._ssh_compose("echo hi")
    assert rc == 1
    assert "AGENTSHROUD_COMPOSE_HOST" in err


async def test_ssh_compose_success(monkeypatch):
    monkeypatch.setenv("AGENTSHROUD_COMPOSE_HOST", "ops@example")
    monkeypatch.setenv("AGENTSHROUD_COMPOSE_DIR", "/srv/shroud")
    proc = SimpleNamespace(communicate=AsyncMock(return_value=(b"pulled", b"")), returncode=0)
    create = AsyncMock(return_value=proc)
    monkeypatch.setattr(asyncio, "create_subprocess_exec", create)
    rc, out, err = await soc_router._ssh_compose("git pull")
    assert (rc, out, err) == (0, "pulled", "")
    assert "cd /srv/shroud && git pull" in create.await_args.args


async def test_ssh_compose_timeout_and_exception(monkeypatch):
    monkeypatch.setenv("AGENTSHROUD_COMPOSE_HOST", "ops@example")
    proc = SimpleNamespace(communicate=AsyncMock(return_value=(b"", b"")), returncode=0)
    monkeypatch.setattr(asyncio, "create_subprocess_exec", AsyncMock(return_value=proc))
    monkeypatch.setattr(asyncio, "wait_for", AsyncMock(side_effect=asyncio.TimeoutError))
    rc, _, err = await soc_router._ssh_compose("slow", timeout=5)
    assert rc == 1
    assert "timed out" in err

    monkeypatch.setattr(asyncio, "create_subprocess_exec", AsyncMock(side_effect=OSError("no ssh")))
    rc, _, err = await soc_router._ssh_compose("cmd")
    assert rc == 1
    assert "no ssh" in err


async def test_upgrade_gateway_paths(client, holder, monkeypatch):
    holder["caller"] = NON_OWNER
    resp = await client.post("/soc/v1/updates/gateway/upgrade", json={"confirm": True})
    assert resp.status_code == 403

    holder["caller"] = OWNER
    resp = await client.post("/soc/v1/updates/gateway/upgrade", json={"confirm": False})
    assert resp.status_code == 409

    monkeypatch.setattr(soc_router, "_ssh_compose", AsyncMock(return_value=(0, "built ok", "")))
    resp = await client.post("/soc/v1/updates/gateway/upgrade", json={"confirm": True})
    assert resp.json() == {
        "ok": True,
        "action": "upgrade",
        "target": "gateway",
        "stdout": "built ok",
    }

    monkeypatch.setattr(soc_router, "_ssh_compose", AsyncMock(return_value=(2, "", "build failed")))
    resp = await client.post("/soc/v1/updates/gateway/upgrade", json={"confirm": True})
    assert resp.status_code == 500
    assert resp.json()["stderr"] == "build failed"


async def test_docker_exec_bot_success_and_frame_parsing():
    frame = b"\x01\x00\x00\x00" + len(b"hello").to_bytes(4, "big") + b"hello"
    responses = [
        SimpleNamespace(status=201, read=lambda: json.dumps({"Id": "e1"}).encode()),
        SimpleNamespace(status=200, read=lambda: frame),
        SimpleNamespace(status=200, read=lambda: json.dumps({"ExitCode": 0}).encode()),
    ]
    with (
        patch.object(http.client.HTTPConnection, "request"),
        patch.object(http.client.HTTPConnection, "getresponse", side_effect=responses),
    ):
        exit_code, output = await soc_router._docker_exec_bot(["echo", "hi"])
    assert exit_code == 0
    assert output == "hello"


async def test_docker_exec_bot_create_failures():
    bad = [SimpleNamespace(status=500, read=lambda: b"daemon error")]
    with (
        patch.object(http.client.HTTPConnection, "request"),
        patch.object(http.client.HTTPConnection, "getresponse", side_effect=bad),
    ):
        exit_code, output = await soc_router._docker_exec_bot(["x"])
    assert exit_code == 1
    assert "Docker exec create failed" in output

    no_id = [SimpleNamespace(status=200, read=lambda: json.dumps({"Id": ""}).encode())]
    with (
        patch.object(http.client.HTTPConnection, "request"),
        patch.object(http.client.HTTPConnection, "getresponse", side_effect=no_id),
    ):
        exit_code, output = await soc_router._docker_exec_bot(["x"])
    assert exit_code == 1
    assert "no ID" in output


async def test_docker_exec_bot_socket_error():
    with patch.object(
        http.client.HTTPConnection, "request", side_effect=OSError("no docker socket")
    ):
        exit_code, output = await soc_router._docker_exec_bot(["x"])
    assert exit_code == 1
    assert "no docker socket" in output


async def test_upgrade_bot_paths(client, holder, monkeypatch):
    holder["caller"] = NON_OWNER
    resp = await client.post("/soc/v1/updates/bot/upgrade", json={"confirm": True})
    assert resp.status_code == 403

    holder["caller"] = OWNER
    resp = await client.post("/soc/v1/updates/bot/upgrade", json={"confirm": False})
    assert resp.status_code == 409

    monkeypatch.setattr(soc_router, "_docker_exec_bot", AsyncMock(return_value=(1, "npm crashed")))
    resp = await client.post("/soc/v1/updates/bot/upgrade", json={"confirm": True})
    assert resp.status_code == 500
    assert resp.json()["output"] == "npm crashed"

    # success: npm install ok, second SDK patch fails, others ok
    monkeypatch.setattr(
        soc_router,
        "_docker_exec_bot",
        AsyncMock(side_effect=[(0, "installed"), (0, "ok"), (1, "patch broken"), (0, "ok")]),
    )
    resp = await client.post("/soc/v1/updates/bot/upgrade", json={"confirm": True})
    data = resp.json()
    assert data["ok"] is True
    assert data["output"] == "installed"
    assert data["sdk_patches"][0] == "patch-anthropic-sdk.sh: ok"
    assert "FAILED" in data["sdk_patches"][1]
    assert data["sdk_patches"][2] == "patch-slack-sdk.sh: ok"


async def test_upgrade_hermes_paths(client, holder, monkeypatch):
    holder["caller"] = NON_OWNER
    resp = await client.post("/soc/v1/updates/hermes/upgrade", json={"confirm": True})
    assert resp.status_code == 403

    holder["caller"] = OWNER
    resp = await client.post("/soc/v1/updates/hermes/upgrade", json={"confirm": False})
    assert resp.status_code == 409

    monkeypatch.setattr(
        "gateway.soc.services.ServiceManager", _make_service_manager(results={"update": False})
    )
    resp = await client.post("/soc/v1/updates/hermes/upgrade", json={"confirm": True})
    assert resp.status_code == 500

    monkeypatch.setattr(
        "gateway.soc.services.ServiceManager", _make_service_manager(results={"update": True})
    )
    resp = await client.post("/soc/v1/updates/hermes/upgrade", json={"confirm": True})
    assert resp.json()["ok"] is True
    assert resp.json()["target"] == "hermes"


async def test_rollback_gateway_paths(client, holder, monkeypatch):
    holder["caller"] = NON_OWNER
    resp = await client.post("/soc/v1/updates/gateway/rollback", json={"confirm": True})
    assert resp.status_code == 403

    holder["caller"] = OWNER
    resp = await client.post("/soc/v1/updates/gateway/rollback", json={"confirm": False})
    assert resp.status_code == 409

    commands = []

    async def _fake_ssh(command, timeout=120):
        commands.append(command)
        return (0, "rolled back", "")

    monkeypatch.setenv("AGENTSHROUD_ROLLBACK_TAG", "v1.0.9")
    monkeypatch.setattr(soc_router, "_ssh_compose", _fake_ssh)
    resp = await client.post("/soc/v1/updates/gateway/rollback", json={"confirm": True})
    assert resp.json()["ok"] is True
    assert "git checkout v1.0.9 -- gateway/" in commands[0]

    monkeypatch.setattr(
        soc_router, "_ssh_compose", AsyncMock(return_value=(1, "", "merge conflict"))
    )
    resp = await client.post("/soc/v1/updates/gateway/rollback", json={"confirm": True})
    assert resp.status_code == 500
    assert resp.json()["stderr"] == "merge conflict"


# ---------------------------------------------------------------------------
# WebSocket + dashboard
# ---------------------------------------------------------------------------


def test_websocket_route_dispatch(monkeypatch):
    import gateway.soc.websocket as ws_mod

    async def fake_endpoint(websocket):
        await websocket.accept()
        await websocket.send_json({"hello": "soc"})
        await websocket.close()

    monkeypatch.setattr(ws_mod, "ws_soc_endpoint", fake_endpoint)
    app = FastAPI()
    app.include_router(soc_router.router)
    with TestClient(app) as tc:
        with tc.websocket_connect("/soc/v1/ws") as ws:
            assert ws.receive_json() == {"hello": "soc"}


async def test_dashboard_serves_template_with_cache_busting(client):
    resp = await client.get("/soc/v1/")
    assert resp.status_code == 200
    assert resp.headers["cache-control"] == "no-cache, no-store, must-revalidate"
    assert f"/soc/static/soc.js?v={soc_router._SOC_JS_HASH}" in resp.text
    assert f"/soc/static/soc.css?v={soc_router._SOC_CSS_HASH}" in resp.text


async def test_dashboard_fallback_when_template_missing(client, monkeypatch):
    class _MissingPath:
        def __init__(self, *_a, **_k):
            pass

        @property
        def parent(self):
            return self

        def __truediv__(self, other):
            return self

        def exists(self):
            return False

    monkeypatch.setattr(soc_router, "Path", _MissingPath)
    resp = await client.get("/soc/v1")
    assert resp.status_code == 200
    assert "AgentShroud SOC — Command Center" in resp.text


def test_minimal_dashboard_html_contents():
    html = soc_router._minimal_dashboard_html()
    assert "/soc/v1/health" in html
    assert html.startswith("<!DOCTYPE html>")
