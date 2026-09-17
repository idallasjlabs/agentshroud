---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "_sleep()"
location: "L1791"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/_sleep
---

# _fake_all_agents()

## Connections
- [[.test_undelivered_new_advisory_retries_not_marked_ingested()]] - `indirect_call` [INFERRED]
- [[.test_undelivered_new_cves_retries_not_marked_checked()]] - `indirect_call` [INFERRED]
- [[.test_zero_new_cves_marks_checked_immediately()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/INFERRED #community/_sleep