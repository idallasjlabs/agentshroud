---
type: community
cohesion: 0.18
members: 15
---

# ._check_budget

**Cohesion:** 0.18 - loosely connected
**Members:** 15 nodes

## Members
- [[dot-__init__()_173]] - code - gateway/security/subagent_governance.py
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
- [[SubagentGovernance]] - code - gateway/security/subagent_governance.py
- [[Unified governance layer for subagent lifecycle.      Wraps SubagentMonitor with]] - rationale - gateway/security/subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_check_budget
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_SubagentGovernance]]
- 6 edges to [[_COMMUNITY_GovernanceAction]]
- 4 edges to [[_COMMUNITY_ResourceUsage]]
- 2 edges to [[_COMMUNITY_TestPatternDetection]]
- 1 edge to [[_COMMUNITY_TestOutputTrustScoring]]
- 1 edge to [[_COMMUNITY_TestSpawnAuthorization]]
- 1 edge to [[_COMMUNITY_TestToolAuthorization]]

## Top bridge nodes
- [[SubagentGovernance]] - degree 30, connects to 7 communities
- [[dot-_check_budget()]] - degree 8, connects to 1 community
- [[dot-authorize_tool()]] - degree 4, connects to 1 community
- [[dot-__init__()_173]] - degree 2, connects to 1 community
