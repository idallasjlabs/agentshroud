---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1690"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# .test_ingest_records_even_when_disk_write_fails()

## Connections
- [[A disk-write failure on the sentinel is swallowed; in-memory guard set.]] - `rationale_for` [EXTRACTED]
- [[TestGhsaIngestScheduler]] - `method` [EXTRACTED]
- [[_fake_ingest()]] - `contains` [EXTRACTED]
- [[_fake_ingest()_1]] - `indirect_call` [INFERRED]
- [[_sleep()]] - `contains` [EXTRACTED]
- [[_sleep()_2]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[now()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
