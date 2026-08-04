---
type: community
cohesion: 0.16
members: 14
---

# Module Group 306

**Cohesion:** 0.16 - loosely connected
**Members:** 14 nodes

## Members
- [[CVE Vulnerability Scanning (OS packages + dependencies)]] - concept - docs/vault/02 - Modules/Security Modules/trivy_report.py.md
- [[Falco Priority → AgentShroud Severity Map]] - concept - docs/vault/02 - Modules/Security Modules/falco_monitor.py.md
- [[Falco Runtime Security Engine Integration]] - concept - docs/vault/02 - Modules/Security Modules/falco_monitor.py.md
- [[File Integrity Monitoring (FIM) Events (rule IDs 550-554)]] - concept - docs/vault/02 - Modules/Security Modules/wazuh_client.py.md
- [[Rootkit Detection Events (rule IDs 510-514)]] - concept - docs/vault/02 - Modules/Security Modules/wazuh_client.py.md
- [[SQLite Health History DB]] - concept - docs/vault/02 - Modules/Security Modules/health_report.py.md
- [[Tool Scoring Weights (trivy0.25, falco0.25, clamav0.20, wazuh0.15, gateway0.15)]] - concept - docs/vault/02 - Modules/Security Modules/health_report.py.md
- [[Wazuh HIDS Integration (OSSEC alert volume)]] - concept - docs/vault/02 - Modules/Security Modules/wazuh_client.py.md
- [[Weighted Composite Security Score (0-100, A-F grade)]] - concept - docs/vault/02 - Modules/Security Modules/health_report.py.md
- [[falco_monitor.py_1]] - code - docs/vault/02 - Modules/Security Modules/falco_monitor.py.md
- [[health_report.py_1]] - code - docs/vault/02 - Modules/Security Modules/health_report.py.md
- [[run_trivy_scan() — subprocess Trivy invocation]] - code - docs/vault/02 - Modules/Security Modules/trivy_report.py.md
- [[trivy_report.py_1]] - code - docs/vault/02 - Modules/Security Modules/trivy_report.py.md
- [[wazuh_client.py_1]] - code - docs/vault/02 - Modules/Security Modules/wazuh_client.py.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_306
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Module Group 436]]
- 2 edges to [[_COMMUNITY_Module Group 449]]

## Top bridge nodes
- [[health_report.py_1]] - degree 9, connects to 2 communities
- [[falco_monitor.py_1]] - degree 5, connects to 1 community
