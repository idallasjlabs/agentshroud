---
type: community
members: 64
---

# Community 77

**Members:** 64 nodes

## Members
- [[.__init__()_70]] - code - gateway/security/delegation.py
- [[._load()]] - code - gateway/security/delegation.py
- [[._require_owner()]] - code - gateway/security/delegation.py
- [[._revoke_by_user_privilege()]] - code - gateway/security/delegation.py
- [[._save()]] - code - gateway/security/delegation.py
- [[.cleanup_expired()_1]] - code - gateway/security/delegation.py
- [[.delegate()]] - code - gateway/security/delegation.py
- [[.from_dict()_4]] - code - gateway/security/delegation.py
- [[.get_active_delegations()]] - code - gateway/security/delegation.py
- [[.get_delegations_for_user()]] - code - gateway/security/delegation.py
- [[.is_active()]] - code - gateway/security/delegation.py
- [[.is_delegated()]] - code - gateway/security/delegation.py
- [[.revoke()]] - code - gateway/security/delegation.py
- [[.revoke_all_for_user()]] - code - gateway/security/delegation.py
- [[.test_cleanup_expired_removes_and_returns_count()]] - code - gateway/tests/test_delegation.py
- [[.test_create_egress_delegation()]] - code - gateway/tests/test_delegation.py
- [[.test_create_user_management_delegation()]] - code - gateway/tests/test_delegation.py
- [[.test_delegation_expires_correctly()]] - code - gateway/tests/test_delegation.py
- [[.test_delegation_has_unique_id()]] - code - gateway/tests/test_delegation.py
- [[.test_delegation_to_dict_and_back()]] - code - gateway/tests/test_delegation.py
- [[.test_duration_over_max_rejected()]] - code - gateway/tests/test_delegation.py
- [[.test_duration_zero_rejected()]] - code - gateway/tests/test_delegation.py
- [[.test_get_active_delegations_excludes_expired()]] - code - gateway/tests/test_delegation.py
- [[.test_get_delegations_for_user()]] - code - gateway/tests/test_delegation.py
- [[.test_is_delegated_returns_false_after_expiry()]] - code - gateway/tests/test_delegation.py
- [[.test_is_delegated_returns_false_for_other_privilege()]] - code - gateway/tests/test_delegation.py
- [[.test_is_delegated_returns_false_for_other_user()]] - code - gateway/tests/test_delegation.py
- [[.test_is_delegated_returns_true_for_active()]] - code - gateway/tests/test_delegation.py
- [[.test_no_active_delegations_initially()]] - code - gateway/tests/test_delegation.py
- [[.test_non_owner_cannot_delegate()]] - code - gateway/tests/test_delegation.py
- [[.test_non_owner_cannot_revoke()]] - code - gateway/tests/test_delegation.py
- [[.test_owner_cannot_self_delegate()]] - code - gateway/tests/test_delegation.py
- [[.test_redelegate_replaces_existing()]] - code - gateway/tests/test_delegation.py
- [[.test_revoke_all_for_user()]] - code - gateway/tests/test_delegation.py
- [[.test_revoke_removes_delegation()]] - code - gateway/tests/test_delegation.py
- [[.test_revoke_returns_false_when_nothing_to_revoke()]] - code - gateway/tests/test_delegation.py
- [[.to_dict()_7]] - code - gateway/security/delegation.py
- [[A single time-bounded privilege delegation record.]] - rationale - gateway/security/delegation.py
- [[Create a time-bounded delegation.          Args             owner_id Must matc]] - rationale - gateway/security/delegation.py
- [[Delegation]] - code - gateway/security/delegation.py
- [[DelegationError]] - code - gateway/security/delegation.py
- [[DelegationManager]] - code - gateway/security/delegation.py
- [[DelegationManager_1]] - code - gateway/tests/test_delegation.py
- [[DelegationPrivilege]] - code - gateway/security/delegation.py
- [[In-memory delegation manager (no disk IO).]] - rationale - gateway/tests/test_delegation.py
- [[Manages owner-away privilege delegations.      Thread-safe via file locking for]] - rationale - gateway/security/delegation.py
- [[Raised when a delegation operation is invalid.]] - rationale - gateway/security/delegation.py
- [[Remove expired delegations, persist result. Returns count removed.]] - rationale - gateway/security/delegation.py
- [[Return True if the user currently holds the delegated privilege.]] - rationale - gateway/security/delegation.py
- [[Return all active delegations held by a specific user.]] - rationale - gateway/security/delegation.py
- [[Return all currently active (non-expired) delegations.]] - rationale - gateway/security/delegation.py
- [[Revoke all delegations for a specific user. Returns count removed.]] - rationale - gateway/security/delegation.py
- [[Revoke an active delegation.          Returns True if a matching active delegati]] - rationale - gateway/security/delegation.py
- [[Subset of privileges that can be delegated by the owner.]] - rationale - gateway/security/delegation.py
- [[TestAccessControl]] - code - gateway/tests/test_delegation.py
- [[TestDelegateBasic]] - code - gateway/tests/test_delegation.py
- [[TestIsDelegated]] - code - gateway/tests/test_delegation.py
- [[TestListAndCleanup]] - code - gateway/tests/test_delegation.py
- [[TestRedelegation]] - code - gateway/tests/test_delegation.py
- [[TestRevoke]] - code - gateway/tests/test_delegation.py
- [[TestSerialization]] - code - gateway/tests/test_delegation.py
- [[delegation.py]] - code - gateway/security/delegation.py
- [[mgr()]] - code - gateway/tests/test_delegation.py
- [[test_delegation.py]] - code - gateway/tests/test_delegation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_77
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 78]]
- 3 edges to [[_COMMUNITY_Community 19]]
- 2 edges to [[_COMMUNITY_Community 6]]
- 2 edges to [[_COMMUNITY_Community 4]]
- 1 edge to [[_COMMUNITY_Community 557]]
- 1 edge to [[_COMMUNITY_Community 134]]
- 1 edge to [[_COMMUNITY_Community 9]]
- 1 edge to [[_COMMUNITY_Community 93]]
- 1 edge to [[_COMMUNITY_Community 75]]
- 1 edge to [[_COMMUNITY_Community 152]]
- 1 edge to [[_COMMUNITY_Community 21]]

## Top bridge nodes
- [[DelegationPrivilege]] - degree 25, connects to 6 communities
- [[DelegationManager]] - degree 26, connects to 2 communities
- [[delegation.py]] - degree 6, connects to 2 communities
- [[DelegationError]] - degree 14, connects to 1 community
- [[.from_dict()_4]] - degree 3, connects to 1 community