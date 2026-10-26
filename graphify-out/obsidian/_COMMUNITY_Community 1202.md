---
type: community
members: 17
---

# Community 1202

**Members:** 17 nodes

## Members
- [[._cve()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_alert_does_not_claim_registration()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_alert_says_when_no_fix_is_published()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_alert_shows_fixed_in_version()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_alert_titled_for_agent_label()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_cve_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_severity_icon()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_total_count()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_handles_missing_optional_fields()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_more_indicator_when_under_item_limit()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_plural_header_for_multiple_cves()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_singular_header_for_one_cve()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_summary_under_telegram_limit_for_100_cves()]] - code - gateway/tests/test_daily_cve_report.py
- [[Format a Telegram alert for newly detected upstream CVEs.      The alert is titl]] - rationale - gateway/security/daily_cve_report.py
- [[TestFormatUpstreamCveAlert]] - code - gateway/tests/test_daily_cve_report.py
- [[The gateway never writes the registry, so the alert must not say it did.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[format_upstream_cve_alert()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1202
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 135]]
- 2 edges to [[_COMMUNITY_Community 127]]

## Top bridge nodes
- [[format_upstream_cve_alert()]] - degree 17, connects to 2 communities
- [[TestFormatUpstreamCveAlert]] - degree 14, connects to 1 community