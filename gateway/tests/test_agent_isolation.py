# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for gateway/security/agent_isolation.py — verify shared-nothing isolation."""

from __future__ import annotations

import pytest

from gateway.security.agent_isolation import (
    AgentRegistry,
    ContainerConfig,
    IsolationCheck,
    IsolationStatus,
    IsolationVerifier,
)


def _make_config(agent_id: str, **overrides) -> ContainerConfig:
    """Helper to create a ContainerConfig with sensible defaults."""
    defaults = dict(
        agent_id=agent_id,
        container_name=f"ctr-{agent_id}",
        network=f"net-{agent_id}",
        volume=f"vol-{agent_id}",
        image="agentshroud/agent:latest",
    )
    defaults.update(overrides)
    return ContainerConfig(**defaults)


# ---------------------------------------------------------------------------
# AgentRegistry CRUD
# ---------------------------------------------------------------------------


class TestAgentRegistry:
    def test_register_and_get(self):
        reg = AgentRegistry()
        cfg = _make_config("bot-a")
        reg.register(cfg)
        assert reg.get("bot-a") is cfg

    def test_get_missing_returns_none(self):
        reg = AgentRegistry()
        assert reg.get("nonexistent") is None

    def test_unregister_removes_agent(self):
        reg = AgentRegistry()
        cfg = _make_config("bot-a")
        reg.register(cfg)
        removed = reg.unregister("bot-a")
        assert removed is cfg
        assert reg.get("bot-a") is None

    def test_unregister_missing_returns_none(self):
        reg = AgentRegistry()
        assert reg.unregister("ghost") is None

    def test_list_agents(self):
        reg = AgentRegistry()
        reg.register(_make_config("x"))
        reg.register(_make_config("y"))
        assert sorted(reg.list_agents()) == ["x", "y"]

    def test_serialization_roundtrip(self):
        reg = AgentRegistry()
        reg.register(_make_config("bot-a"))
        reg.register(_make_config("bot-b"))
        data = reg.to_dict()
        reg2 = AgentRegistry.from_dict(data)
        assert sorted(reg2.list_agents()) == ["bot-a", "bot-b"]
        assert reg2.get("bot-a").network == "net-bot-a"


# ---------------------------------------------------------------------------
# IsolationVerifier — network isolation
# ---------------------------------------------------------------------------


class TestNetworkIsolation:
    def test_separate_networks_pass(self):
        reg = AgentRegistry()
        reg.register(_make_config("a", network="net-a"))
        reg.register(_make_config("b", network="net-b"))
        results = IsolationVerifier(reg).verify_network_isolation()
        for r in results:
            assert r.status == IsolationStatus.ISOLATED
            assert not r.issues

    def test_shared_network_detected(self):
        reg = AgentRegistry()
        reg.register(_make_config("a", network="shared"))
        reg.register(_make_config("b", network="shared"))
        results = IsolationVerifier(reg).verify_network_isolation()
        violations = [r for r in results if r.status == IsolationStatus.VIOLATION]
        assert len(violations) >= 1, "Shared network must be flagged"


# ---------------------------------------------------------------------------
# IsolationVerifier — volume isolation
# ---------------------------------------------------------------------------


class TestVolumeIsolation:
    def test_separate_volumes_pass(self):
        reg = AgentRegistry()
        reg.register(_make_config("a", volume="vol-a"))
        reg.register(_make_config("b", volume="vol-b"))
        results = IsolationVerifier(reg).verify_volume_isolation()
        for r in results:
            assert r.status == IsolationStatus.ISOLATED

    def test_shared_volume_detected(self):
        reg = AgentRegistry()
        reg.register(_make_config("a", volume="shared-vol"))
        reg.register(_make_config("b", volume="shared-vol"))
        results = IsolationVerifier(reg).verify_volume_isolation()
        violations = [r for r in results if r.status == IsolationStatus.VIOLATION]
        assert len(violations) >= 1, "Shared volume must be flagged"


# ---------------------------------------------------------------------------
# IsolationVerifier — shared-nothing (full check)
# ---------------------------------------------------------------------------


class TestSharedNothing:
    def test_fully_isolated_agents_pass(self):
        reg = AgentRegistry()
        reg.register(_make_config("a"))
        reg.register(_make_config("b"))
        results = IsolationVerifier(reg).verify_shared_nothing()
        for r in results:
            assert r.status == IsolationStatus.ISOLATED
            assert not r.issues

    def test_shared_network_flagged_in_full_check(self):
        reg = AgentRegistry()
        reg.register(_make_config("a", network="same-net"))
        reg.register(_make_config("b", network="same-net"))
        results = IsolationVerifier(reg).verify_shared_nothing()
        violations = [r for r in results if r.issues]
        assert len(violations) > 0

    def test_shared_volume_flagged_in_full_check(self):
        reg = AgentRegistry()
        reg.register(_make_config("a", volume="same-vol"))
        reg.register(_make_config("b", volume="same-vol"))
        results = IsolationVerifier(reg).verify_shared_nothing()
        violations = [r for r in results if r.issues]
        assert len(violations) > 0

    def test_writable_root_flagged(self):
        reg = AgentRegistry()
        reg.register(_make_config("a", read_only_root=False))
        results = IsolationVerifier(reg).verify_shared_nothing()
        issues = results[0].issues
        assert any("read-only" in i.lower() or "root" in i.lower() for i in issues)

    def test_new_privileges_allowed_flagged(self):
        reg = AgentRegistry()
        reg.register(_make_config("a", no_new_privileges=False))
        results = IsolationVerifier(reg).verify_shared_nothing()
        issues = results[0].issues
        assert any("privilege" in i.lower() for i in issues)

    def test_capabilities_not_dropped_flagged(self):
        reg = AgentRegistry()
        reg.register(_make_config("a", capabilities_drop=[]))
        results = IsolationVerifier(reg).verify_shared_nothing()
        issues = results[0].issues
        assert any("capabilit" in i.lower() for i in issues)

    def test_single_agent_fully_secure(self):
        """A single properly-configured agent should have zero issues."""
        reg = AgentRegistry()
        reg.register(_make_config("solo"))
        results = IsolationVerifier(reg).verify_shared_nothing()
        assert len(results) == 1
        assert results[0].status == IsolationStatus.ISOLATED


# ---------------------------------------------------------------------------
# IsolationVerifier — Docker Compose generation
# ---------------------------------------------------------------------------


class TestGenerateCompose:
    def test_compose_contains_all_agents(self):
        reg = AgentRegistry()
        reg.register(_make_config("a"))
        reg.register(_make_config("b"))
        compose = IsolationVerifier(reg).generate_compose()
        assert "agent-a" in compose["services"]
        assert "agent-b" in compose["services"]

    def test_compose_networks_are_internal(self):
        reg = AgentRegistry()
        reg.register(_make_config("a"))
        compose = IsolationVerifier(reg).generate_compose()
        for net_cfg in compose["networks"].values():
            assert net_cfg.get("internal") is True

    def test_compose_security_opts(self):
        reg = AgentRegistry()
        reg.register(_make_config("a"))
        compose = IsolationVerifier(reg).generate_compose()
        svc = compose["services"]["agent-a"]
        assert svc["read_only"] is True
        assert any("no-new-privileges" in s for s in svc["security_opt"])
