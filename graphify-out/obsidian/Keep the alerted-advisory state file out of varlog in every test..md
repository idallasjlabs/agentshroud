---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "test_daily_cve_report.py"
location: "L23"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_daily_cve_reportpy
---

# Keep the alerted-advisory state file out of /var/log in every test.

## Connections
- [[_isolated_alert_state()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_daily_cve_reportpy
