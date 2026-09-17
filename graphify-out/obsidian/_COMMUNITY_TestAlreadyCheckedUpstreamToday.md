---
type: community
cohesion: 0.50
members: 4
---

# TestAlreadyCheckedUpstreamToday

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_returns_false_when_checked_yesterday()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()_4]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_checked_today()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyCheckedUpstreamToday_1]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAlreadyCheckedUpstreamToday
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]

## Top bridge nodes
- [[TestAlreadyCheckedUpstreamToday_1]] - degree 4, connects to 1 community