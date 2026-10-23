---
type: community
cohesion: 0.06
members: 65
---

# _make_proxy

**Cohesion:** 0.06 - loosely connected
**Members:** 65 nodes

## Members
- [[dot-__init__()_195]] - code - gateway/security/delegation.py
- [[dot-_load()]] - code - gateway/security/delegation.py
- [[dot-_require_owner()]] - code - gateway/security/delegation.py
- [[dot-_revoke_by_user_privilege()]] - code - gateway/security/delegation.py
- [[dot-_save()]] - code - gateway/security/delegation.py
- [[dot-cleanup_expired()_3]] - code - gateway/security/delegation.py
- [[dot-delegate()]] - code - gateway/security/delegation.py
- [[dot-from_dict()_9]] - code - gateway/security/delegation.py
- [[dot-get_active_delegations()]] - code - gateway/security/delegation.py
- [[dot-get_delegations_for_user()]] - code - gateway/security/delegation.py
- [[dot-is_active()]] - code - gateway/security/delegation.py
- [[dot-is_delegated()]] - code - gateway/security/delegation.py
- [[dot-revoke()]] - code - gateway/security/delegation.py
- [[dot-revoke_all_for_user()]] - code - gateway/security/delegation.py
- [[dot-test_cleanup_expired_removes_and_returns_count()]] - code - gateway/tests/test_delegation.py
- [[dot-test_create_egress_delegation()]] - code - gateway/tests/test_delegation.py
- [[dot-test_create_user_management_delegation()]] - code - gateway/tests/test_delegation.py
- [[dot-test_delegation_expires_correctly()]] - code - gateway/tests/test_delegation.py
- [[dot-test_delegation_has_unique_id()]] - code - gateway/tests/test_delegation.py
- [[dot-test_delegation_to_dict_and_back()]] - code - gateway/tests/test_delegation.py
- [[dot-test_duration_over_max_rejected()]] - code - gateway/tests/test_delegation.py
- [[dot-test_duration_zero_rejected()]] - code - gateway/tests/test_delegation.py
- [[dot-test_get_active_delegations_excludes_expired()]] - code - gateway/tests/test_delegation.py
- [[dot-test_get_delegations_for_user()]] - code - gateway/tests/test_delegation.py
- [[dot-test_is_delegated_returns_false_after_expiry()]] - code - gateway/tests/test_delegation.py
- [[dot-test_is_delegated_returns_false_for_other_privilege()]] - code - gateway/tests/test_delegation.py
- [[dot-test_is_delegated_returns_false_for_other_user()]] - code - gateway/tests/test_delegation.py
- [[dot-test_is_delegated_returns_true_for_active()]] - code - gateway/tests/test_delegation.py
- [[dot-test_no_active_delegations_initially()]] - code - gateway/tests/test_delegation.py
- [[dot-test_non_owner_cannot_delegate()]] - code - gateway/tests/test_delegation.py
- [[dot-test_non_owner_cannot_revoke()]] - code - gateway/tests/test_delegation.py
- [[dot-test_owner_cannot_self_delegate()]] - code - gateway/tests/test_delegation.py
- [[dot-test_redelegate_replaces_existing()]] - code - gateway/tests/test_delegation.py
- [[dot-test_revoke_all_for_user()]] - code - gateway/tests/test_delegation.py
- [[dot-test_revoke_removes_delegation()]] - code - gateway/tests/test_delegation.py
- [[dot-test_revoke_returns_false_when_nothing_to_revoke()]] - code - gateway/tests/test_delegation.py
- [[dot-to_dict()_16]] - code - gateway/security/delegation.py
- [[A single time-bounded privilege delegation record.]] - rationale - gateway/security/delegation.py
- [[Create a time-bounded delegation.          Args             owner_id Must matc]] - rationale - gateway/security/delegation.py
- [[Delegation_1]] - code - gateway/security/delegation.py
- [[DelegationError]] - code - gateway/security/delegation.py
- [[DelegationManager]] - code - gateway/tests/test_delegation.py
- [[DelegationManager_1]] - code - gateway/security/delegation.py
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
- [[TestAccessControl_2]] - code - gateway/tests/test_delegation.py
- [[TestDelegateBasic]] - code - gateway/tests/test_delegation.py
- [[TestIsDelegated]] - code - gateway/tests/test_delegation.py
- [[TestListAndCleanup]] - code - gateway/tests/test_delegation.py
- [[TestRedelegation]] - code - gateway/tests/test_delegation.py
- [[TestRevoke]] - code - gateway/tests/test_delegation.py
- [[TestSerialization_2]] - code - gateway/tests/test_delegation.py
- [[ValueError]] - code
- [[delegation.py]] - code - gateway/security/delegation.py
- [[mgr()_2]] - code - gateway/tests/test_delegation.py
- [[test_delegation.py]] - code - gateway/tests/test_delegation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_make_proxy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 3 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py (2)]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_AuditStore]]
- 1 edge to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]

## Top bridge nodes
- [[DelegationPrivilege]] - degree 25, connects to 5 communities
- [[delegation.py]] - degree 6, connects to 2 communities
- [[DelegationManager_1]] - degree 24, connects to 1 community
- [[dot-from_dict()_9]] - degree 3, connects to 1 community
- [[ValueError]] - degree 2, connects to 1 community
