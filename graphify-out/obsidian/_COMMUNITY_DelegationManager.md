---
type: community
members: 66
---

# DelegationManager

**Members:** 66 nodes

## Members
- [[dot-__init__()_176]] - code - gateway/security/delegation.py
- [[dot-_load()]] - code - gateway/security/delegation.py
- [[dot-_require_owner()]] - code - gateway/security/delegation.py
- [[dot-_revoke_by_user_privilege()]] - code - gateway/security/delegation.py
- [[dot-_save()]] - code - gateway/security/delegation.py
- [[dot-cleanup_expired()_2]] - code - gateway/security/delegation.py
- [[dot-delegate()]] - code - gateway/security/delegation.py
- [[dot-from_dict()_8]] - code - gateway/security/delegation.py
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
- [[dot-to_dict()_13]] - code - gateway/security/delegation.py
- [[A single time-bounded privilege delegation record.]] - rationale - gateway/security/delegation.py
- [[Create a time-bounded delegation.          Args             owner_id Must matc]] - rationale - gateway/security/delegation.py
- [[Delegation_1]] - code - gateway/security/delegation.py
- [[DelegationError]] - code - gateway/security/delegation.py
- [[DelegationManager]] - code - gateway/tests/test_delegation.py
- [[DelegationManager_1]] - code - gateway/security/delegation.py
- [[DelegationPrivilege]] - code - gateway/security/delegation.py
- [[FR2 Use Control]] - concept - docs/compliance/iec-62443-matrix.md
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
- [[mgr()_1]] - code - gateway/tests/test_delegation.py
- [[test_delegation.py]] - code - gateway/tests/test_delegation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DelegationManager
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_Path (4)]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue (2)]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown]]
- 1 edge to [[_COMMUNITY_export-bot-conversations.py (2)]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_05-behavior]]

## Top bridge nodes
- [[FR2 Use Control]] - degree 7, connects to 6 communities
- [[DelegationPrivilege]] - degree 25, connects to 5 communities
- [[DelegationManager_1]] - degree 26, connects to 3 communities
- [[delegation.py]] - degree 6, connects to 1 community
- [[dot-from_dict()_8]] - degree 3, connects to 1 community
