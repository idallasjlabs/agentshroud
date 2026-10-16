---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "test_daily_cve_report.py"
location: "L823"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_daily_cve_reportpy
---

# Background loop: checks for new upstream agent CVEs once per day at report_hour

## Connections
- [[upstream_cve_check_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_daily_cve_reportpy
