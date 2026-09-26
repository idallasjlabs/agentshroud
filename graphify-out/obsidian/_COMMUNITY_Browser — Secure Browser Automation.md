---
type: community
cohesion: 0.50
members: 4
---

# Browser — Secure Browser Automation

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_returns_false_when_checked_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_checked_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyCheckedUpstreamToday]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Browser__Secure_Browser_Automation
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_PrivacyPolicyEnforcer]]

## Top bridge nodes
- [[TestAlreadyCheckedUpstreamToday]] - degree 4, connects to 1 community