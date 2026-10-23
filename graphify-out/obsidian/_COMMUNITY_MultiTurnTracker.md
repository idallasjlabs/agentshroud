---
type: community
cohesion: 0.05
members: 55
---

# MultiTurnTracker

**Cohesion:** 0.05 - loosely connected
**Members:** 55 nodes

## Members
- [[dot-__init__()_35]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_add_disclosure_event()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_analyze_agent_response()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_analyze_user_message()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_check_thresholds()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_cleanup_old_sessions()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_compile_detection_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_detect_hidden_instructions()]] - code - gateway/security/context_guard.py
- [[dot-_detect_instruction_injection()]] - code - gateway/security/context_guard.py
- [[dot-_detect_rapid_context_growth()]] - code - gateway/security/context_guard.py
- [[dot-_detect_repetition_attacks()]] - code - gateway/security/context_guard.py
- [[dot-_normalize_query()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_score_message_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_score_response_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_trigger_alert()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-add_alert_callback()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-analyze_message()]] - code - gateway/security/context_guard.py
- [[dot-get_global_stats()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-get_session_stats()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-reset_session()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-should_block_message()]] - code - gateway/security/context_guard.py
- [[dot-track_message()]] - code - gateway/security/multi_turn_tracker.py
- [[Add a callback function for alerts.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Add a disclosure event to the session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze a message for context poisoning attempts.          Args             ses]] - rationale - gateway/security/context_guard.py
- [[Analyze agent response for potential information leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze user message for disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Any_10]] - code - gateway/security/multi_turn_tracker.py
- [[Check session score against thresholds and take action.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Compile regex patterns for detecting disclosure categories.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Configuration for alert thresholds.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Context tracking for a session.]] - rationale - gateway/security/context_guard.py
- [[ContextAttack]] - code - gateway/security/context_guard.py
- [[Detect hidden instructions buried in large text blocks.]] - rationale - gateway/security/context_guard.py
- [[Detect instruction injection attempts.]] - rationale - gateway/security/context_guard.py
- [[Detect rapid context window filling.]] - rationale - gateway/security/context_guard.py
- [[Detect repetition-based context stuffing attacks.]] - rationale - gateway/security/context_guard.py
- [[Detected context window attack attempt.]] - rationale - gateway/security/context_guard.py
- [[Determine if a message should be blocked.          Returns             Tuple of]] - rationale - gateway/security/context_guard.py
- [[Get global tracking statistics.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Get statistics for a session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Initialize the multi-turn tracker.          Args             config Configurat]] - rationale - gateway/security/multi_turn_tracker.py
- [[Main multi-turn disclosure tracking engine.      Maintains session state and sco]] - rationale - gateway/security/multi_turn_tracker.py
- [[MultiTurnTracker]] - code - gateway/security/multi_turn_tracker.py
- [[Normalize query for repeated query detection.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Remove old sessions to prevent memory bloat.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Reset session score after owner review.          Args             session_id S]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score agent response for potential leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score message based on disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[SessionContext]] - code - gateway/security/context_guard.py
- [[SessionContext_1]] - code - gateway/security/multi_turn_tracker.py
- [[ThresholdConfig]] - code - gateway/security/multi_turn_tracker.py
- [[Track a message and response pair for disclosure analysis.          Args]] - rationale - gateway/security/multi_turn_tracker.py
- [[Trigger alert callbacks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[callable]] - code - gateway/security/multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MultiTurnTracker
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_Enum]]
- 9 edges to [[_COMMUNITY_Any]]
- 6 edges to [[_COMMUNITY_ContextGuard]]
- 6 edges to [[_COMMUNITY_PathIsolationManager]]
- 3 edges to [[_COMMUNITY__t]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]

## Top bridge nodes
- [[MultiTurnTracker]] - degree 42, connects to 4 communities
- [[dot-analyze_message()]] - degree 12, connects to 4 communities
- [[SessionContext_1]] - degree 10, connects to 1 community
- [[dot-_add_disclosure_event()]] - degree 8, connects to 1 community
- [[ContextAttack]] - degree 7, connects to 1 community
