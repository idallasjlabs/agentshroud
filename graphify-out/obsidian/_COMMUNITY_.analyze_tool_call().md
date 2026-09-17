---
type: community
cohesion: 0.08
members: 29
---

# .analyze_tool_call()

**Cohesion:** 0.08 - loosely connected
**Members:** 29 nodes

## Members
- [[.__init__()_156]] - code - gateway/security/tool_chain_analyzer.py
- [[._calculate_risk_score()]] - code - gateway/security/tool_chain_analyzer.py
- [[._cleanup_old_sessions()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[._detect_chain_patterns()]] - code - gateway/security/tool_chain_analyzer.py
- [[._load_default_patterns()]] - code - gateway/security/tool_chain_analyzer.py
- [[._matches_source_pattern()]] - code - gateway/security/tool_chain_analyzer.py
- [[._trigger_alert()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[.analyze_tool_call()]] - code - gateway/security/tool_chain_analyzer.py
- [[.get_global_stats()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[.get_session_stats()_1]] - code - gateway/security/tool_chain_analyzer.py
- [[.sanitize_tool_params()]] - code - gateway/security/tool_chain_analyzer.py
- [[.score_reversibility()]] - code - gateway/security/tool_chain_analyzer.py
- [[Analyze a tool call for suspicious chain patterns.          Args             se]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Any_58]] - code - gateway/security/tool_chain_analyzer.py
- [[Calculate risk score for a detected chain.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Check if a call matches the source pattern, including parameter analysis.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Detect if current call completes a suspicious pattern.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Get global analyzer statistics.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Get statistics for a session._1]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Initialize the tool chain analyzer.          Args             config Configura]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Load default suspicious chain patterns.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Remove old sessions to prevent memory bloat._1]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Represents a single tool call.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Return a reversibility score for the given tool call (1.0 = safe, 0.1 = irrevers]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Scan tool parameters for injection payloads and return sanitized copy.]] - rationale - gateway/security/tool_chain_analyzer.py
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
- 12 edges to [[_COMMUNITY_lifespan.py]]
- 11 edges to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[.analyze_tool_call()]] - degree 9, connects to 2 communities
- [[._detect_chain_patterns()]] - degree 8, connects to 2 communities
- [[._calculate_risk_score()]] - degree 5, connects to 2 communities
- [[.__init__()_156]] - degree 5, connects to 2 communities
- [[._matches_source_pattern()]] - degree 5, connects to 2 communities