---
type: community
cohesion: 0.38
members: 12
---

# Module Group 333

**Cohesion:** 0.38 - loosely connected
**Members:** 12 nodes

## Members
- [[._cve()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_action_required()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_cve_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_disclosed_date()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_severity_icon()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_summary()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_handles_missing_optional_fields()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_plural_header_for_multiple_cves()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_singular_header_for_one_cve()]] - code - gateway/tests/test_daily_cve_report.py
- [[Format a Telegram alert for newly detected upstream CVEs.      Args         new]] - rationale - gateway/security/daily_cve_report.py
- [[TestFormatUpstreamCveAlert]] - code - gateway/tests/test_daily_cve_report.py
- [[format_upstream_cve_alert()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_333
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Module Group 250]]
- 2 edges to [[_COMMUNITY_Module Group 169]]
- 1 edge to [[_COMMUNITY_Module Group 176]]

## Top bridge nodes
- [[format_upstream_cve_alert()]] - degree 13, connects to 3 communities
- [[TestFormatUpstreamCveAlert]] - degree 10, connects to 1 community