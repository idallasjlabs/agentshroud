---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1539"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# .test_skips_when_already_ingested_today()

## Connections
- [[If already ingested today, the loop bumps to tomorrow and never ingests.]] - `rationale_for` [EXTRACTED]
- [[TestGhsaIngestScheduler]] - `method` [EXTRACTED]
- [[_fake_ingest()_3]] - `contains` [EXTRACTED]
- [[_fake_ingest()_1]] - `indirect_call` [INFERRED]
- [[_sleep_then_cancel()]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
