# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for unified egress monitoring."""

from __future__ import annotations

import pytest

from gateway.security.egress_monitor import (
    AlertSeverity,
    EgressChannel,
    EgressEvent,
    EgressMonitor,
    EgressMonitorConfig,
)


@pytest.fixture
def default_config():
    return EgressMonitorConfig()


@pytest.fixture
def monitor_config():
    return EgressMonitorConfig(mode="monitor")


@pytest.fixture
def monitor(monitor_config):
    return EgressMonitor(config=monitor_config)


class TestEgressMonitorConfig:
    def test_default_mode_is_enforce(self, default_config):
        """Default mode is enforce after v0.8.0 enforcement hardening."""
        assert default_config.mode == "enforce"

    def test_generous_baselines(self, default_config):
        assert default_config.http_requests_per_hour >= 200
        assert default_config.dns_queries_per_hour >= 500
        assert default_config.file_writes_per_hour >= 100


class TestEventRecording:
    def test_record_http_event(self, monitor):
        monitor.record(
            EgressEvent(
                channel=EgressChannel.HTTP,
                agent_id="agent1",
                destination="api.github.com",
                size_bytes=1024,
            )
        )
        events = monitor.get_events("agent1")
        assert len(events) == 1

    def test_record_dns_event(self, monitor):
        monitor.record(
            EgressEvent(
                channel=EgressChannel.DNS,
                agent_id="agent1",
                destination="example.com",
                size_bytes=64,
            )
        )
        events = monitor.get_events("agent1")
        assert len(events) == 1

    def test_record_file_event(self, monitor):
        monitor.record(
            EgressEvent(
                channel=EgressChannel.FILE,
                agent_id="agent1",
                destination="/tmp/out.txt",
                size_bytes=2048,
            )
        )
        events = monitor.get_events("agent1")
        assert len(events) == 1

    def test_record_mcp_event(self, monitor):
        monitor.record(
            EgressEvent(
                channel=EgressChannel.MCP,
                agent_id="agent1",
                destination="mcp-tool",
                size_bytes=512,
            )
        )
        events = monitor.get_events("agent1")
        assert len(events) == 1


class TestAnomalyDetection:
    def test_normal_volume_no_alert(self, monitor):
        for i in range(50):
            monitor.record(
                EgressEvent(
                    channel=EgressChannel.HTTP,
                    agent_id="agent1",
                    destination="api.github.com",
                    size_bytes=1024,
                )
            )
        alerts = monitor.check_anomalies("agent1")
        assert len(alerts) == 0

    def test_high_volume_triggers_alert(self, monitor):
        for i in range(500):
            monitor.record(
                EgressEvent(
                    channel=EgressChannel.HTTP,
                    agent_id="agent1",
                    destination="api.github.com",
                    size_bytes=1024,
                )
            )
        alerts = monitor.check_anomalies("agent1")
        assert len(alerts) > 0

    def test_unusual_destination_flagged(self, monitor):
        # Build baseline with normal destinations
        for i in range(20):
            monitor.record(
                EgressEvent(
                    channel=EgressChannel.HTTP,
                    agent_id="agent1",
                    destination="api.github.com",
                    size_bytes=1024,
                )
            )
        # Then hit unusual destination
        monitor.record(
            EgressEvent(
                channel=EgressChannel.HTTP,
                agent_id="agent1",
                destination="suspicious-exfil-server.xyz",
                size_bytes=50000,
                flagged=True,
            )
        )
        alerts = monitor.check_anomalies("agent1")
        assert any(a.severity >= AlertSeverity.MEDIUM for a in alerts)


class TestSlowDripDetection:
    def test_slow_drip_across_channels(self, monitor):
        """Small amounts across multiple channels should be detected."""
        for i in range(30):
            monitor.record(
                EgressEvent(
                    channel=EgressChannel.HTTP,
                    agent_id="agent1",
                    destination=f"dest{i}.example.com",
                    size_bytes=500,
                    flagged=True,
                )
            )
            monitor.record(
                EgressEvent(
                    channel=EgressChannel.DNS,
                    agent_id="agent1",
                    destination=f"query{i}.example.com",
                    size_bytes=100,
                    flagged=True,
                )
            )
        alerts = monitor.check_anomalies("agent1")
        drip = [
            a
            for a in alerts
            if "drip" in a.description.lower() or "coordinated" in a.description.lower()
        ]
        assert len(drip) > 0

    def test_normal_multi_channel_not_flagged(self, monitor):
        """Normal usage across channels should not trigger drip detection."""
        for i in range(5):
            monitor.record(
                EgressEvent(
                    channel=EgressChannel.HTTP,
                    agent_id="agent1",
                    destination="api.github.com",
                    size_bytes=1024,
                )
            )
            monitor.record(
                EgressEvent(
                    channel=EgressChannel.DNS,
                    agent_id="agent1",
                    destination="github.com",
                    size_bytes=64,
                )
            )
        alerts = monitor.check_anomalies("agent1")
        drip = [
            a
            for a in alerts
            if "drip" in a.description.lower() or "coordinated" in a.description.lower()
        ]
        assert len(drip) == 0


class TestDailySummary:
    def test_summary_report(self, monitor):
        monitor.record(
            EgressEvent(
                channel=EgressChannel.HTTP,
                agent_id="agent1",
                destination="api.github.com",
                size_bytes=1024,
            )
        )
        monitor.record(
            EgressEvent(
                channel=EgressChannel.DNS,
                agent_id="agent1",
                destination="github.com",
                size_bytes=64,
            )
        )
        summary = monitor.daily_summary("agent1")
        assert summary.total_events == 2
        assert summary.total_bytes > 0
        assert EgressChannel.HTTP in summary.by_channel
        assert EgressChannel.DNS in summary.by_channel

    def test_empty_summary(self, monitor):
        summary = monitor.daily_summary("agent1")
        assert summary.total_events == 0


class TestAlertGeneration:
    def test_alert_has_severity(self, monitor):
        for i in range(500):
            monitor.record(
                EgressEvent(
                    channel=EgressChannel.HTTP,
                    agent_id="agent1",
                    destination="api.github.com",
                    size_bytes=1024,
                )
            )
        alerts = monitor.check_anomalies("agent1")
        if alerts:
            assert alerts[0].severity is not None

    def test_alert_has_description(self, monitor):
        for i in range(500):
            monitor.record(
                EgressEvent(
                    channel=EgressChannel.HTTP,
                    agent_id="agent1",
                    destination="api.github.com",
                    size_bytes=1024,
                )
            )
        alerts = monitor.check_anomalies("agent1")
        if alerts:
            assert len(alerts[0].description) > 0

    def test_alert_monitor_mode_no_block(self, monitor):
        """Alerts in monitor mode should never block."""
        for i in range(500):
            monitor.record(
                EgressEvent(
                    channel=EgressChannel.HTTP,
                    agent_id="agent1",
                    destination="api.github.com",
                    size_bytes=1024,
                )
            )
        alerts = monitor.check_anomalies("agent1")
        for a in alerts:
            assert a.action == "log"  # not "block"
