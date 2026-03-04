---
title: wazuh_client.py
type: module
file_path: gateway/security/wazuh_client.py
tags: [security, hids, wazuh, file-integrity-monitoring, rootkit-detection, ossec]
related: [[health_report.py]], [[falco_monitor.py]], [[trivy_report.py]]
status: documented
---

# wazuh_client.py

## Purpose
Integrates with the Wazuh Host Intrusion Detection System (HIDS) by reading JSON alert files from the shared OSSEC alert volume. Parses and normalizes alerts with special handling for File Integrity Monitoring (FIM) and rootkit detection rule IDs, then produces a structured summary for the health reporting pipeline.

## Threat Model
Defends against host-level compromise indicators including file tampering (modified, added, or deleted files in monitored paths), rootkit installation (hidden processes, files, and ports), and privilege escalation. Wazuh operates at the OS level independent of container runtime, providing a complementary detection layer to Falco's syscall-level monitoring.

## Responsibilities
- Read Wazuh alert JSON files from the OSSEC alert directory (`/var/ossec/logs/alerts`)
- Map Wazuh numeric alert levels (0–15) to a four-tier severity model
- Identify File Integrity Monitoring (FIM) events by rule ID
- Identify rootkit detection events by rule ID
- Parse syscheck fields (file path, event type, MD5 before/after) from FIM alerts
- Filter alerts by timestamp
- Generate a health-report-compatible summary with FIM and rootkit event counts and modified file paths

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `read_alerts` | Function | Reads all `alerts*.json` files from the alert directory |
| `parse_alert` | Function | Normalizes a raw Wazuh alert JSON into a canonical dict |
| `level_to_severity` | Function | Maps a Wazuh alert level integer to a severity string |
| `get_fim_events` | Function | Filters an alert list to FIM events only |
| `get_rootkit_events` | Function | Filters an alert list to rootkit events only |
| `generate_summary` | Function | Produces a health-report-compatible summary dict |
| `LEVEL_MAP` | Constant | Maps Wazuh level ranges to severity strings |
| `FIM_RULE_IDS` | Constant | Wazuh rule IDs for FIM event types (add, delete, modify, attributes) |
| `ROOTKIT_RULE_IDS` | Constant | Wazuh rule IDs for rootkit event types (trojan, hidden file/process/port) |

## Function Details

### read_alerts(alert_dir, since)
**Purpose:** Scans the alert directory for `alerts*.json` files, reads them line-by-line (NDJSON format), parses each alert, and optionally filters by timestamp. Returns all parsed alerts.
**Parameters:** `alert_dir` — `Path` (default `/var/ossec/logs/alerts`), `since` — `datetime | None`
**Returns:** `list[dict]`

### parse_alert(raw)
**Purpose:** Extracts canonical fields from a raw Wazuh alert. Determines alert type from rule ID (FIM or rootkit), maps alert level to severity, and extracts syscheck fields for FIM events.
**Parameters:** `raw` — raw JSON dict from Wazuh
**Returns:** Normalized `dict` with keys `timestamp`, `rule_id`, `rule_description`, `level`, `severity`, `alert_type`, `agent`, `file_path`, `file_event`, `file_md5_before`, `file_md5_after`, `raw`; returns `None` for empty input

### level_to_severity(level)
**Purpose:** Maps Wazuh's numeric alert level scale to AgentShroud severity strings.
**Parameters:** `level` — int (0–15)
**Returns:** `"CRITICAL"` | `"HIGH"` | `"MEDIUM"` | `"LOW"`

### get_fim_events(alerts) / get_rootkit_events(alerts)
**Purpose:** Filter the alerts list to events whose `alert_type` matches FIM or rootkit rule ID categories, respectively.
**Returns:** Filtered `list[dict]`

### generate_summary(alerts)
**Purpose:** Counts events by severity, identifies FIM and rootkit event counts, builds a list of modified file paths (up to 20), and determines overall status (`"critical"` if any CRITICAL or rootkit events, `"warning"` for HIGH, `"info"` for any other alerts, `"clean"` for none).
**Parameters:** `alerts` — list of parsed alert dicts
**Returns:** `dict` with keys `tool`, `status`, `findings`, `critical`, `high`, `medium`, `low`, `fim_events`, `rootkit_events`, `modified_files`, `timestamp`

## Configuration / Environment Variables
- `DEFAULT_ALERT_DIR = /var/ossec/logs/alerts` — must be mounted as a shared volume from the Wazuh container
- `DEFAULT_LOG_DIR = /var/log/security/wazuh` — referenced but not written to by this module directly

## Wazuh Level to Severity Mapping

| Wazuh Level Range | AgentShroud Severity |
|---|---|
| 0–6 | LOW |
| 7–9 | MEDIUM |
| 10–12 | HIGH |
| 13–15 | CRITICAL |

## Key Rule ID Sets

| Category | Rule IDs |
|---|---|
| FIM — Added | 550 |
| FIM — Deleted | 551 |
| FIM — Modified | 553 |
| FIM — Attributes Changed | 554 |
| Rootkit — Trojan | 510 |
| Rootkit — Hidden File | 512 |
| Rootkit — Hidden Process | 513 |
| Rootkit — Hidden Port | 514 |

## Related
- [[health_report.py]]
- [[falco_monitor.py]]
- [[trivy_report.py]]
