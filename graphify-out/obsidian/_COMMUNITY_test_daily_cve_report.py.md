---
type: community
cohesion: 0.05
members: 73
---

# test_daily_cve_report.py

**Cohesion:** 0.05 - loosely connected
**Members:** 73 nodes

## Members
- [[.test_failed_send_does_not_write_stamp_or_mark_sent_date()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_gives_up_and_marks_sent_after_max_retries()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_ingest_records_even_when_disk_write_fails()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_per_agent_check_error_is_isolated_not_fatal()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_retries_on_failed_send_before_giving_up()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()_5]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_ingested_yesterday()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_sent_yesterday()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_summary_without_token()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_ingested_today()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_sent_today()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_runs_ingest_records_then_skips_next_iteration()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_sends_telegram_on_success()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_short_text_passes_through_unchanged()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_ingest_when_marked_done_after_wake()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_successful_send_marks_sent_immediately_no_retry()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_trivy_error_still_sends_error_report()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_truncates_over_length_text()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_undelivered_new_advisory_retries_not_marked_ingested()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_undelivered_new_cves_retries_not_marked_checked()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_zero_new_cves_marks_checked_immediately()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[A failed send retries (bounded) within the same day, not next-day.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A raised per-agent check error is ISOLATED — the ingest still completes.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After the retry cap, the day IS marked done so the loop moves on.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Any_36]] - code
- [[Background loop pull the GHSA feed as source of truth once per day.      This i]] - rationale - gateway/security/daily_cve_report.py
- [[Check if a Trivy report was already sent today (disk-based, secondary to _sent_d]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the GHSA ingest already ran today (disk-based, secondary guard).]] - rationale - gateway/security/daily_cve_report.py
- [[Fetch one agent's upstream CVEs, alert via Telegram, honestly.      Runs a singl]] - rationale - gateway/security/daily_cve_report.py
- [[Nothing to deliver is a legitimate 'done', not a failure to retry.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Parse raw Trivy JSON output into a structured summary.      Args         raw R]] - rationale - gateway/security/trivy_report.py
- [[Return the CVE-pipeline config for bot_id (raises KeyError if unknown).      A]] - rationale - gateway/security/agent_cve_registry.py
- [[Return the list of registered agent bot IDs with CVE coverage.      Returns]] - rationale - gateway/security/agent_cve_registry.py
- [[Run a Trivy scan and return parsed results.      Args         target Scan targ]] - rationale - gateway/security/trivy_report.py
- [[Run a Trivy scan, format the report, and send via Telegram.      Args         b]] - rationale - gateway/security/daily_cve_report.py
- [[Run the upstream CVE check for EVERY registered agent, independently.      Itera]] - rationale - gateway/security/daily_cve_report.py
- [[Save a Trivy report to the log directory.      Args         report Parsed repo]] - rationale - gateway/security/trivy_report.py
- [[Send a message via Telegram Bot API. Returns True on success.      ``text`` is d]] - rationale - gateway/security/daily_cve_report.py
- [[TestAlreadyIngestedGhsaToday_1]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadySentToday_1]] - code - gateway/tests/test_daily_cve_report.py
- [[TestCveReportSchedulerRetry_1]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestScheduler_1]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestSchedulerRetry_1]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReport_1]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent_1]] - code - gateway/tests/test_daily_cve_report.py
- [[TestSendTelegramTruncation_1]] - code - gateway/tests/test_daily_cve_report.py
- [[TestUpstreamCveCheckSchedulerRetry_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_AGENT_CVE_SOURCES]] - code - gateway/security/agent_cve_registry.py
- [[_already_checked_upstream_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_ingested_ghsa_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_sent_today()]] - code - gateway/security/daily_cve_report.py
- [[_make_error_report()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_running_image()]] - code - gateway/security/daily_cve_report.py
- [[_send_telegram()]] - code - gateway/security/daily_cve_report.py
- [[agent_cve_registry.py]] - code - gateway/security/agent_cve_registry.py
- [[cve_report_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[daily_cve_report.py]] - code - gateway/security/daily_cve_report.py
- [[datetime]] - code
- [[generate_summary()_3]] - code - gateway/security/trivy_report.py
- [[get_agent_cve_source()]] - code - gateway/security/agent_cve_registry.py
- [[get_agent_ghsa_repo()]] - code - gateway/security/agent_cve_registry.py
- [[ghsa_ingest_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[list_cve_agents()]] - code - gateway/security/agent_cve_registry.py
- [[parse_trivy_output()]] - code - gateway/security/trivy_report.py
- [[run_and_send_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[run_trivy_scan()_1]] - code - gateway/security/trivy_report.py
- [[run_upstream_cve_check()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check_all_agents()]] - code - gateway/security/daily_cve_report.py
- [[save_report()_1]] - code - gateway/security/trivy_report.py
- [[test_daily_cve_report.py_1]] - code - gateway/tests/test_daily_cve_report.py
- [[trivy_report.py_2]] - code - gateway/security/trivy_report.py
- [[upstream_cve_check_scheduler()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_daily_cve_reportpy
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY__sleep()]]
- 12 edges to [[_COMMUNITY_gateway.security.daily_cve_report]]
- 10 edges to [[_COMMUNITY_format_cve_report()]]
- 7 edges to [[_COMMUNITY_check_upstream_cves()]]
- 6 edges to [[_COMMUNITY__build_image_targets()]]
- 5 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 5 edges to [[_COMMUNITY_.test_gives_up_and_marks_sent_after_max_retries(]]
- 4 edges to [[_COMMUNITY_format_upstream_cve_alert()]]
- 1 edge to [[_COMMUNITY_patch]]
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_server.py]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_AgentShroud Changelog]]
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY__build_image_targets]]
- 1 edge to [[_COMMUNITY_TestAlreadyCheckedUpstreamToday]]
- 1 edge to [[_COMMUNITY_TestPerAgentUpstreamChecks]]
- 1 edge to [[_COMMUNITY_TestRunAndSendCveReportImageScans]]
- 1 edge to [[_COMMUNITY_TestRunningImageResolution]]
- 1 edge to [[_COMMUNITY_TestRunUpstreamCveCheck]]
- 1 edge to [[_COMMUNITY_TestTrivySkipDirs]]

## Top bridge nodes
- [[test_daily_cve_report.py_1]] - degree 38, connects to 11 communities
- [[datetime]] - degree 33, connects to 6 communities
- [[daily_cve_report.py]] - degree 24, connects to 4 communities
- [[run_and_send_cve_report()]] - degree 15, connects to 3 communities
- [[run_upstream_cve_check()]] - degree 9, connects to 3 communities