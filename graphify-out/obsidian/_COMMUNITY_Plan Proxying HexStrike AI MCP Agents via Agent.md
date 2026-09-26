---
type: community
cohesion: 0.18
members: 11
---

# Plan: Proxying HexStrike AI MCP Agents via Agent

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[.test_bot_command_with_username_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_bot_command_without_username_not_matched()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_caption_entities_supported()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_direct_mention_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_empty_bot_username_never_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_mention_case_insensitive()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_mention_different_bot_not_matched()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_no_entities_not_matched()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Media messages use caption + caption_entities.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestBotIsMentioned]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for TelegramAPIProxy._bot_is_mentioned().]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Plan_Proxying_HexStrike_AI_MCP_Agents_via_Agent
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_a2a_proxy.py]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY_test_soc_bots.py]]

## Top bridge nodes
- [[TestBotIsMentioned]] - degree 13, connects to 4 communities