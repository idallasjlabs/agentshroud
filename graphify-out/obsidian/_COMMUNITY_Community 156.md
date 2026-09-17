---
type: community
cohesion: 0.06
members: 42
---

# Community 156

**Cohesion:** 0.06 - loosely connected
**Members:** 42 nodes

## Members
- [[dot-test_already_ingested_helper_swallows_read_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_ingest_records_even_when_disk_write_fails()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_per_agent_check_error_is_isolated_not_fatal()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_runs_ingest_records_then_skips_next_iteration()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_ingest_when_marked_done_after_wake()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_when_already_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_undelivered_new_advisory_retries_not_marked_ingested()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_undelivered_new_cves_retries_not_marked_checked()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_zero_new_cves_marks_checked_immediately()]] - code - gateway/tests/test_daily_cve_report.py
- [[A disk-write failure on the sentinel is swallowed; in-memory guard set.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A raised per-agent check error is ISOLATED — the ingest still completes. Per-…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After sleeping, if the day is now marked done, the loop skips ingest.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[First iteration ingests + records; second sees dedup and skips.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[If already ingested today, the loop bumps to tomorrow and never ingests.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Nothing to deliver is a legitimate 'done', not a failure to retry.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestScheduler]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestUpstreamCveCheckSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[_already_ingested_ghsa_today returns False on a malformed sentinel.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[_boom()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_all_agents()]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_all_agents()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_all_agents()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_ingest()]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_ingest()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_ingest()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_ingest()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_4]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_5]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_6]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep_then_cancel()]] - code - gateway/tests/test_daily_cve_report.py
- [[now()]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_4]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_5]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_6]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_156
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Community 82]]
- 7 edges to [[_COMMUNITY_Community 124]]
- 3 edges to [[_COMMUNITY_Community 434]]
- 1 edge to [[_COMMUNITY_Community 458]]

## Top bridge nodes
- [[dot-test_runs_ingest_records_then_skips_next_iteration()]] - degree 8, connects to 3 communities
- [[dot-test_ingest_records_even_when_disk_write_fails()]] - degree 9, connects to 2 communities
- [[dot-test_skips_ingest_when_marked_done_after_wake()]] - degree 9, connects to 2 communities
- [[dot-test_zero_new_cves_marks_checked_immediately()]] - degree 9, connects to 2 communities
- [[dot-test_per_agent_check_error_is_isolated_not_fatal()]] - degree 8, connects to 2 communities