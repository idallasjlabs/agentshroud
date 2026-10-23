---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1920"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# .test_undelivered_new_cves_retries_not_marked_checked()

## Connections
- [[TestUpstreamCveCheckSchedulerRetry]] - `method` [EXTRACTED]
- [[_fake_all_agents()_1]] - `indirect_call` [INFERRED]
- [[_sleep()_5]] - `contains` [EXTRACTED]
- [[_sleep()_2]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[now()_5]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
