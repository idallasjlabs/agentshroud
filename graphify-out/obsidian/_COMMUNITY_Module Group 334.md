---
type: community
cohesion: 0.20
members: 12
---

# Module Group 334

**Cohesion:** 0.20 - loosely connected
**Members:** 12 nodes

## Members
- [[._append_decision()]] - code - gateway/security/egress_approval.py
- [[._check_existing_rule()]] - code - gateway/security/egress_approval.py
- [[.approve()]] - code - gateway/security/egress_approval.py
- [[.deny()]] - code - gateway/security/egress_approval.py
- [[.preload_permanent_rules()]] - code - gateway/security/egress_approval.py
- [[Append an entry to the capped decision audit log (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Approve a pending egress request.          Args             request_id ID of r]] - rationale - gateway/security/egress_approval.py
- [[Check if domain matches an existing rule.]] - rationale - gateway/security/egress_approval.py
- [[Deny a pending egress request.          Args             request_id ID of requ]] - rationale - gateway/security/egress_approval.py
- [[EgressRule]] - code - gateway/security/egress_approval.py
- [[Pre-approve known service domains at startup without interactive prompts.]] - rationale - gateway/security/egress_approval.py
- [[Represents an egress allowdeny rule.]] - rationale - gateway/security/egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_334
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Module Group 252]]
- 3 edges to [[_COMMUNITY_Module Group 231]]
- 2 edges to [[_COMMUNITY_Dashboard Routes & WebSocket]]
- 2 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 200]]
- 1 edge to [[_COMMUNITY_Module Group 523]]
- 1 edge to [[_COMMUNITY_Module Group 522]]

## Top bridge nodes
- [[.approve()]] - degree 7, connects to 4 communities
- [[.deny()]] - degree 7, connects to 4 communities
- [[EgressRule]] - degree 8, connects to 3 communities
- [[._check_existing_rule()]] - degree 5, connects to 2 communities
- [[._append_decision()]] - degree 4, connects to 1 community