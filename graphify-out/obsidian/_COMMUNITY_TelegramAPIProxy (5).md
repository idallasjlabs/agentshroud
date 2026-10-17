---
type: community
members: 16
---

# TelegramAPIProxy (5)

**Members:** 16 nodes

## Members
- [[dot-_emit_quarantine_event()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_get_user_projects()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_is_immune()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_notify_collaborator_command_blocked()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_quarantine_blocked_message()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_resolve_collaborator_mode()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_send_disclosure()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_send_telegram_text()]] - code - gateway/proxy/telegram_proxy.py
- [[Best-effort Telegram sender with bounded retries.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Best-effort async event emission for quarantine actions.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Notify a collaborator that a privileged command is not available.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Persist blocked inbound messages for admin review.          Also records the blo]] - rationale - gateway/proxy/telegram_proxy.py
- [[Resolve effective collaboration mode for a user.          Resolution order]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True if user_id has active (non-expired) immunity.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return list of ProjectConfig objects for this user, or empty list.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send the one-time collaborator disclosure notice.          Picks the appropriate]] - rationale - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TelegramAPIProxy_5
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 5 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy (4)]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_test_dashboard.py]]

## Top bridge nodes
- [[dot-_send_telegram_text()]] - degree 11, connects to 4 communities
- [[dot-_emit_quarantine_event()]] - degree 5, connects to 3 communities
- [[dot-_resolve_collaborator_mode()]] - degree 6, connects to 2 communities
- [[dot-_notify_collaborator_command_blocked()]] - degree 5, connects to 2 communities
- [[dot-_quarantine_blocked_message()]] - degree 6, connects to 1 community
