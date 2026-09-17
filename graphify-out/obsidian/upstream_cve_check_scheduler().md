---
source_file: "gateway/security/daily_cve_report.py"
type: "code"
community: "test_daily_cve_report.py"
location: "L815"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_daily_cve_reportpy
---

# upstream_cve_check_scheduler()

## Connections
- [[Background loop checks for new upstream agent CVEs once per day at report_hour]] - `rationale_for` [EXTRACTED]
- [[_already_checked_upstream_today()]] - `calls` [EXTRACTED]
- [[daily_cve_report.py]] - `contains` [EXTRACTED]
- [[run_upstream_cve_check_all_agents()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_daily_cve_reportpy