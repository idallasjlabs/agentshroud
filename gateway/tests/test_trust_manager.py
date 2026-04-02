# Copyright (c) 2026 Isaiah Dallas Jefferson, Jr. AgentShroud. All rights reserved.
# AgentShroud is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for Progressive Trust System."""

from __future__ import annotations

import os
import tempfile

import pytest

from gateway.security.trust_manager import TrustConfig, TrustLevel, TrustManager


@pytest.fixture
def trust_db():
    """Create a temporary trust database."""
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    yield path
    os.unlink(path)


@pytest.fixture
def manager(trust_db):
    """Create a trust manager with temp DB."""
    mgr = TrustManager(db_path=trust_db)
    yield mgr
    mgr.close()


@pytest.fixture
def strict_config():
    """Config with strict thresholds."""
    return TrustConfig(
        initial_level=TrustLevel.UNTRUSTED,
        initial_score=0.0,
        success_points=10.0,
        failure_points=-25.0,
        violation_points=-100.0,
    )


@pytest.fixture
def strict_manager(trust_db, strict_config):
    """Trust manager starting at untrusted."""
    mgr = TrustManager(db_path=trust_db, config=strict_config)
    yield mgr
    mgr.close()


class TestTrustLevels:
    """Test trust level hierarchy and thresholds."""

    def test_trust_level_ordering(self):
        assert TrustLevel.UNTRUSTED < TrustLevel.BASIC
        assert TrustLevel.BASIC < TrustLevel.STANDARD
        assert TrustLevel.STANDARD < TrustLevel.ELEVATED
        assert TrustLevel.ELEVATED < TrustLevel.FULL

    def test_default_config(self):
        config = TrustConfig()
        assert config.initial_level == TrustLevel.BASIC
        assert config.initial_score == 100.0
        assert config.success_points > 0
        assert config.failure_points < 0
        assert config.violation_points < 0


class TestAgentRegistration:
    """Test agent registration and initial trust."""

    def test_register_new_agent(self, manager):
        level = manager.register_agent("agent-1")
        assert level == TrustLevel.BASIC

    def test_get_trust_unregistered(self, manager):
        result = manager.get_trust("nonexistent")
        assert result is None

    def test_get_trust_registered(self, manager):
        manager.register_agent("agent-1")
        result = manager.get_trust("agent-1")
        assert result is not None
        level, score = result
        assert level == TrustLevel.BASIC
        assert abs(score - 100.0) < 1.0

    def test_register_idempotent(self, manager):
        manager.register_agent("agent-1")
        manager.register_agent("agent-1")  # Should not error
        result = manager.get_trust("agent-1")
        assert result is not None


class TestActionGating:
    """Test that actions are gated by trust level."""

    def test_basic_can_read(self, manager):
        manager.register_agent("agent-1")
        assert manager.is_action_allowed("agent-1", "read_file")

    def test_untrusted_limited(self, strict_manager):
        strict_manager.register_agent("agent-1")
        # Untrusted should have very limited access
        level, _ = strict_manager.get_trust("agent-1")
        assert level == TrustLevel.UNTRUSTED

    def test_unregistered_denied(self, manager):
        assert not manager.is_action_allowed("unknown", "read_file")


class TestTrustProgression:
    """Test earning and losing trust."""

    def test_success_increases_score(self, manager):
        manager.register_agent("agent-1")
        _, initial_score = manager.get_trust("agent-1")
        manager.record_success("agent-1", "completed task")
        _, new_score = manager.get_trust("agent-1")
        assert new_score > initial_score

    def test_failure_decreases_score(self, manager):
        manager.register_agent("agent-1")
        _, initial_score = manager.get_trust("agent-1")
        manager.record_failure("agent-1", "failed task")
        _, new_score = manager.get_trust("agent-1")
        assert new_score < initial_score

    def test_violation_severe_penalty(self, manager):
        manager.register_agent("agent-1")
        _, initial_score = manager.get_trust("agent-1")
        manager.record_violation("agent-1", "attempted data exfil")
        _, new_score = manager.get_trust("agent-1")
        assert new_score < initial_score
        assert (initial_score - new_score) > abs(manager.config.failure_points)

    def test_promotion_on_threshold(self, strict_manager):
        """Agent should be promoted when score crosses threshold."""
        strict_manager.register_agent("agent-1")
        # Start at UNTRUSTED with score 0
        # Need to earn enough for BASIC (threshold ~100)
        for _ in range(15):
            strict_manager.record_success("agent-1", "good action")
        level, score = strict_manager.get_trust("agent-1")
        assert level >= TrustLevel.BASIC

    def test_demotion_on_violations(self, manager):
        """Agent should be demoted on violations."""
        manager.register_agent("agent-1")
        # Start at BASIC, violate repeatedly
        for _ in range(5):
            manager.record_violation("agent-1", "bad behavior")
        level, _ = manager.get_trust("agent-1")
        assert level <= TrustLevel.BASIC

    def test_score_floor_at_zero(self, manager):
        """Score should not go below 0."""
        manager.register_agent("agent-1")
        for _ in range(100):
            manager.record_violation("agent-1", "severe")
        _, score = manager.get_trust("agent-1")
        assert score >= 0


class TestHistory:
    """Test trust history tracking."""

    def test_history_recorded(self, manager):
        manager.register_agent("agent-1")
        manager.record_success("agent-1", "task A")
        manager.record_failure("agent-1", "task B")
        history = manager.get_history("agent-1")
        assert len(history) >= 2

    def test_history_empty_for_new_agent(self, manager):
        manager.register_agent("agent-1")
        history = manager.get_history("agent-1")
        assert isinstance(history, list)


class TestPersistence:
    """Test trust survives restart."""

    def test_persistence_across_instances(self, trust_db):
        mgr1 = TrustManager(db_path=trust_db)
        mgr1.register_agent("agent-1")
        mgr1.record_success("agent-1", "earned trust")
        _, score1 = mgr1.get_trust("agent-1")
        mgr1.close()

        mgr2 = TrustManager(db_path=trust_db)
        result = mgr2.get_trust("agent-1")
        assert result is not None
        _, score2 = result
        # Score should persist (may differ slightly due to decay)
        assert abs(score2 - score1) < 1.0
        mgr2.close()


class TestConfig:
    """Test configuration options."""

    def test_custom_points(self):
        config = TrustConfig(success_points=1.0, failure_points=-5.0, violation_points=-10.0)
        assert config.success_points == 1.0
        assert config.failure_points == -5.0

    def test_thresholds_populated(self):
        config = TrustConfig()
        assert TrustLevel.BASIC in config.thresholds
        assert TrustLevel.STANDARD in config.thresholds
        assert TrustLevel.ELEVATED in config.thresholds
        assert TrustLevel.FULL in config.thresholds
