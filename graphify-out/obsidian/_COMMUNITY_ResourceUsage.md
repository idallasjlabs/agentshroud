---
type: community
cohesion: 0.18
members: 12
---

# ResourceUsage

**Cohesion:** 0.18 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-authorize_spawn()]] - code - gateway/security/subagent_governance.py
- [[dot-deregister()_1]] - code - gateway/security/subagent_governance.py
- [[dot-get_summary()_1]] - code - gateway/security/subagent_governance.py
- [[dot-get_usage()]] - code - gateway/security/subagent_governance.py
- [[dot-runtime_seconds()]] - code - gateway/security/subagent_governance.py
- [[dot-to_dict()_17]] - code - gateway/security/subagent_governance.py
- [[Authorize a subagent spawn. Returns (allowed, reason).]] - rationale - gateway/security/subagent_governance.py
- [[Get a summary of all subagent governance state for a session.]] - rationale - gateway/security/subagent_governance.py
- [[Get current resource usage for a subagent.]] - rationale - gateway/security/subagent_governance.py
- [[Remove a subagent from governance tracking. Returns final usage.]] - rationale - gateway/security/subagent_governance.py
- [[ResourceUsage_2]] - code - gateway/security/subagent_governance.py
- [[Tracks cumulative resource consumption for a single subagent.]] - rationale - gateway/security/subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ResourceUsage
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_dot-_check_budget]]
- 2 edges to [[_COMMUNITY_GovernanceAction]]

## Top bridge nodes
- [[dot-authorize_spawn()]] - degree 4, connects to 2 communities
- [[ResourceUsage_2]] - degree 7, connects to 1 community
- [[dot-deregister()_1]] - degree 4, connects to 1 community
- [[dot-get_summary()_1]] - degree 3, connects to 1 community
- [[dot-get_usage()]] - degree 3, connects to 1 community
