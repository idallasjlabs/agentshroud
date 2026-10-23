---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1477"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# .test_runs_ingest_records_then_skips_next_iteration()

## Connections
- [[First iteration ingests + records; second sees dedup and skips.]] - `rationale_for` [EXTRACTED]
- [[TestGhsaIngestScheduler]] - `method` [EXTRACTED]
- [[_fake_ingest()_1]] - `indirect_call` [INFERRED]
- [[_sleep()_2]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[list_cve_agents()]] - `calls` [EXTRACTED]
- [[now()_2]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
