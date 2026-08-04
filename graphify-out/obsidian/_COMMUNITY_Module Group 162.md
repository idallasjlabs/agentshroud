---
type: community
cohesion: 0.08
members: 29
---

# Module Group 162

**Cohesion:** 0.08 - loosely connected
**Members:** 29 nodes

## Members
- [[._cleanup_old_sessions()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[._trigger_alert()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[.add_alert_callback()_2]] - code - gateway/security/tool_chain_analyzer.py
- [[.analyze_tool_call()]] - code - gateway/security/tool_chain_analyzer.py
- [[.approve_pending_call()]] - code - gateway/security/tool_chain_analyzer.py
- [[.get_global_stats()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[.get_session_stats()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[.sanitize_tool_params()]] - code - gateway/security/tool_chain_analyzer.py
- [[.score_reversibility()]] - code - gateway/security/tool_chain_analyzer.py
- [[.test_custom_patterns()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_disabled_analyzer()]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_tool_chain_analyzer_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[Add a callback function for chain detection alerts.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Analyze a tool call for suspicious chain patterns.          Args             se]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Any_55]] - code - gateway/security/tool_chain_analyzer.py
- [[Approve a pending tool call that required approval.          Args             s]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Create a ToolChainAnalyzer instance for testing.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Get global analyzer statistics.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Get statistics for a session._1]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Main tool chain analysis engine.      Tracks sequences of tool calls and identif]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Remove old sessions to prevent memory bloat._1]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Return a reversibility score for the given tool call (1.0 = safe, 0.1 = irrevers]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Scan tool parameters for injection payloads and return sanitized copy.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Test loading custom patterns from configuration.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test that disabled analyzer allows all calls.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[ToolChainAnalyzer]] - code - gateway/security/tool_chain_analyzer.py
- [[Trigger alert callbacks for a detected chain.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[callable_2]] - code - gateway/security/tool_chain_analyzer.py
- [[tool_chain_analyzer()]] - code - gateway/tests/test_tool_chain_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_162
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 12 edges to [[_COMMUNITY_Module Group 179]]
- 5 edges to [[_COMMUNITY_Module Group 438]]
- 5 edges to [[_COMMUNITY_Module Group 382]]
- 3 edges to [[_COMMUNITY_Module Group 119]]
- 2 edges to [[_COMMUNITY_Module Group 447]]

## Top bridge nodes
- [[ToolChainAnalyzer]] - degree 45, connects to 6 communities
- [[.analyze_tool_call()]] - degree 9, connects to 2 communities
- [[Any_55]] - degree 6, connects to 1 community
- [[.sanitize_tool_params()]] - degree 4, connects to 1 community
- [[.score_reversibility()]] - degree 4, connects to 1 community
