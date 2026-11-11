# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Command Center endpoints for the Inbound MCP Edge (SCRUM-216).

``GET /soc/v1/agents``, ``GET /soc/v1/edge/status`` and the owner-only
``POST /soc/v1/edge/{kill,unkill,enroll}``. A standalone FastAPI app mounts only
the SOC router; the caller dependency is overridden and ``_app_state`` points at
a per-test namespace. The edge store and ProgressiveLockdown are the real
modules — kill/unkill assertions read the store back, never a mock.
"""

import asyncio
import logging
import os
from collections import defaultdict
from types import SimpleNamespace

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

import gateway.soc.router as soc_router
from gateway.inbound_edge import profiles as p
from gateway.inbound_edge.call_pipeline import VendorStats
from gateway.inbound_edge.store import EdgeStore
from gateway.ingest_api.event_bus import EventBus, make_event
from gateway.security.progressive_lockdown import LockdownLevel, ProgressiveLockdown
from gateway.security.rbac import Action, Resource
from gateway.security.rbac_config import Role
from gateway.soc.auth import get_caller
from gateway.soc.models import WSEventType
from gateway.soc.websocket import SOCWebSocketHandler, _coerce_to_ws_event

ISSUER = "https://edge.example.ts.net:8443"


class FakeCaller:
    """RBAC is recorded, not enforced; owner is switchable."""

    def __init__(self, owner=True, allow=True):
        self.user_id = "owner-1" if owner else "55555"
        self.role = Role.OWNER if owner else Role.COLLABORATOR
        self._owner = owner
        self._allow = allow
        self.required = []

    def require(self, action, resource):
        self.required.append((action, resource))
        if not self._allow:
            from fastapi import HTTPException

            raise HTTPException(status_code=403, detail={"code": "PERMISSION_DENIED"})

    def is_owner(self):
        return self._owner


def _profile(vendor, enabled=True, mode="enforce"):
    return p.VendorProfile(
        vendor=vendor,
        display_name=vendor.replace("-", " ").title(),
        enabled=enabled,
        mode=mode,
        oauth=True,
        dynamic_registration=True,
        redirect_uris=(),
        static_bearer=False,
        tools={"lab_search": "read"},
        per_client_per_minute=30,
        per_vendor_per_minute=60,
        max_concurrency=4,
        daily_calls=500,
        daily_delegations=20,
        dlp_mode="redact",
        dlp_min_confidence=0.9,
        max_response_bytes=1_048_576,
    )


def _bot(bid, name, hostname, port=8642):
    return SimpleNamespace(
        id=bid,
        name=name,
        hostname=hostname,
        port=port,
        base_url=f"http://{hostname}:{port}",
        resolved_container_name=f"agentshroud-{bid}",
    )


@pytest.fixture
def holder():
    return {"caller": FakeCaller()}


@pytest.fixture
def state(monkeypatch):
    ns = SimpleNamespace(
        inbound_edge=None,
        config=SimpleNamespace(bots={}),
        progressive_lockdown=ProgressiveLockdown(),
    )
    monkeypatch.setattr(soc_router, "_app_state", lambda: ns)
    # Container health is read through ServiceManager; never touch a real engine.
    monkeypatch.setattr(soc_router, "_local_agent_health", lambda: {})
    return ns


@pytest.fixture
async def edge(tmp_path, state):
    store = EdgeStore(tmp_path / "edge.db", seal_key=os.urandom(32))
    await store.init()
    profiles = {
        "claude-duet": _profile("claude-duet"),
        "poke": _profile("poke", enabled=False),
        "gemini-spark": _profile("gemini-spark", mode="monitor"),
        "openai-dots": _profile("openai-dots", enabled=False),
    }
    svc = SimpleNamespace(
        store=store,
        profiles=profiles,
        pipeline=SimpleNamespace(stats=defaultdict(VendorStats)),
        issuer=ISSUER,
    )
    state.inbound_edge = svc
    yield svc
    await store.close()


@pytest.fixture
async def client(holder, state):
    app = FastAPI()
    app.include_router(soc_router.router)
    app.dependency_overrides[get_caller] = lambda: holder["caller"]
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac


def _rows(body, agent_id):
    return [a for a in body["agents"] if a["id"] == agent_id]


# ---------------------------------------------------------------------------
# GET /agents
# ---------------------------------------------------------------------------


class TestAgentsRegistry:
    async def test_requires_read_system(self, client, holder, state):
        await client.get("/soc/v1/agents")
        assert (Action.READ, Resource.SYSTEM) in holder["caller"].required

    async def test_rbac_denial_is_403(self, client, holder, state):
        holder["caller"] = FakeCaller(allow=False)
        resp = await client.get("/soc/v1/agents")
        assert resp.status_code == 403

    async def test_edge_disabled_local_only_derived(self, client, state):
        state.config.bots = {"hermes": _bot("hermes", "Hermes", "agentshroud-hermes-v2")}
        resp = await client.get("/soc/v1/agents")
        assert resp.status_code == 200
        body = resp.json()
        assert body["edge_enabled"] is False
        assert body["derived_mode"] == "local"
        assert body["mode"] == "local"
        assert {a["class"] for a in body["agents"]} == {"local"}
        hermes = _rows(body, "hermes")[0]
        assert hermes["route"] == "http://agentshroud-hermes-v2:8642"
        assert hermes["health"] == "unknown"

    async def test_derived_hosted_local(self, client, state, edge):
        state.config.bots = {"hermes": _bot("hermes", "Hermes", "h")}
        body = (await client.get("/soc/v1/agents")).json()
        assert body["derived_mode"] == "hosted_local"
        classes = {a["class"] for a in body["agents"]}
        assert classes == {"local", "hosted"}

    async def test_derived_hosted_when_no_local_bots(self, client, state, edge):
        body = (await client.get("/soc/v1/agents?mode=auto")).json()
        assert body["derived_mode"] == "hosted"
        assert body["mode"] == "hosted"
        assert {a["class"] for a in body["agents"]} == {"hosted"}

    async def test_explicit_mode_filters_rows(self, client, state, edge):
        state.config.bots = {"hermes": _bot("hermes", "Hermes", "h")}
        local = (await client.get("/soc/v1/agents?mode=local")).json()
        assert local["mode"] == "local" and local["derived_mode"] == "hosted_local"
        assert {a["class"] for a in local["agents"]} == {"local"}
        hosted = (await client.get("/soc/v1/agents?mode=hosted")).json()
        assert {a["class"] for a in hosted["agents"]} == {"hosted"}

    async def test_bad_mode_rejected(self, client, state):
        resp = await client.get("/soc/v1/agents?mode=everything")
        assert resp.status_code == 422

    async def test_vendor_rows_carry_edge_counters(self, client, state, edge):
        await edge.store.add_client("c1", "claude-duet", {}, "s3cret")
        await edge.store.add_client("c2", "claude-duet", {}, "s3cret")
        st = edge.pipeline.stats["claude-duet"]
        st.calls, st.ok, st.dlp_hits, st.canary_hits, st.pending_approvals = 9, 6, 2, 1, 1
        st.denials["rate_limited"] += 3
        st.last_call = 1_800_000_000.0
        state.progressive_lockdown.escalate_to(
            "edge:claude-duet:c2", LockdownLevel.ESCALATED, "test"
        )
        body = (await client.get("/soc/v1/agents?mode=hosted")).json()
        row = _rows(body, "claude-duet")[0]
        assert row["mechanism"] == "inbound_mcp_edge"
        assert row["enabled"] is True and row["mode"] == "enforce"
        assert row["clients"] == 2
        assert row["calls"] == 9 and row["dlp_hits"] == 2 and row["canary_hits"] == 1
        assert row["denials"] == {"rate_limited": 3}
        assert row["pending_approvals"] == 1
        assert row["lockdown"] == "escalated"
        assert row["killed"] is False
        assert row["last_call"] == 1_800_000_000.0
        assert row["status"] == "active"

    async def test_vendor_status_values_are_honest(self, client, state, edge):
        await edge.store.kill("vendor", "gemini-spark", "owner kill")
        body = (await client.get("/soc/v1/agents?mode=hosted")).json()
        assert _rows(body, "poke")[0]["status"] == "disabled"
        spark = _rows(body, "gemini-spark")[0]
        assert spark["killed"] is True and spark["status"] == "killed"
        assert spark["mode"] == "monitor"
        # Enabled but nobody enrolled yet.
        assert _rows(body, "claude-duet")[0]["status"] == "awaiting_enrollment"

    async def test_unhooked_hosted_agents_never_ok(self, client, state, edge):
        body = (await client.get("/soc/v1/agents?mode=hosted")).json()
        watch = [a for a in body["agents"] if a["mechanism"] == "host_egress_watch"]
        assert {a["id"] for a in watch} == {
            "perplexity-personal-computer",
            "meta-muse",
            "gemini-spark-desktop",
            "openai-dots-desktop",
        }
        assert all(a["status"] == "not_configured" for a in watch)
        assert all("SCRUM-219" in a["note"] for a in watch)
        none = [a for a in body["agents"] if a["mechanism"] == "none"]
        assert {a["id"] for a in none} == {"grok-bot", "instinct", "manus-cue"}
        assert all(a["status"] == "no_technical_hook" for a in none)
        assert not any(a["status"] == "ok" for a in body["agents"])

    async def test_hosted_rows_listed_from_disk_when_edge_disabled(self, client, state):
        body = (await client.get("/soc/v1/agents?mode=hosted")).json()
        vendors = {a["id"]: a for a in body["agents"] if a["mechanism"] == "inbound_mcp_edge"}
        assert set(vendors) == {"claude-duet", "poke", "gemini-spark", "openai-dots"}
        assert all(v["status"] == "edge_disabled" for v in vendors.values())

    async def test_local_health_from_service_manager(self, client, state, monkeypatch):
        state.config.bots = {"hermes": _bot("hermes", "Hermes", "h")}
        monkeypatch.setattr(
            soc_router, "_local_agent_health", lambda: {"agentshroud-hermes": "healthy"}
        )
        body = (await client.get("/soc/v1/agents?mode=local")).json()
        assert _rows(body, "hermes")[0]["health"] == "healthy"

    async def test_health_timeout_reads_unknown(self, client, state, monkeypatch):
        state.config.bots = {"hermes": _bot("hermes", "Hermes", "h")}

        async def _timeout(aw, timeout):
            aw.close()
            raise asyncio.TimeoutError

        monkeypatch.setattr(soc_router.asyncio, "wait_for", _timeout)
        body = (await client.get("/soc/v1/agents?mode=local")).json()
        assert _rows(body, "hermes")[0]["health"] == "unknown"

    async def test_suspended_client_marks_vendor_suspended(self, client, state, edge):
        await edge.store.add_client("c1", "claude-duet", {}, "s3cret")
        state.progressive_lockdown.escalate_to(
            "edge:claude-duet:c1", LockdownLevel.SUSPENDED, "test"
        )
        body = (await client.get("/soc/v1/agents?mode=hosted")).json()
        row = _rows(body, "claude-duet")[0]
        assert row["status"] == "suspended" and row["lockdown"] == "suspended"

    async def test_no_lockdown_module_reads_unknown(self, client, state, edge):
        await edge.store.add_client("c1", "claude-duet", {}, "s3cret")
        state.progressive_lockdown = None
        status = (await client.get("/soc/v1/edge/status")).json()
        assert status["vendors"]["claude-duet"]["lockdown"] == "unknown"
        assert status["vendors"]["claude-duet"]["clients"][0]["lockdown"] == "unknown"

    async def test_unreadable_profiles_with_edge_off_list_no_vendor_rows(
        self, client, state, monkeypatch
    ):
        from gateway.inbound_edge import profiles as profiles_mod

        def _bad(*a, **k):
            raise p.ProfileError("broken profile")

        monkeypatch.setattr(profiles_mod, "load_profiles", _bad)
        body = (await client.get("/soc/v1/agents?mode=hosted")).json()
        assert not [a for a in body["agents"] if a["mechanism"] == "inbound_mcp_edge"]
        # The unhooked rows still show, still honest.
        assert any(a["status"] == "not_configured" for a in body["agents"])


class TestLocalAgentHealthHelper:
    def test_maps_container_status_and_health(self, monkeypatch):
        svc = SimpleNamespace(
            name="agentshroud-hermes-v2",
            status=SimpleNamespace(value="running"),
            health=SimpleNamespace(value="healthy"),
        )
        stopped = SimpleNamespace(
            name="agentshroud-openclaw",
            status=SimpleNamespace(value="stopped"),
            health=SimpleNamespace(value="unknown"),
        )

        class _Mgr:
            def list_services(self):
                return [svc, stopped]

        import gateway.soc.services as services_mod

        monkeypatch.setattr(services_mod, "ServiceManager", _Mgr)
        assert soc_router._local_agent_health() == {
            "agentshroud-hermes-v2": "healthy",
            "agentshroud-openclaw": "stopped",
        }

    def test_engine_failure_is_empty_not_raise(self, monkeypatch):
        class _Boom:
            def list_services(self):
                raise RuntimeError("engine down")

        import gateway.soc.services as services_mod

        monkeypatch.setattr(services_mod, "ServiceManager", _Boom)
        assert soc_router._local_agent_health() == {}


# ---------------------------------------------------------------------------
# GET /edge/status
# ---------------------------------------------------------------------------


class TestEdgeStatus:
    async def test_disabled_state(self, client, state):
        resp = await client.get("/soc/v1/edge/status")
        assert resp.status_code == 200
        assert resp.json() == {
            "enabled": False,
            "issuer": None,
            "vendors": {},
            "recent": [],
            "kills": [],
            "clients": [],
        }

    async def test_enabled_state(self, client, holder, state, edge):
        await edge.store.add_client("c1", "claude-duet", {}, "s3cret")
        await edge.store.kill("client", "c9", "test")
        duet = edge.pipeline.stats["claude-duet"]
        spark = edge.pipeline.stats["gemini-spark"]
        duet.calls = 2
        duet.denials["schema"] += 1
        for i in range(30):
            duet.recent.appendleft({"request_id": f"d{i}", "vendor": "claude-duet", "ts": i * 2})
            spark.recent.appendleft(
                {"request_id": f"s{i}", "vendor": "gemini-spark", "ts": i * 2 + 1}
            )
        resp = await client.get("/soc/v1/edge/status")
        body = resp.json()
        assert (Action.READ, Resource.SYSTEM) in holder["caller"].required
        assert body["enabled"] is True and body["issuer"] == ISSUER
        assert set(body["vendors"]) == {"claude-duet", "poke", "gemini-spark", "openai-dots"}
        v = body["vendors"]["claude-duet"]
        assert v["calls"] == 2 and v["denials"] == {"schema": 1}
        assert v["enabled"] is True and v["mode"] == "enforce" and v["killed"] is False
        assert v["clients"] == [{"client_id": "c1", "lockdown": "normal", "killed": False}]
        assert len(body["recent"]) == 50
        assert body["recent"][0]["request_id"] == "s29"  # newest (ts 59) first
        assert [r["ts"] for r in body["recent"]] == sorted(
            (r["ts"] for r in body["recent"]), reverse=True
        )
        assert body["kills"][0]["scope"] == "client" and body["kills"][0]["value"] == "c9"
        assert body["clients"][0]["client_id"] == "c1"


# ---------------------------------------------------------------------------
# POST /edge/kill, /edge/unkill
# ---------------------------------------------------------------------------


class TestEdgeKill:
    async def test_confirm_required(self, client, state, edge):
        resp = await client.post(
            "/soc/v1/edge/kill", json={"scope": "vendor", "value": "poke", "reason": "x"}
        )
        assert resp.status_code == 409
        assert resp.json()["code"] == "CONFIRMATION_REQUIRED"
        assert await edge.store.list_kills() == []

    async def test_requires_manage_and_owner(self, client, holder, state, edge):
        holder["caller"] = FakeCaller(owner=False)
        resp = await client.post(
            "/soc/v1/edge/kill",
            json={"scope": "vendor", "value": "poke", "reason": "x", "confirm": True},
        )
        assert resp.status_code == 403
        assert (Action.MANAGE, Resource.SYSTEM) in holder["caller"].required
        assert await edge.store.list_kills() == []

    async def test_disabled_edge_is_503(self, client, state):
        resp = await client.post(
            "/soc/v1/edge/kill",
            json={"scope": "vendor", "value": "poke", "reason": "x", "confirm": True},
        )
        assert resp.status_code == 503
        assert resp.json()["detail"]["code"] == "EDGE_DISABLED"

    async def test_kill_vendor_writes_store_and_audits(self, client, state, edge, monkeypatch):
        audits = []
        monkeypatch.setattr(soc_router, "_log_audit", lambda *a, **k: audits.append((a, k)))
        resp = await client.post(
            "/soc/v1/edge/kill",
            json={"scope": "vendor", "value": "poke", "reason": "suspicious", "confirm": True},
        )
        assert resp.status_code == 200
        assert resp.json() == {"ok": True, "scope": "vendor", "value": "poke", "killed": True}
        kills = await edge.store.list_kills()
        assert [(k["scope"], k["value"], k["reason"]) for k in kills] == [
            ("vendor", "poke", "suspicious")
        ]
        assert await edge.store.killed_reason("poke", "any", "any") is not None
        assert audits and audits[0][0][1] == "edge kill"

    async def test_kill_client_must_exist(self, client, state, edge):
        resp = await client.post(
            "/soc/v1/edge/kill",
            json={"scope": "client", "value": "ghost", "reason": "x", "confirm": True},
        )
        assert resp.status_code == 404
        await edge.store.add_client("c1", "poke", {}, "s3cret")
        resp = await client.post(
            "/soc/v1/edge/kill",
            json={"scope": "client", "value": "c1", "reason": "x", "confirm": True},
        )
        assert resp.status_code == 200
        assert await edge.store.killed_reason("v", "c1", "j") == "client revoked: x"

    async def test_kill_unknown_vendor_404(self, client, state, edge):
        resp = await client.post(
            "/soc/v1/edge/kill",
            json={"scope": "vendor", "value": "nope", "reason": "x", "confirm": True},
        )
        assert resp.status_code == 404
        assert await edge.store.list_kills() == []

    async def test_kill_jti_must_be_issued(self, client, state, edge):
        resp = await client.post(
            "/soc/v1/edge/kill",
            json={"scope": "jti", "value": "j-unknown", "reason": "x", "confirm": True},
        )
        assert resp.status_code == 404
        await edge.store.record_jti("j-1", "c1", "poke", 9_999_999_999.0)
        resp = await client.post(
            "/soc/v1/edge/kill",
            json={"scope": "jti", "value": "j-1", "reason": "x", "confirm": True},
        )
        assert resp.status_code == 200

    async def test_bad_scope_422(self, client, state, edge):
        resp = await client.post(
            "/soc/v1/edge/kill",
            json={"scope": "everything", "value": "x", "reason": "x", "confirm": True},
        )
        assert resp.status_code == 422

    async def test_unkill_removes_and_noop_is_404(self, client, state, edge):
        await edge.store.kill("vendor", "poke", "x")
        resp = await client.post("/soc/v1/edge/unkill", json={"scope": "vendor", "value": "poke"})
        assert resp.status_code == 409
        assert len(await edge.store.list_kills()) == 1
        resp = await client.post(
            "/soc/v1/edge/unkill", json={"scope": "vendor", "value": "poke", "confirm": True}
        )
        assert resp.status_code == 200
        assert resp.json() == {"ok": True, "scope": "vendor", "value": "poke", "killed": False}
        assert await edge.store.list_kills() == []
        # Nothing to lift: a no-op must not read as success.
        resp = await client.post(
            "/soc/v1/edge/unkill", json={"scope": "vendor", "value": "poke", "confirm": True}
        )
        assert resp.status_code == 404

    async def test_kill_write_that_did_not_land_is_500(self, client, state, edge, monkeypatch):
        async def _lost_write(*a):
            return None  # store accepted the call but nothing changed

        monkeypatch.setattr(edge.store, "kill", _lost_write)
        resp = await client.post(
            "/soc/v1/edge/kill",
            json={"scope": "vendor", "value": "poke", "reason": "x", "confirm": True},
        )
        assert resp.status_code == 500
        assert resp.json()["detail"]["message"] == "Kill not recorded"

    async def test_unkill_write_that_did_not_land_is_500(self, client, state, edge, monkeypatch):
        await edge.store.kill("vendor", "poke", "x")

        async def _lost_write(*a):
            return None

        monkeypatch.setattr(edge.store, "unkill", _lost_write)
        resp = await client.post(
            "/soc/v1/edge/unkill", json={"scope": "vendor", "value": "poke", "confirm": True}
        )
        assert resp.status_code == 500
        assert len(await edge.store.list_kills()) == 1

    async def test_unkill_owner_only(self, client, holder, state, edge):
        await edge.store.kill("vendor", "poke", "x")
        holder["caller"] = FakeCaller(owner=False)
        resp = await client.post(
            "/soc/v1/edge/unkill", json={"scope": "vendor", "value": "poke", "confirm": True}
        )
        assert resp.status_code == 403
        assert len(await edge.store.list_kills()) == 1


# ---------------------------------------------------------------------------
# POST /edge/enroll
# ---------------------------------------------------------------------------


class TestEdgeEnroll:
    async def test_owner_only(self, client, holder, state, edge):
        holder["caller"] = FakeCaller(owner=False)
        resp = await client.post(
            "/soc/v1/edge/enroll", json={"vendor": "claude-duet", "confirm": True}
        )
        assert resp.status_code == 403
        assert await edge.store.enrollment_window_vendor() is None

    async def test_confirm_required(self, client, state, edge):
        resp = await client.post("/soc/v1/edge/enroll", json={"vendor": "claude-duet"})
        assert resp.status_code == 409
        assert await edge.store.enrollment_window_vendor() is None

    async def test_disabled_edge_is_503(self, client, state):
        resp = await client.post(
            "/soc/v1/edge/enroll", json={"vendor": "claude-duet", "confirm": True}
        )
        assert resp.status_code == 503

    async def test_vendor_must_exist_and_be_enabled(self, client, state, edge):
        resp = await client.post("/soc/v1/edge/enroll", json={"vendor": "nope", "confirm": True})
        assert resp.status_code == 404
        resp = await client.post("/soc/v1/edge/enroll", json={"vendor": "poke", "confirm": True})
        assert resp.status_code == 409
        assert resp.json()["detail"]["code"] == "VENDOR_DISABLED"
        assert await edge.store.enrollment_window_vendor() is None

    async def test_killed_vendor_cannot_enroll(self, client, state, edge):
        await edge.store.kill("vendor", "claude-duet", "x")
        resp = await client.post(
            "/soc/v1/edge/enroll", json={"vendor": "claude-duet", "confirm": True}
        )
        assert resp.status_code == 409
        assert resp.json()["detail"]["code"] == "VENDOR_KILLED"
        assert await edge.store.enrollment_window_vendor() is None

    async def test_ttl_capped_at_900(self, client, state, edge):
        resp = await client.post(
            "/soc/v1/edge/enroll", json={"vendor": "claude-duet", "ttl_s": 901, "confirm": True}
        )
        assert resp.status_code == 422

    async def test_returns_working_code_once_and_never_logs_it(
        self, client, state, edge, monkeypatch, caplog
    ):
        audits = []
        monkeypatch.setattr(soc_router, "_log_audit", lambda *a, **k: audits.append((a, k)))
        caplog.set_level(logging.DEBUG)
        resp = await client.post(
            "/soc/v1/edge/enroll", json={"vendor": "claude-duet", "ttl_s": 300, "confirm": True}
        )
        assert resp.status_code == 200
        assert resp.headers["cache-control"] == "no-store"
        body = resp.json()
        assert body["ok"] is True and body["vendor"] == "claude-duet" and body["ttl_s"] == 300
        assert body["expires_at"]
        code = body["code"]
        assert await edge.store.enrollment_window_vendor() == "claude-duet"
        assert await edge.store.consume_enrollment(code, "claude-duet") is True
        assert await edge.store.consume_enrollment(code, "claude-duet") is None
        assert code not in caplog.text
        assert code not in repr(audits)
        assert audits and audits[0][0][1] == "edge enroll"


# ---------------------------------------------------------------------------
# edge_event reaches the Command Center WebSocket
# ---------------------------------------------------------------------------


class TestEdgeEventOverWebSocket:
    def test_edge_gateway_event_is_forwarded(self):
        rec = {"request_id": "r1", "vendor": "poke", "tool": "lab_search", "outcome": "denied"}
        ev = _coerce_to_ws_event(make_event("edge_event", "edge poke lab_search", rec, "warning"))
        assert ev is not None
        assert ev.type == WSEventType.EDGE_EVENT
        assert ev.details == rec
        assert ev.summary == "edge poke lab_search"
        assert ev.severity.value == "medium"

    def test_unmapped_gateway_event_still_dropped(self):
        # Only typed SOC streams cross the bridge; other bus traffic stays off the feed.
        assert _coerce_to_ws_event(make_event("auth_failed", "x")) is None

    async def test_fan_out_honours_edge_subscription(self):
        sent = []
        handler = SOCWebSocketHandler(SimpleNamespace(), "owner-1")
        handler.subscriptions = {"edge_event"}

        async def _send(ev):
            sent.append(ev)

        handler._send_event = _send
        bus = EventBus()
        task = asyncio.create_task(handler._event_fan_out(bus))
        await asyncio.sleep(0)
        await bus.emit(make_event("edge_event", "edge call", {"request_id": "r2"}))
        await bus.emit(make_event("security_event", "other", {}))
        for _ in range(5):
            await asyncio.sleep(0)
        task.cancel()
        assert [e.details["request_id"] for e in sent] == ["r2"]


# ---------------------------------------------------------------------------
# Command Center UI wiring
# ---------------------------------------------------------------------------


def test_command_center_has_agents_and_edge_tabs():
    import re
    from pathlib import Path

    soc_dir = Path(soc_router.__file__).parent
    html = (soc_dir / "templates" / "soc.html").read_text(encoding="utf-8")
    js = (soc_dir / "static" / "soc.js").read_text(encoding="utf-8")
    monitor = html.index('<div class="nav-section">Monitor</div>')
    manage = html.index('<div class="nav-section">Manage</div>')
    for tab, label in (("agents", "Agents"), ("edge", "Inbound Edge")):
        nav = html.index(f'<a class="nav-item" data-tab="{tab}">{label}</a>')
        assert monitor < nav < manage
        assert f'<div id="tab-{tab}" class="tab-pane"' in html
        assert f"_registerTab('{tab}'," in js
    for mode in ("hosted", "hosted_local", "local"):
        assert f'<option value="{mode}">' in html
    assert "'edge_event'" in js.split("subscribe:")[1].split("]")[0]
    assert "/edge/kill" in js and "/edge/unkill" in js and "/edge/enroll" in js
    # Data reaches handlers through data-* attributes, never interpolated into inline JS.
    for handler in ("_edgeKill", "_edgeUnkill", "_edgeEnroll"):
        for call in re.findall(rf"window\.{handler}\(([^)]*)\)", js):
            assert "${" not in call, call


def test_edge_service_exposes_enforced_profiles():
    from gateway.inbound_edge.service import EdgeService

    enforced = {"poke": _profile("poke")}
    svc = EdgeService(
        store=None,
        tokens=None,
        oauth=None,
        approvals=None,
        pipeline=SimpleNamespace(d=SimpleNamespace(profiles=enforced)),
        service_token="t" * 32,
        issuer=ISSUER,
        resource=ISSUER + "/mcp",
    )
    assert svc.profiles is enforced
