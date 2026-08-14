---
type: community
members: 5
---

# scripts/gemini-review.py

**Members:** 5 nodes

## Members
- [[.test_five_with_soc_correlation_and_killswitch()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_four_with_soc_correlation()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_one_baseline_neither_running()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_three_with_falco_and_wazuh()]] - code - gateway/tests/test_scorecard_scoring.py
- [[TestScoreIncidentResponse_1]] - code - gateway/tests/test_scorecard_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/gemini-reviewpy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]

## Top bridge nodes
- [[TestScoreIncidentResponse_1]] - degree 5, connects to 1 community