---
type: community
cohesion: 0.10
members: 26
---

# AgentShroud™ Security Policy

**Cohesion:** 0.10 - loosely connected
**Members:** 26 nodes

## Members
- [[.test_already_ingested_helper_swallows_read_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_gives_up_and_marks_sent_after_max_retries()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_ingest_records_even_when_disk_write_fails()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_per_agent_check_error_is_isolated_not_fatal()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_retries_on_failed_send_before_giving_up()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_runs_ingest_records_then_skips_next_iteration()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_ingest_when_marked_done_after_wake()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_when_already_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_successful_send_marks_sent_immediately_no_retry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_undelivered_new_advisory_retries_not_marked_ingested()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_undelivered_new_cves_retries_not_marked_checked()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_zero_new_cves_marks_checked_immediately()]] - code - gateway/tests/test_daily_cve_report.py
- [[A disk-write failure on the sentinel is swallowed; in-memory guard set.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A failed send retries (bounded) within the same day, not next-day.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A raised per-agent check error is ISOLATED — the ingest still completes.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After sleeping, if the day is now marked done, the loop skips ingest.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After the retry cap, the day IS marked done so the loop moves on.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[First iteration ingests + records; second sees dedup and skips.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[If already ingested today, the loop bumps to tomorrow and never ingests.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Nothing to deliver is a legitimate 'done', not a failure to retry.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestCveReportSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestScheduler]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestUpstreamCveCheckSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[_already_ingested_ghsa_today returns False on a malformed sentinel.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[datetime_2]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Security_Policy
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_PrivacyPolicyEnforcer]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]

## Top bridge nodes
- [[datetime_2]] - degree 14, connects to 1 community
- [[TestGhsaIngestScheduler]] - degree 7, connects to 1 community
- [[TestCveReportSchedulerRetry]] - degree 4, connects to 1 community
- [[.test_runs_ingest_records_then_skips_next_iteration()]] - degree 4, connects to 1 community
- [[TestUpstreamCveCheckSchedulerRetry]] - degree 3, connects to 1 community