---
type: community
cohesion: 0.05
members: 61
---

# Multi Turn Tracker (security)

**Cohesion:** 0.05 - loosely connected
**Members:** 61 nodes

## Members
- [[.__init__()_100]] - code - gateway/security/multi_turn_tracker.py
- [[._add_disclosure_event()]] - code - gateway/security/multi_turn_tracker.py
- [[._analyze_agent_response()]] - code - gateway/security/multi_turn_tracker.py
- [[._analyze_user_message()]] - code - gateway/security/multi_turn_tracker.py
- [[._check_thresholds()]] - code - gateway/security/multi_turn_tracker.py
- [[._cleanup_old_sessions()]] - code - gateway/security/multi_turn_tracker.py
- [[._compile_detection_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[._normalize_query()]] - code - gateway/security/multi_turn_tracker.py
- [[._score_message_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[._score_response_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[._trigger_alert()]] - code - gateway/security/multi_turn_tracker.py
- [[.add_alert_callback()]] - code - gateway/security/multi_turn_tracker.py
- [[.get_global_stats()]] - code - gateway/security/multi_turn_tracker.py
- [[.get_session_stats()]] - code - gateway/security/multi_turn_tracker.py
- [[.reset_session()_1]] - code - gateway/security/multi_turn_tracker.py
- [[.score_response_consistency()]] - code - gateway/security/multi_turn_tracker.py
- [[.test_consistent_response_scores_high()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_language_mismatch_or_anomalies()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_off_topic_response_scores_low()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_unsolicited_tool_call_flagged()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.track_message()]] - code - gateway/security/multi_turn_tracker.py
- [[.tracker()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[A single disclosure event in a session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Add a callback function for alerts.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Add a disclosure event to the session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Alert severity levels.]] - rationale - gateway/security/multi_turn_tracker.py
- [[AlertLevel]] - code - gateway/security/multi_turn_tracker.py
- [[Analyze agent response for potential information leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze user message for disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Any_50]] - code - gateway/security/multi_turn_tracker.py
- [[Categories of information that contribute to disclosure scoring.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Check session score against thresholds and take action.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Compile regex patterns for detecting disclosure categories.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Compute a heuristic consistency score between query and response.          Retur]] - rationale - gateway/security/multi_turn_tracker.py
- [[Configuration for alert thresholds.]] - rationale - gateway/security/multi_turn_tracker.py
- [[ConsistencyScore]] - code - gateway/security/multi_turn_tracker.py
- [[Create a MultiTurnTracker instance for testing.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Create a mock alert callback for testing.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[DisclosureCategory]] - code - gateway/security/multi_turn_tracker.py
- [[DisclosureEvent]] - code - gateway/security/multi_turn_tracker.py
- [[Get global tracking statistics.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Get statistics for a session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Heuristic consistency score between a query and its response.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Initialize the multi-turn tracker.          Args             config Configurat]] - rationale - gateway/security/multi_turn_tracker.py
- [[Main multi-turn disclosure tracking engine.      Maintains session state and sco]] - rationale - gateway/security/multi_turn_tracker.py
- [[MultiTurnTracker]] - code - gateway/security/multi_turn_tracker.py
- [[Normalize query for repeated query detection.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Remove old sessions to prevent memory bloat.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Reset session score after owner review.          Args             session_id S]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score agent response for potential leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score message based on disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[SessionContext_1]] - code - gateway/security/multi_turn_tracker.py
- [[TestResponseConsistency]] - code - gateway/tests/test_multi_turn_tracker.py
- [[ThresholdConfig]] - code - gateway/security/multi_turn_tracker.py
- [[Track a message and response pair for disclosure analysis.          Args]] - rationale - gateway/security/multi_turn_tracker.py
- [[Trigger alert callbacks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[callable]] - code - gateway/security/multi_turn_tracker.py
- [[mock_alert_callback()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[multi_turn_tracker()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[multi_turn_tracker.py]] - code - gateway/security/multi_turn_tracker.py
- [[test_multi_turn_tracker.py]] - code - gateway/tests/test_multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Multi_Turn_Tracker_security
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 7 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 5 edges to [[_COMMUNITY_Multi Turn Tracker]]
- 1 edge to [[_COMMUNITY_Context Guard (security)]]
- 1 edge to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 1 edge to [[_COMMUNITY_All Modules Enforce]]

## Top bridge nodes
- [[MultiTurnTracker]] - degree 42, connects to 3 communities
- [[multi_turn_tracker.py]] - degree 12, connects to 2 communities
- [[AlertLevel]] - degree 8, connects to 2 communities
- [[DisclosureCategory]] - degree 8, connects to 2 communities
- [[SessionContext_1]] - degree 10, connects to 1 community