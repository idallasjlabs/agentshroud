---
type: community
members: 80
---

# test_daily_cve_report.py

**Members:** 80 nodes

## Members
- [[dot-_no_docker()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-_patch_urllib()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_always_includes_every_configured_bot_image()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_always_includes_gateway_image()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_deduplication()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_env_var_adds_extra_targets()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_env_var_empty_string_ignored()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_failed_send_does_not_write_stamp_or_mark_sent_date()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_gateway_container_name_is_env_overridable()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_gives_up_and_marks_sent_after_max_retries()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_raises_on_network_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_retries_on_failed_send_before_giving_up()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_empty_when_all_known()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_file_missing()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_sent_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_new_advisory_not_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_true_when_sent_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_short_text_passes_through_unchanged()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_advisory_whose_cve_is_already_tracked()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_advisory_without_ghsa_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_ghsa_already_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_successful_send_marks_sent_immediately_no_retry()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_truncates_over_length_text()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_undelivered_new_advisory_retries_not_marked_ingested()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_undelivered_new_cves_retries_not_marked_checked()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_uses_github_token_in_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_whitespace_stripped_from_env_var()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_zero_new_cves_marks_checked_immediately()]] - code - gateway/tests/test_daily_cve_report.py
- [[A failed send retries (bounded) within the same day, not next-day.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After the retry cap, the day IS marked done so the loop moves on.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Any_63]] - code - gateway/security/daily_cve_report.py
- [[Background loop checks for new upstream agent CVEs once per day at report_hour]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop pull the GHSA feed as source of truth once per day.      This i]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop sends one CVE report per day at ``report_hour`` UTC.      Runs]] - rationale - gateway/security/daily_cve_report.py
- [[Build a minimal GitHub Security Advisory payload keyed on GHSA id.      ``ghsa_i]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Build the list of container image targets for Trivy image scanning.      Prefers]] - rationale - gateway/security/daily_cve_report.py
- [[Check if a Trivy report was already sent today (disk-based, secondary to _sent_d]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the GHSA ingest already ran today (disk-based, secondary guard).]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the upstream CVE watch already ran today (disk-based).]] - rationale - gateway/security/daily_cve_report.py
- [[Deployments that rename the gateway container (dev runs         agentshroud-marv]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Empty AGENTSHROUD_TRIVY_IMAGES adds no extra entries beyond         gateway + th]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Fetch one agent's GitHub Security Advisories and return advisories we don't trac]] - rationale - gateway/security/daily_cve_report.py
- [[Fetch one agent's upstream CVEs, alert via Telegram, honestly.      Runs a singl]] - rationale - gateway/security/daily_cve_report.py
- [[Nothing to deliver is a legitimate 'done', not a failure to retry.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Path_49]] - code - gateway/security/trivy_report.py
- [[Pin _running_image to the docker-unavailable fallback path so these         test]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Regression guard AGENTSHROUD_TRIVY_IMAGES used to be the ONLY         source of]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Resolve the image tag a container is ACTUALLY running, via docker CLI.      The]] - rationale - gateway/security/daily_cve_report.py
- [[Run a Trivy scan, format the report, and send via Telegram.      Args         b]] - rationale - gateway/security/daily_cve_report.py
- [[Run the upstream CVE check for EVERY registered agent, independently.      Itera]] - rationale - gateway/security/daily_cve_report.py
- [[Save a Trivy report to the log directory.      Args         report Parsed repo]] - rationale - gateway/security/trivy_report.py
- [[Send a message via Telegram Bot API. Returns True on success.      ``text`` is d]] - rationale - gateway/security/daily_cve_report.py
- [[Stub urllib.request.urlopen to return a list of advisories.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestAlreadySentToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestBuildImageTargets]] - code - gateway/tests/test_daily_cve_report.py
- [[TestCheckUpstreamCves]] - code - gateway/tests/test_daily_cve_report.py
- [[TestCveReportSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - code - gateway/tests/test_daily_cve_report.py
- [[TestSendTelegramTruncation]] - code - gateway/tests/test_daily_cve_report.py
- [[TestUpstreamCveCheckSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[_already_checked_upstream_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_ingested_ghsa_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_sent_today()]] - code - gateway/security/daily_cve_report.py
- [[_build_image_targets()]] - code - gateway/security/daily_cve_report.py
- [[_make_github_advisory()]] - code - gateway/tests/test_daily_cve_report.py
- [[_running_image()]] - code - gateway/security/daily_cve_report.py
- [[_send_telegram()]] - code - gateway/security/daily_cve_report.py
- [[check_upstream_cves()]] - code - gateway/security/daily_cve_report.py
- [[cve_report_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[daily_cve_report.py]] - code - gateway/security/daily_cve_report.py
- [[datetime_6]] - code - gateway/security/daily_cve_report.py
- [[ghsa_ingest_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[run_and_send_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check_all_agents()]] - code - gateway/security/daily_cve_report.py
- [[save_report()_1]] - code - gateway/security/trivy_report.py
- [[test_daily_cve_report.py]] - code - gateway/tests/test_daily_cve_report.py
- [[trivy_report.py]] - code - gateway/security/trivy_report.py
- [[upstream_cve_check_scheduler()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_daily_cve_reportpy
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_test_daily_cve_report.py (2)]]
- 8 edges to [[_COMMUNITY_export-bot-conversations.py]]
- 8 edges to [[_COMMUNITY_sync-cve-registry.py (2)]]
- 5 edges to [[_COMMUNITY_parse_trivy_output]]
- 5 edges to [[_COMMUNITY_format_upstream_cve_alert]]
- 5 edges to [[_COMMUNITY_test_daily_cve_report.py (3)]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_TestRunningImageResolution]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_TestTrivySkipDirs]]
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter (8)]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py (4)]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py (5)]]
- 1 edge to [[_COMMUNITY_TestPerAgentUpstreamChecks]]
- 1 edge to [[_COMMUNITY__t]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_TestRunAndSendCveReportImageScans]]

## Top bridge nodes
- [[test_daily_cve_report.py]] - degree 36, connects to 12 communities
- [[daily_cve_report.py]] - degree 25, connects to 5 communities
- [[run_and_send_cve_report()]] - degree 16, connects to 3 communities
- [[save_report()_1]] - degree 11, connects to 3 communities
- [[trivy_report.py]] - degree 7, connects to 3 communities
