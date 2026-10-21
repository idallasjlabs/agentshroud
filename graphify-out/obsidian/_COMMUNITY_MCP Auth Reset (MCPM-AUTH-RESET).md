---
type: community
members: 6
---

# MCP Auth Reset (MCPM-AUTH-RESET)

**Members:** 6 nodes

## Members
- [[dot-test_four_clean_but_stale()]] - code - gateway/tests/test_scorecard_scoring.py
- [[dot-test_one_when_not_run()_1]] - code - gateway/tests/test_scorecard_scoring.py
- [[dot-test_one_with_criticals()]] - code - gateway/tests/test_scorecard_scoring.py
- [[dot-test_three_with_mediums_only()]] - code - gateway/tests/test_scorecard_scoring.py
- [[dot-test_two_with_highs_no_criticals()]] - code - gateway/tests/test_scorecard_scoring.py
- [[TestScoreVulnerabilityManagement]] - code - gateway/tests/test_scorecard_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCP_Auth_Reset_MCPM-AUTH-RESET
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Command Details]]
- 1 edge to [[_COMMUNITY_Feature Global Monitor-Only Mode (Observatory Mode)]]
- 1 edge to [[_COMMUNITY_OpenSCAP]]

## Top bridge nodes
- [[TestScoreVulnerabilityManagement]] - degree 7, connects to 2 communities
- [[dot-test_four_clean_but_stale()]] - degree 2, connects to 1 community
