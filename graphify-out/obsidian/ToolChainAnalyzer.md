---
source_file: "gateway/security/tool_chain_analyzer.py"
type: "code"
community: "Alert Dispatcher & RBAC Reliability"
location: "L176"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Alert_Dispatcher__RBAC_Reliability
---

# ToolChainAnalyzer

## Connections
- [[dot-__init__()_12]] - `calls` [EXTRACTED]
- [[dot-__init__()_156]] - `method` [EXTRACTED]
- [[dot-_calculate_risk_score()]] - `method` [EXTRACTED]
- [[dot-_cleanup_old_sessions()_1]] - `method` [EXTRACTED]
- [[dot-_detect_chain_patterns()]] - `method` [EXTRACTED]
- [[dot-_load_custom_patterns()]] - `method` [EXTRACTED]
- [[dot-_load_default_patterns()]] - `method` [EXTRACTED]
- [[dot-_matches_source_pattern()]] - `method` [EXTRACTED]
- [[dot-_trigger_alert()_1]] - `method` [EXTRACTED]
- [[dot-add_alert_callback()_1]] - `method` [EXTRACTED]
- [[dot-add_pattern()]] - `method` [EXTRACTED]
- [[dot-analyze_tool_call()]] - `method` [EXTRACTED]
- [[dot-analyzer()]] - `calls` [EXTRACTED]
- [[dot-analyzer()_1]] - `calls` [EXTRACTED]
- [[dot-analyzer()_2]] - `calls` [EXTRACTED]
- [[dot-approve_pending_call()]] - `method` [EXTRACTED]
- [[dot-get_global_stats()_1]] - `method` [EXTRACTED]
- [[dot-get_session_stats()_1]] - `method` [EXTRACTED]
- [[dot-sanitize_tool_params()]] - `method` [EXTRACTED]
- [[dot-score_reversibility()]] - `method` [EXTRACTED]
- [[dot-test_custom_patterns()_1]] - `calls` [EXTRACTED]
- [[dot-test_disabled_analyzer()]] - `calls` [EXTRACTED]
- [[dot-test_tool_chain_analyzer_instantiates()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[CorrelationSummary]] - `semantically_similar_to` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[Main tool chain analysis engine.      Tracks sequences of tool calls and identif]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestGetModuleModeEnforceDefault]] - `uses` [INFERRED]
- [[TestModuleConfigDefaults]] - `uses` [INFERRED]
- [[TestModuleInstantiationInEnforceMode]] - `uses` [INFERRED]
- [[TestParamSanitization]] - `uses` [INFERRED]
- [[TestReversibilityScoring]] - `uses` [INFERRED]
- [[TestSecurityConfigDefaults]] - `uses` [INFERRED]
- [[TestShellBleedPatterns]] - `uses` [INFERRED]
- [[TestToolChainAnalyzer_1]] - `uses` [INFERRED]
- [[ToolChainAnalyzer._load_custom_patterns]] - `calls` [EXTRACTED]
- [[ToolChainAnalyzer._load_default_patterns]] - `calls` [EXTRACTED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `imports` [EXTRACTED]
- [[test_tool_chain_analyzer.py]] - `imports` [EXTRACTED]
- [[tool_chain_analyzer()]] - `calls` [EXTRACTED]
- [[tool_chain_analyzer.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Alert_Dispatcher__RBAC_Reliability