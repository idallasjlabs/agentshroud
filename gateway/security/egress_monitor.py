# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Unified Egress Monitoring — aggregate all egress channels, detect anomalies.

Default mode: monitor (alert only, never block).
Aggregates HTTP, DNS, MCP, and file I/O egress into a single view.
"""

import logging
import time
from collections import defaultdict
from dataclasses import dataclass, field
from enum import IntEnum, Enum
from typing import Optional

logger = logging.getLogger(__name__)


class EgressChannel(str, Enum):
    HTTP = "http"
    DNS = "dns"
    MCP = "mcp"
    FILE = "file"


class AlertSeverity(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class EgressEvent:
    channel: EgressChannel
    agent_id: str
    destination: str
    size_bytes: int = 0
    timestamp: float = field(default_factory=time.time)
    flagged: bool = False
    details: str = ""


@dataclass
class AnomalyAlert:
    severity: AlertSeverity
    description: str
    agent_id: str
    channel: Optional[EgressChannel] = None
    action: str = "log"  # "log" or "block" (only in enforce mode)
    timestamp: float = field(default_factory=time.time)


@dataclass
class EgressSummary:
    agent_id: str
    total_events: int
    total_bytes: int
    by_channel: dict[EgressChannel, int] = field(default_factory=dict)
    bytes_by_channel: dict[EgressChannel, int] = field(default_factory=dict)
    unique_destinations: int = 0
    flagged_events: int = 0


@dataclass
class EgressMonitorConfig:
    mode: str = "monitor"  # "monitor" or "enforce"
    http_requests_per_hour: int = 500
    dns_queries_per_hour: int = 1000
    file_writes_per_hour: int = 200
    mcp_calls_per_hour: int = 200
    # Slow drip: flagged events across channels
    drip_flagged_threshold: int = 20
    drip_channel_threshold: int = 2  # must span at least this many channels
    # Volume anomaly multiplier
    volume_alert_multiplier: float = 2.0


class EgressMonitor:
    def __init__(self, config: EgressMonitorConfig):
        self.config = config
        self._events: dict[str, list[EgressEvent]] = defaultdict(list)

    def record(self, event: EgressEvent):
        self._events[event.agent_id].append(event)

    def get_events(
        self, agent_id: str, channel: Optional[EgressChannel] = None
    ) -> list[EgressEvent]:
        events = self._events.get(agent_id, [])
        if channel:
            events = [e for e in events if e.channel == channel]
        return events

    def check_anomalies(self, agent_id: str) -> list[AnomalyAlert]:
        alerts = []
        events = self._events.get(agent_id, [])
        if not events:
            return alerts

        now = time.time()
        hour_ago = now - 3600
        recent = [e for e in events if e.timestamp > hour_ago]

        # Volume anomalies per channel
        limits = {
            EgressChannel.HTTP: self.config.http_requests_per_hour,
            EgressChannel.DNS: self.config.dns_queries_per_hour,
            EgressChannel.FILE: self.config.file_writes_per_hour,
            EgressChannel.MCP: self.config.mcp_calls_per_hour,
        }
        for channel, limit in limits.items():
            count = sum(1 for e in recent if e.channel == channel)
            if count >= limit:
                alerts.append(
                    AnomalyAlert(
                        severity=AlertSeverity.MEDIUM,
                        description=f"High volume: {count} {channel.value} events in 1h (limit: {limit})",
                        agent_id=agent_id,
                        channel=channel,
                        action="log" if self.config.mode == "monitor" else "block",
                    )
                )

        # Flagged event anomalies
        flagged = [e for e in recent if e.flagged]
        if flagged:
            flagged_channels = set(e.channel for e in flagged)
            if (
                len(flagged) >= self.config.drip_flagged_threshold
                and len(flagged_channels) >= self.config.drip_channel_threshold
            ):
                alerts.append(
                    AnomalyAlert(
                        severity=AlertSeverity.HIGH,
                        description=(
                            f"Coordinated drip: {len(flagged)} flagged events "
                            f"across {len(flagged_channels)} channels"
                        ),
                        agent_id=agent_id,
                        action="log" if self.config.mode == "monitor" else "block",
                    )
                )

            # Individual flagged high-severity
            for e in flagged:
                if e.size_bytes > 10000:
                    alerts.append(
                        AnomalyAlert(
                            severity=AlertSeverity.MEDIUM,
                            description=f"Large flagged event: {e.size_bytes}B to {e.destination}",
                            agent_id=agent_id,
                            channel=e.channel,
                            action="log",
                        )
                    )

        return alerts

    def daily_summary(self, agent_id: str) -> EgressSummary:
        events = self._events.get(agent_id, [])
        by_channel: dict[EgressChannel, int] = defaultdict(int)
        bytes_by_channel: dict[EgressChannel, int] = defaultdict(int)
        destinations = set()
        flagged = 0

        for e in events:
            by_channel[e.channel] += 1
            bytes_by_channel[e.channel] += e.size_bytes
            destinations.add(e.destination)
            if e.flagged:
                flagged += 1

        return EgressSummary(
            agent_id=agent_id,
            total_events=len(events),
            total_bytes=sum(e.size_bytes for e in events),
            by_channel=dict(by_channel),
            bytes_by_channel=dict(bytes_by_channel),
            unique_destinations=len(destinations),
            flagged_events=flagged,
        )
