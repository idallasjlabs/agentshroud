---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "Community 434"
location: "L1667"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_434
---

# .test_gives_up_and_marks_sent_after_max_retries()

## Connections
- [[After the retry cap, the day IS marked done so the loop moves on.]] - `rationale_for` [EXTRACTED]
- [[TestCveReportSchedulerRetry]] - `method` [EXTRACTED]
- [[_fake_run()]] - `contains` [EXTRACTED]
- [[_fake_run()_3]] - `indirect_call` [INFERRED]
- [[_sleep()_7]] - `contains` [EXTRACTED]
- [[_sleep()_2]] - `indirect_call` [INFERRED]
- [[asyncio_4]] - `references` [EXTRACTED]
- [[datetime]] - `calls` [INFERRED]
- [[now()_7]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_434