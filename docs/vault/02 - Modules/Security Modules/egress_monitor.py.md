---
title: egress_monitor.py
type: module
file_path: gateway/security/egress_monitor.py
tags: [security, egress-monitoring, anomaly-detection, data-exfiltration, multi-channel, slow-drip]
related: [[egress_config.py]], [[key_vault.py]], [[resource_guard.py]]
status: documented
---

# egress_monitor.py

## Purpose
Aggregates all outbound network and file activity from agent containers across four egress channels (HTTP, DNS, MCP, file I/O) into a single unified view, detects volume anomalies and coordinated multi-channel "slow drip" exfiltration patterns, and generates daily egress summaries per agent.

## Threat Model
Addresses sophisticated data exfiltration that evades single-channel rate limits by distributing data across multiple egress paths — for example, small DNS query payloads combined with low-volume HTTP and MCP calls that individually fall below detection thresholds but collectively constitute a significant data leak. The coordinated drip detection requires both a minimum number of flagged events AND those events to span at least two distinct channels before raising a HIGH severity alert.

## Responsibilities
- Record every egress event (channel, agent, destination, size, flagged status, timestamp)
- Support retrieval of all events or events filtered by channel for a given agent
- Detect per-channel volume anomalies against configurable hourly thresholds
- Detect multi-channel "slow drip" coordinated exfiltration patterns
- Flag individually large payloads on flagged destinations
- Generate per-agent daily egress summaries (total events, total bytes, per-channel breakdown, unique destinations, flagged count)
- Operate in `monitor` (log only) or `enforce` (block) mode

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `EgressMonitor` | Class | Core aggregator; stores events, runs anomaly detection, generates summaries |
| `EgressMonitorConfig` | Dataclass | Configuration: mode, per-channel hourly limits, drip thresholds, volume multiplier |
| `EgressEvent` | Dataclass | A single egress event: channel, agent, destination, size, timestamp, flagged, details |
| `AnomalyAlert` | Dataclass | An anomaly detection result: severity, description, agent, channel, action, timestamp |
| `EgressSummary` | Dataclass | Per-agent daily summary: totals by channel and bytes, unique destinations, flagged count |
| `EgressChannel` | Enum | Channel types: HTTP, DNS, MCP, FILE |
| `AlertSeverity` | IntEnum | Severity levels: LOW (1), MEDIUM (2), HIGH (3), CRITICAL (4) |

## Function Details

### EgressMonitor.record(event)
**Purpose:** Appends an `EgressEvent` to the per-agent event list. Events are never automatically pruned; callers are responsible for lifecycle management.
**Parameters:** `event` — `EgressEvent`

### EgressMonitor.get_events(agent_id, channel)
**Purpose:** Returns all stored events for an agent, optionally filtered to a specific channel.
**Parameters:** `agent_id` (str), `channel` (`EgressChannel | None`)
**Returns:** `list[EgressEvent]`

### EgressMonitor.check_anomalies(agent_id)
**Purpose:** Analyzes events from the last 1 hour for the agent. Checks each channel's event count against its configured hourly limit (MEDIUM severity if exceeded). Checks for coordinated drip: if the number of flagged events meets `drip_flagged_threshold` AND those events span at least `drip_channel_threshold` distinct channels, raises a HIGH severity alert. Also generates MEDIUM alerts for any individually flagged events exceeding 10,000 bytes.
**Parameters:** `agent_id` (str)
**Returns:** `list[AnomalyAlert]`; empty if no anomalies detected

### EgressMonitor.daily_summary(agent_id)
**Purpose:** Aggregates all stored events for an agent into a summary: total event count, total bytes, per-channel event counts and bytes, unique destination count, and flagged event count.
**Parameters:** `agent_id` (str)
**Returns:** `EgressSummary`

## Configuration / Environment Variables
- No environment variables; configuration passed via `EgressMonitorConfig`
- Mode is inherited from `egress_config.py` conventions but managed independently

## Default Thresholds

| Channel | Hourly Limit |
|---|---|
| HTTP | 500 requests |
| DNS | 1,000 queries |
| FILE | 200 writes |
| MCP | 200 calls |

| Drip Detection Parameter | Default |
|---|---|
| Min flagged events to trigger | 20 |
| Min channels flagged events must span | 2 |
| Large payload threshold | 10,000 bytes |
| Volume alert multiplier | 2.0x (reference for future use) |

## Alert Actions

| Mode | Action on Anomaly |
|---|---|
| `monitor` | `"log"` — alert is recorded, traffic not blocked |
| `enforce` | `"block"` — alert is raised and upstream can act to block |

## Related
- [[egress_config.py]]
- [[key_vault.py]]
- [[resource_guard.py]]
