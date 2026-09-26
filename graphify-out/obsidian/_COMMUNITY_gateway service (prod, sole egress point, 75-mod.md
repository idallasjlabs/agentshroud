---
type: community
cohesion: 0.06
members: 41
---

# gateway service (prod, sole egress point, 75-mod

**Cohesion:** 0.06 - loosely connected
**Members:** 41 nodes

## Members
- [[._allowed_networks()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[._mock_app_state_with_registry()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[._mock_request()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_both_bots_registered_distinct_ids()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_client_disconnect_returns_499()]] - code - gateway/tests/test_security_fixes.py
- [[.test_empty_registry_fails_closed()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_hermes_token_resolves_to_hermes()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_miss_debounced_within_rebuild_interval()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_miss_rebuilds_and_recovers_when_secret_becomes_available()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_miss_still_rejected_after_rebuild_if_truly_unknown()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_no_token_collision()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_openclaw_token_resolves_to_openclaw()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_registry_rejects_case_variant()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_registry_rejects_empty_string()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_registry_rejects_partial_token()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_unknown_token_rejected()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_unknown_token_resolves_to_none()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_valid_hermes_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_valid_openclaw_token_accepted()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[A genuinely-unregistered token must not be falsely accepted by the         rebui]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the Hermes token resolves to 'hermes' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A request bearing the OpenClaw token resolves to 'openclaw' bot_id.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[A token missing from a stale cached registry is picked up on retry         once]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[An unregistered token must not be matched — fail-closed.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Build the Telegram bot-token → bot_id registry from configured secrets.]] - rationale - gateway/ingest_api/main.py
- [[If no tokens are registered, any token must be rejected.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Integration tests for the telegram-api{path} route with multi-bot registry.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Proxy Telegram Bot API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Registry maps two distinct tokens to two distinct bot_ids.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Repeated misses within the debounce window must not re-read secrets         on e]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramProxyRouteMultiBot]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistry]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[TestTelegramTokenRegistryRebuildOnMiss]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[The token registry is built lazily on the first telegram-api{path} request]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Token matching must be exact — case-sensitive.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Tokens are the registry keys — no two bots share a token.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Validate the token → bot_id registry logic extracted from the route handler.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[When body() raises ClientDisconnect the handler returns 499 without crashing.]] - rationale - gateway/tests/test_security_fixes.py
- [[_build_telegram_token_registry()]] - code - gateway/ingest_api/main.py
- [[telegram_api_proxy()]] - code - gateway/ingest_api/main.py
- [[test_telegram_proxy_multibot.py]] - code - gateway/tests/test_telegram_proxy_multibot.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/gateway_service_prod_sole_egress_point_75-mod
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_ModeRequest]]
- 4 edges to [[_COMMUNITY_SSHProxy]]
- 4 edges to [[_COMMUNITY_FileSandbox]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_StdioConnection]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Policy - Final Decision]]

## Top bridge nodes
- [[telegram_api_proxy()]] - degree 15, connects to 4 communities
- [[test_telegram_proxy_multibot.py]] - degree 9, connects to 4 communities
- [[TestTelegramTokenRegistry]] - degree 13, connects to 2 communities
- [[TestTelegramTokenRegistryRebuildOnMiss]] - degree 10, connects to 2 communities
- [[TestTelegramProxyRouteMultiBot]] - degree 9, connects to 2 communities