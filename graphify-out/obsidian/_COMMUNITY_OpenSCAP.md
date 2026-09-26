---
type: community
cohesion: 0.30
members: 15
---

# OpenSCAP

**Cohesion:** 0.30 - loosely connected
**Members:** 15 nodes

## Members
- [[._cve()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_alert_states_auto_registered_under_review()]] - code - gateway/tests/test_daily_cve_report.py
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
- [[The alert says CVEs are auto-registered under_review (honest, not 'add manually']] - rationale - gateway/tests/test_daily_cve_report.py
- [[format_upstream_cve_alert()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OpenSCAP
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_PrivacyPolicyEnforcer]]

## Top bridge nodes
- [[format_upstream_cve_alert()]] - degree 15, connects to 1 community
- [[TestFormatUpstreamCveAlert]] - degree 12, connects to 1 community