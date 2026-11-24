---
type: community
members: 18
---

# .analyze_tool_call

**Members:** 18 nodes

## Members
- [[dot-_calculate_risk_score()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_cleanup_old_sessions()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_detect_chain_patterns()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_matches_source_pattern()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_trigger_alert()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-analyze_tool_call()]] - code - gateway/security/tool_chain_analyzer.py
- [[Analyze a tool call for suspicious chain patterns. Args session_id Session…]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Calculate risk score for a detected chain.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ChainPattern]] - code - gateway/security/tool_chain_analyzer.py
- [[Check if a call matches the source pattern, including parameter analysis.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Definition of a suspicious tool call pattern.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Detect if current call completes a suspicious pattern.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Remove old sessions to prevent memory bloat.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Represents a single tool call.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[SessionChainContext]] - code - gateway/security/tool_chain_analyzer.py
- [[Tool call chain context for a session.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ToolCall]] - code - gateway/security/tool_chain_analyzer.py
- [[Trigger alert callbacks for a detected chain.]] - rationale - gateway/security/tool_chain_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/analyze_tool_call
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_tool_chain_analyzer.py]]
- 6 edges to [[_COMMUNITY_ToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_Any_2]]

## Top bridge nodes
- [[dot-analyze_tool_call()]] - degree 9, connects to 3 communities
- [[dot-_detect_chain_patterns()]] - degree 8, connects to 2 communities
- [[ChainPattern]] - degree 6, connects to 2 communities
- [[dot-_trigger_alert()]] - degree 4, connects to 2 communities
- [[ToolCall]] - degree 6, connects to 1 community
