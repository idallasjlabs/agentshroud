---
type: community
members: 14
---

# ._proxy_request_impl

**Members:** 14 nodes

## Members
- [[dot-_forward_file_download()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_is_suppressed_outbound_payload()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_proxy_request_impl()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_resolve_text_field()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_suppress_duplicate_system_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_username_for_bot()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-proxy_request()]] - code - gateway/proxy/telegram_proxy.py
- [[Forward a Telegram file download and return a raw-binary sentinel dict.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Proxy a single Telegram API request.          For getUpdates responses scan eac]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return (field_name, text_value) for Telegram-style outbound payloads.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return the @username (without @) for the given bot_id.          Looks up ``_bot_]] - rationale - gateway/proxy/telegram_proxy.py
- [[Suppress repeated startupshutdown system notices in short windows.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Thin wrapper sets per-request bot identity in contextvars so local replies]] - rationale - gateway/proxy/telegram_proxy.py
- [[True when filtered payload should be dropped instead of forwarded.]] - rationale - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_proxy_request_impl
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 4 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy (4)]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py (2)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (5)]]

## Top bridge nodes
- [[dot-_proxy_request_impl()]] - degree 15, connects to 5 communities
- [[dot-_resolve_text_field()]] - degree 7, connects to 2 communities
- [[dot-_suppress_duplicate_system_notice()]] - degree 4, connects to 1 community
- [[dot-_username_for_bot()]] - degree 4, connects to 1 community
- [[dot-_forward_file_download()]] - degree 3, connects to 1 community
