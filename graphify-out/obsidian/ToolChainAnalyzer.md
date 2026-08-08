---
source_file: "gateway/security/tool_chain_analyzer.py"
type: "code"
community: "Tool Chain Analyzer"
location: "L176"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Tool_Chain_Analyzer
---

# ToolChainAnalyzer

## Connections
- [[.__init__()_18]] - `calls` [EXTRACTED]
- [[.__init__()_118]] - `method` [EXTRACTED]
- [[._calculate_risk_score()]] - `method` [EXTRACTED]
- [[._cleanup_old_sessions()_1]] - `method` [EXTRACTED]
- [[._detect_chain_patterns()]] - `method` [EXTRACTED]
- [[._load_custom_patterns()]] - `method` [EXTRACTED]
- [[._load_default_patterns()]] - `method` [EXTRACTED]
- [[._matches_source_pattern()]] - `method` [EXTRACTED]
- [[._trigger_alert()_1]] - `method` [EXTRACTED]
- [[.add_alert_callback()_2]] - `method` [EXTRACTED]
- [[.add_pattern()]] - `method` [EXTRACTED]
- [[.analyze_tool_call()]] - `method` [EXTRACTED]
- [[.analyzer()]] - `calls` [EXTRACTED]
- [[.analyzer()_1]] - `calls` [EXTRACTED]
- [[.analyzer()_2]] - `calls` [EXTRACTED]
- [[.approve_pending_call()]] - `method` [EXTRACTED]
- [[.get_global_stats()_1]] - `method` [EXTRACTED]
- [[.get_session_stats()_1]] - `method` [EXTRACTED]
- [[.sanitize_tool_params()]] - `method` [EXTRACTED]
- [[.score_reversibility()]] - `method` [EXTRACTED]
- [[.test_custom_patterns()_1]] - `calls` [EXTRACTED]
- [[.test_disabled_analyzer()]] - `calls` [EXTRACTED]
- [[.test_tool_chain_analyzer_instantiates()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_10]] - `uses` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
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
- [[TestToolChainAnalyzer_1]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `imports` [EXTRACTED]
- [[test_tool_chain_analyzer.py]] - `imports` [EXTRACTED]
- [[tool_chain_analyzer()]] - `calls` [EXTRACTED]
- [[tool_chain_analyzer.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Tool_Chain_Analyzer