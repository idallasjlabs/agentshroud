---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "Daily Cve Report (security)"
location: "L1310"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Daily_Cve_Report_security
---

# After sleeping, if the day is now marked done, the loop skips ingest.

## Connections
- [[.test_skips_ingest_when_marked_done_after_wake()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Daily_Cve_Report_security