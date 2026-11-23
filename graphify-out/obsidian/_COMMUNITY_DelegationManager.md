---
type: community
members: 15
---

# DelegationManager

**Members:** 15 nodes

## Members
- [[dot-__init__()_7]] - code - gateway/security/delegation.py
- [[dot-_load()]] - code - gateway/security/delegation.py
- [[dot-_require_owner()]] - code - gateway/security/delegation.py
- [[dot-_revoke_by_user_privilege()]] - code - gateway/security/delegation.py
- [[dot-_save()]] - code - gateway/security/delegation.py
- [[dot-cleanup_expired()]] - code - gateway/security/delegation.py
- [[dot-delegate()]] - code - gateway/security/delegation.py
- [[dot-revoke()]] - code - gateway/security/delegation.py
- [[dot-revoke_all_for_user()]] - code - gateway/security/delegation.py
- [[Create a time-bounded delegation. Args owner_id Must match configured…]] - rationale - gateway/security/delegation.py
- [[DelegationManager]] - code - gateway/security/delegation.py
- [[Manages owner-away privilege delegations. Thread-safe via file locking for…]] - rationale - gateway/security/delegation.py
- [[Remove expired delegations, persist result. Returns count removed.]] - rationale - gateway/security/delegation.py
- [[Revoke all delegations for a specific user. Returns count removed.]] - rationale - gateway/security/delegation.py
- [[Revoke an active delegation. Returns True if a matching active delegation was…]] - rationale - gateway/security/delegation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DelegationManager
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_dot-_cleanup_expired]]
- 3 edges to [[_COMMUNITY_delegation.py]]
- 3 edges to [[_COMMUNITY_telegram_proxy.py]]
- 2 edges to [[_COMMUNITY_Delegation]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_test_delegation.py]]
- 1 edge to [[_COMMUNITY_mgr]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[DelegationManager]] - degree 19, connects to 6 communities
- [[dot-delegate()]] - degree 8, connects to 3 communities
- [[dot-_require_owner()]] - degree 5, connects to 1 community
- [[dot-revoke()]] - degree 5, connects to 1 community
- [[dot-_revoke_by_user_privilege()]] - degree 5, connects to 1 community
