---
type: community
cohesion: 0.03
members: 84
---

# Authentication & Rate Limiting

**Cohesion:** 0.03 - loosely connected
**Members:** 84 nodes

## Members
- [[.__init__()_5]] - code - gateway/ingest_api/auth.py
- [[.check()]] - code - gateway/ingest_api/auth.py
- [[.process_inbound()_5]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.process_inbound()_6]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.process_inbound()_7]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_bot_command_with_username_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_bot_command_without_username_not_matched()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_caption_entities_supported()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_channel_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_clean_message_passes_through()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_notice_falls_back_without_markdown()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_notice_includes_retry_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_resets_after_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_retry_after_seconds_uses_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_direct_mention_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_empty_bot_username_never_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_encoding_detected_on_getUpdates()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_group_is_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_inbound_text_normalized_before_pipeline()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_mention_case_insensitive()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_mention_different_bot_not_matched()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_missing_chat_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_no_entities_not_matched()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_normalize_command_token_handles_empty_or_non_string()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_normalize_command_token_handles_numeric_input_as_non_command()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_normalize_command_token_handles_uppercase_bot_mention()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_normalize_command_token_keeps_allowed_chars_only()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_normalize_command_token_lowercases_and_preserves_command_shape()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_normalize_command_token_normalizes_fullwidth_and_zero_width()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_normalize_command_token_normalizes_fullwidth_mention_punctuation()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_normalize_command_token_preserves_hyphen_and_underscore()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_normalize_command_token_strips_leading_noise_before_symbol_filter()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_normalize_command_token_strips_mention_and_punctuation()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_owner_message_not_blocked()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_owner_unaffected_by_collaborator_rate_limiter()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_private_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_prompt_injection_blocked_on_getUpdates()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_stranger_exceeding_limit_gets_rate_limit_notice_not_owner_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_stranger_rate_limit_cooldown_suppresses_repeated_notices()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_stranger_rate_limit_notice_includes_reset_time()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_stranger_within_limit_triggers_approval_workflow()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_supergroup_is_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[After the rate-limit window expires, collaborator messages go through normally.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Args             max_requests Maximum requests allowed in the time window]] - rationale - gateway/ingest_api/auth.py
- [[Base64-encoded injection via getUpdates must be caught.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[BlockingPipeline]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Check if client is within rate limit          Args             client_id Usual]] - rationale - gateway/ingest_api/auth.py
- [[EncodingDetectingPipeline]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[FakePipelineResult_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[First message from unknown user (within limit) queues approval flow.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[If notice send fails, cooldown should not suppress the next retry attempt.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Media messages use caption + caption_entities.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Messages within the window are blocked; after the window passes they succeed.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Normal messages must pass through the pipeline unmodified.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Once stranger exhausts rate limit, they get a rate-limit notice; owner is NOT no]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner messages are never rate-limited by the collaborator limiter.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner messages must pass even if the pipeline would block them.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Pipeline that blocks any message containing injection keywords.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Pipeline that detects base64-encoded injections.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Prompt injection via getUpdates must be blocked by the pipeline.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Rate-limit notice path should key retry window by user_id, not chat_id.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Rate-limit notice should retry without Markdown when parse-mode send fails.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Rate-limited collaborators should receive a deterministic retry-window notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[RateLimiter]] - code - gateway/ingest_api/auth.py
- [[Repeated rate-limited messages should each receive a deterministic notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Repeated rate-limited messages within the cooldown window send at most one notic]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Simple token-bucket rate limiter      Limits requests per client IP to prevent r]] - rationale - gateway/ingest_api/auth.py
- [[Stub the fire-and-forget owner activity mirror.      The mirror runs via asyncio]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestBotIsMentioned]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestCollaboratorRateLimitRecovery]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestCommandTokenNormalization]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestIsGroupMessage]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestStrangerRateLimit]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for TelegramAPIProxy._bot_is_mentioned().]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for TelegramAPIProxy._is_group_message().]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for command token normalization used by local inbound handlers.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unknownunapproved users have stricter rate limits than collaborators.      Afte]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Zero-width obfuscation should be normalized before pipeline evaluation.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_no_owner_mirror()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_send_stranger_rate_limit_notice must include a reset time in HHMM UTC format.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[test_telegram_proxy_inbound.py]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Authentication__Rate_Limiting
SORT file.name ASC
```

## Connections to other communities
- 77 edges to [[_COMMUNITY_Telegram Proxy Inbound Tests]]
- 15 edges to [[_COMMUNITY_Module Group 64]]
- 10 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 9 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 7 edges to [[_COMMUNITY_Module Group 61]]
- 5 edges to [[_COMMUNITY_Module Group 69]]
- 3 edges to [[_COMMUNITY_Telegram Inbound Test Rationale]]
- 2 edges to [[_COMMUNITY_Module Group 208]]
- 2 edges to [[_COMMUNITY_Module Group 74]]
- 2 edges to [[_COMMUNITY_Module Group 308]]
- 2 edges to [[_COMMUNITY_Module Group 260]]
- 2 edges to [[_COMMUNITY_Module Group 445]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 60]]
- 1 edge to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 1 edge to [[_COMMUNITY_Progressive Lockdown]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Module Group 217]]
- 1 edge to [[_COMMUNITY_Telegram Outbound Test Coverage]]
- 1 edge to [[_COMMUNITY_Module Group 287]]

## Top bridge nodes
- [[RateLimiter]] - degree 44, connects to 14 communities
- [[test_telegram_proxy_inbound.py]] - degree 26, connects to 11 communities
- [[BlockingPipeline]] - degree 13, connects to 5 communities
- [[TestCommandTokenNormalization]] - degree 15, connects to 2 communities
- [[TestBotIsMentioned]] - degree 13, connects to 2 communities
