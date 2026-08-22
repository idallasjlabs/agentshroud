---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "Daily Cve Report (security)"
location: "L342"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Daily_Cve_Report_security
---

# Background loop: sends one CVE report per day at ``report_hour`` UTC.      Runs

## Connections
- [[cve_report_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Daily_Cve_Report_security