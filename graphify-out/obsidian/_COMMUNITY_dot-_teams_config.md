---
type: community
members: 4
---

# ._teams_config

**Members:** 4 nodes

## Members
- [[dot-_teams_config()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-is_group_admin()_1]] - code - gateway/soc/auth.py
- [[Check group admin status via TeamsConfig if available.]] - rationale - gateway/soc/auth.py
- [[Return TeamsConfig from app_state if available.]] - rationale - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_teams_config
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[dot-_teams_config()]] - degree 3, connects to 1 community
- [[dot-is_group_admin()_1]] - degree 3, connects to 1 community
