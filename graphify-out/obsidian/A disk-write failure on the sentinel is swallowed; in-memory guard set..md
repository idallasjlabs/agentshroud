---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1691"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# A disk-write failure on the sentinel is swallowed; in-memory guard set.

## Connections
- [[dot-test_ingest_records_even_when_disk_write_fails()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
