---
source_file: "gateway/security/daily_cve_report.py"
type: "code"
community: "Daily Cve Report (security)"
location: "L336"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Daily_Cve_Report_security
---

# cve_report_scheduler()

## Connections
- [[Background loop sends one CVE report per day at ``report_hour`` UTC.      Runs]] - `rationale_for` [EXTRACTED]
- [[_already_sent_today()]] - `calls` [EXTRACTED]
- [[daily_cve_report.py]] - `contains` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[run_and_send_cve_report()]] - `calls` [EXTRACTED]
- [[upstream_cve_check_scheduler()]] - `conceptually_related_to` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Daily_Cve_Report_security