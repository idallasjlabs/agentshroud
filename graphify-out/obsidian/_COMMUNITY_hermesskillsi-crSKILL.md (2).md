---
type: community
members: 7
---

# hermes/skills/i-cr/SKILL.md (2)

**Members:** 7 nodes

## Members
- [[dot-test_returns_false_for_empty_dir()]] - code - gateway/tests/test_scorecard_scoring.py
- [[dot-test_returns_false_for_missing_dir()]] - code - gateway/tests/test_scorecard_scoring.py
- [[dot-test_returns_false_for_stale_file()]] - code - gateway/tests/test_scorecard_scoring.py
- [[dot-test_returns_true_for_fresh_file()]] - code - gateway/tests/test_scorecard_scoring.py
- [[dot-test_three_zero_failures_no_report_on_disk()]] - code - gateway/tests/test_scorecard_scoring.py
- [[TestIsFresh]] - code - gateway/tests/test_scorecard_scoring.py
- [[_mock_empty_dir()]] - code - gateway/tests/test_scorecard_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/hermes/skills/i-cr/SKILLmd_2
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Command Details]]
- 2 edges to [[_COMMUNITY_Feature Global Monitor-Only Mode (Observatory Mode)]]
- 2 edges to [[_COMMUNITY_OpenSCAP]]

## Top bridge nodes
- [[TestIsFresh]] - degree 5, connects to 1 community
- [[_mock_empty_dir()]] - degree 3, connects to 1 community
- [[dot-test_returns_false_for_missing_dir()]] - degree 2, connects to 1 community
- [[dot-test_returns_false_for_stale_file()]] - degree 2, connects to 1 community
- [[dot-test_returns_true_for_fresh_file()]] - degree 2, connects to 1 community
