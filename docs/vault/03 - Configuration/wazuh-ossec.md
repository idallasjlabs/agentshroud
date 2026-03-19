---
title: wazuh-ossec.conf
type: config
file_path: docker/wazuh/ (if present) or managed via wazuh_client.py
tags: [security, wazuh, siem, intrusion-detection]
related: [Security Modules/wazuh_client.py, Security Modules/health_report.py, Architecture Overview]
status: documented
---

# wazuh-ossec.conf

**Location:** `docker/wazuh/` (external SIEM integration)
**Tool:** Wazuh — SIEM, HIDS (Host-based Intrusion Detection System), FIM (File Integrity Monitoring)
**Integration Class:** `gateway/security/wazuh_client.py`

## Purpose

Wazuh is the external SIEM (Security Information and Event Management) and HIDS integration for AgentShroud. The OSSEC/Wazuh agent configuration defines what log sources, files, and events are monitored and forwarded to the Wazuh manager for correlation and alerting.

## What Wazuh Monitors in AgentShroud

| Category | Source | Purpose |
|----------|--------|---------|
| **Gateway logs** | Uvicorn/FastAPI stdout | Auth failures, 4xx/5xx rates |
| **Audit ledger** | SQLite events | Unusual request patterns |
| **File integrity** | `agentshroud.yaml`, secrets dir | Config tampering detection |
| **Container events** | Docker daemon logs | Container start/stop/crash |
| **Auth events** | Gateway auth module | Brute force, invalid tokens |
| **Egress violations** | Egress filter logs | Blocked domain attempts |

## Key OSSEC Config Sections (Inferred)

```xml
<!-- Log analysis -->
<localfile>
  <log_format>syslog</log_format>
  <location>/var/log/agentshroud/gateway.log</location>
</localfile>

<!-- File integrity monitoring -->
<syscheck>
  <directories check_all="yes">/app/agentshroud.yaml</directories>
  <directories check_all="yes">/run/secrets/</directories>
</syscheck>

<!-- Active response -->
<active-response>
  <command>host-deny</command>
  <rules_id>100001,100002</rules_id>  <!-- auth failures -->
</active-response>
```

## Integration with Gateway

The `wazuh_client.py` module sends events to Wazuh via:
- UDP socket to Wazuh agent (port 1514 by default)
- OR REST API to Wazuh manager (port 55000)
- Event format: JSON with `agent`, `rule_id`, `description`, `level` fields

## Alert Levels

| Level | Wazuh Severity | Action |
|-------|---------------|--------|
| 1-7 | Low-Medium | Log and store |
| 8-11 | High | Alert + dashboard |
| 12-15 | Critical | Active response (block/isolate) |

## Relationship to Other Security Modules

- **`falco_monitor.py`** handles container-level runtime events
- **`wazuh_client.py`** handles log-based SIEM events
- **`alert_dispatcher.py`** consolidates alerts from both sources
- **`health_report.py`** includes Wazuh connectivity in system health

## Related Notes

- [[Security Modules/wazuh_client.py|wazuh_client.py]] — Gateway-side Wazuh client
- [[Security Modules/health_report.py|health_report.py]] — System health including SIEM status
- [[Security Modules/alert_dispatcher.py|alert_dispatcher.py]] — Alert routing
- [[Configuration/falco-rules]] — Complementary runtime detection
