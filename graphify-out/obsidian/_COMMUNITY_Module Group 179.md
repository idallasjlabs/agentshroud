---
type: community
cohesion: 0.12
members: 27
---

# Module Group 179

**Cohesion:** 0.12 - loosely connected
**Members:** 27 nodes

## Members
- [[.analyzer()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.analyzer()_2]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_delete_file_mostly_irreversible()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_legitimate_file_path_passes()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_read_file_fully_reversible()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_reversibility_below_threshold_has_reasoning()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_shell_bleed_bypass_blocked()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_unknown_tool_defaults_low()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[A detected suspicious chain.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Actions to take on suspicious chains.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ChainAction]] - code - gateway/security/tool_chain_analyzer.py
- [[ChainMatch]] - code - gateway/security/tool_chain_analyzer.py
- [[Create a mock alert callback for testing._1]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[How reversible an action is (1.0 = fully reversible, 0.0 = irreversible).]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ParamScanResult]] - code - gateway/security/tool_chain_analyzer.py
- [[Result of scanning tool parameters for injection patterns.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ReversibilityScore]] - code - gateway/security/tool_chain_analyzer.py
- [[Risk levels for tool call chains.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[RiskLevel_1]] - code - gateway/security/tool_chain_analyzer.py
- [[SessionChainContext]] - code - gateway/security/tool_chain_analyzer.py
- [[TestReversibilityScoring]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[TestShellBleedPatterns]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[Tool call chain context for a session.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Verify expanded _PARAM_INJECTION_PATTERNS catch piped-interpreter and     heredo]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[mock_alert_callback()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[test_tool_chain_analyzer.py]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[tool_chain_analyzer.py]] - code - gateway/security/tool_chain_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_179
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Module Group 162]]
- 7 edges to [[_COMMUNITY_Module Group 447]]
- 7 edges to [[_COMMUNITY_Module Group 119]]
- 6 edges to [[_COMMUNITY_Module Group 382]]
- 6 edges to [[_COMMUNITY_Module Group 438]]
- 5 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]

## Top bridge nodes
- [[test_tool_chain_analyzer.py]] - degree 15, connects to 5 communities
- [[tool_chain_analyzer.py]] - degree 10, connects to 4 communities
- [[ChainAction]] - degree 10, connects to 4 communities
- [[ChainMatch]] - degree 10, connects to 4 communities
- [[RiskLevel_1]] - degree 10, connects to 4 communities
