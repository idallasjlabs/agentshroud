---
type: community
cohesion: 0.08
members: 42
---

# SCLClient

**Cohesion:** 0.08 - loosely connected
**Members:** 42 nodes

## Members
- [[.__post_init__()_8]] - code - gateway/security/rbac_config.py
- [[.add_member()]] - code - gateway/security/rbac_config.py
- [[.create_group()]] - code - gateway/security/rbac_config.py
- [[.delete_group()]] - code - gateway/security/rbac_config.py
- [[.get_group()]] - code - gateway/security/rbac_config.py
- [[.init_auto_groups()]] - code - gateway/security/rbac_config.py
- [[.list_groups()]] - code - gateway/security/rbac_config.py
- [[.remove_member()]] - code - gateway/security/rbac_config.py
- [[A named group of users.]] - rationale - gateway/security/rbac_config.py
- [[Add a user to a group (auto-groups are updated in-memory only).]] - rationale - gateway/security/rbac_config.py
- [[Append a collaborator UID to the persistent store (idempotent, file-locked).]] - rationale - gateway/security/rbac_config.py
- [[Create or replace a custom group and persist it.]] - rationale - gateway/security/rbac_config.py
- [[Delete a custom group. Returns True if deleted, False if not found.]] - rationale - gateway/security/rbac_config.py
- [[Derive and reset auto-groups from current RBAC user list, then load custom group]] - rationale - gateway/security/rbac_config.py
- [[Ensure the persistence store's parent directory exists. Returns False on failure]] - rationale - gateway/security/rbac_config.py
- [[Group]] - code - gateway/security/rbac_config.py
- [[Initialize user roles based on configuration.]] - rationale - gateway/security/rbac_config.py
- [[Pause a collaborator's bot access without removing their record (file-locked).]] - rationale - gateway/security/rbac_config.py
- [[Read custom groups from disk.]] - rationale - gateway/security/rbac_config.py
- [[Read dynamically approved collaborator IDs from disk.]] - rationale - gateway/security/rbac_config.py
- [[Read persisted collaborator-removal exclusions from disk (Bug 1 fix).      Appli]] - rationale - gateway/security/rbac_config.py
- [[Read persisted paused-collaborator IDs from disk.      Owner-initiated manual pa]] - rationale - gateway/security/rbac_config.py
- [[Read the full collaborator persistence store (all keys) from disk.]] - rationale - gateway/security/rbac_config.py
- [[Remove a collaborator from effective access (file-locked).      Strips the UID f]] - rationale - gateway/security/rbac_config.py
- [[Remove a user from a group (auto-groups are updated in-memory only).]] - rationale - gateway/security/rbac_config.py
- [[Resume a paused collaborator's bot access (file-locked).      Removes the UID fr]] - rationale - gateway/security/rbac_config.py
- [[Return group by ID, or None.]] - rationale - gateway/security/rbac_config.py
- [[Write only custom groups to disk (auto-groups are derived at runtime).]] - rationale - gateway/security/rbac_config.py
- [[Write the full collaborator persistence store (all keys) to disk.]] - rationale - gateway/security/rbac_config.py
- [[_ensure_collab_dir()]] - code - gateway/security/rbac_config.py
- [[_load_collab_store()]] - code - gateway/security/rbac_config.py
- [[_load_persisted_groups()]] - code - gateway/security/rbac_config.py
- [[_persist_groups()]] - code - gateway/security/rbac_config.py
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
TABLE source_file, type FROM #community/SCLClient
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_MiddlewareManager]]
- 8 edges to [[_COMMUNITY_socrouter.py]]
- 5 edges to [[_COMMUNITY_StdioConnection]]
- 3 edges to [[_COMMUNITY_FileSandbox]]
- 2 edges to [[_COMMUNITY_EncryptedStore]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_main.rs]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_IntelReportStore]]
- 1 edge to [[_COMMUNITY__make_stream_app_state()]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]

## Top bridge nodes
- [[rbac_config.py]] - degree 25, connects to 7 communities
- [[load_paused_collaborator_ids()]] - degree 8, connects to 4 communities
- [[persist_approved_collaborator()]] - degree 10, connects to 3 communities
- [[pause_collaborator()]] - degree 9, connects to 3 communities
- [[unpause_collaborator()]] - degree 9, connects to 3 communities