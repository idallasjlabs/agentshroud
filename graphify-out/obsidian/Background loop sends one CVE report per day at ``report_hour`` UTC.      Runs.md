---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "test_daily_cve_report.py"
location: "L398"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_daily_cve_reportpy
---

# Background loop: sends one CVE report per day at ``report_hour`` UTC.      Runs

## Connections
- [[cve_report_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_daily_cve_reportpy
