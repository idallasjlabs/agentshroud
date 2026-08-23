---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "Daily Cve Report (security)"
location: "L1442"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Daily_Cve_Report_security
---

# A failed send retries (bounded) within the same day, not next-day.

## Connections
- [[.test_retries_on_failed_send_before_giving_up()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Daily_Cve_Report_security