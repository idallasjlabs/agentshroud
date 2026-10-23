---
type: community
cohesion: 0.08
members: 31
---

# ToolChainAnalyzer

**Cohesion:** 0.08 - loosely connected
**Members:** 31 nodes

## Members
- [[dot-__init__()_112]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_load_custom_patterns()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_load_default_patterns()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-add_alert_callback()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-approve_pending_call()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-get_global_stats()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-get_session_stats()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-sanitize_tool_params()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-score_reversibility()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-test_custom_patterns()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_disabled_analyzer()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_tool_chain_analyzer_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[Add a callback function for chain detection alerts.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Any_40]] - code - gateway/security/tool_chain_analyzer.py
- [[Approve a pending tool call that required approval.          Args             s]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Create a ToolChainAnalyzer instance for testing.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Get global analyzer statistics.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Get statistics for a session._1]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Initialize the tool chain analyzer.          Args             config Configura]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Load custom patterns from configuration.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Load default suspicious chain patterns.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Main tool chain analysis engine.      Tracks sequences of tool calls and identif]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Return a reversibility score for the given tool call (1.0 = safe, 0.1 = irrevers]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Scan tool parameters for injection payloads and return sanitized copy.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Test loading custom patterns from configuration.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that disabled analyzer allows all calls.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[ToolChainAnalyzer]] - code - gateway/security/tool_chain_analyzer.py
- [[ToolChainAnalyzer._load_custom_patterns]] - code - gateway/security/tool_chain_analyzer.py
- [[ToolChainAnalyzer._load_default_patterns]] - code - gateway/security/tool_chain_analyzer.py
- [[callable_1]] - code - gateway/security/tool_chain_analyzer.py
- [[tool_chain_analyzer()]] - code - gateway/tests/test_tool_chain_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ToolChainAnalyzer
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_tool_chain_analyzer.py]]
- 10 edges to [[_COMMUNITY_test_tool_chain_analyzer.py]]
- 9 edges to [[_COMMUNITY_Any]]
- 6 edges to [[_COMMUNITY_PathIsolationManager]]
- 3 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_TestParamSanitization]]
- 1 edge to [[_COMMUNITY_ResourceGuard (2)]]

## Top bridge nodes
- [[ToolChainAnalyzer]] - degree 49, connects to 8 communities
- [[dot-_load_custom_patterns()]] - degree 6, connects to 2 communities
- [[Any_40]] - degree 6, connects to 1 community
- [[dot-_load_default_patterns()]] - degree 4, connects to 1 community
- [[dot-sanitize_tool_params()]] - degree 4, connects to 1 community
