---
type: community
cohesion: 0.28
members: 16
---

# format_cve_report()

**Cohesion:** 0.28 - loosely connected
**Members:** 16 nodes

## Members
- [[.test_affected_packages_count_shown()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_cve_ids()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_header()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_package_names()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_severity_counts()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_error_report_shows_error_message()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_fixed_version_shown()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_status_clean_when_no_critical_high()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_status_critical_when_critical_present()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_total_vulnerability_count_shown()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_zero_count_severity_omitted()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[Build a minimal parsed Trivy report.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Format a Trivy scan result into a Telegram-ready Markdown message.      Args]] - rationale - gateway/security/daily_cve_report.py
- [[TestFormatCveReport_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_report()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[format_cve_report()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/format_cve_report
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 2 edges to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_gateway.security.daily_cve_report]]

## Top bridge nodes
- [[format_cve_report()]] - degree 17, connects to 2 communities
- [[_make_report()_1]] - degree 15, connects to 1 community
- [[TestFormatCveReport_1]] - degree 12, connects to 1 community
- [[.test_error_report_shows_error_message()_1]] - degree 3, connects to 1 community
- [[Format a Trivy scan result into a Telegram-ready Markdown message.      Args]] - degree 2, connects to 1 community