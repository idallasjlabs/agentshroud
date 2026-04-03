# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for kill switch monitoring system.

Basic test suite for KillSwitchMonitor and KillSwitchConfig.
"""

import os
import tempfile
import time
from datetime import timedelta
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from gateway.security.killswitch_config import KillSwitchConfig
from gateway.security.killswitch_monitor import KillSwitchMonitor


class TestKillSwitchConfig:
    """Test kill switch configuration."""

    def test_default_config(self):
        """Test default configuration values."""
        config = KillSwitchConfig()

        assert config.verification_interval == timedelta(days=30)
        assert config.heartbeat_interval == timedelta(minutes=5)
        assert config.heartbeat_miss_threshold == 3
        assert config.max_tool_calls_per_minute == 20
        assert config.max_tokens_per_hour == 100000
        assert config.dry_run_enabled is False  # enforce mode: dry_run disabled (v0.8.0)
        assert config.alert_severity == "CRITICAL"


class TestKillSwitchMonitor:
    """Test kill switch monitor functionality."""

    def test_init(self):
        """Test monitor initialization."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            config = KillSwitchConfig()
            config.verification_log_path = tmp_path / "verification.jsonl"
            config.heartbeat_log_path = tmp_path / "heartbeat.jsonl"

            monitor = KillSwitchMonitor(config=config)

            assert monitor.config == config
            assert monitor._consecutive_heartbeat_misses == 0
            assert len(monitor._verification_results) == 0
            assert len(monitor._heartbeat_history) == 0

    def test_verify_killswitch_script_not_exists(self):
        """Test verification when kill switch script does not exist."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            config = KillSwitchConfig()
            config.killswitch_script_path = Path("/nonexistent/script.sh")
            config.verification_log_path = tmp_path / "verification.jsonl"
            config.heartbeat_log_path = tmp_path / "heartbeat.jsonl"

            monitor = KillSwitchMonitor(config=config)
            result = monitor.verify_killswitch(dry_run=True)

            assert result["overall_status"] in ["FAIL", "PARTIAL"]
            assert "script_exists" in result["tests"]
            assert result["tests"]["script_exists"]["status"] == "FAIL"

    def test_heartbeat_check(self):
        """Test basic heartbeat functionality."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            config = KillSwitchConfig()
            config.verification_log_path = tmp_path / "verification.jsonl"
            config.heartbeat_log_path = tmp_path / "heartbeat.jsonl"

            monitor = KillSwitchMonitor(config=config)

            with (
                patch("psutil.cpu_percent", return_value=25.0),
                patch("psutil.virtual_memory") as mock_vm,
                patch("psutil.disk_usage") as mock_disk,
                patch("psutil.pids", return_value=list(range(100))),
                patch("os.getloadavg", return_value=[0.1, 0.2, 0.3]),
            ):

                mock_vm.return_value = Mock(percent=50.0, used=512 * 1024 * 1024)
                mock_disk.return_value = Mock(percent=30.0)

                result = monitor.heartbeat_check()

            assert "status" in result
            assert "system_stats" in result
            # Verify that log file was created
            assert config.heartbeat_log_path.exists()

    def test_anomaly_detection_normal(self):
        """Test anomaly detection with normal metrics."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            config = KillSwitchConfig()
            config.verification_log_path = tmp_path / "verification.jsonl"
            config.heartbeat_log_path = tmp_path / "heartbeat.jsonl"

            monitor = KillSwitchMonitor(config=config)

            # Mock system stats to ensure they dont trigger anomalies
            with (
                patch("psutil.cpu_percent", return_value=25.0),
                patch("psutil.virtual_memory") as mock_vm,
                patch("psutil.disk_usage") as mock_disk,
                patch("psutil.pids", return_value=list(range(100))),
                patch("os.getloadavg", return_value=[0.1, 0.2, 0.3]),
            ):

                mock_vm.return_value = Mock(
                    percent=50.0, used=512 * 1024 * 1024
                )  # 512MB - below threshold
                mock_disk.return_value = Mock(percent=30.0)

                result = monitor.anomaly_detection(tool_calls=5, tokens_used=1000, requests=10)

            assert result["overall_status"] == "NORMAL"
            assert len(result["anomalies_detected"]) == 0
            assert "metrics" in result

    def test_anomaly_detection_excessive_tool_calls(self):
        """Test anomaly detection with excessive tool calls."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            config = KillSwitchConfig()
            config.verification_log_path = tmp_path / "verification.jsonl"
            config.heartbeat_log_path = tmp_path / "heartbeat.jsonl"

            monitor = KillSwitchMonitor(config=config)

            # Simulate many tool calls
            now = time.time()
            for i in range(25):  # Exceeds max_tool_calls_per_minute (20)
                monitor._tool_call_timestamps.append(now - i)

            result = monitor.anomaly_detection()

            assert result["overall_status"] == "ANOMALY_DETECTED"
            assert len(result["anomalies_detected"]) > 0
            assert any(a["type"] == "excessive_tool_calls" for a in result["anomalies_detected"])

    def test_get_status(self):
        """Test status retrieval."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            config = KillSwitchConfig()
            config.verification_log_path = tmp_path / "verification.jsonl"
            config.heartbeat_log_path = tmp_path / "heartbeat.jsonl"

            monitor = KillSwitchMonitor(config=config)
            status = monitor.get_status()

            assert "timestamp" in status
            assert "config" in status
            assert "verification_status" in status
            assert "heartbeat_status" in status
            assert "anomaly_status" in status


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
