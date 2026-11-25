---
type: community
members: 13
---

# EgressRule

**Members:** 13 nodes

## Members
- [[dot-__init__()_16]] - code - gateway/security/egress_approval.py
- [[dot-_append_decision()]] - code - gateway/security/egress_approval.py
- [[dot-_load_rules()]] - code - gateway/security/egress_approval.py
- [[dot-approve()]] - code - gateway/security/egress_approval.py
- [[dot-deny()]] - code - gateway/security/egress_approval.py
- [[dot-from_dict()_3]] - code - gateway/security/egress_approval.py
- [[Append an entry to the capped decision audit log (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Approve a pending egress request. Args request_id ID of request to approve…]] - rationale - gateway/security/egress_approval.py
- [[Deny a pending egress request. Args request_id ID of request to deny mode…]] - rationale - gateway/security/egress_approval.py
- [[EgressRule]] - code - gateway/security/egress_approval.py
- [[Initialize the approval queue. Args rules_file Path to persistent rules…]] - rationale - gateway/security/egress_approval.py
- [[Load rules from persistent storage.]] - rationale - gateway/security/egress_approval.py
- [[Represents an egress allowdeny rule.]] - rationale - gateway/security/egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressRule
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 4 edges to [[_COMMUNITY_EgressScope]]
- 4 edges to [[_COMMUNITY_ApprovalMode]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[dot-approve()]] - degree 7, connects to 4 communities
- [[dot-deny()]] - degree 7, connects to 4 communities
- [[EgressRule]] - degree 8, connects to 3 communities
- [[dot-_load_rules()]] - degree 6, connects to 2 communities
- [[dot-from_dict()_3]] - degree 3, connects to 2 communities
