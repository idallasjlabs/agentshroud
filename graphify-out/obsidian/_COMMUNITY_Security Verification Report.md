---
type: community
cohesion: 0.28
members: 16
---

# Security Verification Report

**Cohesion:** 0.28 - loosely connected
**Members:** 16 nodes

## Members
- [[.test_affected_packages_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_cve_ids()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_package_names()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_severity_counts()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_error_report_shows_error_message()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_fixed_version_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_status_clean_when_no_critical_high()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_status_critical_when_critical_present()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_total_vulnerability_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_zero_count_severity_omitted()]] - code - gateway/tests/test_daily_cve_report.py
- [[Build a minimal parsed Trivy report.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Format a Trivy scan result into a Telegram-ready Markdown message.      Args]] - rationale - gateway/security/daily_cve_report.py
- [[TestFormatCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[format_cve_report()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Security_Verification_Report
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_PrivacyPolicyEnforcer]]

## Top bridge nodes
- [[format_cve_report()]] - degree 17, connects to 1 community
- [[_make_report()]] - degree 15, connects to 1 community
- [[TestFormatCveReport]] - degree 12, connects to 1 community
- [[.test_error_report_shows_error_message()]] - degree 3, connects to 1 community