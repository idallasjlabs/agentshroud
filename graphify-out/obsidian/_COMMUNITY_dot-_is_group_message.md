---
type: community
members: 9
---

# ._is_group_message

**Members:** 9 nodes

## Members
- [[dot-_is_group_message()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-test_channel_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_group_is_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_missing_chat_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_private_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_supergroup_is_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Return True if message originates from a group or supergroup chat.]] - rationale - gateway/proxy/telegram_proxy.py
- [[TestIsGroupMessage]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for TelegramAPIProxy._is_group_message().]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_is_group_message
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_dot-_make_proxy]]

## Top bridge nodes
- [[TestIsGroupMessage]] - degree 8, connects to 2 communities
- [[dot-_is_group_message()]] - degree 8, connects to 1 community
