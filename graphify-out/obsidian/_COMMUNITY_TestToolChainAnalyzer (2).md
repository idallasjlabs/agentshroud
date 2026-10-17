---
type: community
members: 29
---

# TestToolChainAnalyzer (2)

**Members:** 29 nodes

## Members
- [[dot-__init__()_111]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_calculate_risk_score()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_cleanup_old_sessions()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_detect_chain_patterns()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_load_default_patterns()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_matches_source_pattern()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-_trigger_alert()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-analyze_tool_call()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-get_global_stats()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-get_session_stats()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-sanitize_tool_params()]] - code - gateway/security/tool_chain_analyzer.py
- [[dot-score_reversibility()]] - code - gateway/security/tool_chain_analyzer.py
- [[Analyze a tool call for suspicious chain patterns.          Args             se]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Any_40]] - code - gateway/security/tool_chain_analyzer.py
- [[Calculate risk score for a detected chain.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Check if a call matches the source pattern, including parameter analysis.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Detect if current call completes a suspicious pattern.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Get global analyzer statistics.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Get statistics for a session.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Initialize the tool chain analyzer.          Args             config Configura]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Load default suspicious chain patterns.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Remove old sessions to prevent memory bloat.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Represents a single tool call.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Return a reversibility score for the given tool call (1.0 = safe, 0.1 = irrevers]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Scan tool parameters for injection payloads and return sanitized copy.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[SessionChainContext]] - code - gateway/security/tool_chain_analyzer.py
- [[Tool call chain context for a session.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ToolCall]] - code - gateway/security/tool_chain_analyzer.py
- [[Trigger alert callbacks for a detected chain.]] - rationale - gateway/security/tool_chain_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestToolChainAnalyzer_2
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_AlertDispatcher]]
- 11 edges to [[_COMMUNITY_TestToolChainAnalyzer]]

## Top bridge nodes
- [[dot-analyze_tool_call()]] - degree 9, connects to 2 communities
- [[dot-_detect_chain_patterns()]] - degree 8, connects to 2 communities
- [[dot-_calculate_risk_score()]] - degree 5, connects to 2 communities
- [[dot-__init__()_111]] - degree 5, connects to 2 communities
- [[dot-_matches_source_pattern()]] - degree 5, connects to 2 communities
