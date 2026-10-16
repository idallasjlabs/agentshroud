---
type: community
cohesion: 0.12
members: 30
---

# rbac_config.py

**Cohesion:** 0.12 - loosely connected
**Members:** 30 nodes

## Members
- [[dot-__post_init__()_3]] - code - gateway/security/rbac_config.py
- [[dot-_build_record()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_rbac()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_teams()]] - code - gateway/soc/contributors.py
- [[dot-_load_paused_ids()]] - code - gateway/soc/contributors.py
- [[dot-get_contributor()]] - code - gateway/soc/contributors.py
- [[dot-list_contributors()]] - code - gateway/soc/contributors.py
- [[Append a collaborator UID to the persistent store (idempotent, file-locked).]] - rationale - gateway/security/rbac_config.py
- [[ContributorRecord_1]] - code - gateway/soc/contributors.py
- [[Ensure the persistence store's parent directory exists. Returns False on failure]] - rationale - gateway/security/rbac_config.py
- [[Initialize user roles based on configuration.]] - rationale - gateway/security/rbac_config.py
- [[Pause a collaborator's bot access without removing their record (file-locked).]] - rationale - gateway/security/rbac_config.py
- [[Read dynamically approved collaborator IDs from disk.]] - rationale - gateway/security/rbac_config.py
- [[Read persisted collaborator-removal exclusions from disk (Bug 1 fix).      Appli]] - rationale - gateway/security/rbac_config.py
- [[Read persisted paused-collaborator IDs from disk.      Owner-initiated manual pa]] - rationale - gateway/security/rbac_config.py
- [[Read the full collaborator persistence store (all keys) from disk.]] - rationale - gateway/security/rbac_config.py
- [[Remove a collaborator from effective access (file-locked).      Strips the UID f]] - rationale - gateway/security/rbac_config.py
- [[Resume a paused collaborator's bot access (file-locked).      Removes the UID fr]] - rationale - gateway/security/rbac_config.py
- [[Write the full collaborator persistence store (all keys) to disk.]] - rationale - gateway/security/rbac_config.py
- [[_ensure_collab_dir()]] - code - gateway/security/rbac_config.py
- [[_load_collab_store()]] - code - gateway/security/rbac_config.py
- [[_write_collab_store()]] - code - gateway/security/rbac_config.py
- [[load_paused_collaborator_ids()]] - code - gateway/security/rbac_config.py
- [[load_persisted_collaborators()]] - code - gateway/security/rbac_config.py
- [[load_removed_collaborator_ids()]] - code - gateway/security/rbac_config.py
- [[pause_collaborator()]] - code - gateway/security/rbac_config.py
- [[persist_approved_collaborator()]] - code - gateway/security/rbac_config.py
- [[rbac_config.py]] - code - gateway/security/rbac_config.py
- [[revoke_approved_collaborator()]] - code - gateway/security/rbac_config.py
- [[unpause_collaborator()]] - code - gateway/security/rbac_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/rbac_configpy
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_socrouter.py]]
- 8 edges to [[_COMMUNITY_Action]]
- 5 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 5 edges to [[_COMMUNITY_RBACConfig]]
- 4 edges to [[_COMMUNITY_telegram_proxy.py]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 1 edge to [[_COMMUNITY_group_config.py]]
- 1 edge to [[_COMMUNITY_MCPPolicyEngine]]
- 1 edge to [[_COMMUNITY_RBACConfig_2]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown]]

## Top bridge nodes
- [[rbac_config.py]] - degree 24, connects to 5 communities
- [[load_paused_collaborator_ids()]] - degree 8, connects to 4 communities
- [[persist_approved_collaborator()]] - degree 10, connects to 3 communities
- [[pause_collaborator()]] - degree 9, connects to 3 communities
- [[unpause_collaborator()]] - degree 9, connects to 3 communities
