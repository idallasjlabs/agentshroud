---
type: community
cohesion: 0.12
members: 20
---

# Module Group 231

**Cohesion:** 0.12 - loosely connected
**Members:** 20 nodes

## Members
- [[._rule_to_dict()]] - code - gateway/security/egress_approval.py
- [[._save_rules()]] - code - gateway/security/egress_approval.py
- [[.add_rule()]] - code - gateway/security/egress_approval.py
- [[.cleanup_expired()_2]] - code - gateway/security/egress_approval.py
- [[.get_all_rules()]] - code - gateway/security/egress_approval.py
- [[.get_rules_for_user()]] - code - gateway/security/egress_approval.py
- [[.matches()]] - code - gateway/security/egress_approval.py
- [[.remove_rule()]] - code - gateway/security/egress_approval.py
- [[.revoke_decision()]] - code - gateway/security/egress_approval.py
- [[.to_dict()_8]] - code - gateway/security/egress_approval.py
- [[Add or modify an egress rule.          Args             domain Target domain]] - rationale - gateway/security/egress_approval.py
- [[Defines who an egress rule applies to.      kind values       all   — applies]] - rationale - gateway/security/egress_approval.py
- [[EgressScope]] - code - gateway/security/egress_approval.py
- [[Get all rules (permanent and session) with scope information.]] - rationale - gateway/security/egress_approval.py
- [[Remove an egress rule.          Args             domain Domain to remove rule]] - rationale - gateway/security/egress_approval.py
- [[Remove expired session rules and timed-out requests.]] - rationale - gateway/security/egress_approval.py
- [[Return True if this scope applies to the given user context.]] - rationale - gateway/security/egress_approval.py
- [[Return all rules whose scope matches the given user context (synchronous, lock-f]] - rationale - gateway/security/egress_approval.py
- [[Revoke an active rule associated with a decision log entry (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Save rules to persistent storage.]] - rationale - gateway/security/egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_231
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Module Group 252]]
- 3 edges to [[_COMMUNITY_Module Group 334]]
- 2 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 1 edge to [[_COMMUNITY_Module Group 200]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 523]]

## Top bridge nodes
- [[EgressScope]] - degree 11, connects to 3 communities
- [[.add_rule()]] - degree 6, connects to 3 communities
- [[._save_rules()]] - degree 10, connects to 2 communities
- [[.get_rules_for_user()]] - degree 4, connects to 1 community
- [[._rule_to_dict()]] - degree 4, connects to 1 community