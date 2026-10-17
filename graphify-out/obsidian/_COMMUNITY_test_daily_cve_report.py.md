---
type: community
members: 79
---

# test_daily_cve_report.py

**Members:** 79 nodes

## Members
- [[dot-test_already_ingested_helper_swallows_read_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_failed_send_does_not_write_stamp_or_mark_sent_date()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_gives_up_and_marks_sent_after_max_retries()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_ingest_records_even_when_disk_write_fails()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_no_alert_when_registry_current()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_no_telegram_send_when_no_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_per_agent_check_error_is_isolated_not_fatal()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_retries_on_failed_send_before_giving_up()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_error_on_github_api_failure()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_checked_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_file_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_file_missing()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_file_missing()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_ingested_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_sent_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_summary_without_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_true_when_checked_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_true_when_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_true_when_sent_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_runs_ingest_records_then_skips_next_iteration()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_sends_alert_when_new_cves_found()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_sends_telegram_on_success()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_short_text_passes_through_unchanged()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_ingest_when_marked_done_after_wake()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_when_already_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_successful_send_marks_sent_immediately_no_retry()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_trivy_error_still_sends_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_truncates_over_length_text()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_undelivered_new_advisory_retries_not_marked_ingested()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_undelivered_new_cves_retries_not_marked_checked()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_zero_new_cves_marks_checked_immediately()]] - code - gateway/tests/test_daily_cve_report.py
- [[A disk-write failure on the sentinel is swallowed; in-memory guard set.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A failed send retries (bounded) within the same day, not next-day.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A raised per-agent check error is ISOLATED — the ingest still completes.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After sleeping, if the day is now marked done, the loop skips ingest.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After the retry cap, the day IS marked done so the loop moves on.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Any_67]] - code - gateway/security/daily_cve_report.py
- [[Background loop checks for new upstream agent CVEs once per day at report_hour]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop pull the GHSA feed as source of truth once per day.      This i]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop sends one CVE report per day at ``report_hour`` UTC.      Runs]] - rationale - gateway/security/daily_cve_report.py
- [[Check if a Trivy report was already sent today (disk-based, secondary to _sent_d]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the GHSA ingest already ran today (disk-based, secondary guard).]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the upstream CVE watch already ran today (disk-based).]] - rationale - gateway/security/daily_cve_report.py
- [[Fetch one agent's upstream CVEs, alert via Telegram, honestly.      Runs a singl]] - rationale - gateway/security/daily_cve_report.py
- [[First iteration ingests + records; second sees dedup and skips.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[If already ingested today, the loop bumps to tomorrow and never ingests.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Nothing to deliver is a legitimate 'done', not a failure to retry.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Resolve the image tag a container is ACTUALLY running, via docker CLI.      The]] - rationale - gateway/security/daily_cve_report.py
- [[Run a Trivy scan, format the report, and send via Telegram.      Args         b]] - rationale - gateway/security/daily_cve_report.py
- [[Run the upstream CVE check for EVERY registered agent, independently.      Itera]] - rationale - gateway/security/daily_cve_report.py
- [[Send a message via Telegram Bot API. Returns True on success.      ``text`` is d]] - rationale - gateway/security/daily_cve_report.py
- [[TestAlreadyCheckedUpstreamToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyIngestedGhsaToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadySentToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestCveReportSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestScheduler]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunUpstreamCveCheck]] - code - gateway/tests/test_daily_cve_report.py
- [[TestSendTelegramTruncation]] - code - gateway/tests/test_daily_cve_report.py
- [[TestUpstreamCveCheckSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[_already_checked_upstream_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_ingested_ghsa_today returns False on a malformed sentinel.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[_already_ingested_ghsa_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_sent_today()]] - code - gateway/security/daily_cve_report.py
- [[_make_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[_running_image()]] - code - gateway/security/daily_cve_report.py
- [[_send_telegram()]] - code - gateway/security/daily_cve_report.py
- [[cve_report_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[daily_cve_report.py]] - code - gateway/security/daily_cve_report.py
- [[datetime_4]] - code - gateway/security/daily_cve_report.py
- [[ghsa_ingest_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[run_and_send_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check_all_agents()]] - code - gateway/security/daily_cve_report.py
- [[test_daily_cve_report.py]] - code - gateway/tests/test_daily_cve_report.py
- [[trivy_report.py]] - code - gateway/security/trivy_report.py
- [[upstream_cve_check_scheduler()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_daily_cve_reportpy
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_test_daily_cve_report.py (2)]]
- 9 edges to [[_COMMUNITY_check_upstream_cves]]
- 7 edges to [[_COMMUNITY_parse_trivy_output (2)]]
- 5 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 5 edges to [[_COMMUNITY__build_image_targets]]
- 5 edges to [[_COMMUNITY_format_upstream_cve_alert]]
- 4 edges to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 4 edges to [[_COMMUNITY_parse_trivy_output]]
- 1 edge to [[_COMMUNITY_AlertDispatcher (2)]]
- 1 edge to [[_COMMUNITY_TestRunningImageResolution]]
- 1 edge to [[_COMMUNITY_TestTrivySkipDirs]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 1 edge to [[_COMMUNITY_TestPerAgentUpstreamChecks]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_TestRunAndSendCveReportImageScans]]

## Top bridge nodes
- [[test_daily_cve_report.py]] - degree 36, connects to 10 communities
- [[daily_cve_report.py]] - degree 25, connects to 8 communities
- [[run_and_send_cve_report()]] - degree 16, connects to 5 communities
- [[trivy_report.py]] - degree 8, connects to 4 communities
- [[Any_67]] - degree 6, connects to 3 communities
