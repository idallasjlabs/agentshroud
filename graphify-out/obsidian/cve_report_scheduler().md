---
source_file: "gateway/security/daily_cve_report.py"
type: "code"
community: "sync-cve-registry.py"
location: "L396"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/sync-cve-registrypy
---

# cve_report_scheduler()

## Connections
- [[Background loop sends one CVE report per day at ``report_hour`` UTC. Runs…]] - `rationale_for` [EXTRACTED]
- [[_already_sent_today()]] - `calls` [EXTRACTED]
- [[daily_cve_report.py]] - `contains` [EXTRACTED]
- [[run_and_send_cve_report()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/sync-cve-registrypy
