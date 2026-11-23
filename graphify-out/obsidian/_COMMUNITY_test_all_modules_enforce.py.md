---
type: community
members: 80
---

# test_all_modules_enforce.py

**Members:** 80 nodes

## Members
- [[dot-__init__()_22]] - code - gateway/security/multi_turn_tracker.py
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
- [[dot-add_alert_callback()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-get_global_stats()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-get_session_stats()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-reset_session()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-score_response_consistency()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-test_consistent_response_scores_high()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_context_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_egress_filter_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_file_sandbox_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_git_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_language_mismatch_or_anomalies()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_multi_turn_tracker_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_off_topic_response_scores_low()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_path_isolation_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_prompt_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
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
- [[Any_9]] - code
- [[Batch F5 exit criterion verify ALL core security modules default to enforce…]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[Categories of information that contribute to disclosure scoring.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Check session score against thresholds and take action.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Compile regex patterns for detecting disclosure categories.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Compute a heuristic consistency score between query and response. Returns…]] - rationale - gateway/security/multi_turn_tracker.py
- [[Configuration for alert thresholds.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Configuration for path isolation system.]] - rationale - gateway/security/path_isolation.py
- [[ConsistencyScore]] - code - gateway/security/multi_turn_tracker.py
- [[Context tracking for a single session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Create a MultiTurnTracker instance for testing.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Create a mock alert callback for testing.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[DisclosureCategory]] - code - gateway/security/multi_turn_tracker.py
- [[DisclosureEvent]] - code - gateway/security/multi_turn_tracker.py
- [[Enum_13]] - code
- [[Get global tracking statistics.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Get statistics for a session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Heuristic consistency score between a query and its response.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Initialize the multi-turn tracker. Args config Configuration dictionary with…]] - rationale - gateway/security/multi_turn_tracker.py
- [[Main multi-turn disclosure tracking engine. Maintains session state and scores…]] - rationale - gateway/security/multi_turn_tracker.py
- [[Multi-Turn Context Tracker for AgentShroud Gateway Tracks cumulative…]] - rationale - gateway/security/multi_turn_tracker.py
- [[MultiTurnTracker]] - code - gateway/security/multi_turn_tracker.py
- [[Normalize query for repeated query detection.]] - rationale - gateway/security/multi_turn_tracker.py
- [[PathIsolationConfig]] - code - gateway/security/path_isolation.py
- [[Remove old sessions to prevent memory bloat.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Reset session score after owner review. Args session_id Session to reset…]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score agent response for potential leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score message based on disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[SessionContext]] - code - gateway/security/multi_turn_tracker.py
- [[TestModuleInstantiationInEnforceMode]] - code - gateway/tests/test_all_modules_enforce.py
- [[TestResponseConsistency]] - code - gateway/tests/test_multi_turn_tracker.py
- [[Tests for Multi-Turn Context Tracker module.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[ThresholdConfig]] - code - gateway/security/multi_turn_tracker.py
- [[Track a message and response pair for disclosure analysis. Args session_id…]] - rationale - gateway/security/multi_turn_tracker.py
- [[Trigger alert callbacks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Verify modules can instantiate and operate in enforce mode.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[callable]] - code
- [[fixture_18]] - code
- [[mock_alert_callback()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[multi_turn_tracker()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[multi_turn_tracker.py]] - code - gateway/security/multi_turn_tracker.py
- [[str_8]] - code
- [[test_all_modules_enforce.py]] - code - gateway/tests/test_all_modules_enforce.py
- [[test_multi_turn_tracker.py]] - code - gateway/tests/test_multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_all_modules_enforcepy
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_middleware.py]]
- 6 edges to [[_COMMUNITY_PathRewriteResult]]
- 5 edges to [[_COMMUNITY_TestMultiTurnTracker]]
- 5 edges to [[_COMMUNITY_SecurityConfig]]
- 4 edges to [[_COMMUNITY_PathIsolationManager]]
- 4 edges to [[_COMMUNITY_ToolChainAnalyzer]]
- 4 edges to [[_COMMUNITY_BrowserSecurityGuard]]
- 4 edges to [[_COMMUNITY_OutputCanary]]
- 4 edges to [[_COMMUNITY_ContextGuard]]
- 4 edges to [[_COMMUNITY_GitGuard]]
- 4 edges to [[_COMMUNITY_EgressFilter]]
- 3 edges to [[_COMMUNITY_PromptGuard]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_TestPathIsolationManager]]
- 2 edges to [[_COMMUNITY_DNSFilterConfig]]
- 2 edges to [[_COMMUNITY_EgressEvent]]
- 2 edges to [[_COMMUNITY_SubagentMonitor]]
- 2 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 2 edges to [[_COMMUNITY_KillSwitchConfig]]
- 1 edge to [[_COMMUNITY_TestModuleConfigDefaults]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_prompt_guard.py]]

## Top bridge nodes
- [[test_all_modules_enforce.py]] - degree 40, connects to 18 communities
- [[TestModuleInstantiationInEnforceMode]] - degree 24, connects to 9 communities
- [[PathIsolationConfig]] - degree 17, connects to 5 communities
- [[MultiTurnTracker]] - degree 31, connects to 3 communities
- [[multi_turn_tracker.py]] - degree 12, connects to 1 community
