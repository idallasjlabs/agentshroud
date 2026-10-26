---
type: community
members: 18
---

# Community 1119

**Members:** 18 nodes

## Members
- [[._handle_addtogroup_command()]] - code - gateway/proxy/telegram_proxy.py
- [[._handle_groups_command()]] - code - gateway/proxy/telegram_proxy.py
- [[._handle_projects_command()]] - code - gateway/proxy/telegram_proxy.py
- [[._handle_rmfromgroup_command()]] - code - gateway/proxy/telegram_proxy.py
- [[._handle_setmode_command()]] - code - gateway/proxy/telegram_proxy.py
- [[._queue_collaborator_access_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_collaborator_pending_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_owner_admin_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_telegram_with_keyboard()]] - code - gateway/proxy/telegram_proxy.py
- [[Handle addtogroup user_id group_id (owner only).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Handle groups — list groups this user belongs to.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Handle projects — list accessible projects.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Handle rmfromgroup user_id group_id (owner or group admin).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Handle setmode group_iduser_id local_onlyproject_scopedfull_access (owne]] - rationale - gateway/proxy/telegram_proxy.py
- [[Queue owner approval request for unknownrevoked users.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send a Telegram message with an inline keyboard.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic owner admin notice without model invocation.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic pending-approval notice to unknownrevoked users.]] - rationale - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1119
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_Community 14]]
- 8 edges to [[_COMMUNITY_Community 18]]
- 3 edges to [[_COMMUNITY_Community 223]]
- 1 edge to [[_COMMUNITY_Community 146]]
- 1 edge to [[_COMMUNITY_Community 605]]

## Top bridge nodes
- [[._send_owner_admin_notice()]] - degree 12, connects to 3 communities
- [[._handle_addtogroup_command()]] - degree 7, connects to 3 communities
- [[._handle_rmfromgroup_command()]] - degree 7, connects to 3 communities
- [[._handle_setmode_command()]] - degree 6, connects to 3 communities
- [[._handle_groups_command()]] - degree 5, connects to 2 communities