---
type: community
members: 63
---

# First iteration ingests + records; second sees dedup and skips.

**Members:** 63 nodes

## Members
- [[dot-test_already_ingested_helper_swallows_read_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_gives_up_and_marks_sent_after_max_retries()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_ingest_records_even_when_disk_write_fails()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_no_skip_dirs_flag_when_omitted()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_per_agent_check_error_is_isolated_not_fatal()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_retries_on_failed_send_before_giving_up()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_runs_ingest_records_then_skips_next_iteration()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skip_dirs_added_to_command()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_ingest_when_marked_done_after_wake()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_when_already_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_successful_send_marks_sent_immediately_no_retry()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_undelivered_new_advisory_retries_not_marked_ingested()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_undelivered_new_cves_retries_not_marked_checked()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_zero_new_cves_marks_checked_immediately()]] - code - gateway/tests/test_daily_cve_report.py
- [[A disk-write failure on the sentinel is swallowed; in-memory guard set.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A failed send retries (bounded) within the same day, not next-day.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A raised per-agent check error is ISOLATED — the ingest still completes. Per-…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After sleeping, if the day is now marked done, the loop skips ingest.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After the retry cap, the day IS marked done so the loop moves on.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[First iteration ingests + records; second sees dedup and skips.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[If already ingested today, the loop bumps to tomorrow and never ingests.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Nothing to deliver is a legitimate 'done', not a failure to retry.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestCveReportSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestScheduler]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestTrivySkipDirs]] - code - gateway/tests/test_daily_cve_report.py
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
- [[_fake_run()]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_run()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_run()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_run()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_run()_4]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_run()_5]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_4]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_5]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_6]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_7]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_8]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_9]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep_then_cancel()]] - code - gateway/tests/test_daily_cve_report.py
- [[now()]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_4]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_5]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_6]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_7]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_8]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_9]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/First_iteration_ingests__records_second_sees_dedup_and_skips
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_ApprovalQueueConfig (2) (2)]]
- 5 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_format_cve_report() (2)]]
- 1 edge to [[_COMMUNITY_OpenClaw and Hermes are processed on fully separate paths; one failing never… (2)]]
- 1 edge to [[_COMMUNITY_A2APolicyEngine]]

## Top bridge nodes
- [[dot-test_runs_ingest_records_then_skips_next_iteration()]] - degree 7, connects to 2 communities
- [[TestTrivySkipDirs]] - degree 4, connects to 2 communities
- [[dot-test_gives_up_and_marks_sent_after_max_retries()]] - degree 8, connects to 1 community
- [[dot-test_retries_on_failed_send_before_giving_up()]] - degree 8, connects to 1 community
- [[dot-test_ingest_records_even_when_disk_write_fails()]] - degree 8, connects to 1 community
