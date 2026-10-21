---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "sync-cve-registry.py"
location: "L873"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/sync-cve-registrypy
---

# Background loop: checks for new upstream agent CVEs once per day at report_hour…

## Connections
- [[upstream_cve_check_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/sync-cve-registrypy
