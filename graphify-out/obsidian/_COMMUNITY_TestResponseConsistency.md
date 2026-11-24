---
type: community
members: 11
---

# TestResponseConsistency

**Members:** 11 nodes

## Members
- [[dot-test_consistent_response_scores_high()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_language_mismatch_or_anomalies()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_off_topic_response_scores_low()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_unsolicited_tool_call_flagged()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-tracker()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[Create a MultiTurnTracker instance for testing.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Create a mock alert callback for testing.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[TestResponseConsistency]] - code - gateway/tests/test_multi_turn_tracker.py
- [[fixture_49]] - code
- [[mock_alert_callback()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[multi_turn_tracker()]] - code - gateway/tests/test_multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestResponseConsistency
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_multi_turn_tracker.py]]
- 3 edges to [[_COMMUNITY_MultiTurnTracker]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[multi_turn_tracker()]] - degree 5, connects to 3 communities
- [[TestResponseConsistency]] - degree 7, connects to 2 communities
- [[mock_alert_callback()]] - degree 3, connects to 1 community
- [[dot-tracker()]] - degree 3, connects to 1 community
