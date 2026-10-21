---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1634"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# .test_skips_ingest_when_marked_done_after_wake()

## Connections
- [[After sleeping, if the day is now marked done, the loop skips ingest.]] - `rationale_for` [EXTRACTED]
- [[TestGhsaIngestScheduler]] - `method` [EXTRACTED]
- [[_fake_ingest()_2]] - `contains` [EXTRACTED]
- [[_fake_ingest()_1]] - `indirect_call` [INFERRED]
- [[_sleep()_6]] - `contains` [EXTRACTED]
- [[_sleep()_5]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[now()_6]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
