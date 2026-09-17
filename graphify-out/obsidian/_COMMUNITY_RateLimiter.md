---
type: community
cohesion: 0.03
members: 81
---

# RateLimiter

**Cohesion:** 0.03 - loosely connected
**Members:** 81 nodes

## Members
- [[.__init__()_43]] - code - gateway/ingest_api/auth.py
- [[.check()]] - code - gateway/ingest_api/auth.py
- [[.test_channel_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_notice_falls_back_without_markdown()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_notice_includes_retry_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_retry_after_seconds_uses_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_group_is_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_missing_chat_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
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
- [[.test_private_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_supergroup_is_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Args             max_requests Maximum requests allowed in the time window]] - rationale - gateway/ingest_api/auth.py
- [[Auth Methods]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Auth dependency that uses the app state config._2]] - rationale - gateway/ingest_api/routes/health.py
- [[Check if client is within rate limit          Args             client_id Usual]] - rationale - gateway/ingest_api/auth.py
- [[Create authentication dependency callable      This is a synchronous wrapper tha]] - rationale - gateway/ingest_api/auth.py
- [[Current Usage]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Factory that returns authentication dependency for FastAPI      This allows us t]] - rationale - gateway/ingest_api/auth.py
- [[GatewayConfig]] - code - gateway/ingest_api/auth.py
- [[If notice send fails, cooldown should not suppress the next retry attempt.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Key Features]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Purpose_3]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Rate-limit notice path should key retry window by user_id, not chat_id.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Rate-limit notice should retry without Markdown when parse-mode send fails.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Rate-limited collaborators should receive a deterministic retry-window notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[RateLimiter]] - code - gateway/ingest_api/auth.py
- [[Related Notes_3]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Repeated rate-limited messages should each receive a deterministic notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Request_5]] - code - gateway/ingest_api/routes/health.py
- [[Security Note]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Simple token-bucket rate limiter      Limits requests per client IP to prevent r]] - rationale - gateway/ingest_api/auth.py
- [[Test auth dependency with invalid auth scheme]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with missing Authorization header]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with valid token]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter allows requests under limit]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter blocks requests over limit]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter cleans up old requests]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter tracks clients separately]] - rationale - gateway/tests/test_auth.py
- [[Test that token verification uses constant-time comparison]] - rationale - gateway/tests/test_auth.py
- [[Test token verification with valid token]] - rationale - gateway/tests/test_auth.py
- [[TestCommandTokenNormalization]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestIsGroupMessage]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for TelegramAPIProxy._is_group_message().]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for command token normalization used by local inbound handlers.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Verify authentication doesn't leak timing information]] - rationale - gateway/tests/test_security.py
- [[Verify token comparison is constant-time]] - rationale - gateway/tests/test_security.py
- [[Verify token using constant-time comparison      Uses hmac.compare_digest to pre]] - rationale - gateway/ingest_api/auth.py
- [[auth.py]] - document - docs/vault/02 - Modules/Gateway Core/auth.py.md
- [[auth_dep()_3]] - code - gateway/ingest_api/routes/health.py
- [[create_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[get_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[python-jose]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[python-jose_1]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[rate_limiter (module-level instance)]] - code - gateway/ingest_api/auth.py
- [[test_auth.py]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_scheme()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_token()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_missing_header()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_valid_token()]] - code - gateway/tests/test_auth.py
- [[test_constant_time_comparison()]] - code - gateway/tests/test_security.py
- [[test_rate_limiter_allows_requests()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_blocks_excess_requests()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_separate_clients()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_window_cleanup()]] - code - gateway/tests/test_auth.py
- [[test_timing_attack_resistance()]] - code - gateway/tests/test_security.py
- [[test_verify_token_constant_time()]] - code - gateway/tests/test_auth.py
- [[test_verify_token_invalid()]] - code - gateway/tests/test_auth.py
- [[test_verify_token_valid()]] - code - gateway/tests/test_auth.py
- [[verify_token()]] - code - gateway/ingest_api/auth.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RateLimiter
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 11 edges to [[_COMMUNITY__wrap_response()]]
- 8 edges to [[_COMMUNITY_SSHProxy]]
- 5 edges to [[_COMMUNITY_AgentTarget]]
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]
- 4 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 3 edges to [[_COMMUNITY_BlockingPipeline]]
- 3 edges to [[_COMMUNITY_TestNoResponseGuarantee]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 2 edges to [[_COMMUNITY_approval.py]]
- 2 edges to [[_COMMUNITY_test_dashboard.py]]
- 2 edges to [[_COMMUNITY_forward.py]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_rbac_config.py]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_TestBotIsMentioned]]
- 1 edge to [[_COMMUNITY_TestFileDownload]]
- 1 edge to [[_COMMUNITY_TestFullAccessMiddlewareBypass]]
- 1 edge to [[_COMMUNITY_TestStrangerRateLimit]]
- 1 edge to [[_COMMUNITY_All Dependencies]]
- 1 edge to [[_COMMUNITY_Error Index]]
- 1 edge to [[_COMMUNITY_auth.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_ModeRequest]]

## Top bridge nodes
- [[RateLimiter]] - degree 47, connects to 16 communities
- [[create_auth_dependency()]] - degree 20, connects to 5 communities
- [[verify_token()]] - degree 13, connects to 4 communities
- [[auth.py]] - degree 10, connects to 4 communities
- [[TestCommandTokenNormalization]] - degree 15, connects to 3 communities