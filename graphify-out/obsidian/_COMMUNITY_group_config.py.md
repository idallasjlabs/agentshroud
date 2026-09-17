---
type: community
cohesion: 0.22
members: 17
---

# group_config.py

**Cohesion:** 0.22 - loosely connected
**Members:** 17 nodes

## Members
- [[.test_persist_user_collab_mode()]] - code - gateway/tests/test_group_config.py
- [[.test_persist_user_collab_mode_update()]] - code - gateway/tests/test_group_config.py
- [[Calling persist_user_collab_mode twice updates the stored value.]] - rationale - gateway/tests/test_group_config.py
- [[Persist a per-user collab mode override set via the SOC dashboard.      Stored u]] - rationale - gateway/security/group_config.py
- [[Persist a runtime collab mode change for a group.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group creation so it survives container restarts.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group membership addition.]] - rationale - gateway/security/group_config.py
- [[_load_overrides()]] - code - gateway/security/group_config.py
- [[_save_overrides()]] - code - gateway/security/group_config.py
- [[group_config.py]] - code - gateway/security/group_config.py
- [[persist_group_collab_mode()]] - code - gateway/security/group_config.py
- [[persist_group_create()]] - code - gateway/security/group_config.py
- [[persist_group_delete()]] - code - gateway/security/group_config.py
- [[persist_group_member_add()]] - code - gateway/security/group_config.py
- [[persist_group_member_remove()]] - code - gateway/security/group_config.py
- [[persist_user_collab_mode writes under __user_overrides__ key.]] - rationale - gateway/tests/test_group_config.py
- [[persist_user_collab_mode()]] - code - gateway/security/group_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/group_configpy
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_socrouter.py]]
- 11 edges to [[_COMMUNITY_TeamsConfig]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_ToolACLEnforcer]]
- 1 edge to [[_COMMUNITY_rbac_config.py]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[group_config.py]] - degree 17, connects to 5 communities
- [[persist_group_collab_mode()]] - degree 8, connects to 3 communities
- [[persist_group_member_add()]] - degree 8, connects to 3 communities
- [[persist_group_member_remove()]] - degree 8, connects to 3 communities
- [[persist_user_collab_mode()]] - degree 9, connects to 2 communities