---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "sync-cve-registry.py"
location: "L402"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/sync-cve-registrypy
---

# Background loop: sends one CVE report per day at ``report_hour`` UTC. Runs…

## Connections
- [[cve_report_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/sync-cve-registrypy
