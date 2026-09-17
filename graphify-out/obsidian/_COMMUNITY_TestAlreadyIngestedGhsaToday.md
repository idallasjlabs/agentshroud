---
type: community
cohesion: 0.50
members: 4
---

# TestAlreadyIngestedGhsaToday

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_returns_false_when_file_missing()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_ingested_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyIngestedGhsaToday]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAlreadyIngestedGhsaToday
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_asyncio]]

## Top bridge nodes
- [[TestAlreadyIngestedGhsaToday]] - degree 4, connects to 1 community