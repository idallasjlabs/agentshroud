# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for M5 per-bot SOC backend.

Covers:
  - GET /bots list endpoint (with and without config)
  - bot_id filter on: security/events, egress/pending, egress/history, egress/log,
    scanners, agent-cves, collaborators/activity, services, scorecard, config
  - compute_bot_scorecard: formula correctness, clamping, clean-image, missing-bot

Test pattern: call async handlers directly (pytest-asyncio), mock _app_state() and
the SCLCaller via patch — no real containers, no real network, no skip markers.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.security.rbac_config import Role
from gateway.security.scanner_integration import compute_bot_scorecard
from gateway.soc.auth import SCLCaller
from gateway.soc.router import (
    get_agent_cves,
    get_collaborator_activity,
    get_config,
    get_egress_history,
    get_egress_log,
    get_egress_pending,
    get_scanner_results,
    get_security_events,
    get_security_scorecard,
    list_bots,
    list_services,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_owner_caller() -> SCLCaller:
    """Build an SCLCaller with OWNER role — no FastAPI dependency resolution."""
    from gateway.security.rbac_config import RBACConfig, Role

    rbac_cfg = MagicMock(spec=RBACConfig)
    rbac_cfg.owner_user_id = "owner-test"
    rbac_cfg.is_owner.return_value = True

    rbac = MagicMock()
    rbac.config = rbac_cfg
    perm = MagicMock()
    perm.allowed = True
    rbac.check_permission.return_value = perm

    return SCLCaller(user_id="owner-test", role=Role.OWNER, rbac=rbac)


def _make_bot_config(
    name: str = "OpenClaw",
    hostname: str = "agentshroud",
    port: int = 18789,
    image: str = "agentshroud/openclaw:latest",
    egress_domains: list | None = None,
) -> MagicMock:
    b = MagicMock()
    b.name = name
    b.hostname = hostname
    b.port = port
    b.image = image
    b.egress_domains = egress_domains or ["api.telegram.org"]
    b.default = False
    return b


def _make_app_state(bots: dict | None = None) -> MagicMock:
    app = MagicMock()
    cfg = MagicMock()
    cfg.bots = bots or {}
    cfg.bind = "0.0.0.0"
    cfg.port = 8080
    cfg.log_level = "INFO"
    cfg.teams = None
    app.config = cfg
    app.audit_store = None
    app.egress_approval_queue = None
    app.scanner_results = {}
    app.egress_filter = None
    app.collaborator_tracker = None
    return app


# ---------------------------------------------------------------------------
# /bots endpoint
# ---------------------------------------------------------------------------


class TestListBots:
    @pytest.mark.asyncio
    async def test_returns_registered_bots(self):
        openclaw = _make_bot_config(name="OpenClaw", hostname="agentshroud")
        hermes = _make_bot_config(name="Hermes", hostname="agentshroud-hermes")
        app = _make_app_state(bots={"openclaw": openclaw, "hermes": hermes})
        caller = _make_owner_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await list_bots(caller=caller)

        assert isinstance(result, list)
        assert len(result) == 2
        ids = {r["id"] for r in result}
        assert "openclaw" in ids
        assert "hermes" in ids

    @pytest.mark.asyncio
    async def test_returns_default_when_no_bots_config(self):
        """Backward-compat: no bots section → return single OpenClaw default."""
        app = _make_app_state(bots={})
        caller = _make_owner_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await list_bots(caller=caller)

        assert len(result) == 1
        assert result[0]["id"] == "openclaw"
        assert result[0]["default"] is True

    @pytest.mark.asyncio
    async def test_returns_default_when_config_is_none(self):
        """Backward-compat: config attr absent → return single OpenClaw default."""
        app = MagicMock()
        app.config = None
        caller = _make_owner_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await list_bots(caller=caller)

        assert result[0]["id"] == "openclaw"

    @pytest.mark.asyncio
    async def test_bot_dict_has_required_keys(self):
        bot = _make_bot_config()
        app = _make_app_state(bots={"openclaw": bot})
        caller = _make_owner_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await list_bots(caller=caller)

        assert {"id", "name", "hostname", "default"} <= set(result[0].keys())


# ---------------------------------------------------------------------------
# /security/events + bot_id filter
# ---------------------------------------------------------------------------


class TestSecurityEventsBotFilter:
    @pytest.mark.asyncio
    async def test_filters_events_by_exact_bot_id(self):
        from gateway.soc.models import SecurityEvent, Severity

        ev_openclaw = SecurityEvent(
            event_type="egress.check",
            summary="s",
            agent_id="openclaw",
            severity=Severity.INFO,
        )
        ev_hermes = SecurityEvent(
            event_type="egress.check",
            summary="s",
            agent_id="hermes",
            severity=Severity.INFO,
        )
        ev_sub = SecurityEvent(
            event_type="egress.check",
            summary="s",
            agent_id="openclaw:session-1",
            severity=Severity.INFO,
        )
        app = _make_app_state()
        caller = _make_owner_caller()

        with (
            patch("gateway.soc.router._app_state", return_value=app),
            patch(
                "gateway.soc.event_adapter.collect_recent_events",
                new=AsyncMock(return_value=[ev_openclaw, ev_hermes, ev_sub]),
            ),
        ):
            result = await get_security_events(limit=50, severity=None, bot_id="openclaw", caller=caller)

        agent_ids = [r["agent_id"] for r in result]
        assert "openclaw" in agent_ids
        assert "openclaw:session-1" in agent_ids
        assert "hermes" not in agent_ids

    @pytest.mark.asyncio
    async def test_no_bot_id_returns_all_events(self):
        from gateway.soc.models import SecurityEvent, Severity

        events = [
            SecurityEvent(event_type="e", summary="s", agent_id="openclaw", severity=Severity.INFO),
            SecurityEvent(event_type="e", summary="s", agent_id="hermes", severity=Severity.INFO),
        ]
        app = _make_app_state()
        caller = _make_owner_caller()

        with (
            patch("gateway.soc.router._app_state", return_value=app),
            patch(
                "gateway.soc.event_adapter.collect_recent_events",
                new=AsyncMock(return_value=events),
            ),
        ):
            result = await get_security_events(limit=50, severity=None, bot_id=None, caller=caller)

        assert len(result) == 2


# ---------------------------------------------------------------------------
# /egress/pending + bot_id filter
# ---------------------------------------------------------------------------


class TestEgressPendingBotFilter:
    @pytest.mark.asyncio
    async def test_filters_pending_by_bot_id(self):
        pending = [
            {"request_id": "r1", "agent_id": "openclaw", "domain": "api.telegram.org"},
            {"request_id": "r2", "agent_id": "hermes", "domain": "api.hermes.ai"},
        ]
        app = _make_app_state()
        eq = MagicMock()
        eq.get_pending_requests = AsyncMock(return_value=pending)
        app.egress_approval_queue = eq
        caller = _make_owner_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await get_egress_pending(bot_id="openclaw", caller=caller)

        assert all(r["agent_id"] == "openclaw" for r in result)
        assert len(result) == 1

    @pytest.mark.asyncio
    async def test_no_bot_id_returns_all_pending(self):
        pending = [
            {"request_id": "r1", "agent_id": "openclaw", "domain": "a.com"},
            {"request_id": "r2", "agent_id": "hermes", "domain": "b.com"},
        ]
        app = _make_app_state()
        eq = MagicMock()
        eq.get_pending_requests = AsyncMock(return_value=pending)
        app.egress_approval_queue = eq
        caller = _make_owner_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await get_egress_pending(bot_id=None, caller=caller)

        assert len(result) == 2


# ---------------------------------------------------------------------------
# /egress/history + bot_id filter
# ---------------------------------------------------------------------------


class TestEgressHistoryBotFilter:
    @pytest.mark.asyncio
    async def test_filters_history_by_bot_id(self):
        log = [
            {"entry_id": "e1", "agent_id": "openclaw", "decision": "approved"},
            {"entry_id": "e2", "agent_id": "hermes", "decision": "denied"},
        ]
        app = _make_app_state()
        eq = MagicMock()
        eq.get_decision_log = AsyncMock(return_value=log)
        app.egress_approval_queue = eq
        caller = _make_owner_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await get_egress_history(limit=100, bot_id="hermes", caller=caller)

        assert len(result) == 1
        assert result[0]["agent_id"] == "hermes"

    @pytest.mark.asyncio
    async def test_no_bot_id_returns_full_history(self):
        log = [
            {"entry_id": "e1", "agent_id": "openclaw", "decision": "approved"},
            {"entry_id": "e2", "agent_id": "hermes", "decision": "denied"},
        ]
        app = _make_app_state()
        eq = MagicMock()
        eq.get_decision_log = AsyncMock(return_value=log)
        app.egress_approval_queue = eq
        caller = _make_owner_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await get_egress_history(limit=100, bot_id=None, caller=caller)

        assert len(result) == 2


# ---------------------------------------------------------------------------
# /egress/log + bot_id filter
# ---------------------------------------------------------------------------


class TestEgressLogBotFilter:
    @pytest.mark.asyncio
    async def test_filters_egress_log_by_bot_id(self):
        from gateway.soc.models import SecurityEvent, Severity

        ev_openclaw = SecurityEvent(
            event_type="egress.allowed",
            summary="s",
            agent_id="openclaw",
            severity=Severity.INFO,
        )
        ev_hermes = SecurityEvent(
            event_type="egress.denied",
            summary="s",
            agent_id="hermes",
            severity=Severity.HIGH,
        )
        app = _make_app_state()
        caller = _make_owner_caller()

        with (
            patch("gateway.soc.router._app_state", return_value=app),
            patch(
                "gateway.soc.event_adapter.collect_recent_events",
                new=AsyncMock(return_value=[ev_openclaw, ev_hermes]),
            ),
        ):
            result = await get_egress_log(limit=50, bot_id="openclaw", caller=caller)

        assert all(r["agent_id"] == "openclaw" for r in result)


# ---------------------------------------------------------------------------
# /scanners + bot_id augmentation
# ---------------------------------------------------------------------------


class TestScannersBotId:
    @pytest.mark.asyncio
    async def test_bot_id_augments_result_with_image_scan(self):
        bot = _make_bot_config(image="agentshroud/openclaw:latest")
        app = _make_app_state(bots={"openclaw": bot})
        app.scanner_results = {
            "trivy:image:agentshroud/openclaw:latest": {
                "summary": {"critical": 0, "high": 2, "medium": 5}
            }
        }
        caller = _make_owner_caller()

        with (
            patch("gateway.soc.router._app_state", return_value=app),
            patch(
                "gateway.security.scanner_integration.aggregate_results",
                return_value={"status": "clean", "scanners": {}, "totals": {}},
            ),
        ):
            result = await get_scanner_results(bot_id="openclaw", caller=caller)

        assert result["bot_id"] == "openclaw"
        assert result["bot_image"] is not None
        assert result["bot_image"]["high"] == 2

    @pytest.mark.asyncio
    async def test_no_bot_id_omits_bot_keys(self):
        app = _make_app_state()
        caller = _make_owner_caller()

        with (
            patch("gateway.soc.router._app_state", return_value=app),
            patch(
                "gateway.security.scanner_integration.aggregate_results",
                return_value={"status": "clean", "scanners": {}, "totals": {}},
            ),
        ):
            result = await get_scanner_results(bot_id=None, caller=caller)

        assert "bot_id" not in result
        assert "bot_image" not in result


# ---------------------------------------------------------------------------
# /agent-cves + bot_id
# ---------------------------------------------------------------------------


class TestAgentCvesBotId:
    @pytest.mark.asyncio
    async def test_known_bot_returns_cve_summary(self):
        caller = _make_owner_caller()

        with patch(
            "gateway.security.agent_cve_registry.get_agent_cve_summary",
            return_value={"wrapped_agent": "OpenClaw", "total_cves": 5},
        ):
            result = await get_agent_cves(bot_id="openclaw", caller=caller)

        assert "wrapped_agent" in result

    @pytest.mark.asyncio
    async def test_unknown_bot_returns_error(self):
        caller = _make_owner_caller()
        result = await get_agent_cves(bot_id="unknown-bot-xyz", caller=caller)
        assert "error" in result
        assert "unknown bot_id" in result["error"]

    @pytest.mark.asyncio
    async def test_no_bot_id_defaults_to_openclaw(self):
        caller = _make_owner_caller()

        with patch(
            "gateway.security.agent_cve_registry.get_agent_cve_summary",
            return_value={"wrapped_agent": "OpenClaw", "total_cves": 3},
        ):
            result = await get_agent_cves(bot_id=None, caller=caller)

        assert "total_cves" in result


# ---------------------------------------------------------------------------
# /collaborators/activity + bot_id filter
# ---------------------------------------------------------------------------


class TestCollaboratorActivityBotFilter:
    @pytest.mark.asyncio
    async def test_filters_activity_by_bot_id_in_source(self):
        entries = [
            {"user_id": "u1", "source": "openclaw", "direction": "inbound", "timestamp": 1.0},
            {"user_id": "u2", "source": "hermes", "direction": "inbound", "timestamp": 2.0},
        ]
        app = _make_app_state()
        tracker = MagicMock()
        tracker.get_activity = MagicMock(return_value=entries)
        app.collaborator_tracker = tracker
        caller = _make_owner_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            response = await get_collaborator_activity(
                since=0.0,
                limit=0,
                offset=0,
                user_id=None,
                direction=None,
                search=None,
                is_owner=None,
                bot_id="openclaw",
                caller=caller,
            )

        data = response.body
        import json

        parsed = json.loads(data)
        assert all("openclaw" in (e.get("source") or "") for e in parsed["entries"])


# ---------------------------------------------------------------------------
# /services + bot_id filter
# ---------------------------------------------------------------------------


class TestServicesBotFilter:
    @pytest.mark.asyncio
    async def test_filters_services_by_bot_image(self):
        """When bot_id is given, services whose image matches the bot's image are returned.

        Uses image matching to distinguish OpenClaw from Hermes. The hostname filter
        also applies (name contains hostname), so we verify both paths.
        """
        from gateway.soc.models import ServiceDescriptor, ServiceStatus

        svc_openclaw = ServiceDescriptor(name="agentshroud-bot", status=ServiceStatus.RUNNING, image="openclaw:latest")
        svc_hermes = ServiceDescriptor(name="agentshroud-hermes", status=ServiceStatus.RUNNING, image="hermes-agent:latest")
        svc_gateway = ServiceDescriptor(name="agentshroud-gateway", status=ServiceStatus.RUNNING, image="gateway:latest")

        # Use a very specific hostname that only matches agentshroud-bot
        bot = _make_bot_config(hostname="agentshroud-bot", image="openclaw:latest")
        app = _make_app_state(bots={"openclaw": bot})
        caller = _make_owner_caller()

        with (
            patch("gateway.soc.router._app_state", return_value=app),
            patch(
                "gateway.soc.services.ServiceManager.list_services",
                return_value=[svc_openclaw, svc_hermes, svc_gateway],
            ),
        ):
            result = await list_services(bot_id="openclaw", caller=caller)

        names = [r["name"] for r in result]
        # agentshroud-bot matches both hostname and image; gateway/hermes do not
        assert "agentshroud-bot" in names
        assert "agentshroud-hermes" not in names
        assert "agentshroud-gateway" not in names

    @pytest.mark.asyncio
    async def test_no_bot_id_returns_all_services(self):
        from gateway.soc.models import ServiceDescriptor, ServiceStatus

        svcs = [
            ServiceDescriptor(name="agentshroud-bot", status=ServiceStatus.RUNNING),
            ServiceDescriptor(name="agentshroud-hermes", status=ServiceStatus.RUNNING),
        ]
        app = _make_app_state()
        caller = _make_owner_caller()

        with (
            patch("gateway.soc.router._app_state", return_value=app),
            patch(
                "gateway.soc.services.ServiceManager.list_services",
                return_value=svcs,
            ),
        ):
            result = await list_services(bot_id=None, caller=caller)

        assert len(result) == 2


# ---------------------------------------------------------------------------
# /scorecard + bot_id
# ---------------------------------------------------------------------------


class TestScorecardBotId:
    @pytest.mark.asyncio
    async def test_bot_id_calls_compute_bot_scorecard(self):
        bot_card = {
            "score": 90,
            "risk_level": "green",
            "bot_id": "openclaw",
            "image": "openclaw:latest",
            "critical": 0,
            "high": 0,
            "medium": 0,
            "egress_denials": 0,
            "domains": [],
        }
        app = _make_app_state()
        caller = _make_owner_caller()

        with (
            patch("gateway.soc.router._app_state", return_value=app),
            patch(
                "gateway.security.scanner_integration.compute_bot_scorecard",
                return_value=bot_card,
            ),
        ):
            result = await get_security_scorecard(bot_id="openclaw", caller=caller)

        assert result["bot_id"] == "openclaw"
        assert result["score"] == 90

    @pytest.mark.asyncio
    async def test_no_bot_id_calls_global_scorecard(self):
        global_card = {"version": "v0.9.0", "domains": [], "totals": {"score": 100, "max": 165}}
        caller = _make_owner_caller()
        app = _make_app_state()

        with (
            patch("gateway.soc.router._app_state", return_value=app),
            patch(
                "gateway.security.scanner_integration.compute_scorecard",
                return_value=global_card,
            ),
        ):
            result = await get_security_scorecard(bot_id=None, caller=caller)

        assert "version" in result


# ---------------------------------------------------------------------------
# /config + bot_id
# ---------------------------------------------------------------------------


class TestConfigBotId:
    @pytest.mark.asyncio
    async def test_bot_id_returns_per_bot_config(self):
        bot = _make_bot_config(name="OpenClaw", hostname="agentshroud", port=18789, image="openclaw:latest")
        app = _make_app_state(bots={"openclaw": bot})
        caller = _make_owner_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await get_config(bot_id="openclaw", caller=caller)

        assert result["id"] == "openclaw"
        assert result["hostname"] == "agentshroud"
        assert "egress_domains" in result

    @pytest.mark.asyncio
    async def test_unknown_bot_id_returns_error(self):
        app = _make_app_state(bots={})
        caller = _make_owner_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await get_config(bot_id="ghost-bot", caller=caller)

        assert "error" in result
        assert "ghost-bot" in result["error"]

    @pytest.mark.asyncio
    async def test_no_bot_id_returns_global_config(self):
        bot = _make_bot_config()
        app = _make_app_state(bots={"openclaw": bot})
        caller = _make_owner_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await get_config(bot_id=None, caller=caller)

        assert "bind" in result
        assert "bots" in result

    @pytest.mark.asyncio
    async def test_config_none_returns_empty_dict(self):
        """When app_state.config is None, return empty dict (backward-compat)."""
        app = MagicMock()
        app.config = None
        caller = _make_owner_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await get_config(bot_id=None, caller=caller)

        assert result == {}


# ---------------------------------------------------------------------------
# compute_bot_scorecard — unit tests
# ---------------------------------------------------------------------------


class TestComputeBotScorecard:
    def _make_state_with_bot(
        self,
        image: str = "openclaw:latest",
        critical: int = 0,
        high: int = 0,
        medium: int = 0,
        denials: int = 0,
    ) -> MagicMock:
        bot = _make_bot_config(image=image)
        app = _make_app_state(bots={"openclaw": bot})
        app.scanner_results = {
            f"trivy:image:{image}": {
                "summary": {"critical": critical, "high": high, "medium": medium}
            }
        } if image else {}
        ef = MagicMock()
        ef.get_stats = MagicMock(return_value={"denied": denials})
        app.egress_filter = ef
        return app

    def test_clean_image_score_100(self):
        app = self._make_state_with_bot(critical=0, high=0, medium=0, denials=0)
        result = compute_bot_scorecard("openclaw", app)
        assert result["score"] == 100
        assert result["risk_level"] == "green"

    def test_formula_critical_penalty(self):
        # 100 - 1*20 = 80
        app = self._make_state_with_bot(critical=1, high=0, medium=0, denials=0)
        result = compute_bot_scorecard("openclaw", app)
        assert result["score"] == 80

    def test_formula_high_penalty(self):
        # 100 - 2*10 = 80
        app = self._make_state_with_bot(critical=0, high=2, medium=0, denials=0)
        result = compute_bot_scorecard("openclaw", app)
        assert result["score"] == 80

    def test_formula_medium_penalty(self):
        # 100 - 3*3 = 91
        app = self._make_state_with_bot(critical=0, high=0, medium=3, denials=0)
        result = compute_bot_scorecard("openclaw", app)
        assert result["score"] == 91

    def test_formula_egress_denials_penalty(self):
        # 100 - 2*5 = 90
        app = self._make_state_with_bot(critical=0, high=0, medium=0, denials=2)
        result = compute_bot_scorecard("openclaw", app)
        assert result["score"] == 90

    def test_formula_combined_penalty(self):
        # 100 - 1*20 - 1*10 - 1*3 - 1*5 = 62
        app = self._make_state_with_bot(critical=1, high=1, medium=1, denials=1)
        result = compute_bot_scorecard("openclaw", app)
        assert result["score"] == 62

    def test_score_clamped_to_zero(self):
        # Very high findings must not go below 0
        app = self._make_state_with_bot(critical=10, high=10, medium=10, denials=10)
        result = compute_bot_scorecard("openclaw", app)
        assert result["score"] == 0

    def test_score_clamped_to_hundred(self):
        # Zeroed findings must not exceed 100
        app = self._make_state_with_bot(critical=0, high=0, medium=0, denials=0)
        result = compute_bot_scorecard("openclaw", app)
        assert result["score"] <= 100

    def test_risk_level_red_below_50(self):
        # 100 - 3*20 = 40 → red
        app = self._make_state_with_bot(critical=3, high=0, medium=0, denials=0)
        result = compute_bot_scorecard("openclaw", app)
        assert result["risk_level"] == "red"

    def test_risk_level_yellow_50_to_79(self):
        # 100 - 2*20 = 60 → yellow
        app = self._make_state_with_bot(critical=2, high=0, medium=0, denials=0)
        result = compute_bot_scorecard("openclaw", app)
        assert result["risk_level"] == "yellow"

    def test_no_scan_data_defaults_zeros(self):
        """Bot with no image scan data should default critical/high/medium to 0."""
        bot = _make_bot_config(image="openclaw:latest")
        app = _make_app_state(bots={"openclaw": bot})
        app.scanner_results = {}  # No scan data
        ef = MagicMock()
        ef.get_stats = MagicMock(return_value={"denied": 0})
        app.egress_filter = ef

        result = compute_bot_scorecard("openclaw", app)
        assert result["critical"] == 0
        assert result["high"] == 0
        assert result["score"] == 100

    def test_missing_bot_returns_empty_image(self):
        """Bot not in config → image='', scan skipped, score based on egress only."""
        app = _make_app_state(bots={})  # "unknownbot" not present
        ef = MagicMock()
        ef.get_stats = MagicMock(return_value={"denied": 0})
        app.egress_filter = ef

        result = compute_bot_scorecard("unknownbot", app)
        assert result["image"] == ""
        assert result["score"] == 100  # No penalties without scan data or denials

    def test_result_structure_has_required_keys(self):
        app = self._make_state_with_bot()
        result = compute_bot_scorecard("openclaw", app)
        required = {"score", "risk_level", "bot_id", "image", "critical", "high", "medium", "egress_denials", "domains"}
        assert required <= set(result.keys())

    def test_domains_has_vuln_and_egress(self):
        app = self._make_state_with_bot()
        result = compute_bot_scorecard("openclaw", app)
        domain_names = {d["domain"] for d in result["domains"]}
        assert "vuln_scan" in domain_names
        assert "egress" in domain_names

    def test_egress_filter_exception_defaults_denials_zero(self):
        """If egress_filter.get_stats raises, denials defaults to 0 (no crash)."""
        bot = _make_bot_config(image="openclaw:latest")
        app = _make_app_state(bots={"openclaw": bot})
        app.scanner_results = {}
        ef = MagicMock()
        ef.get_stats = MagicMock(side_effect=RuntimeError("unavailable"))
        app.egress_filter = ef

        result = compute_bot_scorecard("openclaw", app)
        assert result["egress_denials"] == 0
        assert result["score"] == 100


# ---------------------------------------------------------------------------
# M6: TestBotSelectorFrontend — /soc/v1/bots + bot_id filtering
# ---------------------------------------------------------------------------


def _make_m6_caller() -> SCLCaller:
    caller = MagicMock(spec=SCLCaller)
    caller.user_id = "owner-test"
    caller.role = Role.OWNER
    caller.require = MagicMock()
    caller.is_owner = MagicMock(return_value=True)
    return caller


def _make_m6_bot_config(bot_id: str, name: str, hostname: str, default: bool = False) -> MagicMock:
    bot = MagicMock()
    bot.id = bot_id
    bot.name = name
    bot.hostname = hostname
    bot.default = default
    return bot


def _make_m6_app_state(bots: dict) -> MagicMock:
    cfg = MagicMock()
    cfg.bots = bots
    app = MagicMock()
    app.config = cfg
    app.audit_store = None
    return app


class TestBotSelectorFrontend:
    """Unit tests for the M6 bot selector backend — /soc/v1/bots + bot_id filtering."""

    @pytest.mark.asyncio
    async def test_bots_returns_correct_structure(self):
        bots = {
            "openclaw": _make_m6_bot_config("openclaw", "OpenClaw", "agentshroud", default=True),
            "hermes": _make_m6_bot_config("hermes", "Hermes", "agentshroud-hermes", default=False),
        }
        app = _make_m6_app_state(bots)
        caller = _make_m6_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await list_bots(caller=caller)

        assert isinstance(result, list)
        assert len(result) == 2
        ids = {b["id"] for b in result}
        assert "openclaw" in ids
        assert "hermes" in ids
        for entry in result:
            assert "id" in entry
            assert "name" in entry
            assert "hostname" in entry
            assert "default" in entry

    @pytest.mark.asyncio
    async def test_single_bot_returns_list_of_one(self):
        bots = {"openclaw": _make_m6_bot_config("openclaw", "OpenClaw", "agentshroud", default=True)}
        app = _make_m6_app_state(bots)
        caller = _make_m6_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await list_bots(caller=caller)

        assert len(result) == 1
        assert result[0]["id"] == "openclaw"

    @pytest.mark.asyncio
    async def test_bots_returns_default_true_on_default_bot(self):
        bots = {
            "openclaw": _make_m6_bot_config("openclaw", "OpenClaw", "agentshroud", default=True),
            "hermes": _make_m6_bot_config("hermes", "Hermes", "agentshroud-hermes", default=False),
        }
        app = _make_m6_app_state(bots)
        caller = _make_m6_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await list_bots(caller=caller)

        by_id = {b["id"]: b for b in result}
        assert by_id["openclaw"]["default"] is True
        assert by_id["hermes"]["default"] is False

    @pytest.mark.asyncio
    async def test_security_events_filters_by_bot_id(self):
        # Router filters on e.agent_id (SecurityEvent attribute), not on the dict field.
        hermes_event = MagicMock()
        hermes_event.agent_id = "hermes"
        hermes_event.model_dump.return_value = {
            "event_id": "evt-1", "agent_id": "hermes",
            "event_type": "security_event", "severity": "info",
            "source_module": "hermes.promptguard", "summary": "prompt checked",
            "timestamp": "2026-05-29T00:00:00Z",
        }
        openclaw_event = MagicMock()
        openclaw_event.agent_id = "openclaw"
        openclaw_event.model_dump.return_value = {
            "event_id": "evt-2", "agent_id": "openclaw",
            "event_type": "security_event", "severity": "info",
            "source_module": "openclaw.promptguard", "summary": "openclaw event",
            "timestamp": "2026-05-29T00:00:00Z",
        }

        caller = _make_m6_caller()
        app = MagicMock()
        app.audit_store = None

        with (
            patch("gateway.soc.router._app_state", return_value=app),
            patch(
                "gateway.soc.event_adapter.collect_recent_events",
                new=AsyncMock(return_value=[hermes_event, openclaw_event]),
            ),
        ):
            result = await get_security_events(limit=50, severity=None, bot_id="hermes", caller=caller)

        assert len(result) == 1
        assert result[0]["agent_id"] == "hermes"

    @pytest.mark.asyncio
    async def test_security_events_nonexistent_bot_returns_empty_not_404(self):
        evt = MagicMock()
        evt.agent_id = "openclaw"
        evt.model_dump.return_value = {
            "event_id": "evt-3", "agent_id": "openclaw",
            "event_type": "security_event", "severity": "info",
            "source_module": "openclaw.module", "summary": "some event",
            "timestamp": "2026-05-29T00:00:00Z",
        }

        caller = _make_m6_caller()
        app = MagicMock()
        app.audit_store = None

        with (
            patch("gateway.soc.router._app_state", return_value=app),
            patch(
                "gateway.soc.event_adapter.collect_recent_events",
                new=AsyncMock(return_value=[evt]),
            ),
        ):
            result = await get_security_events(limit=50, severity=None, bot_id="nonexistent", caller=caller)

        assert isinstance(result, list)
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_bots_backward_compat_no_bots_config(self):
        app = MagicMock()
        app.config = MagicMock()
        app.config.bots = {}
        caller = _make_m6_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await list_bots(caller=caller)

        assert len(result) == 1
        assert result[0]["id"] == "openclaw"
        assert result[0]["default"] is True

    @pytest.mark.asyncio
    async def test_bots_no_config_returns_synthetic_entry(self):
        app = MagicMock()
        app.config = None
        caller = _make_m6_caller()

        with patch("gateway.soc.router._app_state", return_value=app):
            result = await list_bots(caller=caller)

        assert len(result) == 1
        assert result[0]["id"] == "openclaw"
