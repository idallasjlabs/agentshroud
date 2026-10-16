---
type: community
cohesion: 0.25
members: 8
---

# GovernanceAction

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-acceptable()]] - code - gateway/security/subagent_governance.py
- [[Configuration for subagent output trust scoring.]] - rationale - gateway/security/subagent_governance.py
- [[OutputScore]] - code - gateway/security/subagent_governance.py
- [[OutputTrustConfig]] - code - gateway/security/subagent_governance.py
- [[Privilege escalation prevention policy.]] - rationale - gateway/security/subagent_governance.py
- [[PrivilegePolicy]] - code - gateway/security/subagent_governance.py
- [[Result of scoring a subagent's output.]] - rationale - gateway/security/subagent_governance.py
- [[subagent_governance.py]] - code - gateway/security/subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GovernanceAction
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_TestPatternDetection]]
- 3 edges to [[_COMMUNITY_GovernanceAction]]
- 3 edges to [[_COMMUNITY_SubagentGovernance]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_ResourceUsage]]

## Top bridge nodes
- [[subagent_governance.py]] - degree 15, connects to 5 communities
- [[OutputScore]] - degree 4, connects to 1 community
