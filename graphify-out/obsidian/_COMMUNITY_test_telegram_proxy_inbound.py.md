---
type: community
members: 55
---

# test_telegram_proxy_inbound.py

**Members:** 55 nodes

## Members
- [[dot-_bot_is_mentioned()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_is_group_message()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_normalize_command_token()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-test_bot_command_with_username_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_bot_command_without_username_not_matched()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_caption_entities_supported()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_channel_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_direct_mention_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_empty_bot_username_never_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_group_is_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_mention_case_insensitive()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_mention_different_bot_not_matched()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_missing_chat_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_no_entities_not_matched()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_normalize_command_token_handles_empty_or_non_string()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_normalize_command_token_handles_numeric_input_as_non_command()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_normalize_command_token_handles_uppercase_bot_mention()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_normalize_command_token_keeps_allowed_chars_only()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_normalize_command_token_lowercases_and_preserves_command_shape()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_normalize_command_token_normalizes_fullwidth_and_zero_width()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_normalize_command_token_normalizes_fullwidth_mention_punctuation()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_normalize_command_token_preserves_hyphen_and_underscore()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_normalize_command_token_strips_leading_noise_before_symbol_filter()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_normalize_command_token_strips_mention_and_punctuation()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_private_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_supergroup_is_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[After the rate-limit window expires, collaborator messages go through normally.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Every collaborator message must produce a response — never a silent drop.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Fail any real urlopen fast unless a test installs its own fake. Blocked-message…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Media messages use caption + caption_entities.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Normalize first command token so small obfuscations don't bypass local handlers.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True if message originates from a group or supergroup chat.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True if the bot is @mentioned or a bot_command targets this bot. Checks…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Stub the fire-and-forget owner activity mirror. The mirror runs via…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestBotIsMentioned]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestCollaboratorRateLimitRecovery]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestCommandTokenNormalization]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestFileDownload]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestFullAccessMiddlewareBypass]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestIsGroupMessage]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestNoResponseGuarantee]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestStrangerRateLimit]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Tests for TelegramAPIProxy inbound security pipeline integration. Proves that…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Tests for _forward_file_download() and proxy_request() binary path. Regression…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for TelegramAPIProxy._bot_is_mentioned().]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for TelegramAPIProxy._is_group_message().]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for command token normalization used by local inbound handlers.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unknownunapproved users have stricter rate limits than collaborators. After…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_no_owner_mirror()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_no_real_telegram_network()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_noop()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_refuse()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fixture_31]] - code
- [[full_access collaborators must pass through middleware and secondary pipeline…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[test_telegram_proxy_inbound.py]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_telegram_proxy_inboundpy
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 9 edges to [[_COMMUNITY_dot-_make_proxy]]
- 9 edges to [[_COMMUNITY_asyncio_7]]
- 5 edges to [[_COMMUNITY_FakeRBAC]]
- 3 edges to [[_COMMUNITY_dot-test_collaborator_rate_limit_resets_after_window]]
- 3 edges to [[_COMMUNITY__wrap_response]]
- 3 edges to [[_COMMUNITY_dot-test_full_access_collaborator_passes_despite_multi_turn_middleware_block_without_interrogative]]
- 3 edges to [[_COMMUNITY_BlockingPipeline]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_fastapi]]
- 1 edge to [[_COMMUNITY_test_soc_services_coverage.py]]
- 1 edge to [[_COMMUNITY_fake_owner_notice]]
- 1 edge to [[_COMMUNITY_dot-test_stranger_rate_limit_notice_includes_reset_time]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[test_telegram_proxy_inbound.py]] - degree 32, connects to 11 communities
- [[TestFullAccessMiddlewareBypass]] - degree 12, connects to 5 communities
- [[TestFileDownload]] - degree 10, connects to 4 communities
- [[TestStrangerRateLimit]] - degree 7, connects to 4 communities
- [[TestCollaboratorRateLimitRecovery]] - degree 6, connects to 4 communities
