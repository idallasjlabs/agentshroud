---
type: community
cohesion: 0.27
members: 10
---

# Subagent Governance (security)

**Cohesion:** 0.27 - loosely connected
**Members:** 10 nodes

## Members
- [[._log_event()]] - code - gateway/security/subagent_governance.py
- [[.acceptable()]] - code - gateway/security/subagent_governance.py
- [[.get_governance_events()]] - code - gateway/security/subagent_governance.py
- [[Action to take when a governance limit is hit.]] - rationale - gateway/security/subagent_governance.py
- [[GovernanceAction]] - code - gateway/security/subagent_governance.py
- [[GovernanceEvent]] - code - gateway/security/subagent_governance.py
- [[GovernanceEventType]] - code - gateway/security/subagent_governance.py
- [[OutputScore]] - code - gateway/security/subagent_governance.py
- [[Result of scoring a subagent's output.]] - rationale - gateway/security/subagent_governance.py
- [[subagent_governance.py]] - code - gateway/security/subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Subagent_Governance_security
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Subagent Governance]]
- 6 edges to [[_COMMUNITY_Subagent Governance]]
- 6 edges to [[_COMMUNITY_Subagent Governance]]
- 5 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 5 edges to [[_COMMUNITY_Subagent Governance (security)]]
- 2 edges to [[_COMMUNITY_Subagent Governance (security)]]
- 2 edges to [[_COMMUNITY_Subagent Governance]]
- 2 edges to [[_COMMUNITY_Subagent Governance]]
- 1 edge to [[_COMMUNITY_A2a Governance (security)]]

## Top bridge nodes
- [[subagent_governance.py]] - degree 14, connects to 6 communities
- [[GovernanceAction]] - degree 12, connects to 6 communities
- [[GovernanceEventType]] - degree 12, connects to 6 communities
- [[._log_event()]] - degree 8, connects to 3 communities
- [[.get_governance_events()]] - degree 4, connects to 2 communities