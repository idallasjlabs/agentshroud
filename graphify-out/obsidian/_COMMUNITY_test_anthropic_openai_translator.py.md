---
type: community
members: 62
---

# test_anthropic_openai_translator.py

**Members:** 62 nodes

## Members
- [[Anthropic v1messages response → OpenAI v1chatcompletions envelope.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Anthropic Messages API ↔ Ollama OpenAI-compat translator. Pure functions — no…]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Claude-model-via-OpenAI-path translation. Hermes v0.16.0 routes Claude calls…]] - rationale - gateway/tests/test_claude_via_openai_path.py
- [[Convert an Anthropic message content field to OpenAI format.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Failover reply with choices (e.g. rate-limit stub) must not return…]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Failover reply with empty-string content must not return content.]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Failover reply with null content and no tool_calls must not return content.]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Failover to a qwen-family model must disable thinking mode Qwen3's think…]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Feed raw SSE bytes into the translator and collect Anthropic events.]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Flatten Anthropic system prompt (string or content-block list) to plain text.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[LLM API Reverse Proxy — intercepts all OpenClaw ↔ (AnthropicOpenAIGoogle)…]] - rationale - gateway/proxy/llm_proxy.py
- [[OpenAI-compat SSE stream → Anthropic SSE stream translator. Consumes an async…]] - rationale - gateway/proxy/anthropic_openai_sse_translator.py
- [[Tests for gatewayproxyanthropic_openai_translator.py and…]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[The combined path v1chatcompletions with model=claude- must end up POSTing…]] - rationale - gateway/tests/test_claude_via_openai_path.py
- [[Tool-call-only SSE stream must produce tool_use at index 0 (no text gap).]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Translate an Anthropic Messages request body to OpenAI chat completions format.…]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Translate an Ollama OpenAI-compat response to Anthropic Messages API format.…]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Translate an OpenAI v1chatcompletions request body to Anthropic…]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Translate an OpenAI-compat SSE byte stream to Anthropic SSE byte events. Yields…]] - rationale - gateway/proxy/anthropic_openai_sse_translator.py
- [[_anthropic_content_to_openai()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[_anthropic_system_to_openai()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[_collect_sse()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[_random_msg_id()]] - code - gateway/proxy/anthropic_openai_sse_translator.py
- [[_random_msg_id()_1]] - code - gateway/proxy/anthropic_openai_translator.py
- [[_sse()]] - code - gateway/proxy/anthropic_openai_sse_translator.py
- [[anthropic_openai_sse_translator.py]] - code - gateway/proxy/anthropic_openai_sse_translator.py
- [[anthropic_openai_translator.py]] - code - gateway/proxy/anthropic_openai_translator.py
- [[anthropic_to_openai_request()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[anthropic_to_openai_response()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[asyncio_18]] - code
- [[fake_open()]] - code - gateway/tests/test_claude_via_openai_path.py
- [[llm_proxy.py]] - code - gateway/proxy/llm_proxy.py
- [[mock_forward()]] - code - gateway/tests/test_claude_via_openai_path.py
- [[openai_to_anthropic_request()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[openai_to_anthropic_response()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[test_anthropic_openai_translator.py]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_anthropic_to_openai_response_envelope()]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_claude_via_openai_path.py]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_openai_to_anthropic_request_strips_system_role()]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_proxy_rewrites_claude_via_openai_path()]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_sse_translator_basic_text_stream()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_sse_translator_empty_stream_emits_full_sequence()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_sse_translator_model_preserved_in_message_start()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_sse_translator_stop_reason_propagated()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_sse_translator_tool_call_only_starts_at_index_0()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_anthropic_tool_definitions()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_basic_text_message()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_empty_choices_yields_nonempty_content()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_empty_string_content_yields_nonempty_content()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_max_tokens_finish_reason()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_no_system_prompt()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_non_qwen_target_unchanged()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_null_content_no_tool_calls_yields_nonempty_content()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_openai_to_anthropic_basic()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_preserves_original_model()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_qwen_target_injects_no_think()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_qwen_target_no_system_still_gets_no_think()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_system_block_list()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_tool_calls_to_tool_use()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_tool_result_becomes_tool_role_message()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_translator_tool_use_blocks()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[translate_openai_sse_to_anthropic()]] - code - gateway/proxy/anthropic_openai_sse_translator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_anthropic_openai_translatorpy
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_LLMProxy]]
- 6 edges to [[_COMMUNITY_test_gemini_openai_translator.py]]
- 4 edges to [[_COMMUNITY_is_quota_exhausted]]
- 2 edges to [[_COMMUNITY_main.rs]]
- 1 edge to [[_COMMUNITY_StreamHead]]
- 1 edge to [[_COMMUNITY_email_send]]
- 1 edge to [[_COMMUNITY_is_overloaded]]
- 1 edge to [[_COMMUNITY_dot-_suppress_qwen3_thinking]]
- 1 edge to [[_COMMUNITY_test_proxy_gemini_translation_failure_falls_through_gracefully]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_failover.py]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]

## Top bridge nodes
- [[llm_proxy.py]] - degree 27, connects to 9 communities
- [[anthropic_to_openai_request()]] - degree 19, connects to 1 community
- [[openai_to_anthropic_response()]] - degree 13, connects to 1 community
- [[anthropic_openai_translator.py]] - degree 12, connects to 1 community
- [[_collect_sse()]] - degree 9, connects to 1 community
