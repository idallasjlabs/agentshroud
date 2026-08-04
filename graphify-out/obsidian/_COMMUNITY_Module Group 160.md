---
type: community
cohesion: 0.07
members: 30
---

# Module Group 160

**Cohesion:** 0.07 - loosely connected
**Members:** 30 nodes

## Members
- [[._active_bot_id()]] - code - gateway/proxy/telegram_proxy.py
- [[._build_collaborator_safe_info_response()]] - code - gateway/proxy/telegram_proxy.py
- [[._emit_quarantine_event()]] - code - gateway/proxy/telegram_proxy.py
- [[._forward_file_download()]] - code - gateway/proxy/telegram_proxy.py
- [[._is_immune()]] - code - gateway/proxy/telegram_proxy.py
- [[._is_suppressed_outbound_payload()]] - code - gateway/proxy/telegram_proxy.py
- [[._notify_collaborator_command_blocked()]] - code - gateway/proxy/telegram_proxy.py
- [[._proxy_request_impl()]] - code - gateway/proxy/telegram_proxy.py
- [[._quarantine_blocked_message()]] - code - gateway/proxy/telegram_proxy.py
- [[._resolve_text_field()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_collaborator_safe_info_response()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_disclosure()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_telegram_text()]] - code - gateway/proxy/telegram_proxy.py
- [[._suppress_duplicate_system_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[.proxy_request()]] - code - gateway/proxy/telegram_proxy.py
- [[Best-effort Telegram sender with bounded retries.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Best-effort async event emission for quarantine actions.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Build informative but non-sensitive response for collaborator conceptual questio]] - rationale - gateway/proxy/telegram_proxy.py
- [[Forward a Telegram file download and return a raw-binary sentinel dict.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Notify a collaborator that a privileged command is not available.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Per-request bot_id for activity tracking.          Returns the bot_id set by pro]] - rationale - gateway/proxy/telegram_proxy.py
- [[Persist blocked inbound messages for admin review.          Also records the blo]] - rationale - gateway/proxy/telegram_proxy.py
- [[Proxy a single Telegram API request.          For getUpdates responses scan eac]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return (field_name, text_value) for Telegram-style outbound payloads.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True if user_id has active (non-expired) immunity.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send tailored safe informational response for collaborator conceptual query.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send the one-time collaborator disclosure notice.          Picks the appropriate]] - rationale - gateway/proxy/telegram_proxy.py
- [[Suppress repeated startupshutdown system notices in short windows.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Thin wrapper sets per-request bot identity in contextvars so local replies]] - rationale - gateway/proxy/telegram_proxy.py
- [[True when filtered payload should be dropped instead of forwarded.]] - rationale - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_160
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 8 edges to [[_COMMUNITY_Module Group 60]]
- 4 edges to [[_COMMUNITY_Module Group 87]]
- 2 edges to [[_COMMUNITY_Collaborator Responses]]
- 1 edge to [[_COMMUNITY_Dashboard Routes & WebSocket]]

## Top bridge nodes
- [[._proxy_request_impl()]] - degree 14, connects to 4 communities
- [[._send_telegram_text()]] - degree 11, connects to 4 communities
- [[._emit_quarantine_event()]] - degree 5, connects to 3 communities
- [[._resolve_text_field()]] - degree 7, connects to 2 communities
- [[._notify_collaborator_command_blocked()]] - degree 5, connects to 2 communities
