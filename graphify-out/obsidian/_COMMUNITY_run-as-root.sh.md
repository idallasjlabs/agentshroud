---
type: community
members: 4
---

# run-as-root.sh

**Members:** 4 nodes

## Members
- [[dot-test_five_openscap_all_passing()]] - code - gateway/tests/test_scorecard_scoring.py
- [[dot-test_four_with_openscap_running_but_failures()]] - code - gateway/tests/test_scorecard_scoring.py
- [[dot-test_three_baseline_no_openscap()]] - code - gateway/tests/test_scorecard_scoring.py
- [[TestScoreContainerHardening]] - code - gateway/tests/test_scorecard_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/run-as-rootsh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Feature Global Monitor-Only Mode (Observatory Mode)]]

## Top bridge nodes
- [[TestScoreContainerHardening]] - degree 4, connects to 1 community
