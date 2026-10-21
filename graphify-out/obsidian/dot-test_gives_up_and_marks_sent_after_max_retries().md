---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "First iteration ingests + records; second sees dedup and skips."
location: "L1816"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips
---

# .test_gives_up_and_marks_sent_after_max_retries()

## Connections
- [[After the retry cap, the day IS marked done so the loop moves on.]] - `rationale_for` [EXTRACTED]
- [[TestCveReportSchedulerRetry]] - `method` [EXTRACTED]
- [[_fake_run()]] - `contains` [EXTRACTED]
- [[_fake_run()_3]] - `indirect_call` [INFERRED]
- [[_sleep()]] - `contains` [EXTRACTED]
- [[_sleep()_5]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[now()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips
