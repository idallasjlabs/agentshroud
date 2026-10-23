---
type: community
cohesion: 0.25
members: 8
---

# TestParamSanitization

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-analyzer()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_clean_params_pass()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_multiple_params_scanned()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_param_path_traversal_blocked()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_param_sql_injection_blocked()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_param_template_injection_blocked()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_sanitization_returns_cleaned()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[TestParamSanitization]] - code - gateway/tests/test_tool_chain_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestParamSanitization
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_tool_chain_analyzer.py]]
- 2 edges to [[_COMMUNITY_ToolChainAnalyzer]]
- 1 edge to [[_COMMUNITY_tool_chain_analyzer.py]]

## Top bridge nodes
- [[TestParamSanitization]] - degree 14, connects to 3 communities
- [[dot-analyzer()]] - degree 2, connects to 1 community
