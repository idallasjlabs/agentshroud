---
type: community
cohesion: 0.40
members: 5
---

# TestRunUpstreamCveCheck

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_no_alert_when_registry_current()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_telegram_send_when_no_token()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_error_on_github_api_failure()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_sends_alert_when_new_cves_found()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunUpstreamCveCheck_1]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestRunUpstreamCveCheck
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]

## Top bridge nodes
- [[TestRunUpstreamCveCheck_1]] - degree 5, connects to 1 community