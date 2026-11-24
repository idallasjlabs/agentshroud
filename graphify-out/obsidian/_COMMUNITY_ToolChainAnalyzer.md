---
type: community
members: 24
---

# ToolChainAnalyzer

**Members:** 24 nodes

## Members
- [[dot-add_alert_callback()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-analyzer()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-analyzer()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-analyzer()_2]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-approve_pending_call()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-test_custom_patterns()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_disabled_analyzer()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_legitimate_file_path_passes()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_shell_bleed_bypass_blocked()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[Add a callback function for chain detection alerts.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Approve a pending tool call that required approval. Args session_id Session…]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Create a ToolChainAnalyzer instance for testing.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Create a mock alert callback for testing._1]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Main tool chain analysis engine. Tracks sequences of tool calls and identifies…]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Test loading custom patterns from configuration.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that disabled analyzer allows all calls.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[TestShellBleedPatterns]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[ToolChainAnalyzer]] - code - gateway/security/tool_chain_analyzer.py
- [[Verify expanded _PARAM_INJECTION_PATTERNS catch piped-interpreter and heredoc…]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[callable]] - code
- [[fixture_128]] - code
- [[mock_alert_callback()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[parametrize_25]] - code
- [[tool_chain_analyzer()]] - code - gateway/tests/test_tool_chain_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ToolChainAnalyzer
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_tool_chain_analyzer.py]]
- 6 edges to [[_COMMUNITY_Any_2]]
- 6 edges to [[_COMMUNITY_dot-analyze_tool_call]]
- 3 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_TestParamSanitization]]
- 2 edges to [[_COMMUNITY_TestReversibilityScoring]]
- 2 edges to [[_COMMUNITY_PathIsolationManager]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[ToolChainAnalyzer]] - degree 34, connects to 10 communities
- [[TestShellBleedPatterns]] - degree 6, connects to 1 community
- [[tool_chain_analyzer()]] - degree 4, connects to 1 community
- [[mock_alert_callback()_1]] - degree 3, connects to 1 community
- [[dot-analyzer()]] - degree 3, connects to 1 community
