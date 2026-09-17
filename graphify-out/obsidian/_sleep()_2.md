---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "_sleep()"
location: "L1365"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/_sleep
---

# _sleep()

## Connections
- [[.test_gives_up_and_marks_sent_after_max_retries()]] - `indirect_call` [INFERRED]
- [[.test_ingest_records_even_when_disk_write_fails()]] - `indirect_call` [INFERRED]
- [[.test_per_agent_check_error_is_isolated_not_fatal()]] - `indirect_call` [INFERRED]
- [[.test_retries_on_failed_send_before_giving_up()]] - `indirect_call` [INFERRED]
- [[.test_runs_ingest_records_then_skips_next_iteration()]] - `indirect_call` [INFERRED]
- [[.test_skips_ingest_when_marked_done_after_wake()]] - `indirect_call` [INFERRED]
- [[.test_successful_send_marks_sent_immediately_no_retry()]] - `indirect_call` [INFERRED]
- [[.test_undelivered_new_advisory_retries_not_marked_ingested()]] - `indirect_call` [INFERRED]
- [[.test_undelivered_new_cves_retries_not_marked_checked()]] - `indirect_call` [INFERRED]
- [[.test_zero_new_cves_marks_checked_immediately()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/INFERRED #community/_sleep