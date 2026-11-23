---
type: community
members: 7
---

# ._cleanup_expired

**Members:** 7 nodes

## Members
- [[dot-_cleanup_expired()]] - code - gateway/security/delegation.py
- [[dot-get_active_delegations()]] - code - gateway/security/delegation.py
- [[dot-get_delegations_for_user()]] - code - gateway/security/delegation.py
- [[dot-is_delegated()]] - code - gateway/security/delegation.py
- [[Return True if the user currently holds the delegated privilege.]] - rationale - gateway/security/delegation.py
- [[Return all active delegations held by a specific user.]] - rationale - gateway/security/delegation.py
- [[Return all currently active (non-expired) delegations.]] - rationale - gateway/security/delegation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_cleanup_expired
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_DelegationManager]]
- 2 edges to [[_COMMUNITY_Delegation]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]

## Top bridge nodes
- [[dot-get_active_delegations()]] - degree 4, connects to 2 communities
- [[dot-get_delegations_for_user()]] - degree 4, connects to 2 communities
- [[dot-is_delegated()]] - degree 4, connects to 2 communities
- [[dot-_cleanup_expired()]] - degree 4, connects to 1 community
