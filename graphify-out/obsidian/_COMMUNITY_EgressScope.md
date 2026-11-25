---
type: community
members: 15
---

# EgressScope

**Members:** 15 nodes

## Members
- [[dot-_save_rules()]] - code - gateway/security/egress_approval.py
- [[dot-add_rule()]] - code - gateway/security/egress_approval.py
- [[dot-cleanup_expired()_1]] - code - gateway/security/egress_approval.py
- [[dot-matches()]] - code - gateway/security/egress_approval.py
- [[dot-remove_rule()]] - code - gateway/security/egress_approval.py
- [[dot-revoke_decision()]] - code - gateway/security/egress_approval.py
- [[dot-to_dict()_2]] - code - gateway/security/egress_approval.py
- [[Add or modify an egress rule. Args domain Target domain action allow or…]] - rationale - gateway/security/egress_approval.py
- [[Defines who an egress rule applies to. kind values all — applies to every…]] - rationale - gateway/security/egress_approval.py
- [[EgressScope]] - code - gateway/security/egress_approval.py
- [[Remove an egress rule. Args domain Domain to remove rule for Returns True if…]] - rationale - gateway/security/egress_approval.py
- [[Remove expired session rules and timed-out requests.]] - rationale - gateway/security/egress_approval.py
- [[Return True if this scope applies to the given user context.]] - rationale - gateway/security/egress_approval.py
- [[Revoke an active rule associated with a decision log entry (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Save rules to persistent storage.]] - rationale - gateway/security/egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressScope
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 4 edges to [[_COMMUNITY_EgressRule]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_ApprovalMode]]

## Top bridge nodes
- [[EgressScope]] - degree 10, connects to 4 communities
- [[dot-add_rule()]] - degree 6, connects to 3 communities
- [[dot-_save_rules()]] - degree 9, connects to 2 communities
- [[dot-cleanup_expired()_1]] - degree 3, connects to 1 community
- [[dot-remove_rule()]] - degree 3, connects to 1 community
