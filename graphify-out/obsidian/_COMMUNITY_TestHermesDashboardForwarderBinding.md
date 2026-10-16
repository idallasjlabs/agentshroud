---
type: community
cohesion: 0.33
members: 6
---

# TestHermesDashboardForwarderBinding

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[dot-test_consistent_response_scores_high()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_language_mismatch_or_anomalies()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_off_topic_response_scores_low()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_unsolicited_tool_call_flagged()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-tracker()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[TestResponseConsistency]] - code - gateway/tests/test_multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestHermesDashboardForwarderBinding
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_MultiTurnTracker_1]]

## Top bridge nodes
- [[TestResponseConsistency]] - degree 9, connects to 2 communities
- [[dot-tracker()]] - degree 2, connects to 1 community
