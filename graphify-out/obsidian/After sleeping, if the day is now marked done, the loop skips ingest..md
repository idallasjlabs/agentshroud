---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1635"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# After sleeping, if the day is now marked done, the loop skips ingest.

## Connections
- [[dot-test_skips_ingest_when_marked_done_after_wake()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
