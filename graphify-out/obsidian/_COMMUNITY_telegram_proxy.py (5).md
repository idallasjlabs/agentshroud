---
type: community
members: 13
---

# telegram_proxy.py (5)

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
TABLE source_file, type FROM #community/telegram_proxypy_5
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_socrouter.py]]
- 5 edges to [[_COMMUNITY_telegram_proxy.py]]
- 4 edges to [[_COMMUNITY_GroupConfig]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 3 edges to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py (2)]]

## Top bridge nodes
- [[group_config.py]] - degree 16, connects to 5 communities
- [[persist_group_collab_mode()]] - degree 8, connects to 3 communities
- [[persist_group_member_add()]] - degree 8, connects to 3 communities
- [[persist_group_member_remove()]] - degree 8, connects to 3 communities
- [[persist_user_collab_mode()]] - degree 9, connects to 2 communities
