---
type: community
cohesion: 0.12
members: 23
---

# Community 388

**Cohesion:** 0.12 - loosely connected
**Members:** 23 nodes

## Members
- [[dot-__post_init__()_6]] - code - gateway/security/rbac_config.py
- [[Append a collaborator UID to the persistent store (idempotent, file-locked).]] - rationale - gateway/security/rbac_config.py
- [[DELETE users{user_id}collaborator endpoint]] - code - gateway/soc/router.py
- [[Ensure the persistence store's parent directory exists. Returns False on failure]] - rationale - gateway/security/rbac_config.py
- [[Initialize user roles based on configuration.]] - rationale - gateway/security/rbac_config.py
- [[POST userscollaborator endpoint]] - code - gateway/soc/router.py
- [[POST users{user_id}pause endpoint]] - code - gateway/soc/router.py
- [[Pause a collaborator's bot access without removing their record (file-locked).]] - rationale - gateway/security/rbac_config.py
- [[Read dynamically approved collaborator IDs from disk.]] - rationale - gateway/security/rbac_config.py
- [[Read persisted collaborator-removal exclusions from disk (Bug 1 fix).      Appli]] - rationale - gateway/security/rbac_config.py
- [[Read the full collaborator persistence store (all keys) from disk.]] - rationale - gateway/security/rbac_config.py
- [[Remove a collaborator from effective access (file-locked).      Strips the UID f]] - rationale - gateway/security/rbac_config.py
- [[Resume a paused collaborator's bot access (file-locked).      Removes the UID fr]] - rationale - gateway/security/rbac_config.py
- [[Write the full collaborator persistence store (all keys) to disk.]] - rationale - gateway/security/rbac_config.py
- [[_ensure_collab_dir()]] - code - gateway/security/rbac_config.py
- [[_load_collab_store()]] - code - gateway/security/rbac_config.py
- [[_write_collab_store()]] - code - gateway/security/rbac_config.py
- [[load_persisted_collaborators()]] - code - gateway/security/rbac_config.py
- [[load_removed_collaborator_ids()]] - code - gateway/security/rbac_config.py
- [[pause_collaborator()]] - code - gateway/security/rbac_config.py
- [[persist_approved_collaborator()]] - code - gateway/security/rbac_config.py
- [[revoke_approved_collaborator()]] - code - gateway/security/rbac_config.py
- [[unpause_collaborator()]] - code - gateway/security/rbac_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_388
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Ingest API & RBAC Core]]
- 8 edges to [[_COMMUNITY_SOC Correlation & Router]]
- 3 edges to [[_COMMUNITY_TeamsGroup Collaborator Responses]]
- 3 edges to [[_COMMUNITY_Collaborator Activity & Telegram Proxy]]
- 1 edge to [[_COMMUNITY_Community 226]]

## Top bridge nodes
- [[persist_approved_collaborator()]] - degree 11, connects to 4 communities
- [[pause_collaborator()]] - degree 10, connects to 4 communities
- [[unpause_collaborator()]] - degree 9, connects to 4 communities
- [[_load_collab_store()]] - degree 9, connects to 2 communities
- [[revoke_approved_collaborator()]] - degree 9, connects to 2 communities