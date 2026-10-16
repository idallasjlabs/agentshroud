---
type: community
cohesion: 0.15
members: 13
---

# Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[dot-test_both_bots_registered_distinct_ids()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_hermes_token_resolves_to_hermes()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_no_token_collision()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_openclaw_token_resolves_to_openclaw()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_registry_rejects_case_variant()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_registry_rejects_empty_string()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_registry_rejects_partial_token()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[dot-test_unknown_token_resolves_to_none()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[Registry maps two distinct tokens to two distinct bot_ids.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistry]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[Token matching must be exact — case-sensitive.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Tokens are the registry keys — no two bots share a token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Validate the token → bot_id registry logic extracted from the route handler.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Upgrade_Report_2026-09-27_dev_PARTIAL_Hermes_creds
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_2]]

## Top bridge nodes
- [[TestTelegramTokenRegistry]] - degree 13, connects to 3 communities
