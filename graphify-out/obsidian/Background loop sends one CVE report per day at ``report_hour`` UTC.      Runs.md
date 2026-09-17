---
source_file: "gateway/security/daily_cve_report.py"
type: "rationale"
community: "gateway.security.daily_cve_report"
location: "L398"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/gatewaysecuritydaily_cve_report
---

# Background loop: sends one CVE report per day at ``report_hour`` UTC.      Runs

## Connections
- [[cve_report_scheduler]] - `rationale_for` [EXTRACTED]
- [[cve_report_scheduler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/gatewaysecuritydaily_cve_report