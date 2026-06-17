---
type: community
cohesion: 0.14
members: 23
---

# Module Group 208

**Cohesion:** 0.14 - loosely connected
**Members:** 23 nodes

## Members
- [[.test_persist_user_collab_mode()]] - code - gateway/tests/test_group_config.py
- [[.test_persist_user_collab_mode_update()]] - code - gateway/tests/test_group_config.py
- [[Calling persist_user_collab_mode twice updates the stored value.]] - rationale - gateway/tests/test_group_config.py
- [[Persist a per-user collab mode override set via the SOC dashboard.      Stored u]] - rationale - gateway/security/group_config.py
- [[Persist a runtime collab mode change for a group.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group creation so it survives container restarts.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group deletion so it survives container restarts.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group membership addition.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group membership removal.]] - rationale - gateway/security/group_config.py
- [[Result of the shared outbound text security scan.      processed a scan path (c]] - rationale - gateway/proxy/telegram_proxy.py
- [[_OutboundScan]] - code - gateway/proxy/telegram_proxy.py
- [[_ipv4_first_getaddrinfo()]] - code - gateway/proxy/telegram_proxy.py
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
- [[telegram_proxy.py]] - code - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_208
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_Collaborator Responses]]
- 13 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 6 edges to [[_COMMUNITY_Group Config & Teams]]
- 3 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 2 edges to [[_COMMUNITY_Authentication & Rate Limiting]]
- 2 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 2 edges to [[_COMMUNITY_Module Group 190]]
- 2 edges to [[_COMMUNITY_Module Group 60]]
- 2 edges to [[_COMMUNITY_Progressive Lockdown]]
- 2 edges to [[_COMMUNITY_RBAC Configuration]]
- 2 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Dashboard Routes & WebSocket]]
- 1 edge to [[_COMMUNITY_Module Group 127]]

## Top bridge nodes
- [[telegram_proxy.py]] - degree 26, connects to 12 communities
- [[_OutboundScan]] - degree 8, connects to 6 communities
- [[group_config.py]] - degree 15, connects to 4 communities
- [[persist_user_collab_mode()]] - degree 9, connects to 2 communities
- [[persist_group_collab_mode()]] - degree 8, connects to 2 communities