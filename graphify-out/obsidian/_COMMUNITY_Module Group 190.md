---
type: community
cohesion: 0.13
members: 25
---

# Module Group 190

**Cohesion:** 0.13 - loosely connected
**Members:** 25 nodes

## Members
- [[.__init__()_55]] - code - gateway/security/delegation.py
- [[._load()]] - code - gateway/security/delegation.py
- [[._require_owner()]] - code - gateway/security/delegation.py
- [[._revoke_by_user_privilege()]] - code - gateway/security/delegation.py
- [[._save()]] - code - gateway/security/delegation.py
- [[.cleanup_expired()_1]] - code - gateway/security/delegation.py
- [[.delegate()]] - code - gateway/security/delegation.py
- [[.from_dict()_3]] - code - gateway/security/delegation.py
- [[.get_active_delegations()]] - code - gateway/security/delegation.py
- [[.get_delegations_for_user()]] - code - gateway/security/delegation.py
- [[.is_delegated()]] - code - gateway/security/delegation.py
- [[.revoke()]] - code - gateway/security/delegation.py
- [[.revoke_all_for_user()]] - code - gateway/security/delegation.py
- [[Create a time-bounded delegation.          Args             owner_id Must matc]] - rationale - gateway/security/delegation.py
- [[DelegationManager]] - code - gateway/security/delegation.py
- [[DelegationPrivilege]] - code - gateway/security/delegation.py
- [[Manages owner-away privilege delegations.      Thread-safe via file locking for]] - rationale - gateway/security/delegation.py
- [[Remove expired delegations, persist result. Returns count removed.]] - rationale - gateway/security/delegation.py
- [[Return True if the user currently holds the delegated privilege.]] - rationale - gateway/security/delegation.py
- [[Return all active delegations held by a specific user.]] - rationale - gateway/security/delegation.py
- [[Return all currently active (non-expired) delegations.]] - rationale - gateway/security/delegation.py
- [[Revoke all delegations for a specific user. Returns count removed.]] - rationale - gateway/security/delegation.py
- [[Revoke an active delegation.          Returns True if a matching active delegati]] - rationale - gateway/security/delegation.py
- [[Subset of privileges that can be delegated by the owner.]] - rationale - gateway/security/delegation.py
- [[delegation.py]] - code - gateway/security/delegation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_190
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_Module Group 167]]
- 3 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 3 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_Module Group 208]]
- 2 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 2 edges to [[_COMMUNITY_Module Group 486]]
- 2 edges to [[_COMMUNITY_Module Group 526]]
- 1 edge to [[_COMMUNITY_Module Group 60]]

## Top bridge nodes
- [[DelegationPrivilege]] - degree 25, connects to 8 communities
- [[DelegationManager]] - degree 25, connects to 4 communities
- [[delegation.py]] - degree 5, connects to 2 communities
- [[.delegate()]] - degree 8, connects to 1 community
- [[._save()]] - degree 6, connects to 1 community
