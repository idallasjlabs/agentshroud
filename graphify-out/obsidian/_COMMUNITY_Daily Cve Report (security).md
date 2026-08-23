---
type: community
cohesion: 0.05
members: 73
---

# Daily Cve Report (security)

**Cohesion:** 0.05 - loosely connected
**Members:** 73 nodes

## Members
- [[.test_already_ingested_helper_swallows_read_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_custom_prefix()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_default_prefix()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_gives_up_and_marks_sent_after_max_retries()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_ingest_records_even_when_disk_write_fails()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_log_dir_created_if_missing()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_per_agent_check_error_is_isolated_not_fatal()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_report_content_persisted()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_retries_on_failed_send_before_giving_up()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_run_binary_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_image_scan_type()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_parse_error()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_success()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_timeout()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_runs_ingest_records_then_skips_next_iteration()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_ingest_when_marked_done_after_wake()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_when_already_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_successful_send_marks_sent_immediately_no_retry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_trivy_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[.test_undelivered_new_advisory_retries_not_marked_ingested()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_undelivered_new_cves_retries_not_marked_checked()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_zero_new_cves_marks_checked_immediately()]] - code - gateway/tests/test_daily_cve_report.py
- [[A disk-write failure on the sentinel is swallowed; in-memory guard set.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A failed send retries (bounded) within the same day, not next-day.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A raised per-agent check error is ISOLATED — the ingest still completes.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After sleeping, if the day is now marked done, the loop skips ingest.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After the retry cap, the day IS marked done so the loop moves on.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Any_37]] - code - gateway/security/daily_cve_report.py
- [[Any_64]] - code - gateway/security/trivy_report.py
- [[Background loop checks for new upstream agent CVEs once per day at report_hour]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop pull the GHSA feed as source of truth once per day.      This i]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop sends one CVE report per day at ``report_hour`` UTC.      Runs]] - rationale - gateway/security/daily_cve_report.py
- [[Check if a Trivy report was already sent today (disk-based, secondary to _sent_d]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the GHSA ingest already ran today (disk-based, secondary guard).]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the upstream CVE watch already ran today (disk-based).]] - rationale - gateway/security/daily_cve_report.py
- [[Custom report_prefix is used verbatim.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Default report_prefix produces a 'trivy-' filename.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Fetch one agent's upstream CVEs, alert via Telegram, honestly.      Runs a singl]] - rationale - gateway/security/daily_cve_report.py
- [[First iteration ingests + records; second sees dedup and skips.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Generate a summary dict suitable for the health report.      Args         repor]] - rationale - gateway/security/trivy_report.py
- [[If already ingested today, the loop bumps to tomorrow and never ingests.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Nothing to deliver is a legitimate 'done', not a failure to retry.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Run a Trivy scan and return parsed results.      Args         target Scan targ]] - rationale - gateway/security/trivy_report.py
- [[Run a Trivy scan, format the report, and send via Telegram.      Args         b]] - rationale - gateway/security/daily_cve_report.py
- [[Run the upstream CVE check for EVERY registered agent, independently.      Itera]] - rationale - gateway/security/daily_cve_report.py
- [[Save a Trivy report to the log directory.      Args         report Parsed repo]] - rationale - gateway/security/trivy_report.py
- [[Saved file is valid JSON containing the report keys.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Send a message via Telegram Bot API. Returns True on success.      ``text`` is d]] - rationale - gateway/security/daily_cve_report.py
- [[TestCveReportSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestScheduler]] - code - gateway/tests/test_daily_cve_report.py
- [[TestTrivyRun]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivySaveReport]] - code - gateway/tests/test_security_toolchain.py
- [[TestUpstreamCveCheckSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[_already_checked_upstream_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_ingested_ghsa_today returns False on a malformed sentinel.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[_already_ingested_ghsa_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_sent_today()]] - code - gateway/security/daily_cve_report.py
- [[_send_telegram()]] - code - gateway/security/daily_cve_report.py
- [[cve_report_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[daily_cve_report.py]] - code - gateway/security/daily_cve_report.py
- [[datetime_9]] - code - gateway/security/daily_cve_report.py
- [[datetime_2]] - code - gateway/security/daily_cve_report.py
- [[generate_summary()_2]] - code - gateway/security/trivy_report.py
- [[ghsa_ingest_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[run_and_send_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[run_trivy_scan()_1]] - code - gateway/security/trivy_report.py
- [[run_upstream_cve_check()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check_all_agents()]] - code - gateway/security/daily_cve_report.py
- [[save_report creates the log directory if it does not exist.]] - rationale - gateway/tests/test_security_toolchain.py
- [[save_report()_1]] - code - gateway/security/trivy_report.py
- [[scan_type='image' is passed correctly to the trivy binary.]] - rationale - gateway/tests/test_security_toolchain.py
- [[trivy_report.py]] - code - gateway/security/trivy_report.py
- [[upstream_cve_check_scheduler()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Daily_Cve_Report_security
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Daily Cve Report]]
- 8 edges to [[_COMMUNITY_Daily Cve Report]]
- 7 edges to [[_COMMUNITY_Security Toolchain]]
- 6 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 5 edges to [[_COMMUNITY_Generate Cve Page (scripts)]]
- 5 edges to [[_COMMUNITY_Security Toolchain]]
- 3 edges to [[_COMMUNITY_Daily Cve Report]]
- 3 edges to [[_COMMUNITY_Daily Cve Report]]
- 3 edges to [[_COMMUNITY_Health Report (security)]]
- 3 edges to [[_COMMUNITY_OAuth & Metadata Guard]]
- 2 edges to [[_COMMUNITY_Group Config & Collaborator Responses]]
- 2 edges to [[_COMMUNITY_SOC Router (Collaborator Mgmt)]]
- 2 edges to [[_COMMUNITY_Deployment (runbooks)]]
- 1 edge to [[_COMMUNITY_Enhanced Approval]]
- 1 edge to [[_COMMUNITY_Queue (approval_queue)]]
- 1 edge to [[_COMMUNITY_Config]]
- 1 edge to [[_COMMUNITY_Sync Cve Registry (scripts)]]
- 1 edge to [[_COMMUNITY_Cron State Monitor]]
- 1 edge to [[_COMMUNITY_Apply Patches (openclaw)]]
- 1 edge to [[_COMMUNITY_Openapi (gateway)]]
- 1 edge to [[_COMMUNITY_Security]]
- 1 edge to [[_COMMUNITY_Scanner Integration (security)]]
- 1 edge to [[_COMMUNITY_Scanner Integration Coverage]]
- 1 edge to [[_COMMUNITY_Soc Models]]
- 1 edge to [[_COMMUNITY_Generate Job Schedule (scripts)]]
- 1 edge to [[_COMMUNITY_Browse (scripts)]]

## Top bridge nodes
- [[daily_cve_report.py]] - degree 31, connects to 13 communities
- [[datetime_9]] - degree 22, connects to 8 communities
- [[trivy_report.py]] - degree 11, connects to 6 communities
- [[run_and_send_cve_report()]] - degree 16, connects to 4 communities
- [[generate_summary()_2]] - degree 9, connects to 4 communities