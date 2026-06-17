---
source_file: "docs/vault/02 - Modules/Security Modules/health_report.py.md"
type: "code"
community: "Module Group 306"
location: "gateway/security/health_report.py"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Module_Group_306
---

# health_report.py

## Connections
- [[SQLite Health History DB]] - `uses` [EXTRACTED]
- [[Tool Scoring Weights (trivy0.25, falco0.25, clamav0.20, wazuh0.15, gateway0.15)]] - `contains` [EXTRACTED]
- [[Weighted Composite Security Score (0-100, A-F grade)]] - `implements` [EXTRACTED]
- [[api.py (gatewaywebapi.py)]] - `references` [INFERRED]
- [[falco_monitor.py_1]] - `aggregates` [EXTRACTED]
- [[proxy_status.py (gatewaydashboardproxy_status.py)]] - `references` [EXTRACTED]
- [[resource_guard.py_1]] - `references` [EXTRACTED]
- [[trivy_report.py_1]] - `feeds_into` [EXTRACTED]
- [[wazuh_client.py_1]] - `feeds_into` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Module_Group_306