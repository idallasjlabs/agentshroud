---
type: community
cohesion: 0.32
members: 8
---

# Module Group 438

**Cohesion:** 0.32 - loosely connected
**Members:** 8 nodes

## Members
- [[._calculate_risk_score()]] - code - gateway/security/tool_chain_analyzer.py
- [[._detect_chain_patterns()]] - code - gateway/security/tool_chain_analyzer.py
- [[._matches_source_pattern()]] - code - gateway/security/tool_chain_analyzer.py
- [[Calculate risk score for a detected chain.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Check if a call matches the source pattern, including parameter analysis.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Detect if current call completes a suspicious pattern.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[Represents a single tool call.]] - rationale - gateway/security/tool_chain_analyzer.py
- [[ToolCall]] - code - gateway/security/tool_chain_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_438
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Module Group 179]]
- 5 edges to [[_COMMUNITY_Module Group 162]]
- 2 edges to [[_COMMUNITY_Module Group 382]]
- 1 edge to [[_COMMUNITY_Module Group 447]]
- 1 edge to [[_COMMUNITY_Module Group 119]]

## Top bridge nodes
- [[ToolCall]] - degree 11, connects to 4 communities
- [[._detect_chain_patterns()]] - degree 8, connects to 2 communities
- [[._calculate_risk_score()]] - degree 5, connects to 2 communities
- [[._matches_source_pattern()]] - degree 5, connects to 2 communities