---
source_file: "gateway/security/daily_cve_report.py"
type: "code"
community: "Gateway Security Module"
location: "L710"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Security_Module
---

# upstream_cve_check_scheduler()

## Connections
- [[Background loop checks for new upstream agent CVEs once per day at report_hour]] - `rationale_for` [EXTRACTED]
- [[_already_checked_upstream_today()]] - `calls` [EXTRACTED]
- [[daily_cve_report.py]] - `contains` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[run_upstream_cve_check()]] - `calls` [EXTRACTED]
- [[run_upstream_cve_check_all_agents()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Security_Module