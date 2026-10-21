---
type: community
members: 18
---

# telegram_proxy.py (3)

**Members:** 18 nodes

## Members
- [[dot-add_member()]] - code - gateway/security/rbac_config.py
- [[dot-create_group()]] - code - gateway/security/rbac_config.py
- [[dot-delete_group()]] - code - gateway/security/rbac_config.py
- [[dot-get_group()]] - code - gateway/security/rbac_config.py
- [[dot-init_auto_groups()]] - code - gateway/security/rbac_config.py
- [[dot-remove_member()]] - code - gateway/security/rbac_config.py
- [[A named group of users.]] - rationale - gateway/security/rbac_config.py
- [[Add a user to a group (auto-groups are updated in-memory only).]] - rationale - gateway/security/rbac_config.py
- [[Create or replace a custom group and persist it.]] - rationale - gateway/security/rbac_config.py
- [[Delete a custom group. Returns True if deleted, False if not found.]] - rationale - gateway/security/rbac_config.py
- [[Derive and reset auto-groups from current RBAC user list, then load custom group]] - rationale - gateway/security/rbac_config.py
- [[Group]] - code - gateway/security/rbac_config.py
- [[Read custom groups from disk.]] - rationale - gateway/security/rbac_config.py
- [[Remove a user from a group (auto-groups are updated in-memory only).]] - rationale - gateway/security/rbac_config.py
- [[Return group by ID, or None.]] - rationale - gateway/security/rbac_config.py
- [[Write only custom groups to disk (auto-groups are derived at runtime).]] - rationale - gateway/security/rbac_config.py
- [[_load_persisted_groups()]] - code - gateway/security/rbac_config.py
- [[_persist_groups()]] - code - gateway/security/rbac_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/telegram_proxypy_3
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Action (2)]]
- 3 edges to [[_COMMUNITY_telegram_proxy.py (2)]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]

## Top bridge nodes
- [[Group]] - degree 9, connects to 3 communities
- [[_persist_groups()]] - degree 8, connects to 2 communities
- [[dot-create_group()]] - degree 4, connects to 1 community
- [[dot-delete_group()]] - degree 4, connects to 1 community
- [[dot-init_auto_groups()]] - degree 4, connects to 1 community
