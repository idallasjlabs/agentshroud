---
type: community
members: 23
---

# Community 762

**Members:** 23 nodes

## Members
- [[.test_affected_packages_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_cve_ids()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_package_names()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_severity_counts()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_error_report_shows_error_message()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_failed_send_does_not_write_stamp_or_mark_sent_date()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_fixed_version_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_summary_without_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_sends_telegram_on_success()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_status_clean_when_no_critical_high()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_status_critical_when_critical_present()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_total_vulnerability_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_trivy_error_still_sends_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_zero_count_severity_omitted()]] - code - gateway/tests/test_daily_cve_report.py
- [[Build a minimal parsed Trivy report.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Format a Trivy scan result into a Telegram-ready Markdown message.      Args]] - rationale - gateway/security/daily_cve_report.py
- [[TestFormatCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[format_cve_report()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_762
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Community 736]]
- 6 edges to [[_COMMUNITY_Community 127]]
- 1 edge to [[_COMMUNITY_Community 131]]

## Top bridge nodes
- [[format_cve_report()]] - degree 17, connects to 3 communities
- [[_make_report()]] - degree 15, connects to 1 community
- [[TestFormatCveReport]] - degree 12, connects to 1 community
- [[TestRunAndSendCveReport]] - degree 4, connects to 1 community
- [[_make_error_report()]] - degree 3, connects to 1 community