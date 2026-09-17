---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "Community 434"
location: "L1617"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_434
---

# .test_retries_on_failed_send_before_giving_up()

## Connections
- [[A failed send retries (bounded) within the same day, not next-day.]] - `rationale_for` [EXTRACTED]
- [[TestCveReportSchedulerRetry]] - `method` [EXTRACTED]
- [[_fake_run()_1]] - `contains` [EXTRACTED]
- [[_fake_run()_3]] - `indirect_call` [INFERRED]
- [[_sleep()_8]] - `contains` [EXTRACTED]
- [[_sleep()_2]] - `indirect_call` [INFERRED]
- [[asyncio_4]] - `references` [EXTRACTED]
- [[datetime]] - `calls` [INFERRED]
- [[now()_8]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_434