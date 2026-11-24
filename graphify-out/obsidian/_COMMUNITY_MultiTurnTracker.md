---
type: community
members: 22
---

# MultiTurnTracker

**Members:** 22 nodes

## Members
- [[dot-__init__()_212]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_cleanup_old_sessions()_1]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_compile_detection_patterns()_1]] - code - gateway/security/multi_turn_tracker.py
- [[dot-add_alert_callback()_2]] - code - gateway/security/multi_turn_tracker.py
- [[dot-get_global_stats()_1]] - code - gateway/security/multi_turn_tracker.py
- [[dot-get_session_stats()_1]] - code - gateway/security/multi_turn_tracker.py
- [[dot-reset_session()_1]] - code - gateway/security/multi_turn_tracker.py
- [[dot-test_disabled_tracker()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[Add a callback function for alerts.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Any_82]] - code
- [[Compile regex patterns for detecting disclosure categories.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Configuration for alert thresholds.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Get global tracking statistics.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Get statistics for a session._1]] - rationale - gateway/security/multi_turn_tracker.py
- [[Initialize the multi-turn tracker. Args config Configuration dictionary with…]] - rationale - gateway/security/multi_turn_tracker.py
- [[Main multi-turn disclosure tracking engine. Maintains session state and scores…]] - rationale - gateway/security/multi_turn_tracker.py
- [[MultiTurnTracker]] - code - gateway/security/multi_turn_tracker.py
- [[Remove old sessions to prevent memory bloat._1]] - rationale - gateway/security/multi_turn_tracker.py
- [[Reset session score after owner review. Args session_id Session to reset…]] - rationale - gateway/security/multi_turn_tracker.py
- [[Test that disabled tracker doesn't track or score.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[ThresholdConfig]] - code - gateway/security/multi_turn_tracker.py
- [[callable_1]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MultiTurnTracker
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_SessionContext]]
- 3 edges to [[_COMMUNITY_TestResponseConsistency]]
- 3 edges to [[_COMMUNITY_multi_turn_tracker.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_TestMultiTurnTracker]]
- 2 edges to [[_COMMUNITY_PathIsolationManager]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_ConsistencyScore]]

## Top bridge nodes
- [[MultiTurnTracker]] - degree 31, connects to 9 communities
- [[ThresholdConfig]] - degree 3, connects to 1 community
- [[dot-_cleanup_old_sessions()_1]] - degree 3, connects to 1 community
- [[dot-test_disabled_tracker()]] - degree 3, connects to 1 community
