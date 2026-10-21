---
type: community
members: 105
---

# MultiTurnTracker

**Members:** 105 nodes

## Members
- [[dot-__init__()_122]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_add_disclosure_event()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_analyze_agent_response()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_analyze_user_message()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_check_thresholds()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_cleanup_old_sessions()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_compile_detection_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_normalize_query()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_score_message_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_score_response_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_trigger_alert()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-add_alert_callback()_2]] - code - gateway/security/multi_turn_tracker.py
- [[dot-get_global_stats()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-get_session_stats()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-reset_session()_1]] - code - gateway/security/multi_turn_tracker.py
- [[dot-score_response_consistency()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-test_agent_response_analysis()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_alert_callbacks()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_basic_message_tracking()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_blocked_session_behavior()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_consistent_response_scores_high()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_credential_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_cumulative_scoring()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_disabled_tracker()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_edge_cases()_1]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_file_reference_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_infrastructure_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_initialization()_3]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_language_mismatch_or_anomalies()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_off_topic_response_scores_low()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_pii_fragment_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_repeated_query_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_sequential_extraction_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_session_blocking()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_session_cleanup()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_session_reset()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_session_stats()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_system_info_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_threshold_warnings()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_tool_name_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_unsolicited_tool_call_flagged()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-track_message()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-tracker()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[A single disclosure event in a session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Add a callback function for alerts.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Add a disclosure event to the session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Alert severity levels.]] - rationale - gateway/security/multi_turn_tracker.py
- [[AlertLevel]] - code - gateway/security/multi_turn_tracker.py
- [[Analyze agent response for potential information leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze user message for disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Any_41]] - code - gateway/security/multi_turn_tracker.py
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
- [[Test alert callback functionality.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test analysis of agent responses for potential leaks.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test basic message tracking functionality.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test behavior of blocked sessions.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test cases for MultiTurnTracker class.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test cleanup of old sessions.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of PII fragment patterns.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of credential-related queries.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of file reference patterns.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of infrastructure-related queries.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of repeated queries with different phrasing.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of sequential extraction patterns.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of system information queries.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of tool inventory queries.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test edge cases and error conditions.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test getting session statistics.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test proper initialization of MultiTurnTracker.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test session reset functionality.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test that disabled tracker doesn't track or score.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test that scores accumulate across turns.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test that sessions get blocked at high scores.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test threshold-based warning system.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[TestMultiTurnTracker]] - code - gateway/tests/test_multi_turn_tracker.py
- [[TestResponseConsistency]] - code - gateway/tests/test_multi_turn_tracker.py
- [[ThresholdConfig]] - code - gateway/security/multi_turn_tracker.py
- [[Track a message and response pair for disclosure analysis.          Args]] - rationale - gateway/security/multi_turn_tracker.py
- [[Trigger alert callbacks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[callable_1]] - code - gateway/security/multi_turn_tracker.py
- [[mock_alert_callback()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[multi_turn_tracker()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[multi_turn_tracker.py]] - code - gateway/security/multi_turn_tracker.py
- [[test_multi_turn_tracker.py]] - code - gateway/tests/test_multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MultiTurnTracker
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_MiddlewareManager]]
- 5 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY_SecurityPipeline (2)]]
- 1 edge to [[_COMMUNITY__t]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_DelegationManager]]

## Top bridge nodes
- [[multi_turn_tracker.py]] - degree 11, connects to 3 communities
- [[MultiTurnTracker]] - degree 42, connects to 1 community
- [[TestMultiTurnTracker]] - degree 27, connects to 1 community
- [[SessionContext_1]] - degree 10, connects to 1 community
- [[AlertLevel]] - degree 8, connects to 1 community
