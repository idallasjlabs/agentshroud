---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "_sleep()"
location: "L1486"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_sleep
---

# After sleeping, if the day is now marked done, the loop skips ingest.

## Connections
- [[.test_skips_ingest_when_marked_done_after_wake()]] - `rationale_for` [EXTRACTED]
- [[.test_skips_ingest_when_marked_done_after_wake()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_sleep