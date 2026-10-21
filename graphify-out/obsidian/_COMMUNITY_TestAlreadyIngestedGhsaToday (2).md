---
type: community
members: 4
---

# TestAlreadyIngestedGhsaToday (2)

**Members:** 4 nodes

## Members
- [[dot-test_returns_false_when_file_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_ingested_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_true_when_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyIngestedGhsaToday]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAlreadyIngestedGhsaToday_2
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]

## Top bridge nodes
- [[TestAlreadyIngestedGhsaToday]] - degree 4, connects to 1 community
