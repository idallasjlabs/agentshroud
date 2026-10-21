---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "sync-cve-registry.py"
location: "L23"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/sync-cve-registrypy
---

# Keep the alerted-advisory state file out of /var/log in every test.

## Connections
- [[_isolated_alert_state()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/sync-cve-registrypy
