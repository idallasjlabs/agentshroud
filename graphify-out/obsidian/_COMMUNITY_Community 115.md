---
type: community
cohesion: 0.04
members: 50
---

# Community 115

**Cohesion:** 0.04 - loosely connected
**Members:** 50 nodes

## Members
- [[.__init__()_10]] - code - gateway/ingest_api/auth.py
- [[.check()]] - code - gateway/ingest_api/auth.py
- [[.test_channel_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_always_gets_response_for_generic_message()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_blocked_command_always_gets_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_notice_falls_back_without_markdown()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_notice_includes_retry_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_rate_limit_resets_after_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
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
- [[.test_owner_unaffected_by_collaborator_rate_limiter()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_private_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_supergroup_is_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_unknown_user_always_gets_pending_or_rate_limit_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[A blocked slash command must always produce a protected notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[After the rate-limit window expires, collaborator messages go through normally.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Args             max_requests Maximum requests allowed in the time window]] - rationale - gateway/ingest_api/auth.py
- [[Check if client is within rate limit          Args             client_id Usual]] - rationale - gateway/ingest_api/auth.py
- [[Even a generic message triggers _send_collaborator_safe_info_response (local_inf]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Every collaborator message must produce a response — never a silent drop.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[If notice send fails, cooldown should not suppress the next retry attempt.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Messages within the window are blocked; after the window passes they succeed.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner messages are never rate-limited by the collaborator limiter.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Rate-limit notice path should key retry window by user_id, not chat_id.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Rate-limit notice should retry without Markdown when parse-mode send fails.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Rate-limited collaborators should receive a deterministic retry-window notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[RateLimiter]] - code - gateway/ingest_api/auth.py
- [[Repeated rate-limited messages should each receive a deterministic notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Simple token-bucket rate limiter      Limits requests per client IP to prevent r]] - rationale - gateway/ingest_api/auth.py
- [[TestCollaboratorRateLimitRecovery]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestCommandTokenNormalization]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestIsGroupMessage]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestNoResponseGuarantee]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for TelegramAPIProxy._is_group_message().]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for command token normalization used by local inbound handlers.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unknown users must always receive either a pending notice or a rate-limit notice]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_115
SORT file.name ASC
```

## Connections to other communities
- 49 edges to [[_COMMUNITY_Telegram Proxy Inbound]]
- 18 edges to [[_COMMUNITY_Community 31]]
- 8 edges to [[_COMMUNITY_Ingest API & Approval Routes]]
- 5 edges to [[_COMMUNITY_Adversarial Injection Guards]]
- 4 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 3 edges to [[_COMMUNITY_Community 509]]
- 2 edges to [[_COMMUNITY_Community 70]]
- 2 edges to [[_COMMUNITY_Config Validation & Router]]
- 2 edges to [[_COMMUNITY_Community 38]]
- 1 edge to [[_COMMUNITY_Community 43]]
- 1 edge to [[_COMMUNITY_Community 49]]
- 1 edge to [[_COMMUNITY_Community 60]]
- 1 edge to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 815]]
- 1 edge to [[_COMMUNITY_Community 546]]
- 1 edge to [[_COMMUNITY_Community 510]]
- 1 edge to [[_COMMUNITY_Community 871]]

## Top bridge nodes
- [[RateLimiter]] - degree 47, connects to 16 communities
- [[TestCommandTokenNormalization]] - degree 15, connects to 3 communities
- [[TestIsGroupMessage]] - degree 10, connects to 3 communities
- [[TestNoResponseGuarantee]] - degree 9, connects to 3 communities
- [[TestCollaboratorRateLimitRecovery]] - degree 7, connects to 3 communities