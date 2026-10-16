---
type: community
cohesion: 0.07
members: 42
---

# MultiTurnTracker

**Cohesion:** 0.07 - loosely connected
**Members:** 42 nodes

## Members
- [[dot-__init__()_139]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_add_disclosure_event()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_analyze_agent_response()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_analyze_user_message()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_check_thresholds()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_cleanup_old_sessions()_1]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_compile_detection_patterns()_1]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_normalize_query()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_score_message_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_score_response_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_trigger_alert()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-add_alert_callback()_2]] - code - gateway/security/multi_turn_tracker.py
- [[dot-get_global_stats()_1]] - code - gateway/security/multi_turn_tracker.py
- [[dot-get_session_stats()_1]] - code - gateway/security/multi_turn_tracker.py
- [[dot-reset_session()_1]] - code - gateway/security/multi_turn_tracker.py
- [[dot-test_multi_turn_tracker_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-track_message()]] - code - gateway/security/multi_turn_tracker.py
- [[A single disclosure event in a session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Add a callback function for alerts.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Add a disclosure event to the session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze agent response for potential information leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze user message for disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Any_58]] - code - gateway/security/multi_turn_tracker.py
- [[Check session score against thresholds and take action.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Compile regex patterns for detecting disclosure categories.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Configuration for alert thresholds.]] - rationale - gateway/security/multi_turn_tracker.py
- [[DisclosureEvent]] - code - gateway/security/multi_turn_tracker.py
- [[Get global tracking statistics.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Get statistics for a session._1]] - rationale - gateway/security/multi_turn_tracker.py
- [[Initialize the multi-turn tracker.          Args             config Configurat]] - rationale - gateway/security/multi_turn_tracker.py
- [[Main multi-turn disclosure tracking engine.      Maintains session state and sco]] - rationale - gateway/security/multi_turn_tracker.py
- [[MultiTurnTracker]] - code - gateway/security/multi_turn_tracker.py
- [[Normalize query for repeated query detection.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Remove old sessions to prevent memory bloat._1]] - rationale - gateway/security/multi_turn_tracker.py
- [[Reset session score after owner review.          Args             session_id S]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score agent response for potential leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score message based on disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[SessionContext_1]] - code - gateway/security/multi_turn_tracker.py
- [[ThresholdConfig]] - code - gateway/security/multi_turn_tracker.py
- [[Track a message and response pair for disclosure analysis.          Args]] - rationale - gateway/security/multi_turn_tracker.py
- [[Trigger alert callbacks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[callable_1]] - code - gateway/security/multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MultiTurnTracker
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_MiddlewareManager]]
- 11 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_TestMultiTurnTracker]]
- 1 edge to [[_COMMUNITY_dot-analyze_message]]

## Top bridge nodes
- [[MultiTurnTracker]] - degree 42, connects to 3 communities
- [[SessionContext_1]] - degree 10, connects to 2 communities
- [[dot-_add_disclosure_event()]] - degree 8, connects to 1 community
- [[dot-_trigger_alert()]] - degree 5, connects to 1 community
- [[DisclosureEvent]] - degree 3, connects to 1 community
