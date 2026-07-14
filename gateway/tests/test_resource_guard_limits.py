# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Behavior tests for ResourceGuard per-agent limit checks and VRAM pre-flight.

The existing resource_guard tests cover check_resource / debounce / wiring.
These cover the psutil-backed limit checks (CPU/memory/disk), the VRAM headroom
guard, temp-file tracking, usage stats, request tracking, expired-usage cleanup,
and the lazy global accessor. psutil is mocked so tests are deterministic and
host-independent — no real system probing, no sleeps.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

import gateway.security.resource_guard as rg_mod
from gateway.security.resource_guard import (
    ResourceGuard,
    ResourceLimits,
    VRAMHeadroomError,
    get_resource_guard,
)


@pytest.fixture
def guard():
    g = ResourceGuard(ResourceLimits(max_temp_files=3))
    yield g
    g.stop_monitoring()
    task = getattr(g, "_monitor_task", None)
    if task and not task.done():
        task.cancel()


class TestCpuMemoryDiskLimits:
    @patch("gateway.security.resource_guard.psutil")
    def test_cpu_limit_ok_when_under(self, mock_psutil, guard):
        proc = MagicMock()
        proc.cpu_times.return_value = MagicMock(user=1.0, system=0.5)
        mock_psutil.Process.return_value = proc
        guard.usage_by_agent["a"].cpu_seconds = 1.0  # baseline
        # 1.5 - 1.0 = 0.5s used, well under the 30s default.
        assert guard.check_cpu_limit("a") is True

    @patch("gateway.security.resource_guard.psutil")
    def test_cpu_limit_exceeded(self, mock_psutil, guard):
        proc = MagicMock()
        proc.cpu_times.return_value = MagicMock(user=40.0, system=5.0)
        mock_psutil.Process.return_value = proc
        guard.usage_by_agent["a"].cpu_seconds = 0.0
        # 45s used > 30s default → blocked.
        assert guard.check_cpu_limit("a") is False

    @patch("gateway.security.resource_guard.psutil")
    def test_cpu_limit_fails_closed_on_psutil_error(self, mock_psutil, guard):
        mock_psutil.Process.side_effect = RuntimeError("no process")
        # Fail-closed: an error denies rather than allows.
        assert guard.check_cpu_limit("a") is False

    @patch("gateway.security.resource_guard.psutil")
    def test_memory_limit_ok_and_exceeded(self, mock_psutil, guard):
        proc = MagicMock()
        proc.memory_info.return_value = MagicMock(rss=100 * 1024 * 1024)  # 100 MB
        mock_psutil.Process.return_value = proc
        guard.usage_by_agent["a"].memory_mb = 0.0
        assert guard.check_memory_limit("a") is True  # 100 MB < 512 default

        proc.memory_info.return_value = MagicMock(rss=1024 * 1024 * 1024)  # 1 GB
        assert guard.check_memory_limit("a") is False  # 1024 MB > 512 default

    @patch("gateway.security.resource_guard.psutil")
    def test_memory_limit_fails_closed_on_error(self, mock_psutil, guard):
        mock_psutil.Process.side_effect = OSError("boom")
        assert guard.check_memory_limit("a") is False

    def test_disk_write_limit_allows_when_no_baseline(self, guard):
        # If disk IO stats are empty, the check cannot compute a delta → allow.
        guard.baseline_disk_io = {}
        assert guard.check_disk_write_limit("a") is True

    @patch("gateway.security.resource_guard.psutil")
    def test_disk_write_limit_exceeded(self, mock_psutil, guard):
        guard.limits.max_disk_writes_mb_per_minute = 1
        guard.baseline_disk_io = {"write_bytes": 0}
        io = MagicMock()
        io._asdict.return_value = {"write_bytes": 50 * 1024 * 1024}  # 50 MB written
        mock_psutil.disk_io_counters.return_value = io
        assert guard.check_disk_write_limit("a") is False

    @patch("gateway.security.resource_guard.psutil")
    def test_disk_write_limit_under_threshold(self, mock_psutil, guard):
        guard.limits.max_disk_writes_mb_per_minute = 100
        guard.baseline_disk_io = {"write_bytes": 0}
        io = MagicMock()
        io._asdict.return_value = {"write_bytes": 1 * 1024 * 1024}  # 1 MB written
        mock_psutil.disk_io_counters.return_value = io
        assert guard.check_disk_write_limit("a") is True


class TestVramHeadroom:
    def test_disabled_when_threshold_zero(self, guard):
        guard.limits.max_vram_headroom_mb = 0
        # Disabled → never raises regardless of tokens/vram.
        assert guard.check_vram_headroom("a", 100000, available_vram_mb=0) is None

    def test_passes_with_sufficient_headroom(self, guard):
        guard.limits.max_vram_headroom_mb = 2000
        # available >= threshold → passes silently.
        assert guard.check_vram_headroom("a", 8000, available_vram_mb=4000) is None

    def test_rejects_insufficient_headroom(self, guard):
        guard.limits.max_vram_headroom_mb = 2000
        with pytest.raises(VRAMHeadroomError) as exc:
            guard.check_vram_headroom("a", 32000, available_vram_mb=500)
        # Error message must carry the actionable numbers for the caller/log.
        assert "500" in str(exc.value)
        assert "2000" in str(exc.value)


class TestTempFiles:
    def test_register_under_limit(self, guard):
        assert guard.register_temp_file("a", "/tmp/x1") is True
        assert guard.register_temp_file("a", "/tmp/x2") is True
        assert guard.temp_files_by_agent["a"] == ["/tmp/x1", "/tmp/x2"]

    def test_register_blocks_over_limit(self, guard):
        for i in range(3):  # limit is 3
            assert guard.register_temp_file("a", f"/tmp/f{i}") is True
        assert guard.register_temp_file("a", "/tmp/overflow") is False

    def test_cleanup_unlinks_existing_and_clears_registry(self, guard, tmp_path):
        f = tmp_path / "temp.txt"
        f.write_text("data")
        guard.register_temp_file("a", str(f))
        guard.cleanup_temp_files("a")
        assert not f.exists()
        assert "a" not in guard.temp_files_by_agent

    def test_cleanup_tolerates_missing_file(self, guard):
        guard.register_temp_file("a", "/nonexistent/path/file.txt")
        # Must not raise even though the file was never created.
        guard.cleanup_temp_files("a")
        assert "a" not in guard.temp_files_by_agent


class TestUsageStatsAndTracking:
    @patch("gateway.security.resource_guard.psutil")
    def test_start_request_tracking_records_baseline(self, mock_psutil, guard):
        proc = MagicMock()
        proc.cpu_times.return_value = MagicMock(user=2.0, system=1.0)
        proc.memory_info.return_value = MagicMock(rss=64 * 1024 * 1024)
        proc.open_files.return_value = ["f1", "f2"]
        mock_psutil.Process.return_value = proc

        rid = guard.start_request_tracking("agent-x")
        assert rid == "agent-x"
        usage = guard.usage_by_agent["agent-x"]
        assert usage.cpu_seconds == 3.0
        assert usage.memory_mb == 64.0
        assert usage.open_files_count == 2

    @patch("gateway.security.resource_guard.psutil")
    def test_start_request_tracking_survives_psutil_error(self, mock_psutil, guard):
        mock_psutil.Process.side_effect = RuntimeError("nope")
        # Should not raise; baseline stats simply stay at defaults.
        assert guard.start_request_tracking("agent-y") == "agent-y"

    def test_get_usage_stats_for_agent(self, guard):
        guard.check_resource("agent-1", "disk_writes_mb", 5)
        stats = guard.get_usage_stats("agent-1")
        assert stats["agent_id"] == "agent-1"
        assert stats["disk_writes_mb"] == 5
        assert "temp_files_count" in stats

    @patch("gateway.security.resource_guard.psutil")
    def test_get_usage_stats_system_wide(self, mock_psutil, guard):
        mock_psutil.cpu_percent.return_value = 12.5
        mock_psutil.virtual_memory.return_value.percent = 40.0
        guard.check_resource("agent-1", "requests", 1)
        stats = guard.get_usage_stats()
        assert stats["total_agents"] >= 1
        assert stats["system_cpu_percent"] == 12.5
        assert stats["limits"]["max_temp_files"] == 3


class TestExpiredUsageCleanup:
    def test_cleanup_removes_stale_agents(self, guard):
        import time

        guard.check_resource("stale", "requests", 1)
        guard.register_temp_file("stale", "/tmp/x")
        # Force the last_reset well past the 5-minute cutoff.
        guard.usage_by_agent["stale"].last_reset = time.time() - 400
        guard._cleanup_expired_usage()
        assert "stale" not in guard.usage_by_agent
        assert "stale" not in guard.temp_files_by_agent

    def test_cleanup_keeps_fresh_agents(self, guard):
        import time

        guard.check_resource("fresh", "requests", 1)
        guard.usage_by_agent["fresh"].last_reset = time.time()
        guard._cleanup_expired_usage()
        assert "fresh" in guard.usage_by_agent


class TestGlobalAccessor:
    def test_get_resource_guard_is_lazy_singleton(self):
        # Reset module global so we exercise the lazy-create branch.
        rg_mod._global_resource_guard = None
        g1 = get_resource_guard()
        g2 = get_resource_guard()
        assert g1 is g2
        g1.stop_monitoring()
