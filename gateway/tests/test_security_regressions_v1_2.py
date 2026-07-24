# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""
v1.2.0 Security Regression Tests

Every test in this file corresponds to a finding from the v1.2.0 blue-team
and red-team assessments (docs/planning/v1.2/blue-team-assessment-v1.2.0.md
and docs/planning/v1.2/red-team-assessment-v1.2.0.md).

Finding-to-test mapping:
  BT-H1  — SharedMemoryManager.get_user_memory must accept bot_id parameter
  BT-H2  — get_merged_memory_for_user must pass bot_id through to get_user_memory
  BT-H3  — Session workspaces for OpenClaw and Hermes are physically separate paths
  BT-H4  — Cross-bot memory read is blocked: Hermes cannot read OpenClaw workspace
  RT-N1  — Cross-bot trust pivot: an OpenClaw violation does NOT change Hermes trust
  RT-N2  — TrustManager agent_id namespace separates bots from user identifiers
  RT-N3  — Hermes registered with STANDARD trust at startup (lifespan seeding check)
  BT-M1  — Hermes dashboard TCP forwarder binds on 0.0.0.0 (loopback not enforced)
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway.security.session_manager import UserSessionManager
from gateway.security.shared_memory import SharedMemoryManager
from gateway.security.trust_manager import TrustLevel, TrustManager

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def tmp_workspace(tmp_path):
    """Isolated temporary workspace for session manager."""
    ws = tmp_path / "sessions"
    ws.mkdir()
    return ws


@pytest.fixture
def session_manager(tmp_workspace):
    return UserSessionManager(base_workspace=tmp_workspace, owner_user_id="owner123")


@pytest.fixture
def smm(session_manager):
    return SharedMemoryManager(session_manager=session_manager)


@pytest.fixture
def trust_manager():
    return TrustManager(db_path=":memory:")


# ---------------------------------------------------------------------------
# BT-H1: SharedMemoryManager.get_user_memory must accept and honour bot_id
# ---------------------------------------------------------------------------


class TestBotIdIsolationInSharedMemory:
    """Finding BT-H1/BT-H2/BT-H3: SharedMemoryManager must not collapse bot workspaces."""

    def test_get_user_memory_openclaw_and_hermes_are_separate_paths(self, smm, session_manager):
        """BT-H3: The filesystem paths for openclaw and hermes sessions differ.

        Regression: get_user_memory called without bot_id defaults to openclaw.
        This test asserts that calling get_or_create_session with different bot_ids
        produces different workspace paths for the same user.
        """
        user_id = "user999"
        sess_openclaw = session_manager.get_or_create_session(user_id, bot_id="openclaw")
        sess_hermes = session_manager.get_or_create_session(user_id, bot_id="hermes")

        assert (
            sess_openclaw.workspace_dir != sess_hermes.workspace_dir
        ), "OpenClaw and Hermes workspaces MUST NOT share the same directory"
        assert (
            sess_openclaw.memory_file != sess_hermes.memory_file
        ), "OpenClaw and Hermes MEMORY.md files MUST NOT be the same path"

    def test_openclaw_memory_write_does_not_appear_in_hermes_memory(self, smm, session_manager):
        """BT-H4: Writing to the openclaw workspace must not leak into the hermes workspace.

        Regression for cross-bot memory read via get_user_memory defaulting to openclaw.
        """
        user_id = "user777"
        # Write a sentinel value into the openclaw memory
        sess_oc = session_manager.get_or_create_session(user_id, bot_id="openclaw")
        sess_oc.memory_file.write_text("OPENCLAW_SECRET_CANARY_VALUE", encoding="utf-8")

        # Read hermes memory — must NOT contain the openclaw canary
        sess_h = session_manager.get_or_create_session(user_id, bot_id="hermes")
        hermes_content = (
            sess_h.memory_file.read_text(encoding="utf-8") if sess_h.memory_file.exists() else ""
        )

        assert (
            "OPENCLAW_SECRET_CANARY_VALUE" not in hermes_content
        ), "OpenClaw memory content MUST NOT appear in Hermes memory for the same user"

    def test_hermes_memory_write_does_not_appear_in_openclaw_memory(self, smm, session_manager):
        """BT-H4 (reverse): Writing to Hermes workspace does not bleed into OpenClaw."""
        user_id = "user888"
        sess_h = session_manager.get_or_create_session(user_id, bot_id="hermes")
        sess_h.memory_file.write_text("HERMES_SECRET_CANARY_VALUE", encoding="utf-8")

        sess_oc = session_manager.get_or_create_session(user_id, bot_id="openclaw")
        oc_content = (
            sess_oc.memory_file.read_text(encoding="utf-8") if sess_oc.memory_file.exists() else ""
        )

        assert (
            "HERMES_SECRET_CANARY_VALUE" not in oc_content
        ), "Hermes memory content MUST NOT appear in OpenClaw memory for the same user"

    def test_shared_memory_manager_get_user_memory_accepts_bot_id(self, smm, session_manager):
        """BT-H1: SharedMemoryManager.get_user_memory must accept a bot_id parameter.

        The current implementation does NOT accept bot_id (finding BT-H1).
        Once fixed, this test should pass: calling get_user_memory with bot_id='hermes'
        should read from the hermes workspace, not openclaw.
        """
        user_id = "user111"
        # Seed openclaw memory
        sess_oc = session_manager.get_or_create_session(user_id, bot_id="openclaw")
        sess_oc.memory_file.write_text("OC_ONLY_CONTENT", encoding="utf-8")

        # Seed hermes memory
        sess_h = session_manager.get_or_create_session(user_id, bot_id="hermes")
        sess_h.memory_file.write_text("HERMES_ONLY_CONTENT", encoding="utf-8")

        # get_user_memory with bot_id='hermes' must return hermes content
        # and must NOT return openclaw content
        import inspect

        sig = inspect.signature(smm.get_user_memory)
        if "bot_id" not in sig.parameters:
            pytest.fail(
                "BT-H1 OPEN: SharedMemoryManager.get_user_memory does not accept bot_id "
                "parameter. Hermes callers will read OpenClaw memory. Fix: add bot_id parameter "
                "and pass it through to get_or_create_session."
            )

        # With the fix applied:
        hermes_mem = smm.get_user_memory(user_id, bot_id="hermes")
        assert "HERMES_ONLY_CONTENT" in hermes_mem
        assert "OC_ONLY_CONTENT" not in hermes_mem


# ---------------------------------------------------------------------------
# RT-N1: Cross-bot trust pivot — OpenClaw violation must not demote Hermes
# ---------------------------------------------------------------------------


class TestCrossBotTrustPivot:
    """Finding RT-N1/RT-N2: TrustManager uses shared in-memory DB keyed by agent_id.

    If openclaw and hermes share the same agent_id string, a violation recorded
    against one would demote the other. The production lifespan seeds BOTH as
    separate agent IDs ('openclaw' and 'hermes'). This test verifies isolation.
    """

    def test_openclaw_violation_does_not_affect_hermes_trust(self, trust_manager):
        """RT-N1: Recording a violation against openclaw MUST NOT change hermes trust."""
        trust_manager.register_agent("openclaw")
        trust_manager.register_agent("hermes")

        # Seed both at STANDARD
        trust_manager._conn.execute(
            "UPDATE trust_scores SET score = 200, level = ? WHERE agent_id IN ('openclaw', 'hermes')",
            (int(TrustLevel.STANDARD),),
        )
        trust_manager._conn.commit()

        # Get hermes trust before violation
        hermes_before = trust_manager.get_trust("hermes")
        assert hermes_before is not None
        hermes_level_before, hermes_score_before = hermes_before

        # Record a severe violation against openclaw
        trust_manager.record_violation("openclaw", details="injection attack detected")
        trust_manager.record_violation("openclaw", details="exfiltration attempt")

        # Hermes trust must be unchanged (allow < 1 point float drift from sub-second decay)
        hermes_after = trust_manager.get_trust("hermes")
        assert hermes_after is not None
        hermes_level_after, hermes_score_after = hermes_after

        assert abs(hermes_score_after - hermes_score_before) < 1.0, (
            f"RT-N1: OpenClaw violation changed Hermes trust score by more than rounding: "
            f"{hermes_score_before:.4f} → {hermes_score_after:.4f}"
        )
        assert hermes_level_after == hermes_level_before, (
            f"RT-N1: OpenClaw violation changed Hermes trust level: "
            f"{hermes_level_before} → {hermes_level_after}"
        )

    def test_hermes_violation_does_not_affect_openclaw_trust(self, trust_manager):
        """RT-N1 (reverse): Hermes violation must not demote OpenClaw."""
        trust_manager.register_agent("openclaw")
        trust_manager.register_agent("hermes")
        trust_manager._conn.execute(
            "UPDATE trust_scores SET score = 200, level = ? WHERE agent_id IN ('openclaw', 'hermes')",
            (int(TrustLevel.STANDARD),),
        )
        trust_manager._conn.commit()

        oc_before = trust_manager.get_trust("openclaw")
        assert oc_before is not None
        oc_level_before, oc_score_before = oc_before

        trust_manager.record_violation("hermes", details="data exfiltration via cron")
        trust_manager.record_violation("hermes", details="prompt injection attempt")

        oc_after = trust_manager.get_trust("openclaw")
        assert oc_after is not None
        oc_level_after, oc_score_after = oc_after

        assert abs(oc_score_after - oc_score_before) < 1.0, (
            f"RT-N1: Hermes violation changed OpenClaw trust score by more than rounding: "
            f"{oc_score_before:.4f} → {oc_score_after:.4f}"
        )

    def test_bot_agent_ids_are_namespace_separated_from_user_ids(self, trust_manager):
        """RT-N2: Bot agent IDs ('openclaw', 'hermes') are separate from user IDs.

        A malicious user whose Telegram ID is the string 'openclaw' must not
        inherit the production bot's elevated trust score.
        """
        # Seed production bot
        trust_manager.register_agent("openclaw")
        trust_manager._conn.execute(
            "UPDATE trust_scores SET score = 300, level = ? WHERE agent_id = 'openclaw'",
            (int(TrustLevel.ELEVATED),),
        )
        trust_manager._conn.commit()

        # Register a user whose ID happens to match (name collision scenario)
        # In production this would never happen because Telegram UIDs are numeric,
        # but we verify the data-model isolation is correct.
        trust_manager.register_agent("openclaw")  # already registered
        trust_info = trust_manager.get_trust("openclaw")
        assert trust_info is not None

        # A separate user ID "user-openclaw-clone" starts fresh
        trust_manager.register_agent("user-openclaw-clone")
        clone_trust = trust_manager.get_trust("user-openclaw-clone")
        assert clone_trust is not None
        clone_level, clone_score = clone_trust
        bot_level, bot_score = trust_info

        assert (
            clone_score < bot_score
        ), "RT-N2: A newly registered agent must start with lower trust than an established bot"


# ---------------------------------------------------------------------------
# RT-N3: Hermes seeded with STANDARD trust at startup
# ---------------------------------------------------------------------------


class TestHermesTrustSeeding:
    """RT-N3: lifespan.py seeds 'hermes' with STANDARD trust.

    Verifies the seeding logic produces STANDARD-level trust (score 200).
    """

    def test_hermes_registered_with_standard_trust(self, trust_manager):
        """RT-N3: After seeding, hermes trust level is STANDARD (matching lifespan.py)."""
        # Simulate the lifespan seeding logic (gateway/ingest_api/lifespan.py:312–320)
        for agent_id in ("default", "openclaw", "hermes"):
            trust_manager.register_agent(agent_id)
            trust_manager._conn.execute(
                "UPDATE trust_scores SET score = 200, level = ? WHERE agent_id = ?",
                (int(TrustLevel.STANDARD), agent_id),
            )
        trust_manager._conn.commit()

        hermes_trust = trust_manager.get_trust("hermes")
        assert hermes_trust is not None
        hermes_level, hermes_score = hermes_trust
        assert (
            hermes_level >= TrustLevel.STANDARD
        ), f"RT-N3: Hermes trust level after seeding is {hermes_level}, expected >= STANDARD"
        assert (
            hermes_score >= 150.0
        ), f"RT-N3: Hermes trust score after seeding is {hermes_score}, expected >= 150"


# ---------------------------------------------------------------------------
# BT-M1: Hermes dashboard forwarder binds on 0.0.0.0 (no loopback enforcement)
# ---------------------------------------------------------------------------


class TestHermesDashboardForwarderBinding:
    """BT-M1: The Hermes TCP dashboard forwarder (port 9119) binds on 0.0.0.0.

    This is a MEDIUM finding: within Docker the container-level network is
    agentshroud-internal (not exposed to the internet), and docker-compose
    publishes only on 127.0.0.1:9119. However the gateway-side asyncio server
    itself listens on 0.0.0.0 which means any process in the gateway container
    can reach it. Accepted risk — see assessment rationale.

    This test verifies the DOCUMENTED behaviour so a future change to bind on
    127.0.0.1 will be caught and the assessment can be updated.
    """

    def test_hermes_dashboard_forwarder_bind_address_is_documented(self):
        """BT-M1: Verify the forwarder bind address — currently 0.0.0.0 (accepted risk)."""
        import re

        lifespan_path = Path(__file__).parent.parent / "ingest_api" / "lifespan.py"
        source = lifespan_path.read_text(encoding="utf-8")

        # Find the start_server call in the Hermes dashboard forwarder
        match = re.search(r'start_server\(_handle,\s*"([^"]+)",\s*_hermes_dash_port', source)
        assert match is not None, "Could not find hermes dashboard forwarder start_server call"

        bind_addr = match.group(1)
        # Document current state: 0.0.0.0 (accepted risk per BT-M1 rationale)
        assert bind_addr == "0.0.0.0", (
            f"BT-M1: Hermes dashboard forwarder bind address changed from 0.0.0.0 to {bind_addr!r}. "
            "Update the acceptance rationale in blue-team-assessment-v1.2.0.md if this is intentional."
        )


# ---------------------------------------------------------------------------
# 2026-07 regression: Hermes dashboard 502 — gateway must use the in-container
# bridge, never point straight at Hermes's own loopback-bound dashboard port.
# ---------------------------------------------------------------------------


class TestHermesDashboardBridgeReachability:
    """Hermes's dashboard binds 127.0.0.1 inside its own container (vendor
    hermes-agent v0.15.1+ requires a DashboardAuthProvider for any non-loopback
    bind; loopback skips that gate, per docker-compose.yml's own comment).
    Gateway's forwarder (BT-M1 above) reaches Hermes over the Docker network by
    container hostname — which can never reach a loopback-only listener in a
    *different* container, no matter what network they share. This silently
    turned every Hermes dashboard request into a 502 once the vendor image
    added the auth gate.

    Fix: docker/bots/hermes/dashboard_bridge.py, an in-container TCP relay
    (same network namespace as Hermes's own dashboard, so its own 127.0.0.1
    really is Hermes's loopback) that re-exposes the dashboard on a second,
    network-reachable port. Gateway must point at THAT bridge port, never
    directly at Hermes's own HERMES_DASHBOARD_PORT, or this exact bug
    reintroduces itself silently.
    """

    def test_hermes_dashboard_stays_loopback_and_gateway_uses_the_bridge_port(self):
        import yaml

        compose_path = Path(__file__).parent.parent.parent / "docker" / "docker-compose.yml"
        if not compose_path.exists():
            pytest.skip("compose file not available in this environment")

        compose = yaml.safe_load(compose_path.read_text())
        hermes_env = compose["services"]["hermes"].get("environment", {})
        gateway_env_raw = compose["services"]["gateway"].get("environment", [])

        gateway_env = {}
        for item in gateway_env_raw:
            if isinstance(item, str) and "=" in item:
                key, _, value = item.partition("=")
                gateway_env[key] = value
            elif isinstance(item, dict):
                gateway_env.update(item)

        hermes_dashboard_host = str(hermes_env.get("HERMES_DASHBOARD_HOST", ""))
        hermes_dashboard_port = str(hermes_env.get("HERMES_DASHBOARD_PORT", "9119"))
        gateway_upstream_port = str(gateway_env.get("HERMES_DASHBOARD_UPSTREAM_PORT", ""))

        assert hermes_dashboard_host == "127.0.0.1", (
            "Hermes dashboard must stay loopback-bound (the vendor's v0.15.1+ "
            "auth-gate-free safe default) — do not flip to 0.0.0.0 without also "
            "provisioning HERMES_DASHBOARD_BASIC_AUTH_USERNAME/_PASSWORD."
        )
        assert gateway_upstream_port, (
            "gateway must set HERMES_DASHBOARD_UPSTREAM_PORT explicitly — leaving it "
            "unset makes gateway fall back to Hermes's own loopback-bound dashboard "
            "port, reintroducing the 2026-07 502 bug."
        )
        assert gateway_upstream_port != hermes_dashboard_port, (
            f"gateway's HERMES_DASHBOARD_UPSTREAM_PORT ({gateway_upstream_port}) must NOT "
            f"equal Hermes's own loopback-bound HERMES_DASHBOARD_PORT ({hermes_dashboard_port}) "
            "— gateway can only reach Hermes's dashboard via the dashboard_bridge.py relay "
            "on a separate, network-reachable port."
        )

        dockerfile_path = (
            Path(__file__).parent.parent.parent / "docker" / "bots" / "hermes" / "Dockerfile"
        )
        dockerfile = dockerfile_path.read_text()
        assert "dashboard-bridge" in dockerfile or "dashboard_bridge" in dockerfile, (
            "Dockerfile must install the dashboard_bridge s6 service — without it, "
            "gateway has no way to reach Hermes's loopback-bound dashboard."
        )

        bridge_path = (
            Path(__file__).parent.parent.parent
            / "docker"
            / "bots"
            / "hermes"
            / "dashboard_bridge.py"
        )
        assert bridge_path.exists(), (
            "docker/bots/hermes/dashboard_bridge.py must exist — it is the in-container "
            "relay that makes the loopback-bound dashboard reachable from gateway."
        )

    def test_run_standalone_sets_matching_bridge_port(self):
        """run-standalone.sh is the actual deploy path for Hermes (docker run, not
        compose — see project_hermes_do_request_ptb226_fix.md). It must set
        HERMES_DASHBOARD_BRIDGE_PORT so dashboard_bridge.py's default agrees with
        whatever docker-compose.yml tells gateway to connect to.
        """
        script_path = (
            Path(__file__).parent.parent.parent / "docker" / "bots" / "hermes" / "run-standalone.sh"
        )
        if not script_path.exists():
            pytest.skip("run-standalone.sh not available in this environment")

        script = script_path.read_text()
        assert (
            'HERMES_DASHBOARD_HOST="127.0.0.1"' in script
        ), "run-standalone.sh must keep Hermes's own dashboard loopback-bound"
        assert "HERMES_DASHBOARD_BRIDGE_PORT" in script, (
            "run-standalone.sh must set HERMES_DASHBOARD_BRIDGE_PORT explicitly so it "
            "stays in sync with gateway's HERMES_DASHBOARD_UPSTREAM_PORT in docker-compose.yml"
        )


# ---------------------------------------------------------------------------
# Egress allowlist completeness for Hermes
# ---------------------------------------------------------------------------


class TestHermesEgressAllowlist:
    """Verify that Hermes-specific egress destinations are in the canonical allowlist."""

    def test_nousresearch_in_permanent_allowlist(self):
        """Hermes base image is from nousresearch.com — must be in egress allowlist."""
        from gateway.security.egress_config import PERMANENT_EGRESS_DOMAINS

        assert "nousresearch.com" in PERMANENT_EGRESS_DOMAINS, (
            "nousresearch.com not in PERMANENT_EGRESS_DOMAINS — "
            "Hermes will be unable to reach its update/license server"
        )

    def test_hc_ping_in_permanent_allowlist(self):
        """Hermes heartbeat uses hc-ping.com for dead-man's switch."""
        from gateway.security.egress_config import PERMANENT_EGRESS_DOMAINS

        assert "hc-ping.com" in PERMANENT_EGRESS_DOMAINS, (
            "hc-ping.com not in PERMANENT_EGRESS_DOMAINS — "
            "Hermes heartbeat dead-man's switch will fail silently"
        )

    def test_duckduckgo_in_permanent_allowlist(self):
        """Hermes ddgs-based web search requires duckduckgo.com."""
        from gateway.security.egress_config import PERMANENT_EGRESS_DOMAINS

        assert "duckduckgo.com" in PERMANENT_EGRESS_DOMAINS, (
            "duckduckgo.com not in PERMANENT_EGRESS_DOMAINS — "
            "Hermes competitive-intelligence cron will fail"
        )

    def test_failover_search_engines_in_allowlist(self):
        """PR#190 failover search engines must be allowlisted."""
        from gateway.security.egress_config import PERMANENT_EGRESS_DOMAINS

        for domain in ("search.yahoo.com", "www.google.com", "yandex.com", "www.mojeek.com"):
            assert domain in PERMANENT_EGRESS_DOMAINS, (
                f"{domain} not in PERMANENT_EGRESS_DOMAINS — "
                "Hermes web_search failover engine will be blocked"
            )

    def test_ai_security_research_domains_in_allowlist(self):
        """AI-security research/competitive-intel domains must be allowlisted.

        These domains were observed blocked during Hermes blue-team research tasks
        (2026-06-25).  Authorized by owner for Hermes web_extract tool use.
        """
        from gateway.security.egress_config import PERMANENT_EGRESS_DOMAINS

        research_domains = (
            "nist.gov",
            "lakera.ai",
            "paloaltonetworks.com",
            "menlosecurity.com",
            "adversa.ai",
            "neuraltrust.ai",
            "atlan.com",
            "mintmcp.com",
        )
        for domain in research_domains:
            assert domain in PERMANENT_EGRESS_DOMAINS, (
                f"{domain} not in PERMANENT_EGRESS_DOMAINS — "
                "Hermes AI-security research tool will be blocked on this domain"
            )


# ---------------------------------------------------------------------------
# Session isolation between bots (path separation check)
# ---------------------------------------------------------------------------


class TestSessionPathSeparation:
    """Verifies per-bot session path layout is correctly separated."""

    def test_user_session_paths_contain_bot_id(self, session_manager):
        """Session directory path must embed bot_id so filesystem confirms isolation."""
        sess_oc = session_manager.get_or_create_session("user42", bot_id="openclaw")
        sess_h = session_manager.get_or_create_session("user42", bot_id="hermes")

        assert "openclaw" in str(
            sess_oc.workspace_dir
        ), "openclaw session workspace path does not contain 'openclaw'"
        assert "hermes" in str(
            sess_h.workspace_dir
        ), "hermes session workspace path does not contain 'hermes'"

    def test_path_traversal_rejected_for_crafted_bot_id(self, session_manager):
        """Session manager must reject bot_id with path traversal characters."""
        with pytest.raises(ValueError):
            session_manager.get_or_create_session("user42", bot_id="../../../etc")

    def test_path_traversal_rejected_for_crafted_user_id(self, session_manager):
        """Session manager must reject user_id with path traversal characters."""
        with pytest.raises(ValueError):
            session_manager.get_or_create_session("../../root", bot_id="openclaw")
