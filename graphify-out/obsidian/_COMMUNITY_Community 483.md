---
type: community
cohesion: 0.16
members: 19
---

# Community 483

**Cohesion:** 0.16 - loosely connected
**Members:** 19 nodes

## Members
- [[._check_budget()]] - code - gateway/security/subagent_governance.py
- [[._log_event()]] - code - gateway/security/subagent_governance.py
- [[.authorize_spawn()]] - code - gateway/security/subagent_governance.py
- [[.authorize_tool()]] - code - gateway/security/subagent_governance.py
- [[.record_api_call()]] - code - gateway/security/subagent_governance.py
- [[.record_egress()]] - code - gateway/security/subagent_governance.py
- [[.record_tokens()]] - code - gateway/security/subagent_governance.py
- [[.record_tool_call()]] - code - gateway/security/subagent_governance.py
- [[.score_output()]] - code - gateway/security/subagent_governance.py
- [[Authorize a subagent spawn. Returns (allowed, reason).]] - rationale - gateway/security/subagent_governance.py
- [[Check if a resource budget is exceeded.]] - rationale - gateway/security/subagent_governance.py
- [[Check if a subagent is allowed to use a specific tool.]] - rationale - gateway/security/subagent_governance.py
- [[Record a tool invocation.]] - rationale - gateway/security/subagent_governance.py
- [[Record an LLM API call.]] - rationale - gateway/security/subagent_governance.py
- [[Record outbound data volume.]] - rationale - gateway/security/subagent_governance.py
- [[Record token consumption. Returns (within_budget, message).]] - rationale - gateway/security/subagent_governance.py
- [[Score a subagent's output for safety and quality.          In a full deployment,]] - rationale - gateway/security/subagent_governance.py
- [[SubagentGovernance]] - code - gateway/security/subagent_governance.py
- [[Unified governance layer for subagent lifecycle.      Wraps SubagentMonitor with]] - rationale - gateway/security/subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_483
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Community 507]]
- 5 edges to [[_COMMUNITY_Community 982]]
- 4 edges to [[_COMMUNITY_Community 864]]
- 4 edges to [[_COMMUNITY_Community 541]]
- 2 edges to [[_COMMUNITY_Community 912]]
- 2 edges to [[_COMMUNITY_Community 639]]
- 1 edge to [[_COMMUNITY_Community 1062]]

## Top bridge nodes
- [[SubagentGovernance]] - degree 30, connects to 7 communities
- [[._log_event()]] - degree 8, connects to 2 communities
- [[.score_output()]] - degree 7, connects to 2 communities
- [[.authorize_spawn()]] - degree 4, connects to 1 community