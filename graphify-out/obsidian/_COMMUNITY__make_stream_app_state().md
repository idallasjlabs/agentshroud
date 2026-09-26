---
type: community
cohesion: 0.33
members: 13
---

# _make_stream_app_state()

**Cohesion:** 0.33 - loosely connected
**Members:** 13 nodes

## Members
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
- [[persist_user_collab_mode()]] - code - gateway/security/group_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_make_stream_app_state
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_socrouter.py]]
- 8 edges to [[_COMMUNITY_StdioConnection]]
- 4 edges to [[_COMMUNITY_PermissionLevel]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_SCLClient]]

## Top bridge nodes
- [[group_config.py]] - degree 16, connects to 6 communities
- [[persist_user_collab_mode()]] - degree 9, connects to 2 communities
- [[persist_group_collab_mode()]] - degree 8, connects to 2 communities
- [[persist_group_member_add()]] - degree 8, connects to 2 communities
- [[persist_group_member_remove()]] - degree 8, connects to 2 communities