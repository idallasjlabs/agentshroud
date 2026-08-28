---
type: community
cohesion: 0.40
members: 5
---

# Community 1270

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_no_alert_when_registry_current()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_telegram_send_when_no_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_error_on_github_api_failure()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_sends_alert_when_new_cves_found()]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunUpstreamCveCheck]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1270
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Community 122]]

## Top bridge nodes
- [[TestRunUpstreamCveCheck]] - degree 5, connects to 1 community