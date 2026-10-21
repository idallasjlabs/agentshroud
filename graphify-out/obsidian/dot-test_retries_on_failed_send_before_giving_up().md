---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1766"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# .test_retries_on_failed_send_before_giving_up()

## Connections
- [[A failed send retries (bounded) within the same day, not next-day.]] - `rationale_for` [EXTRACTED]
- [[TestCveReportSchedulerRetry]] - `method` [EXTRACTED]
- [[_fake_run()_1]] - `contains` [EXTRACTED]
- [[_fake_run()_3]] - `indirect_call` [INFERRED]
- [[_sleep()_1]] - `contains` [EXTRACTED]
- [[_sleep()_5]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[now()_1]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
