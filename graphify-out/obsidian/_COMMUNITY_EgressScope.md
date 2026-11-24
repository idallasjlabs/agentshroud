---
type: community
members: 18
---

# EgressScope

**Members:** 18 nodes

## Members
- [[dot-__init__()_15]] - code - gateway/security/egress_approval.py
- [[dot-_check_existing_rule()]] - code - gateway/security/egress_approval.py
- [[dot-_load_rules()]] - code - gateway/security/egress_approval.py
- [[dot-add_rule()]] - code - gateway/security/egress_approval.py
- [[dot-from_dict()_1]] - code - gateway/security/egress_approval.py
- [[dot-matches()]] - code - gateway/security/egress_approval.py
- [[dot-preload_permanent_rules()]] - code - gateway/security/egress_approval.py
- [[dot-to_dict()_3]] - code - gateway/security/egress_approval.py
- [[Add or modify an egress rule. Args domain Target domain action allow or…]] - rationale - gateway/security/egress_approval.py
- [[Check if domain matches an existing rule.]] - rationale - gateway/security/egress_approval.py
- [[Defines who an egress rule applies to. kind values all — applies to every…]] - rationale - gateway/security/egress_approval.py
- [[EgressRule]] - code - gateway/security/egress_approval.py
- [[EgressScope]] - code - gateway/security/egress_approval.py
- [[Initialize the approval queue. Args rules_file Path to persistent rules…]] - rationale - gateway/security/egress_approval.py
- [[Load rules from persistent storage.]] - rationale - gateway/security/egress_approval.py
- [[Pre-approve known service domains at startup without interactive prompts.…]] - rationale - gateway/security/egress_approval.py
- [[Represents an egress allowdeny rule.]] - rationale - gateway/security/egress_approval.py
- [[Return True if this scope applies to the given user context.]] - rationale - gateway/security/egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressScope
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 3 edges to [[_COMMUNITY_egress_approval.py]]
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[EgressScope]] - degree 10, connects to 3 communities
- [[EgressRule]] - degree 8, connects to 2 communities
- [[dot-add_rule()]] - degree 6, connects to 2 communities
- [[dot-_load_rules()]] - degree 6, connects to 2 communities
- [[dot-_check_existing_rule()]] - degree 5, connects to 2 communities
