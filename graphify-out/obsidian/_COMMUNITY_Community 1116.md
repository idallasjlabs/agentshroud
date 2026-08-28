---
type: community
cohesion: 0.33
members: 6
---

# Community 1116

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[ToolChainAnalyzer._calculate_risk_score]] - code - gateway/security/tool_chain_analyzer.py
- [[ToolChainAnalyzer._cleanup_old_sessions]] - code - gateway/security/tool_chain_analyzer.py
- [[ToolChainAnalyzer._detect_chain_patterns]] - code - gateway/security/tool_chain_analyzer.py
- [[ToolChainAnalyzer._matches_source_pattern]] - code - gateway/security/tool_chain_analyzer.py
- [[ToolChainAnalyzer._trigger_alert]] - code - gateway/security/tool_chain_analyzer.py
- [[ToolChainAnalyzer.analyze_tool_call]] - code - gateway/security/tool_chain_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1116
SORT file.name ASC
```
