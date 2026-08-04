---
type: community
cohesion: 0.04
members: 68
---

# URL Analyzer & Content Scanner

**Cohesion:** 0.04 - loosely connected
**Members:** 68 nodes

## Members
- [[._add_disclosure_event()]] - code - gateway/security/multi_turn_tracker.py
- [[._analyze_agent_response()]] - code - gateway/security/multi_turn_tracker.py
- [[._analyze_user_message()]] - code - gateway/security/multi_turn_tracker.py
- [[._check_thresholds()]] - code - gateway/security/multi_turn_tracker.py
- [[._cleanup_old_sessions()]] - code - gateway/security/multi_turn_tracker.py
- [[._normalize_query()]] - code - gateway/security/multi_turn_tracker.py
- [[._score_message_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[._score_response_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[._trigger_alert()]] - code - gateway/security/multi_turn_tracker.py
- [[.score_response_consistency()]] - code - gateway/security/multi_turn_tracker.py
- [[.test_approved_status()]] - code - gateway/tests/test_soc_egress.py
- [[.test_consistent_response_scores_high()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_construction()]] - code - gateway/tests/test_soc_models.py
- [[.test_destructive_requires_confirmation()]] - code - gateway/tests/test_soc_egress.py
- [[.test_language_mismatch_or_anomalies()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_off_topic_response_scores_low()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_pending_status_default()]] - code - gateway/tests/test_soc_egress.py
- [[.test_permission_denied_error()]] - code - gateway/tests/test_soc_egress.py
- [[.test_red_risk_high_threat()]] - code - gateway/tests/test_soc_egress.py
- [[.test_unsolicited_tool_call_flagged()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.track_message()]] - code - gateway/security/multi_turn_tracker.py
- [[.tracker()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[A single disclosure event in a session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Add a disclosure event to the session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[AlarmStatus]] - code - gateway/soc/models.py
- [[Alert severity levels.]] - rationale - gateway/security/multi_turn_tracker.py
- [[AlertLevel]] - code - gateway/security/multi_turn_tracker.py
- [[Analyze agent response for potential information leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze user message for disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Categories of information that contribute to disclosure scoring.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Check session score against thresholds and take action.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Compute a heuristic consistency score between query and response.          Retur]] - rationale - gateway/security/multi_turn_tracker.py
- [[Configuration for alert thresholds.]] - rationale - gateway/security/multi_turn_tracker.py
- [[ConsistencyScore]] - code - gateway/security/multi_turn_tracker.py
- [[Context tracking for a single session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Create a MultiTurnTracker instance for testing.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Create a mock alert callback for testing.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[DisclosureCategory]] - code - gateway/security/multi_turn_tracker.py
- [[DisclosureEvent]] - code - gateway/security/multi_turn_tracker.py
- [[EgressRequest_1]] - code - gateway/soc/models.py
- [[EgressStatus]] - code - gateway/soc/models.py
- [[Enum]] - code
- [[FindingSeverity]] - code - gateway/proxy/web_content_scanner.py
- [[Heuristic consistency score between a query and its response.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Normalize query for repeated query detection.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Remove old sessions to prevent memory bloat.]] - rationale - gateway/security/multi_turn_tracker.py
- [[RiskLevel_2]] - code - gateway/soc/models.py
- [[Score agent response for potential leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score message based on disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[SessionContext_1]] - code - gateway/security/multi_turn_tracker.py
- [[TestConfirmationModel]] - code - gateway/tests/test_soc_egress.py
- [[TestEgressRequest]] - code - gateway/tests/test_soc_models.py
- [[TestEgressRequestModel]] - code - gateway/tests/test_soc_egress.py
- [[TestResponseConsistency]] - code - gateway/tests/test_multi_turn_tracker.py
- [[Threat levels for detected issues.]] - rationale - gateway/security/git_guard.py
- [[ThreatLevel_2]] - code - gateway/security/git_guard.py
- [[ThresholdConfig]] - code - gateway/security/multi_turn_tracker.py
- [[Track a message and response pair for disclosure analysis.          Args]] - rationale - gateway/security/multi_turn_tracker.py
- [[Trigger alert callbacks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[URLVerdict]] - code - gateway/proxy/url_analyzer.py
- [[mock_alert_callback()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[multi_turn_tracker()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[multi_turn_tracker.py]] - code - gateway/security/multi_turn_tracker.py
- [[str]] - code
- [[test_multi_turn_tracker.py]] - code - gateway/tests/test_multi_turn_tracker.py
- [[test_soc_egress.py]] - code - gateway/tests/test_soc_egress.py
- [[url_analyzer.py]] - code - gateway/proxy/url_analyzer.py
- [[web_content_scanner.py]] - code - gateway/proxy/web_content_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/URL_Analyzer__Content_Scanner
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 17 edges to [[_COMMUNITY_SOC Services & Health Status]]
- 13 edges to [[_COMMUNITY_Module Group 83]]
- 10 edges to [[_COMMUNITY_RBAC Configuration]]
- 10 edges to [[_COMMUNITY_Module Group 62]]
- 5 edges to [[_COMMUNITY_Module Group 179]]
- 5 edges to [[_COMMUNITY_Module Group 76]]
- 5 edges to [[_COMMUNITY_Module Group 90]]
- 4 edges to [[_COMMUNITY_MCP Inspector & Audit]]
- 4 edges to [[_COMMUNITY_Module Group 79]]
- 4 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 3 edges to [[_COMMUNITY_Module Group 190]]
- 3 edges to [[_COMMUNITY_Privacy Policy]]
- 3 edges to [[_COMMUNITY_Progressive Lockdown]]
- 3 edges to [[_COMMUNITY_Subagent Monitor]]
- 3 edges to [[_COMMUNITY_Module Group 77]]
- 3 edges to [[_COMMUNITY_Module Group 199]]
- 2 edges to [[_COMMUNITY_MCP Config & Proxy]]
- 2 edges to [[_COMMUNITY_Module Group 154]]
- 2 edges to [[_COMMUNITY_Pipeline Action & Instruction Envelope]]
- 2 edges to [[_COMMUNITY_HTTP CONNECT Proxy & Egress]]
- 2 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_Module Group 95]]
- 2 edges to [[_COMMUNITY_Module Group 200]]
- 2 edges to [[_COMMUNITY_Module Group 80]]
- 2 edges to [[_COMMUNITY_Module Group 93]]
- 2 edges to [[_COMMUNITY_Module Group 143]]
- 2 edges to [[_COMMUNITY_Module Group 142]]
- 2 edges to [[_COMMUNITY_Module Group 282]]
- 1 edge to [[_COMMUNITY_Agent Isolation & Container Config]]
- 1 edge to [[_COMMUNITY_Module Group 113]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Egress Filter & Approval]]
- 1 edge to [[_COMMUNITY_Module Group 240]]
- 1 edge to [[_COMMUNITY_Module Group 218]]
- 1 edge to [[_COMMUNITY_Module Group 396]]

## Top bridge nodes
- [[Enum]] - degree 81, connects to 32 communities
- [[str]] - degree 36, connects to 16 communities
- [[URLVerdict]] - degree 10, connects to 2 communities
- [[test_multi_turn_tracker.py]] - degree 9, connects to 2 communities
- [[EgressRequest_1]] - degree 8, connects to 2 communities
