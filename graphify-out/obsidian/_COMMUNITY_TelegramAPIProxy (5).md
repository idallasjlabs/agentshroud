---
type: community
members: 14
---

# TelegramAPIProxy (5)

**Members:** 14 nodes

## Members
- [[dot-_active_bot_id()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_build_collaborator_safe_info_response()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_is_immune()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_notify_collaborator_command_blocked()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_quarantine_blocked_message()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_send_collaborator_safe_info_response()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_send_telegram_text()]] - code - gateway/proxy/telegram_proxy.py
- [[Best-effort Telegram sender with bounded retries.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Build informative but non-sensitive response for collaborator conceptual questio]] - rationale - gateway/proxy/telegram_proxy.py
- [[Notify a collaborator that a privileged command is not available.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Per-request bot_id for activity tracking.          Returns the bot_id set by pro]] - rationale - gateway/proxy/telegram_proxy.py
- [[Persist blocked inbound messages for admin review.          Also records the blo]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True if user_id has active (non-expired) immunity.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send tailored safe informational response for collaborator conceptual query.]] - rationale - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TelegramAPIProxy_5
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 3 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy (4)]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py (2)]]
- 1 edge to [[_COMMUNITY_dot-_proxy_request_impl]]

## Top bridge nodes
- [[dot-_send_telegram_text()]] - degree 11, connects to 4 communities
- [[dot-_quarantine_blocked_message()]] - degree 6, connects to 2 communities
- [[dot-_active_bot_id()]] - degree 5, connects to 2 communities
- [[dot-_notify_collaborator_command_blocked()]] - degree 5, connects to 2 communities
- [[dot-_send_collaborator_safe_info_response()]] - degree 6, connects to 1 community
