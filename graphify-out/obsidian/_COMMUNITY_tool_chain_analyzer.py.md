---
type: community
cohesion: 0.13
members: 23
---

# tool_chain_analyzer.py

**Cohesion:** 0.13 - loosely connected
**Members:** 23 nodes

## Members
- [[dot-_calculate_risk_score()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_cleanup_old_sessions()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_detect_chain_patterns()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_matches_source_pattern()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_trigger_alert()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-add_pattern()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-analyze_tool_call()]] - code - gateway/security/tool_chain_analyzer.py
- [[A detected suspicious chain.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Add a new chain pattern at runtime.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Analyze a tool call for suspicious chain patterns.          Args             se]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Calculate risk score for a detected chain.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ChainMatch]] - code - gateway/security/tool_chain_analyzer.py
- [[ChainPattern]] - code - gateway/security/tool_chain_analyzer.py
- [[Check if a call matches the source pattern, including parameter analysis.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Definition of a suspicious tool call pattern.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Detect if current call completes a suspicious pattern.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Remove old sessions to prevent memory bloat._1]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Represents a single tool call.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[SessionChainContext]] - code - gateway/security/tool_chain_analyzer.py
- [[Tool call chain context for a session.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ToolCall]] - code - gateway/security/tool_chain_analyzer.py
- [[Trigger alert callbacks for a detected chain.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[tool_chain_analyzer.py]] - code - gateway/security/tool_chain_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/tool_chain_analyzerpy
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_ToolChainAnalyzer]]
- 7 edges to [[_COMMUNITY_test_tool_chain_analyzer.py]]
- 1 edge to [[_COMMUNITY_TestParamSanitization]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[tool_chain_analyzer.py]] - degree 11, connects to 4 communities
- [[ChainMatch]] - degree 10, connects to 3 communities
- [[dot-analyze_tool_call()]] - degree 9, connects to 1 community
- [[dot-_detect_chain_patterns()]] - degree 8, connects to 1 community
- [[ChainPattern]] - degree 7, connects to 1 community
