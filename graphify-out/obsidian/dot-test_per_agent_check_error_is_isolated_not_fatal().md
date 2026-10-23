---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1572"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# .test_per_agent_check_error_is_isolated_not_fatal()

## Connections
- [[A raised per-agent check error is ISOLATED — the ingest still completes. Per-…]] - `rationale_for` [EXTRACTED]
- [[TestGhsaIngestScheduler]] - `method` [EXTRACTED]
- [[_boom()]] - `indirect_call` [INFERRED]
- [[_sleep()_1]] - `contains` [EXTRACTED]
- [[_sleep()_2]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[now()_1]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
