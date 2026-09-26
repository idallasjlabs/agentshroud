---
type: community
cohesion: 0.17
members: 12
---

# purge_low_value_events()

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[._check_budget()]] - code - gateway/security/subagent_governance.py
- [[.authorize_tool()]] - code - gateway/security/subagent_governance.py
- [[.record_api_call()]] - code - gateway/security/subagent_governance.py
- [[.record_egress()]] - code - gateway/security/subagent_governance.py
- [[.record_tokens()]] - code - gateway/security/subagent_governance.py
- [[.record_tool_call()]] - code - gateway/security/subagent_governance.py
- [[Check if a resource budget is exceeded.]] - rationale - gateway/security/subagent_governance.py
- [[Check if a subagent is allowed to use a specific tool.]] - rationale - gateway/security/subagent_governance.py
- [[Record a tool invocation.]] - rationale - gateway/security/subagent_governance.py
- [[Record an LLM API call.]] - rationale - gateway/security/subagent_governance.py
- [[Record outbound data volume.]] - rationale - gateway/security/subagent_governance.py
- [[Record token consumption. Returns (within_budget, message).]] - rationale - gateway/security/subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/purge_low_value_events
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Quick Reference — AgentShroud]]
- 2 edges to [[_COMMUNITY_TestCanvasAuthHelpers]]

## Top bridge nodes
- [[._check_budget()]] - degree 8, connects to 2 communities
- [[.authorize_tool()]] - degree 4, connects to 2 communities
- [[.record_api_call()]] - degree 3, connects to 1 community
- [[.record_egress()]] - degree 3, connects to 1 community
- [[.record_tokens()]] - degree 3, connects to 1 community