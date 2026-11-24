---
type: community
members: 13
---

# ._bot_is_mentioned

**Members:** 13 nodes

## Members
- [[dot-_bot_is_mentioned()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-test_bot_command_with_username_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_bot_command_without_username_not_matched()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_caption_entities_supported()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_direct_mention_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_empty_bot_username_never_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_mention_case_insensitive()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_mention_different_bot_not_matched()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_no_entities_not_matched()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Media messages use caption + caption_entities.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Return True if the bot is @mentioned or a bot_command targets this bot. Checks…]] - rationale - gateway/proxy/telegram_proxy.py
- [[TestBotIsMentioned]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for TelegramAPIProxy._bot_is_mentioned().]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_bot_is_mentioned
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_dot-_make_proxy]]

## Top bridge nodes
- [[TestBotIsMentioned]] - degree 11, connects to 2 communities
- [[dot-_bot_is_mentioned()]] - degree 11, connects to 1 community
