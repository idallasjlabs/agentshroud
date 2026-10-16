---
type: community
cohesion: 0.08
members: 45
---

# test_daily_cve_report.py

**Cohesion:** 0.08 - loosely connected
**Members:** 45 nodes

## Members
- [[dot-test_affected_packages_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_cve_ids()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_package_names()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_severity_counts()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_error_report_shows_error_message()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_failed_send_does_not_write_stamp_or_mark_sent_date()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_fixed_version_shown()]] - code - gateway/tests/test_daily_cve_report.py
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
- [[dot-test_sends_telegram_on_success()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_short_text_passes_through_unchanged()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_status_clean_when_no_critical_high()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_status_critical_when_critical_present()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_total_vulnerability_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_trivy_error_still_sends_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_truncates_over_length_text()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_zero_count_severity_omitted()]] - code - gateway/tests/test_daily_cve_report.py
- [[Background loop sends one CVE report per day at ``report_hour`` UTC.      Runs]] - rationale - gateway/security/daily_cve_report.py
- [[Build a minimal parsed Trivy report.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Check if a Trivy report was already sent today (disk-based, secondary to _sent_d]] - rationale - gateway/security/daily_cve_report.py
- [[Format a Trivy scan result into a Telegram-ready Markdown message.      Args]] - rationale - gateway/security/daily_cve_report.py
- [[Run a Trivy scan, format the report, and send via Telegram.      Args         b]] - rationale - gateway/security/daily_cve_report.py
- [[TestAlreadyCheckedUpstreamToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyIngestedGhsaToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadySentToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestFormatCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - code - gateway/tests/test_daily_cve_report.py
- [[TestSendTelegramTruncation]] - code - gateway/tests/test_daily_cve_report.py
- [[_already_sent_today()]] - code - gateway/security/daily_cve_report.py
- [[_make_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[cve_report_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[format_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[run_and_send_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[test_daily_cve_report.py]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_daily_cve_reportpy
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_test_daily_cve_report.py_1]]
- 5 edges to [[_COMMUNITY_test_daily_cve_report.py_2]]
- 4 edges to [[_COMMUNITY__build_image_targets]]
- 3 edges to [[_COMMUNITY_check_upstream_cves]]
- 2 edges to [[_COMMUNITY_export-bot-conversations.py_1]]
- 2 edges to [[_COMMUNITY_format_upstream_cve_alert]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_TestRunningImageResolution]]
- 1 edge to [[_COMMUNITY_TestTrivySkipDirs]]
- 1 edge to [[_COMMUNITY_TestRunAndSendCveReportImageScans]]
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter_6]]
- 1 edge to [[_COMMUNITY_TestPerAgentUpstreamChecks]]

## Top bridge nodes
- [[test_daily_cve_report.py]] - degree 36, connects to 13 communities
- [[run_and_send_cve_report()]] - degree 16, connects to 4 communities
- [[_already_sent_today()]] - degree 6, connects to 2 communities
- [[cve_report_scheduler()]] - degree 5, connects to 2 communities
- [[format_cve_report()]] - degree 17, connects to 1 community
