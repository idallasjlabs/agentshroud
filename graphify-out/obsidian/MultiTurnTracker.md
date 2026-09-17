---
source_file: "gateway/security/multi_turn_tracker.py"
type: "code"
community: "lifespan.py"
location: "L86"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/lifespanpy
---

# MultiTurnTracker

## Connections
- [[.__init__()_12]] - `calls` [EXTRACTED]
- [[.__init__()_130]] - `method` [EXTRACTED]
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
- [[.reset_session()]] - `method` [EXTRACTED]
- [[.score_response_consistency()]] - `method` [EXTRACTED]
- [[.test_disabled_tracker()]] - `calls` [EXTRACTED]
- [[.test_multi_turn_tracker_instantiates()]] - `calls` [EXTRACTED]
- [[.track_message()]] - `method` [EXTRACTED]
- [[.tracker()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[Main multi-turn disclosure tracking engine.      Maintains session state and sco]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestGetModuleModeEnforceDefault]] - `uses` [INFERRED]
- [[TestModuleConfigDefaults]] - `uses` [INFERRED]
- [[TestModuleInstantiationInEnforceMode]] - `uses` [INFERRED]
- [[TestMultiTurnTracker]] - `uses` [INFERRED]
- [[TestResponseConsistency]] - `uses` [INFERRED]
- [[TestSecurityConfigDefaults]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[multi_turn_tracker()]] - `calls` [EXTRACTED]
- [[multi_turn_tracker.py]] - `contains` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `imports` [EXTRACTED]
- [[test_multi_turn_tracker.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/lifespanpy