# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for Resource Exhaustion Guard"""

from __future__ import annotations

import time
from unittest.mock import patch

import pytest

from gateway.security.resource_guard import ResourceGuard, ResourceLimits


class TestResourceGuard:

    def setup_method(self):
        # Use lower limits for testing
        limits = ResourceLimits(
            max_disk_writes_mb_per_minute=10,
            max_temp_files=5,
            max_open_files_per_agent=10,
        )
        self.guard = ResourceGuard(limits)

    def teardown_method(self):
        self.guard.monitoring_active = False
        task = getattr(self.guard, "_monitor_task", None)
        if task and not task.done():
            task.cancel()

    def test_check_resource_under_limit_passes(self):
        """Test that resource usage under limits passes."""
        agent_id = "test_agent"

        # Should pass when under limit
        allowed, reason = self.guard.check_resource(agent_id, "disk_writes_mb", 5)
        assert allowed is True
        assert reason == ""

    def test_check_resource_over_limit_blocked(self):
        """Test that resource usage over limits is blocked."""
        agent_id = "test_agent"

        # Exceed disk write limit
        allowed, reason = self.guard.check_resource(agent_id, "disk_writes_mb", 15)
        assert allowed is False
        assert "exceeds limit" in reason.lower()
        assert "disk_writes_mb" in reason

    def test_check_resource_temp_files_limit(self):
        """Test temp file count limiting."""
        agent_id = "test_agent"

        # Add temp files up to limit
        for i in range(5):
            allowed, _ = self.guard.check_resource(agent_id, "temp_files", 1)
            assert allowed is True

        # Should block when over limit
        allowed, reason = self.guard.check_resource(agent_id, "temp_files", 1)
        assert allowed is False
        assert "temp_files" in reason

    def test_window_expiry_resets_usage(self):
        """Test that resource usage resets after time window."""
        agent_id = "test_agent"

        # Use up most of the disk write quota
        self.guard.check_resource(agent_id, "disk_writes_mb", 9)

        # Should be near limit
        allowed, _ = self.guard.check_resource(agent_id, "disk_writes_mb", 2)
        assert allowed is False

        # Simulate time passing (60+ seconds)
        usage = self.guard.usage_by_agent[agent_id]
        usage.last_reset = time.time() - 70  # 70 seconds ago

        # Should now allow the request
        allowed, _ = self.guard.check_resource(agent_id, "disk_writes_mb", 2)
        assert allowed is True

    def test_request_count_limiting(self):
        """Test request count per minute limiting."""
        agent_id = "test_agent"

        # Default limit is 300 requests per minute in ResourceLimits
        # For testing, let's manually set a lower limit
        self.guard.limits.max_requests_per_minute = 3

        # Should allow first few requests
        for i in range(3):
            allowed, _ = self.guard.check_resource(agent_id, "requests", 1)
            assert allowed is True

        # Should block additional requests
        allowed, reason = self.guard.check_resource(agent_id, "requests", 1)
        assert allowed is False
        assert "requests" in reason.lower()

    @patch("gateway.security.resource_guard.psutil")
    def test_system_resource_monitoring_alerts_after_debounce(self, mock_psutil):
        """Sustained high CPU fires the alert after debounce samples are crossed."""
        mock_psutil.cpu_percent.return_value = 95.0
        mock_psutil.virtual_memory.return_value.percent = 50.0  # below memory threshold

        # Force tight debounce for a deterministic assertion.
        self.guard.limits.alert_spike_debounce_samples = 2
        self.guard._cpu_over_count = 0

        with patch.object(self.guard, "_alert_high_usage") as mock_alert:
            self.guard._check_system_resources()
            assert mock_alert.call_count == 0, "First over-threshold sample must not alert"
            self.guard._check_system_resources()
            assert (
                mock_alert.call_count == 1
            ), "Second consecutive over-threshold sample fires the alert"

    @patch("gateway.security.resource_guard.psutil")
    def test_brief_spike_below_debounce_does_not_alert(self, mock_psutil):
        """A single over-threshold sample followed by an under-threshold sample is suppressed."""
        self.guard.limits.alert_spike_debounce_samples = 3
        self.guard._cpu_over_count = 0
        mock_psutil.virtual_memory.return_value.percent = 50.0  # quiet memory side

        with patch.object(self.guard, "_alert_high_usage") as mock_alert:
            mock_psutil.cpu_percent.return_value = 95.0
            self.guard._check_system_resources()  # 1st over
            mock_psutil.cpu_percent.return_value = 10.0
            self.guard._check_system_resources()  # under-threshold → resets counter
            mock_psutil.cpu_percent.return_value = 95.0
            self.guard._check_system_resources()  # 1st over again
            mock_psutil.cpu_percent.return_value = 95.0
            self.guard._check_system_resources()  # 2nd over (still below 3)
            assert (
                mock_alert.call_count == 0
            ), "Brief spikes that don't accumulate must not produce alerts"

    def test_multiple_agents_isolated(self):
        """Test that different agents have isolated resource tracking."""
        agent1 = "agent_1"
        agent2 = "agent_2"

        # Agent 1 uses resources
        self.guard.check_resource(agent1, "disk_writes_mb", 8)

        # Agent 2 should still have full quota
        allowed, _ = self.guard.check_resource(agent2, "disk_writes_mb", 8)
        assert allowed is True

        # Agent 1 should be near limit
        allowed, _ = self.guard.check_resource(agent1, "disk_writes_mb", 3)
        assert allowed is False

    def test_invalid_resource_type(self):
        """Test handling of invalid resource types."""
        agent_id = "test_agent"

        with pytest.raises((KeyError, ValueError)):
            self.guard.check_resource(agent_id, "invalid_resource", 1)

    def test_resource_guard_config(self):
        """Test ResourceGuardConfig dataclass."""
        # Test default values
        config = ResourceLimits()
        assert config.max_disk_writes_mb_per_minute == 100
        assert config.max_temp_files == 1000
        assert hasattr(
            config, "max_requests_per_minute"
        )  # Should have this field based on requirements

        # Test custom values
        custom_config = ResourceLimits(max_disk_writes_mb_per_minute=50, max_temp_files=500)
        assert custom_config.max_disk_writes_mb_per_minute == 50
        assert custom_config.max_temp_files == 500

    @pytest.mark.asyncio
    async def test_stop_cancels_monitor_task(self):
        """stop() should cancel background monitor cleanly."""
        guard = ResourceGuard(ResourceLimits())
        await guard.stop()
        task = getattr(guard, "_monitor_task", None)
        if task:
            assert task.cancelled() or task.done()
