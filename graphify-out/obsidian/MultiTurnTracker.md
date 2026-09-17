---
source_file: "gateway/security/multi_turn_tracker.py"
type: "code"
community: "Alert Dispatcher & RBAC Reliability"
location: "L86"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Alert_Dispatcher__RBAC_Reliability
---

# MultiTurnTracker

## Connections
- [[dot-__init__()_12]] - `calls` [EXTRACTED]
- [[dot-__init__()_130]] - `method` [EXTRACTED]
- [[dot-_add_disclosure_event()]] - `method` [EXTRACTED]
- [[dot-_analyze_agent_response()]] - `method` [EXTRACTED]
- [[dot-_analyze_user_message()]] - `method` [EXTRACTED]
- [[dot-_check_thresholds()]] - `method` [EXTRACTED]
- [[dot-_cleanup_old_sessions()]] - `method` [EXTRACTED]
- [[dot-_compile_detection_patterns()]] - `method` [EXTRACTED]
- [[dot-_normalize_query()]] - `method` [EXTRACTED]
- [[dot-_score_message_patterns()]] - `method` [EXTRACTED]
- [[dot-_score_response_patterns()]] - `method` [EXTRACTED]
- [[dot-_trigger_alert()]] - `method` [EXTRACTED]
- [[dot-add_alert_callback()]] - `method` [EXTRACTED]
- [[dot-get_global_stats()]] - `method` [EXTRACTED]
- [[dot-get_session_stats()]] - `method` [EXTRACTED]
- [[dot-reset_session()]] - `method` [EXTRACTED]
- [[dot-score_response_consistency()]] - `method` [EXTRACTED]
- [[dot-test_disabled_tracker()]] - `calls` [EXTRACTED]
- [[dot-test_multi_turn_tracker_instantiates()]] - `calls` [EXTRACTED]
- [[dot-track_message()]] - `method` [EXTRACTED]
- [[dot-tracker()]] - `calls` [EXTRACTED]
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

#graphify/code #graphify/EXTRACTED #community/Alert_Dispatcher__RBAC_Reliability