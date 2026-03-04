---
title: falco_monitor.py
type: module
file_path: gateway/security/falco_monitor.py
tags: [security, runtime-security, falco, threat-detection, syscall-monitoring]
related: [[health_report.py]], [[wazuh_client.py]], [[subagent_monitor.py]]
status: documented
---

# falco_monitor.py

## Purpose
Integrates with the Falco runtime security engine by reading JSON alert files written to a shared volume mount. Parses, normalizes, and summarizes syscall-level security events for consumption by the health reporting pipeline.

## Threat Model
Defends against container escape, privilege escalation, unauthorized file access, unexpected outbound connections, and crypto-mining workloads executing inside agent containers. Falco monitors at the kernel syscall level, making it highly resistant to evasion from within the container userspace.

## Responsibilities
- Read Falco alert files from a shared volume (`/var/log/falco`)
- Parse raw Falco JSON alert format into normalized dicts
- Filter alerts by timestamp window or AgentShroud-specific rules
- Map Falco priority levels to a four-tier severity model (CRITICAL / HIGH / MEDIUM / LOW)
- Categorize alerts by severity
- Generate a structured summary dict for the health report

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `read_alerts` | Function | Reads all `.json` alert files from the alert dir; supports time and rule filters |
| `parse_alert` | Function | Normalizes a single raw Falco alert JSON into a canonical dict |
| `is_agentshroud_rule` | Function | Returns `True` if a rule name matches any AgentShroud-specific prefix |
| `categorize_alerts` | Function | Buckets a list of parsed alerts into CRITICAL / HIGH / MEDIUM / LOW groups |
| `generate_summary` | Function | Builds a health-report-compatible summary dict from a list of parsed alerts |
| `PRIORITY_MAP` | Constant | Maps Falco priority strings to AgentShroud severity levels |
| `AGENTSHROUD_RULES` | Constant | List of rule name prefixes that are AgentShroud-specific |

## Function Details

### read_alerts(alert_dir, since, agentshroud_only)
**Purpose:** Entry point for alert ingestion. Reads all `.json` files in the alert directory, applies optional time and rule-name filters, and returns the normalized alert list.
**Parameters:**
- `alert_dir` — `Path`, defaults to `/var/log/falco`
- `since` — `datetime | None`, ISO timestamp lower bound for filtering
- `agentshroud_only` — `bool`, when `True` limits results to AgentShroud-prefixed rules
**Returns:** `list[dict]` of normalized alert dicts

### parse_alert(raw)
**Purpose:** Extracts the canonical fields from a raw Falco alert and maps priority to severity.
**Parameters:** `raw` — raw JSON dict from Falco
**Returns:** Normalized dict with keys `timestamp`, `rule`, `severity`, `priority`, `output`, `source`, `hostname`, `container_id`, `container_name`, `process`, `raw`; returns `None` for empty input

### is_agentshroud_rule(rule_name)
**Purpose:** Determines whether a given rule name corresponds to a rule that is AgentShroud-specific, allowing separate tracking of platform-relevant events.
**Parameters:** `rule_name` — string
**Returns:** `bool`

### categorize_alerts(alerts)
**Purpose:** Groups alerts into severity buckets for downstream scoring and reporting.
**Parameters:** `alerts` — list of normalized alert dicts
**Returns:** `dict` mapping `"CRITICAL" | "HIGH" | "MEDIUM" | "LOW"` to lists of alerts

### generate_summary(alerts)
**Purpose:** Produces the standardized summary dict consumed by `health_report.py`. Computes overall status, per-severity counts, top rules by frequency, and a count of AgentShroud-specific alerts.
**Parameters:** `alerts` — list of normalized alert dicts
**Returns:** `dict` with keys `tool`, `status`, `findings`, `critical`, `high`, `medium`, `low`, `top_rules`, `agentshroud_alerts`, `timestamp`

## Configuration / Environment Variables
- Alert files are read from `DEFAULT_ALERT_DIR = /var/log/falco` — this path must be mounted as a shared volume from the Falco sidecar container
- Log output directory `DEFAULT_LOG_DIR = /var/log/security/falco` is referenced but not written to by this module directly

## Priority Mapping

| Falco Priority | AgentShroud Severity |
|---|---|
| Emergency, Alert, Critical | CRITICAL |
| Error | HIGH |
| Warning | MEDIUM |
| Notice, Informational, Debug | LOW |

## Related
- [[health_report.py]]
- [[wazuh_client.py]]
- [[subagent_monitor.py]]
