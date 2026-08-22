---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "Daily Cve Report"
location: "L744"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Daily_Cve_Report
---

# A Telegram failure on the new-CVE alert path never raises.

## Connections
- [[.test_alert_send_failure_is_swallowed()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Daily_Cve_Report