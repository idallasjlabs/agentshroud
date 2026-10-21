---
type: community
members: 53
---

# test_telegram_proxy_inbound.py

**Members:** 53 nodes

## Members
- [[dot-process_inbound()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-process_inbound()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-process_inbound()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_bot_command_with_username_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_bot_command_without_username_not_matched()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_caption_entities_supported()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_channel_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_clean_message_passes_through()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_direct_mention_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_empty_bot_username_never_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_encoding_detected_on_getUpdates()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_group_is_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_inbound_text_normalized_before_pipeline()]] - code - gateway/tests/test_telegram_proxy_inbound.py
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
- [[dot-test_owner_message_not_blocked()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_pipeline_not_called_without_text()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_private_is_not_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_prompt_injection_blocked_on_getUpdates()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_supergroup_is_group()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Base64-encoded injection via getUpdates must be caught.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[BlockingPipeline]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[EncodingDetectingPipeline]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[FakePipelineResult]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Media messages use caption + caption_entities.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Normal messages must pass through the pipeline unmodified.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner messages must pass even if the pipeline would block them.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Pipeline that blocks any message containing injection keywords.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Pipeline that detects base64-encoded injections.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Prompt injection via getUpdates must be blocked by the pipeline.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestBotIsMentioned]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestCommandTokenNormalization]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestIsGroupMessage]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Tests for TelegramAPIProxy inbound security pipeline integration. Proves that…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for TelegramAPIProxy._bot_is_mentioned().]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for TelegramAPIProxy._is_group_message().]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unit tests for command token normalization used by local inbound handlers.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Updates without text (e.g. photos) should skip the pipeline.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Zero-width obfuscation should be normalized before pipeline evaluation.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[process_inbound()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[test_telegram_proxy_inbound.py]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_telegram_proxy_inboundpy
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY__wrap_response()]]
- 8 edges to [[_COMMUNITY_asyncio]]
- 7 edges to [[_COMMUNITY_TestInboundPipelineOnGetUpdates]]
- 5 edges to [[_COMMUNITY_dot-_make_proxy()]]
- 2 edges to [[_COMMUNITY_dot-test_stranger_within_limit_triggers_approval_workflow()]]
- 2 edges to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 1 edge to [[_COMMUNITY_TestMultipartOutboundPipeline]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (2)]]
- 1 edge to [[_COMMUNITY_TestMultipartOutboundPipeline (2)]]
- 1 edge to [[_COMMUNITY_TestFullAccessMiddlewareBypass]]
- 1 edge to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_dot-test_unknown_user_always_gets_pending_or_rate_limit_notice()]]

## Top bridge nodes
- [[test_telegram_proxy_inbound.py]] - degree 27, connects to 10 communities
- [[BlockingPipeline]] - degree 10, connects to 3 communities
- [[dot-test_clean_message_passes_through()]] - degree 7, connects to 3 communities
- [[dot-test_encoding_detected_on_getUpdates()]] - degree 7, connects to 3 communities
- [[dot-test_inbound_text_normalized_before_pipeline()]] - degree 7, connects to 3 communities
