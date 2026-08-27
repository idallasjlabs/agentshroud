---
type: community
members: 20
---

# Community 445

**Members:** 20 nodes

## Members
- [[._make_proxy()_4]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_active_bot_id_falls_back_to_openclaw()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_active_bot_id_returns_contextvar_when_set()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_active_send_token_returns_contextvar_inside_request()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_active_send_token_returns_default_outside_request()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_proxy_request_contextvar_visible_inside_impl()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_proxy_request_resets_contextvar_after_return()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_send_telegram_text_falls_back_to_default_token()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_send_telegram_text_uses_inbound_token()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[After proxy_request returns, _inbound_bot_token is reset to its prior value.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Cross-bot reply misrouting fix via contextvar-scoped send token]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Outside a proxy_request call, _active_bot_id() returns 'openclaw'.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Outside a proxy_request call, _active_send_token() returns self._bot_token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestMultiBotContextvarRouting]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[Tests for per-request bot token routing via contextvars.      Regression suite f]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[The contextvar set by proxy_request is visible throughout _proxy_request_impl.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[When _inbound_bot_id is set, _active_bot_id() returns it.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[When _inbound_bot_token is set, _active_send_token() returns it.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Without contextvar, _send_telegram_text uses self._bot_token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[_send_telegram_text uses the inbound contextvar token, not self._bot_token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_445
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 273]]
- 1 edge to [[_COMMUNITY_Community 4]]

## Top bridge nodes
- [[TestMultiBotContextvarRouting]] - degree 14, connects to 2 communities