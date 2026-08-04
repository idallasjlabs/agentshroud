---
type: community
cohesion: 0.10
members: 28
---

# Module Group 167

**Cohesion:** 0.10 - loosely connected
**Members:** 28 nodes

## Members
- [[.is_active()]] - code - gateway/security/delegation.py
- [[.test_cleanup_expired_removes_and_returns_count()]] - code - gateway/tests/test_delegation.py
- [[.test_delegation_to_dict_and_back()]] - code - gateway/tests/test_delegation.py
- [[.test_get_active_delegations_excludes_expired()]] - code - gateway/tests/test_delegation.py
- [[.test_get_delegations_for_user()]] - code - gateway/tests/test_delegation.py
- [[.test_is_delegated_returns_false_after_expiry()]] - code - gateway/tests/test_delegation.py
- [[.test_is_delegated_returns_false_for_other_privilege()]] - code - gateway/tests/test_delegation.py
- [[.test_is_delegated_returns_false_for_other_user()]] - code - gateway/tests/test_delegation.py
- [[.test_is_delegated_returns_true_for_active()]] - code - gateway/tests/test_delegation.py
- [[.test_no_active_delegations_initially()]] - code - gateway/tests/test_delegation.py
- [[.test_redelegate_replaces_existing()]] - code - gateway/tests/test_delegation.py
- [[.test_revoke_all_for_user()]] - code - gateway/tests/test_delegation.py
- [[.test_revoke_removes_delegation()]] - code - gateway/tests/test_delegation.py
- [[.test_revoke_returns_false_when_nothing_to_revoke()]] - code - gateway/tests/test_delegation.py
- [[.to_dict()_6]] - code - gateway/security/delegation.py
- [[A single time-bounded privilege delegation record.]] - rationale - gateway/security/delegation.py
- [[Delegation]] - code - gateway/security/delegation.py
- [[DelegationError]] - code - gateway/security/delegation.py
- [[DelegationManager_1]] - code - gateway/tests/test_delegation.py
- [[In-memory delegation manager (no disk IO).]] - rationale - gateway/tests/test_delegation.py
- [[Raised when a delegation operation is invalid.]] - rationale - gateway/security/delegation.py
- [[TestIsDelegated]] - code - gateway/tests/test_delegation.py
- [[TestListAndCleanup]] - code - gateway/tests/test_delegation.py
- [[TestRedelegation]] - code - gateway/tests/test_delegation.py
- [[TestRevoke]] - code - gateway/tests/test_delegation.py
- [[TestSerialization]] - code - gateway/tests/test_delegation.py
- [[mgr()]] - code - gateway/tests/test_delegation.py
- [[test_delegation.py]] - code - gateway/tests/test_delegation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_167
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_Module Group 190]]
- 3 edges to [[_COMMUNITY_Module Group 486]]
- 3 edges to [[_COMMUNITY_Module Group 526]]
- 1 edge to [[_COMMUNITY_Module Group 189]]

## Top bridge nodes
- [[DelegationError]] - degree 14, connects to 4 communities
- [[Delegation]] - degree 17, connects to 3 communities
- [[test_delegation.py]] - degree 12, connects to 3 communities
- [[TestIsDelegated]] - degree 9, connects to 1 community
- [[TestListAndCleanup]] - degree 9, connects to 1 community
