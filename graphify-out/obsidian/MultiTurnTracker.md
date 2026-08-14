---
source_file: "gateway/security/multi_turn_tracker.py"
type: "code"
community: "Egress & RBAC Security Core"
location: "L86"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress__RBAC_Security_Core
---

# MultiTurnTracker

## Connections
- [[.__init__()_13]] - `calls` [EXTRACTED]
- [[.__init__()_97]] - `method` [EXTRACTED]
- [[._add_disclosure_event()]] - `method` [EXTRACTED]
- [[._analyze_agent_response()]] - `method` [EXTRACTED]
- [[._analyze_user_message()]] - `method` [EXTRACTED]
- [[._check_thresholds()]] - `method` [EXTRACTED]
- [[._cleanup_old_sessions()]] - `method` [EXTRACTED]
- [[._compile_detection_patterns()]] - `method` [EXTRACTED]
- [[._normalize_query()]] - `method` [EXTRACTED]
- [[._score_message_patterns()]] - `method` [EXTRACTED]
- [[._score_response_patterns()]] - `method` [EXTRACTED]
- [[._trigger_alert()]] - `method` [EXTRACTED]
- [[.add_alert_callback()]] - `method` [EXTRACTED]
- [[.get_global_stats()]] - `method` [EXTRACTED]
- [[.get_session_stats()]] - `method` [EXTRACTED]
- [[.reset_session()_1]] - `method` [EXTRACTED]
- [[.score_response_consistency()]] - `method` [EXTRACTED]
- [[.test_disabled_tracker()]] - `calls` [EXTRACTED]
- [[.test_multi_turn_tracker_instantiates()]] - `calls` [EXTRACTED]
- [[.track_message()]] - `method` [EXTRACTED]
- [[.tracker()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_8]] - `uses` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[Main multi-turn disclosure tracking engine.      Maintains session state and sco]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestGetModuleModeEnforceDefault]] - `uses` [INFERRED]
- [[TestModuleConfigDefaults]] - `uses` [INFERRED]
- [[TestModuleInstantiationInEnforceMode]] - `uses` [INFERRED]
- [[TestMultiTurnTracker_1]] - `uses` [INFERRED]
- [[TestResponseConsistency]] - `uses` [INFERRED]
- [[TestSecurityConfigDefaults]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[multi_turn_tracker()]] - `calls` [EXTRACTED]
- [[multi_turn_tracker.py]] - `contains` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `imports` [EXTRACTED]
- [[test_multi_turn_tracker.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress__RBAC_Security_Core