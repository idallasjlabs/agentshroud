---
type: community
cohesion: 0.17
members: 12
---

# Community 813

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-test_default_revert_minutes_is_30()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_invalid_mode_returns_400()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_response_includes_previous_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_response_includes_revert_minutes()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_revert_minutes_clamped_max()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_revert_minutes_clamped_min()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_set_enforce_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_set_monitor_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_set_observatory_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[TestSetMode]] - code - gateway/tests/test_observatory_mode.py
- [[revert_after_minutes above 480 is clamped to 480.]] - rationale - gateway/tests/test_observatory_mode.py
- [[revert_after_minutes below 1 is clamped to 1.]] - rationale - gateway/tests/test_observatory_mode.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_813
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 42]]
- 1 edge to [[_COMMUNITY_Signed Instruction Envelopes & Security Pipeline]]
- 1 edge to [[_COMMUNITY_Community 54]]

## Top bridge nodes
- [[TestSetMode]] - degree 14, connects to 3 communities