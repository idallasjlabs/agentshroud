# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Behavior tests for KillSwitchMonitor verify/heartbeat/anomaly paths.

The existing killswitch tests cover config + mode helpers. These drive the
public verify_killswitch / heartbeat_check / anomaly_detection / get_status
flows and their alert dispatch, with psutil and subprocess mocked so results are
deterministic and host-independent. Log files are written under tmp_path.
No network, no sleeps.
"""

from __future__ import annotations

import json
from datetime import timedelta
from unittest.mock import MagicMock, patch

import pytest

from gateway.security.killswitch_config import KillSwitchConfig
from gateway.security.killswitch_monitor import KillSwitchMonitor


@pytest.fixture
def config(tmp_path):
    return KillSwitchConfig(
        killswitch_script_path=tmp_path / "killswitch.sh",
        verification_log_path=tmp_path / "logs" / "verify.jsonl",
        heartbeat_log_path=tmp_path / "logs" / "heartbeat.jsonl",
    )


@pytest.fixture
def dispatcher():
    return MagicMock()


def _fake_stats(**overrides):
    stats = {
        "cpu_percent": 5.0,
        "memory_percent": 20.0,
        "memory_mb": 100,
        "disk_percent": 30.0,
        "process_count": 50,
        "load_average": [0, 0, 0],
    }
    stats.update(overrides)
    return stats


class TestVerifyKillswitch:
    def test_all_pass_when_script_valid(self, config, tmp_path):
        script = tmp_path / "killswitch.sh"
        script.write_text("#!/bin/bash\necho ok\n")
        script.chmod(0o755)
        mon = KillSwitchMonitor(config=config)

        with patch("gateway.security.killswitch_monitor.subprocess.run") as run:
            run.return_value = MagicMock(returncode=0, stderr="", stdout="")
            result = mon.verify_killswitch(dry_run=False)

        assert result["overall_status"] == "PASS"
        assert result["tests"]["script_exists"]["status"] == "PASS"
        assert result["tests"]["permissions"]["status"] == "PASS"
        assert result["duration_seconds"] >= 0.0
        # Result was persisted to the verification log.
        logged = config.verification_log_path.read_text().strip()
        assert json.loads(logged)["overall_status"] == "PASS"

    def test_fail_when_script_missing_triggers_alert(self, config, dispatcher):
        # Script path does not exist → script_exists FAIL → overall FAIL → alert.
        mon = KillSwitchMonitor(config=config, alert_dispatcher=dispatcher)
        with patch("gateway.security.killswitch_monitor.subprocess.run") as run:
            run.return_value = MagicMock(returncode=0, stderr="", stdout="")
            result = mon.verify_killswitch(dry_run=False)

        assert result["overall_status"] == "FAIL"
        assert result["tests"]["script_exists"]["status"] == "FAIL"
        dispatcher.dispatch.assert_called_once()
        alert = dispatcher.dispatch.call_args.args[0]
        assert alert["tool"] == "killswitch_monitor"
        assert "Verification" in alert["title"]

    def test_dry_run_exercises_enabled_modes(self, config, tmp_path):
        script = tmp_path / "killswitch.sh"
        script.write_text("#!/bin/bash\necho ok\n")
        script.chmod(0o755)
        config.test_freeze_mode = True
        config.test_shutdown_mode = True
        config.test_disconnect_mode = True
        mon = KillSwitchMonitor(config=config)

        with patch("gateway.security.killswitch_monitor.subprocess.run") as run:
            run.return_value = MagicMock(returncode=0, stderr="", stdout="")
            result = mon.verify_killswitch(dry_run=True)

        assert "freeze_mode" in result["tests"]
        assert "shutdown_mode" in result["tests"]
        assert "disconnect_mode" in result["tests"]
        assert result["tests"]["freeze_mode"]["status"] == "PASS"

    def test_docker_unavailable_is_fail(self, config, tmp_path):
        script = tmp_path / "killswitch.sh"
        script.write_text("#!/bin/bash\n")
        script.chmod(0o755)
        mon = KillSwitchMonitor(config=config)
        with patch("gateway.security.killswitch_monitor.subprocess.run") as run:
            run.side_effect = FileNotFoundError("docker missing")
            result = mon.verify_killswitch(dry_run=False)
        assert result["tests"]["docker_available"]["status"] == "FAIL"


class TestHeartbeat:
    def test_healthy_resets_miss_counter(self, config):
        mon = KillSwitchMonitor(config=config)
        mon._consecutive_heartbeat_misses = 2
        with patch.object(mon, "_get_system_stats", return_value=_fake_stats()):
            result = mon.heartbeat_check()
        assert result["status"] == "HEALTHY"
        assert mon._consecutive_heartbeat_misses == 0

    def test_failure_increments_and_alerts_at_threshold(self, config, dispatcher):
        config.heartbeat_miss_threshold = 1
        mon = KillSwitchMonitor(config=config, alert_dispatcher=dispatcher)
        with patch.object(mon, "_get_system_stats", side_effect=RuntimeError("boom")):
            result = mon.heartbeat_check()
        assert result["status"] == "FAILED"
        assert mon._consecutive_heartbeat_misses == 1
        dispatcher.dispatch.assert_called_once()
        assert dispatcher.dispatch.call_args.args[0]["severity"] == "HIGH"

    def test_slow_when_response_exceeds_timeout(self, config):
        # A zero-length timeout forces the SLOW branch deterministically.
        config.heartbeat_timeout = timedelta(seconds=0)
        mon = KillSwitchMonitor(config=config)
        with patch.object(mon, "_get_system_stats", return_value=_fake_stats()):
            result = mon.heartbeat_check()
        assert result["status"] == "SLOW"
        assert mon._consecutive_heartbeat_misses == 1


class TestAnomalyDetection:
    def test_no_anomaly_when_within_limits(self, config):
        mon = KillSwitchMonitor(config=config)
        with patch.object(mon, "_get_system_stats", return_value=_fake_stats()):
            result = mon.anomaly_detection(tool_calls=1, tokens_used=10, requests=1)
        assert result["overall_status"] == "NORMAL"
        assert result["anomalies_detected"] == []
        assert result["metrics"]["tool_calls_last_minute"] == 1

    def test_excessive_tool_calls_flagged_and_alerted(self, config, dispatcher):
        config.max_tool_calls_per_minute = 2
        mon = KillSwitchMonitor(config=config, alert_dispatcher=dispatcher)
        with patch.object(mon, "_get_system_stats", return_value=_fake_stats()):
            for _ in range(5):
                result = mon.anomaly_detection(tool_calls=1)
        assert result["overall_status"] == "ANOMALY_DETECTED"
        types = {a["type"] for a in result["anomalies_detected"]}
        assert "excessive_tool_calls" in types
        dispatcher.dispatch.assert_called()
        assert dispatcher.dispatch.call_args.args[0]["severity"] == "HIGH"

    def test_excessive_tokens_flagged(self, config):
        config.max_tokens_per_hour = 100
        mon = KillSwitchMonitor(config=config)
        with patch.object(mon, "_get_system_stats", return_value=_fake_stats()):
            result = mon.anomaly_detection(tokens_used=500)
        types = {a["type"] for a in result["anomalies_detected"]}
        assert "excessive_token_usage" in types

    def test_excessive_requests_flagged(self, config):
        config.max_requests_per_minute = 2
        mon = KillSwitchMonitor(config=config)
        with patch.object(mon, "_get_system_stats", return_value=_fake_stats()):
            for _ in range(4):
                result = mon.anomaly_detection(requests=1)
        types = {a["type"] for a in result["anomalies_detected"]}
        assert "excessive_requests" in types

    def test_system_resource_memory_anomaly(self, config):
        config.memory_threshold_mb = 50
        mon = KillSwitchMonitor(config=config)
        with patch.object(mon, "_get_system_stats", return_value=_fake_stats(memory_mb=999)):
            result = mon.anomaly_detection()
        types = {a["type"] for a in result["anomalies_detected"]}
        assert "excessive_memory_usage" in types

    def test_system_resource_cpu_anomaly(self, config):
        config.cpu_threshold_percent = 10.0
        mon = KillSwitchMonitor(config=config)
        with patch.object(
            mon, "_get_system_stats", return_value=_fake_stats(memory_mb=1, cpu_percent=95.0)
        ):
            result = mon.anomaly_detection()
        types = {a["type"] for a in result["anomalies_detected"]}
        assert "excessive_cpu_usage" in types


class TestStatusAndStats:
    def test_get_status_reports_verification_due(self, config):
        mon = KillSwitchMonitor(config=config)
        with patch.object(mon, "_get_system_stats", return_value=_fake_stats()):
            status = mon.get_status()
        # No verification has run yet → due.
        assert status["verification_status"]["verification_due"] is True
        assert status["heartbeat_status"]["consecutive_misses"] == 0
        assert "current_system_stats" in status["anomaly_status"]

    def test_get_system_stats_handles_psutil_error(self, config):
        mon = KillSwitchMonitor(config=config)
        with patch(
            "gateway.security.killswitch_monitor.psutil.cpu_percent",
            side_effect=RuntimeError("no psutil"),
        ):
            stats = mon._get_system_stats()
        assert "error" in stats

    def test_clean_old_metrics_drops_stale_entries(self, config):
        mon = KillSwitchMonitor(config=config)
        # Seed with timestamps far in the past; cutoff of now should drop them.
        mon._tool_call_timestamps.extend([1.0, 2.0])
        mon._token_usage_history.extend([(1.0, 5), (2.0, 5)])
        mon._request_timestamps.extend([1.0, 2.0])
        import time

        mon._clean_old_metrics(time.time())
        assert len(mon._tool_call_timestamps) == 0
        assert len(mon._token_usage_history) == 0
        assert len(mon._request_timestamps) == 0
