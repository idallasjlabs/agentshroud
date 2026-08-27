---
type: community
members: 40
---

# Community 134

**Members:** 40 nodes

## Members
- [[.__post_init__()_8]] - code - gateway/security/rbac_config.py
- [[Append a collaborator UID to the persistent store (idempotent, file-locked).]] - rationale - gateway/security/rbac_config.py
- [[DELETE users{user_id}collaborator endpoint]] - code - gateway/soc/router.py
- [[Ensure the persistence store's parent directory exists. Returns False on failure]] - rationale - gateway/security/rbac_config.py
- [[Initialize user roles based on configuration.]] - rationale - gateway/security/rbac_config.py
- [[POST userscollaborator endpoint]] - code - gateway/soc/router.py
- [[POST users{user_id}pause endpoint]] - code - gateway/soc/router.py
- [[Pause a collaborator's bot access without removing their record (file-locked).]] - rationale - gateway/security/rbac_config.py
- [[Persist a per-user collab mode override set via the SOC dashboard.      Stored u]] - rationale - gateway/security/group_config.py
- [[Persist a runtime collab mode change for a group.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group creation so it survives container restarts.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group deletion so it survives container restarts.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group membership addition.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group membership removal.]] - rationale - gateway/security/group_config.py
- [[Read dynamically approved collaborator IDs from disk.]] - rationale - gateway/security/rbac_config.py
- [[Read persisted collaborator-removal exclusions from disk (Bug 1 fix).      Appli]] - rationale - gateway/security/rbac_config.py
- [[Read the full collaborator persistence store (all keys) from disk.]] - rationale - gateway/security/rbac_config.py
- [[Remove a collaborator from effective access (file-locked).      Strips the UID f]] - rationale - gateway/security/rbac_config.py
- [[Resume a paused collaborator's bot access (file-locked).      Removes the UID fr]] - rationale - gateway/security/rbac_config.py
- [[Write the full collaborator persistence store (all keys) to disk.]] - rationale - gateway/security/rbac_config.py
- [[_ensure_collab_dir()]] - code - gateway/security/rbac_config.py
- [[_ipv4_first_getaddrinfo()]] - code - gateway/proxy/telegram_proxy.py
- [[_load_collab_store()]] - code - gateway/security/rbac_config.py
- [[_load_overrides()]] - code - gateway/security/group_config.py
- [[_save_overrides()]] - code - gateway/security/group_config.py
- [[_write_collab_store()]] - code - gateway/security/rbac_config.py
- [[group_config.py]] - code - gateway/security/group_config.py
- [[load_persisted_collaborators()]] - code - gateway/security/rbac_config.py
- [[load_removed_collaborator_ids()]] - code - gateway/security/rbac_config.py
- [[pause_collaborator()]] - code - gateway/security/rbac_config.py
- [[persist_approved_collaborator()]] - code - gateway/security/rbac_config.py
- [[persist_group_collab_mode()]] - code - gateway/security/group_config.py
- [[persist_group_create()]] - code - gateway/security/group_config.py
- [[persist_group_delete()]] - code - gateway/security/group_config.py
- [[persist_group_member_add()]] - code - gateway/security/group_config.py
- [[persist_group_member_remove()]] - code - gateway/security/group_config.py
- [[persist_user_collab_mode()]] - code - gateway/security/group_config.py
- [[revoke_approved_collaborator()]] - code - gateway/security/rbac_config.py
- [[telegram_proxy.py]] - code - gateway/proxy/telegram_proxy.py
- [[unpause_collaborator()]] - code - gateway/security/rbac_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_134
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_Community 19]]
- 16 edges to [[_COMMUNITY_Community 81]]
- 12 edges to [[_COMMUNITY_Community 15]]
- 7 edges to [[_COMMUNITY_Community 4]]
- 3 edges to [[_COMMUNITY_Community 9]]
- 2 edges to [[_COMMUNITY_Community 326]]
- 2 edges to [[_COMMUNITY_Community 787]]
- 2 edges to [[_COMMUNITY_Community 61]]
- 2 edges to [[_COMMUNITY_Community 49]]
- 1 edge to [[_COMMUNITY_Community 124]]
- 1 edge to [[_COMMUNITY_Community 1325]]
- 1 edge to [[_COMMUNITY_Community 374]]
- 1 edge to [[_COMMUNITY_Community 30]]
- 1 edge to [[_COMMUNITY_Community 126]]
- 1 edge to [[_COMMUNITY_Community 855]]
- 1 edge to [[_COMMUNITY_Community 129]]
- 1 edge to [[_COMMUNITY_Community 77]]
- 1 edge to [[_COMMUNITY_Community 263]]
- 1 edge to [[_COMMUNITY_Community 862]]
- 1 edge to [[_COMMUNITY_Community 62]]
- 1 edge to [[_COMMUNITY_Community 1844]]
- 1 edge to [[_COMMUNITY_Community 779]]
- 1 edge to [[_COMMUNITY_Community 755]]
- 1 edge to [[_COMMUNITY_Community 273]]

## Top bridge nodes
- [[telegram_proxy.py]] - degree 40, connects to 22 communities
- [[group_config.py]] - degree 16, connects to 4 communities
- [[persist_approved_collaborator()]] - degree 11, connects to 3 communities
- [[pause_collaborator()]] - degree 10, connects to 3 communities
- [[unpause_collaborator()]] - degree 9, connects to 3 communities