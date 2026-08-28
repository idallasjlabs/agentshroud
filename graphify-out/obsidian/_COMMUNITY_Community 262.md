---
type: community
cohesion: 0.09
members: 30
---

# Community 262

**Cohesion:** 0.09 - loosely connected
**Members:** 30 nodes

## Members
- [[.analyzer()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.analyzer()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.analyzer()_2]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_clean_params_pass()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_delete_file_mostly_irreversible()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_legitimate_file_path_passes()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_multiple_params_scanned()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_param_path_traversal_blocked()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_param_sql_injection_blocked()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_param_template_injection_blocked()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_read_file_fully_reversible()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_reversibility_below_threshold_has_reasoning()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_sanitization_returns_cleaned()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_shell_bleed_bypass_blocked()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_unknown_tool_defaults_low()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[Actions to take on suspicious chains.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ChainAction]] - code - gateway/security/tool_chain_analyzer.py
- [[Create a mock alert callback for testing._1]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[How reversible an action is (1.0 = fully reversible, 0.0 = irreversible).]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ParamScanResult]] - code - gateway/security/tool_chain_analyzer.py
- [[Result of scanning tool parameters for injection patterns.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ReversibilityScore]] - code - gateway/security/tool_chain_analyzer.py
- [[Risk levels for tool call chains.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[RiskLevel_4]] - code - gateway/security/tool_chain_analyzer.py
- [[TestParamSanitization]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[TestReversibilityScoring]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[TestShellBleedPatterns]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[Verify expanded _PARAM_INJECTION_PATTERNS catch piped-interpreter and     heredo]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[mock_alert_callback()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[test_tool_chain_analyzer.py]] - code - gateway/tests/test_tool_chain_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_262
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Community 223]]
- 8 edges to [[_COMMUNITY_Community 431]]
- 5 edges to [[_COMMUNITY_Community 169]]
- 4 edges to [[_COMMUNITY_Community 19]]

## Top bridge nodes
- [[ChainAction]] - degree 10, connects to 4 communities
- [[RiskLevel_4]] - degree 10, connects to 4 communities
- [[test_tool_chain_analyzer.py]] - degree 12, connects to 3 communities
- [[ParamScanResult]] - degree 8, connects to 3 communities
- [[ReversibilityScore]] - degree 8, connects to 3 communities