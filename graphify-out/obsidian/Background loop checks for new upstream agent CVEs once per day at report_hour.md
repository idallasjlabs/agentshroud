---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "Daily Cve Report (security)"
location: "L767"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Daily_Cve_Report_security
---

# Background loop: checks for new upstream agent CVEs once per day at report_hour

## Connections
- [[upstream_cve_check_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Daily_Cve_Report_security