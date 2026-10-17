---
source_file: "gateway/security/tool_chain_analyzer.py"
type: "code"
community: "AlertDispatcher"
location: "L176"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AlertDispatcher
---

# ToolChainAnalyzer

## Connections
- [[dot-__init__()_10]] - `calls` [EXTRACTED]
- [[dot-__init__()_111]] - `method` [EXTRACTED]
- [[dot-_calculate_risk_score()]] - `method` [EXTRACTED]
- [[dot-_cleanup_old_sessions()]] - `method` [EXTRACTED]
- [[dot-_detect_chain_patterns()]] - `method` [EXTRACTED]
- [[dot-_load_custom_patterns()]] - `method` [EXTRACTED]
- [[dot-_load_default_patterns()]] - `method` [EXTRACTED]
- [[dot-_matches_source_pattern()]] - `method` [EXTRACTED]
- [[dot-_trigger_alert()]] - `method` [EXTRACTED]
- [[dot-add_alert_callback()_2]] - `method` [EXTRACTED]
- [[dot-add_pattern()]] - `method` [EXTRACTED]
- [[dot-analyze_tool_call()]] - `method` [EXTRACTED]
- [[dot-analyzer()]] - `calls` [EXTRACTED]
- [[dot-analyzer()_1]] - `calls` [EXTRACTED]
- [[dot-analyzer()_2]] - `calls` [EXTRACTED]
- [[dot-approve_pending_call()]] - `method` [EXTRACTED]
- [[dot-get_global_stats()]] - `method` [EXTRACTED]
- [[dot-get_session_stats()]] - `method` [EXTRACTED]
- [[dot-sanitize_tool_params()]] - `method` [EXTRACTED]
- [[dot-score_reversibility()]] - `method` [EXTRACTED]
- [[dot-test_custom_patterns()_1]] - `calls` [EXTRACTED]
- [[dot-test_disabled_analyzer()]] - `calls` [EXTRACTED]
- [[dot-test_tool_chain_analyzer_instantiates()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any]] - `uses` [INFERRED]
- [[CorrelationSummary]] - `semantically_similar_to` [INFERRED]
- [[Exception]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[Main tool chain analysis engine.      Tracks sequences of tool calls and identif]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestGetModuleModeEnforceDefault]] - `uses` [INFERRED]
- [[TestModuleConfigDefaults]] - `uses` [INFERRED]
- [[TestModuleInstantiationInEnforceMode]] - `uses` [INFERRED]
- [[TestParamSanitization]] - `uses` [INFERRED]
- [[TestReversibilityScoring]] - `uses` [INFERRED]
- [[TestSecurityConfigDefaults]] - `uses` [INFERRED]
- [[TestShellBleedPatterns]] - `uses` [INFERRED]
- [[TestToolChainAnalyzer]] - `uses` [INFERRED]
- [[ToolChainAnalyzer._load_custom_patterns]] - `calls` [EXTRACTED]
- [[ToolChainAnalyzer._load_default_patterns]] - `calls` [EXTRACTED]
- [[ToolTier]] - `uses` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `imports` [EXTRACTED]
- [[test_tool_chain_analyzer.py]] - `imports` [EXTRACTED]
- [[tool_chain_analyzer()]] - `calls` [EXTRACTED]
- [[tool_chain_analyzer.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AlertDispatcher
