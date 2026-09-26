---
type: community
cohesion: 0.50
members: 4
---

# Red Team Adversarial Tester (SEC-OFFENSE)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_five_all_pillars()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_one_baseline()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_two_with_wazuh()]] - code - gateway/tests/test_scorecard_scoring.py
- [[TestScoreLoggingMonitoring_1]] - code - gateway/tests/test_scorecard_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Red_Team_Adversarial_Tester_SEC-OFFENSE
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Skill Create PR with Pre-Flight Audit (CRPR)]]

## Top bridge nodes
- [[TestScoreLoggingMonitoring_1]] - degree 4, connects to 1 community