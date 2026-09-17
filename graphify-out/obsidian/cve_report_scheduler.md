---
source_file: "gateway/security/daily_cve_report.py"
type: "code"
community: "gateway.security.daily_cve_report"
location: "392"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/gatewaysecuritydaily_cve_report
---

# cve_report_scheduler

## Connections
- [[Background loop sends one CVE report per day at ``report_hour`` UTC.      Runs]] - `rationale_for` [EXTRACTED]
- [[_already_sent_today]] - `calls` [EXTRACTED]
- [[gateway.security.daily_cve_report]] - `contains` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[run_and_send_cve_report]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/gatewaysecuritydaily_cve_report