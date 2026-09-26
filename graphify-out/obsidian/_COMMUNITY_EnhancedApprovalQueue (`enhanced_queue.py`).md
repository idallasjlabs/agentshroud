---
type: community
cohesion: 0.22
members: 10
---

# EnhancedApprovalQueue (`enhanced_queue.py`)

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[.deregister()]] - code - gateway/security/subagent_governance.py
- [[.get_summary()_1]] - code - gateway/security/subagent_governance.py
- [[.get_usage()]] - code - gateway/security/subagent_governance.py
- [[.runtime_seconds()]] - code - gateway/security/subagent_governance.py
- [[.to_dict()_14]] - code - gateway/security/subagent_governance.py
- [[Get a summary of all subagent governance state for a session.]] - rationale - gateway/security/subagent_governance.py
- [[Get current resource usage for a subagent.]] - rationale - gateway/security/subagent_governance.py
- [[Remove a subagent from governance tracking. Returns final usage.]] - rationale - gateway/security/subagent_governance.py
- [[ResourceUsage_1]] - code - gateway/security/subagent_governance.py
- [[Tracks cumulative resource consumption for a single subagent.]] - rationale - gateway/security/subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EnhancedApprovalQueue_enhanced_queuepy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Quick Reference — AgentShroud]]
- 1 edge to [[_COMMUNITY_Vulcan — Subject Matter Auditor]]
- 1 edge to [[_COMMUNITY_TestCanvasAuthHelpers]]

## Top bridge nodes
- [[ResourceUsage_1]] - degree 7, connects to 2 communities
- [[.deregister()]] - degree 4, connects to 1 community
- [[.get_summary()_1]] - degree 3, connects to 1 community
- [[.get_usage()]] - degree 3, connects to 1 community