# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for sub-agent oversight and monitoring."""
from __future__ import annotations


import pytest
from gateway.security.subagent_monitor import (
    SubagentMonitor,
    SubagentMonitorConfig,
    SubagentEventType,
)


@pytest.fixture
def default_config():
    return SubagentMonitorConfig()


@pytest.fixture
def strict_config():
    return SubagentMonitorConfig(
        mode="enforce",
        max_concurrent_per_session=3,
        inherit_trust=True,
    )


@pytest.fixture
def monitor(default_config):
    return SubagentMonitor(config=default_config)


@pytest.fixture
def strict_monitor(strict_config):
    return SubagentMonitor(config=strict_config)


class TestSubagentMonitorConfig:
    def test_default_mode_is_monitor(self, default_config):
        assert default_config.mode == "monitor"

    def test_generous_concurrent_default(self, default_config):
        assert default_config.max_concurrent_per_session >= 10

    def test_trust_inheritance_default_on(self, default_config):
        assert default_config.inherit_trust is True


class TestSubagentTracking:
    def test_register_subagent(self, monitor):
        info = monitor.register_spawn(
            session_id="sess1",
            agent_id="sub1",
            parent_id="main",
            parent_trust=3,
        )
        assert info.agent_id == "sub1"
        assert info.parent_id == "main"

    def test_list_active_subagents(self, monitor):
        monitor.register_spawn("sess1", "sub1", "main", 3)
        monitor.register_spawn("sess1", "sub2", "main", 3)
        active = monitor.get_active("sess1")
        assert len(active) == 2

    def test_deregister_subagent(self, monitor):
        monitor.register_spawn("sess1", "sub1", "main", 3)
        monitor.deregister("sess1", "sub1")
        assert len(monitor.get_active("sess1")) == 0

    def test_subagent_info_has_spawn_time(self, monitor):
        info = monitor.register_spawn("sess1", "sub1", "main", 3)
        assert info.spawn_time > 0


class TestTrustInheritance:
    def test_subagent_inherits_parent_trust(self, monitor):
        info = monitor.register_spawn("sess1", "sub1", "main", 3)
        assert info.effective_trust <= 3

    def test_subagent_cannot_exceed_parent(self, monitor):
        info = monitor.register_spawn("sess1", "sub1", "main", 2)
        assert info.effective_trust <= 2

    def test_nested_subagent_inherits_chain(self, monitor):
        monitor.register_spawn("sess1", "sub1", "main", 3)
        info = monitor.register_spawn("sess1", "sub2", "sub1", 2)
        assert info.effective_trust <= 2

    def test_trust_violation_flagged(self, monitor):
        """If sub-agent tries tool above its trust, flag it."""
        monitor.register_spawn("sess1", "sub1", "main", 1)
        result = monitor.check_tool_usage(
            "sess1", "sub1", "send_email", required_trust=3
        )
        assert result.flagged is True

    def test_tool_within_trust_allowed(self, monitor):
        monitor.register_spawn("sess1", "sub1", "main", 3)
        result = monitor.check_tool_usage(
            "sess1", "sub1", "read_file", required_trust=1
        )
        assert result.flagged is False


class TestConcurrentLimits:
    def test_monitor_mode_allows_over_limit(self, monitor):
        """Monitor mode flags but allows."""
        for i in range(25):
            info = monitor.register_spawn("sess1", f"sub{i}", "main", 3)
        assert info is not None  # still allowed
        flagged = monitor.get_flagged_events("sess1")
        assert any(e.event_type == SubagentEventType.LIMIT_EXCEEDED for e in flagged)

    def test_enforce_mode_blocks_over_limit(self, strict_monitor):
        for i in range(3):
            strict_monitor.register_spawn("sess1", f"sub{i}", "main", 3)
        with pytest.raises(Exception):
            strict_monitor.register_spawn("sess1", "sub3", "main", 3)

    def test_deregister_frees_slot(self, strict_monitor):
        for i in range(3):
            strict_monitor.register_spawn("sess1", f"sub{i}", "main", 3)
        strict_monitor.deregister("sess1", "sub0")
        info = strict_monitor.register_spawn("sess1", "sub3", "main", 3)
        assert info is not None


class TestKillSwitch:
    def test_kill_switch_marks_all_for_termination(self, monitor):
        monitor.register_spawn("sess1", "sub1", "main", 3)
        monitor.register_spawn("sess1", "sub2", "main", 3)
        killed = monitor.kill_all("sess1")
        assert killed == 2
        assert len(monitor.get_active("sess1")) == 0

    def test_kill_switch_propagates_to_children(self, monitor):
        monitor.register_spawn("sess1", "sub1", "main", 3)
        monitor.register_spawn("sess1", "sub2", "sub1", 2)
        killed = monitor.kill_all("sess1")
        assert killed == 2

    def test_kill_specific_agent(self, monitor):
        monitor.register_spawn("sess1", "sub1", "main", 3)
        monitor.register_spawn("sess1", "sub2", "main", 3)
        monitor.kill_agent("sess1", "sub1")
        active = monitor.get_active("sess1")
        assert len(active) == 1
        assert active[0].agent_id == "sub2"

    def test_kill_logs_event(self, monitor):
        monitor.register_spawn("sess1", "sub1", "main", 3)
        monitor.kill_all("sess1")
        events = monitor.get_audit_log("sess1")
        assert any(e.event_type == SubagentEventType.KILLED for e in events)


class TestPermissionMonitoring:
    def test_tool_usage_logged(self, monitor):
        monitor.register_spawn("sess1", "sub1", "main", 3)
        monitor.check_tool_usage("sess1", "sub1", "web_search", required_trust=1)
        events = monitor.get_audit_log("sess1")
        assert any(e.event_type == SubagentEventType.TOOL_USED for e in events)

    def test_monitor_mode_allows_all_tools(self, monitor):
        """In monitor mode, even trust violations are allowed (just flagged)."""
        monitor.register_spawn("sess1", "sub1", "main", 1)
        result = monitor.check_tool_usage(
            "sess1", "sub1", "send_email", required_trust=3
        )
        assert result.allowed is True
        assert result.flagged is True

    def test_enforce_mode_blocks_trust_violation(self, strict_monitor):
        strict_monitor.register_spawn("sess1", "sub1", "main", 1)
        result = strict_monitor.check_tool_usage(
            "sess1", "sub1", "send_email", required_trust=3
        )
        assert result.allowed is False


class TestAuditTrail:
    def test_spawn_logged(self, monitor):
        monitor.register_spawn("sess1", "sub1", "main", 3)
        events = monitor.get_audit_log("sess1")
        assert any(e.event_type == SubagentEventType.SPAWNED for e in events)

    def test_deregister_logged(self, monitor):
        monitor.register_spawn("sess1", "sub1", "main", 3)
        monitor.deregister("sess1", "sub1")
        events = monitor.get_audit_log("sess1")
        assert any(e.event_type == SubagentEventType.TERMINATED for e in events)

    def test_audit_has_timestamps(self, monitor):
        monitor.register_spawn("sess1", "sub1", "main", 3)
        events = monitor.get_audit_log("sess1")
        assert events[0].timestamp > 0

    def test_audit_filterable_by_agent(self, monitor):
        monitor.register_spawn("sess1", "sub1", "main", 3)
        monitor.register_spawn("sess1", "sub2", "main", 3)
        events = monitor.get_audit_log("sess1", agent_id="sub1")
        assert all(e.agent_id == "sub1" for e in events)
