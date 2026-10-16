---
type: community
cohesion: 0.05
members: 38
---

# TestToolChainAnalyzer

**Cohesion:** 0.05 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-test_alert_callbacks()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_approval_system()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_basic_tool_call_tracking()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_chain_length_limits()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_config_file_to_outbound()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_credential_to_outbound_blocking()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_edge_cases()_2]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_exec_to_network_pattern()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_initialization()_3]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_normal_tool_sequences_allowed()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_pattern_configuration()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_rapid_file_enumeration()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_read_to_http_exfiltration()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_read_to_message_exfiltration()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_risk_score_calculation()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_session_cleanup()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_session_stats()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_time_window_expiry()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[Test alert callback functionality._1]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test approval system interface.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test basic tool call tracking functionality.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test cases for ToolChainAnalyzer class.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test cleanup of old sessions._1]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test detection of config file access → outbound pattern.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test detection of exec → network communication pattern.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test detection of rapid file enumeration.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test detection of read → HTTP exfiltration pattern.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test detection of read → message exfiltration pattern.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test edge cases and error conditions._1]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test getting session statistics._1]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test proper initialization of ToolChainAnalyzer.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test risk score calculation for detected chains.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that chain length limits are respected.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that credential access → outbound tools are blocked.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that normal tool sequences pass through.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that patterns are properly configured.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that patterns don't match outside time windows.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[TestToolChainAnalyzer_1]] - code - gateway/tests/test_tool_chain_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestToolChainAnalyzer
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_TestParamSanitization]]
- 3 edges to [[_COMMUNITY_ToolChainAnalyzer]]
- 1 edge to [[_COMMUNITY_Test getting statistics.]]
- 1 edge to [[_COMMUNITY_tool_chain_analyzer.py]]

## Top bridge nodes
- [[TestToolChainAnalyzer_1]] - degree 29, connects to 4 communities
