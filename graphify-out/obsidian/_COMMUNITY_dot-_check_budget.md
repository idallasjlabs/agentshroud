---
type: community
cohesion: 0.17
members: 12
---

# ._check_budget

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-_check_budget()]] - code - gateway/security/subagent_governance.py
- [[dot-authorize_tool()]] - code - gateway/security/subagent_governance.py
- [[dot-record_api_call()]] - code - gateway/security/subagent_governance.py
- [[dot-record_egress()]] - code - gateway/security/subagent_governance.py
- [[dot-record_tokens()]] - code - gateway/security/subagent_governance.py
- [[dot-record_tool_call()]] - code - gateway/security/subagent_governance.py
- [[Check if a resource budget is exceeded.]] - rationale - gateway/security/subagent_governance.py
- [[Check if a subagent is allowed to use a specific tool.]] - rationale - gateway/security/subagent_governance.py
- [[Record a tool invocation.]] - rationale - gateway/security/subagent_governance.py
- [[Record an LLM API call.]] - rationale - gateway/security/subagent_governance.py
- [[Record outbound data volume.]] - rationale - gateway/security/subagent_governance.py
- [[Record token consumption. Returns (within_budget, message).]] - rationale - gateway/security/subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_check_budget
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_SubagentGovernance]]
- 2 edges to [[_COMMUNITY_GovernanceAction]]

## Top bridge nodes
- [[dot-_check_budget()]] - degree 8, connects to 2 communities
- [[dot-authorize_tool()]] - degree 4, connects to 2 communities
- [[dot-record_api_call()]] - degree 3, connects to 1 community
- [[dot-record_egress()]] - degree 3, connects to 1 community
- [[dot-record_tokens()]] - degree 3, connects to 1 community
