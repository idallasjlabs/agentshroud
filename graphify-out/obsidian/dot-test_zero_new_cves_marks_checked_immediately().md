---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1966"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# .test_zero_new_cves_marks_checked_immediately()

## Connections
- [[Nothing to deliver is a legitimate 'done', not a failure to retry.]] - `rationale_for` [EXTRACTED]
- [[TestUpstreamCveCheckSchedulerRetry]] - `method` [EXTRACTED]
- [[_fake_all_agents()_2]] - `contains` [EXTRACTED]
- [[_fake_all_agents()_1]] - `indirect_call` [INFERRED]
- [[_sleep()_6]] - `contains` [EXTRACTED]
- [[_sleep()_2]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[now()_6]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
