---
type: community
members: 28
---

# test_daily_cve_report.py

**Members:** 28 nodes

## Members
- [[dot-test_affected_packages_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_cve_ids()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_package_names()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_severity_counts()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_error_report_shows_error_message()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_fixed_version_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_checked_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_file_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_file_missing()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_ingested_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_true_when_checked_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_true_when_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_status_clean_when_no_critical_high()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_status_critical_when_critical_present()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_total_vulnerability_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_zero_count_severity_omitted()]] - code - gateway/tests/test_daily_cve_report.py
- [[Build a minimal parsed Trivy report.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Format a Trivy scan result into a Telegram-ready Markdown message. Args…]] - rationale - gateway/security/daily_cve_report.py
- [[TestAlreadyCheckedUpstreamToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyIngestedGhsaToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestFormatCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - code - gateway/tests/test_daily_cve_report.py
- [[Tests for gateway.security.daily_cve_report.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[_make_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[format_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[test_daily_cve_report.py]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_daily_cve_reportpy
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_asyncio_1]]
- 5 edges to [[_COMMUNITY_daily_cve_report.py]]
- 3 edges to [[_COMMUNITY_check_upstream_cves]]
- 3 edges to [[_COMMUNITY__sleep]]
- 3 edges to [[_COMMUNITY__build_image_targets]]
- 2 edges to [[_COMMUNITY_format_upstream_cve_alert]]
- 2 edges to [[_COMMUNITY_dot-test_gives_up_and_marks_sent_after_max_retries]]
- 2 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_TestRunningImageResolution]]
- 1 edge to [[_COMMUNITY_TestUpstreamAlertDedup]]
- 1 edge to [[_COMMUNITY_dot-_run_proxy]]
- 1 edge to [[_COMMUNITY_list_cve_agents]]
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]

## Top bridge nodes
- [[test_daily_cve_report.py]] - degree 35, connects to 13 communities
- [[format_cve_report()]] - degree 17, connects to 3 communities
- [[_make_report()]] - degree 21, connects to 1 community
- [[_make_error_report()]] - degree 3, connects to 1 community
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - degree 2, connects to 1 community
