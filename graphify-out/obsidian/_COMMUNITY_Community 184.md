---
type: community
members: 51
---

# Community 184

**Members:** 51 nodes

## Members
- [[.test_affected_packages_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_cve_ids()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_package_names()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_severity_counts()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_error_report_shows_error_message()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_failed_send_does_not_write_stamp_or_mark_sent_date()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_fixed_version_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_alert_when_registry_current()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_telegram_send_when_no_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_error_on_github_api_failure()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_checked_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_ingested_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_sent_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_summary_without_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_checked_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_sent_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_sends_alert_when_new_cves_found()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_sends_telegram_on_success()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_short_text_passes_through_unchanged()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_status_clean_when_no_critical_high()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_status_critical_when_critical_present()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_total_vulnerability_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_trivy_error_still_sends_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_truncates_over_length_text()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_undelivered_new_advisory_retries_not_marked_ingested()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_undelivered_new_cves_retries_not_marked_checked()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_zero_count_severity_omitted()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_zero_new_cves_marks_checked_immediately()]] - code - gateway/tests/test_daily_cve_report.py
- [[Build a minimal parsed Trivy report.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Format a Trivy scan result into a Telegram-ready Markdown message.      Args]] - rationale - gateway/security/daily_cve_report.py
- [[Nothing to deliver is a legitimate 'done', not a failure to retry.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyCheckedUpstreamToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyIngestedGhsaToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadySentToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestFormatCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunUpstreamCveCheck]] - code - gateway/tests/test_daily_cve_report.py
- [[TestSendTelegramTruncation]] - code - gateway/tests/test_daily_cve_report.py
- [[TestUpstreamCveCheckSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[daily_cve_report module]] - code - gateway/security/daily_cve_report.py
- [[format_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[test_daily_cve_report.py]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_184
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Community 779]]
- 2 edges to [[_COMMUNITY_Community 990]]
- 2 edges to [[_COMMUNITY_Community 482]]
- 2 edges to [[_COMMUNITY_Community 639]]
- 1 edge to [[_COMMUNITY_Community 162]]
- 1 edge to [[_COMMUNITY_Community 451]]
- 1 edge to [[_COMMUNITY_Community 813]]

## Top bridge nodes
- [[test_daily_cve_report.py]] - degree 30, connects to 6 communities
- [[format_cve_report()]] - degree 17, connects to 2 communities
- [[.test_sends_telegram_on_success()]] - degree 3, connects to 1 community
- [[.test_returns_summary_without_token()]] - degree 3, connects to 1 community
- [[.test_trivy_error_still_sends_error_report()]] - degree 3, connects to 1 community