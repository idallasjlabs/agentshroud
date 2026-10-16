---
type: community
cohesion: 0.02
members: 112
---

# TestToolChainAnalyzer

**Cohesion:** 0.02 - loosely connected
**Members:** 112 nodes

## Members
- [[dot-__init__()_129]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_calculate_risk_score()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_cleanup_old_sessions()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_detect_chain_patterns()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_load_custom_patterns()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_load_default_patterns()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_matches_source_pattern()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_trigger_alert()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-add_pattern()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-analyze_tool_call()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-analyzer()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-analyzer()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-analyzer()_2]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-get_global_stats()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-get_session_stats()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-sanitize_tool_params()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-score_reversibility()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-test_alert_callbacks()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_approval_system()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_basic_tool_call_tracking()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_chain_length_limits()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_clean_params_pass()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_config_file_to_outbound()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_credential_to_outbound_blocking()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_custom_patterns()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_delete_file_mostly_irreversible()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_disabled_analyzer()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_edge_cases()_2]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_exec_to_network_pattern()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_initialization()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_legitimate_file_path_passes()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_multiple_params_scanned()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_normal_tool_sequences_allowed()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_param_path_traversal_blocked()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_param_sql_injection_blocked()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_param_template_injection_blocked()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_pattern_configuration()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_rapid_file_enumeration()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_read_file_fully_reversible()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_read_to_http_exfiltration()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_read_to_message_exfiltration()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_reversibility_below_threshold_has_reasoning()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_risk_score_calculation()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_sanitization_returns_cleaned()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_session_cleanup()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_session_stats()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_shell_bleed_bypass_blocked()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_time_window_expiry()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_unknown_tool_defaults_low()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[A detected suspicious chain.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Actions to take on suspicious chains.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Add a new chain pattern at runtime.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Analyze a tool call for suspicious chain patterns.          Args             se]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Any_46]] - code - gateway/security/tool_chain_analyzer.py
- [[Calculate risk score for a detected chain.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ChainAction]] - code - gateway/security/tool_chain_analyzer.py
- [[ChainMatch]] - code - gateway/security/tool_chain_analyzer.py
- [[ChainPattern]] - code - gateway/security/tool_chain_analyzer.py
- [[Check if a call matches the source pattern, including parameter analysis.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Create a ToolChainAnalyzer instance for testing.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Create a mock alert callback for testing.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Definition of a suspicious tool call pattern.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Detect if current call completes a suspicious pattern.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Get global analyzer statistics.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Get statistics for a session.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[How reversible an action is (1.0 = fully reversible, 0.0 = irreversible).]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Initialize the tool chain analyzer.          Args             config Configura]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Load custom patterns from configuration.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Load default suspicious chain patterns.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ParamScanResult]] - code - gateway/security/tool_chain_analyzer.py
- [[Remove old sessions to prevent memory bloat.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Represents a single tool call.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Result of scanning tool parameters for injection patterns.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Return a reversibility score for the given tool call (1.0 = safe, 0.1 = irrevers]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ReversibilityScore]] - code - gateway/security/tool_chain_analyzer.py
- [[Risk levels for tool call chains.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[RiskLevel_6]] - code - gateway/security/tool_chain_analyzer.py
- [[Scan tool parameters for injection payloads and return sanitized copy.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[SessionChainContext]] - code - gateway/security/tool_chain_analyzer.py
- [[Test alert callback functionality.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test approval system interface.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test basic tool call tracking functionality.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test cases for ToolChainAnalyzer class.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test cleanup of old sessions.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test detection of config file access → outbound pattern.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test detection of exec → network communication pattern.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test detection of rapid file enumeration.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test detection of read → HTTP exfiltration pattern.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test detection of read → message exfiltration pattern.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test edge cases and error conditions._1]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test getting session statistics.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test loading custom patterns from configuration.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test proper initialization of ToolChainAnalyzer.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test risk score calculation for detected chains.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that chain length limits are respected.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that credential access → outbound tools are blocked.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that disabled analyzer allows all calls.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that normal tool sequences pass through.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that patterns are properly configured.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that patterns don't match outside time windows.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[TestParamSanitization]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[TestReversibilityScoring]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[TestShellBleedPatterns]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[TestToolChainAnalyzer_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[Tool call chain context for a session.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ToolCall]] - code - gateway/security/tool_chain_analyzer.py
- [[Trigger alert callbacks for a detected chain.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Verify expanded _PARAM_INJECTION_PATTERNS catch piped-interpreter and     heredo]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[mock_alert_callback()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[test_tool_chain_analyzer.py]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[tool_chain_analyzer()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[tool_chain_analyzer.py]] - code - gateway/security/tool_chain_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestToolChainAnalyzer
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_Action]]
- 2 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_Test getting statistics.]]

## Top bridge nodes
- [[tool_chain_analyzer.py]] - degree 12, connects to 3 communities
- [[TestToolChainAnalyzer_1]] - degree 29, connects to 2 communities
- [[ChainAction]] - degree 10, connects to 2 communities
- [[RiskLevel_6]] - degree 10, connects to 2 communities
- [[TestParamSanitization]] - degree 14, connects to 1 community
