---
type: community
members: 52
---

# Community 127

**Members:** 52 nodes

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
- [[.test_zero_count_severity_omitted()]] - code - gateway/tests/test_daily_cve_report.py
- [[Background loop sends one CVE report per day at ``report_hour`` UTC.      Runs]] - rationale - gateway/security/daily_cve_report.py
- [[Build a minimal parsed Trivy report.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Check if a Trivy report was already sent today (disk-based, secondary to _sent_d]] - rationale - gateway/security/daily_cve_report.py
- [[Format a Trivy scan result into a Telegram-ready Markdown message.      Args]] - rationale - gateway/security/daily_cve_report.py
- [[Keep the alerted-advisory state file out of varlog in every test.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Run a Trivy scan, format the report, and send via Telegram.      Args         b]] - rationale - gateway/security/daily_cve_report.py
- [[TestAlreadyCheckedUpstreamToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyIngestedGhsaToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadySentToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestFormatCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunUpstreamCveCheck]] - code - gateway/tests/test_daily_cve_report.py
- [[TestSendTelegramTruncation]] - code - gateway/tests/test_daily_cve_report.py
- [[_already_sent_today()]] - code - gateway/security/daily_cve_report.py
- [[_isolated_alert_state()]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[cve_report_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[format_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[run_and_send_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[test_daily_cve_report.py]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_127
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Community 135]]
- 5 edges to [[_COMMUNITY_Community 131]]
- 5 edges to [[_COMMUNITY_Community 736]]
- 3 edges to [[_COMMUNITY_Community 1200]]
- 2 edges to [[_COMMUNITY_Community 1202]]
- 1 edge to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 74]]
- 1 edge to [[_COMMUNITY_Community 42]]
- 1 edge to [[_COMMUNITY_Community 10]]
- 1 edge to [[_COMMUNITY_Community 1001]]
- 1 edge to [[_COMMUNITY_Community 1554]]
- 1 edge to [[_COMMUNITY_Community 2048]]
- 1 edge to [[_COMMUNITY_Community 2099]]
- 1 edge to [[_COMMUNITY_Community 2003]]

## Top bridge nodes
- [[test_daily_cve_report.py]] - degree 34, connects to 12 communities
- [[run_and_send_cve_report()]] - degree 16, connects to 4 communities
- [[format_cve_report()]] - degree 17, connects to 2 communities
- [[_already_sent_today()]] - degree 6, connects to 2 communities
- [[cve_report_scheduler()]] - degree 5, connects to 2 communities