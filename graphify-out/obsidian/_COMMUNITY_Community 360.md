---
type: community
members: 56
---

# Community 360

**Members:** 56 nodes

## Members
- [[Anthropic v1messages response → OpenAI v1chatcompletions envelope.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Convert an Anthropic message content field to OpenAI format.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Failover reply with choices (e.g. rate-limit stub) must not return content]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Failover reply with empty-string content must not return content.]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Failover reply with null content and no tool_calls must not return content.]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Failover to a qwen-family model must disable thinking mode Qwen3's     think]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Feed raw SSE bytes into the translator and collect Anthropic events.]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Flatten Anthropic system prompt (string or content-block list) to plain text.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Hermes v0.16.0 OpenAI-Client Compatibility Incident (3-day cron outage)]] - rationale - gateway/tests/test_chat_completions_alias.py
- [[Regression don't break the existing v1messages path.]] - rationale - gateway/tests/test_chat_completions_alias.py
- [[The combined path v1chatcompletions with model=claude- must     end up POST]] - rationale - gateway/tests/test_claude_via_openai_path.py
- [[Tool-call-only SSE stream must produce tool_use at index 0 (no text gap).]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Translate an Anthropic Messages request body to OpenAI chat completions format.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Translate an Ollama OpenAI-compat response to Anthropic Messages API format.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Translate an OpenAI v1chatcompletions request body to Anthropic v1messages.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[_anthropic_content_to_openai()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[_anthropic_system_to_openai()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[_collect_sse()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[_random_msg_id()_1]] - code - gateway/proxy/anthropic_openai_translator.py
- [[anthropic_openai_translator.py]] - code - gateway/proxy/anthropic_openai_translator.py
- [[anthropic_to_openai_request()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[anthropic_to_openai_response()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[client()_3]] - code - gateway/tests/test_chat_completions_alias.py
- [[openai_to_anthropic_request()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[openai_to_anthropic_response()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[test_anthropic_openai_translator.py]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_anthropic_to_openai_response_envelope()]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_chat_completions_alias.py]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_chat_completions_alias_passes_correct_path_to_proxy()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_chat_completions_alias_routes_to_v1_path()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_claude_via_openai_path.py]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_get_chat_completions_alias_also_routes()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_openai_to_anthropic_request_strips_system_role()]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_proxy_rewrites_claude_via_openai_path()]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_root_v1_messages_still_works_unchanged()]] - code - gateway/tests/test_chat_completions_alias.py
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

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_360
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 361]]
- 5 edges to [[_COMMUNITY_Community 1787]]
- 3 edges to [[_COMMUNITY_Community 1278]]
- 1 edge to [[_COMMUNITY_Community 39]]
- 1 edge to [[_COMMUNITY_Community 1127]]

## Top bridge nodes
- [[anthropic_to_openai_request()]] - degree 19, connects to 2 communities
- [[openai_to_anthropic_response()]] - degree 14, connects to 2 communities
- [[anthropic_to_openai_response()]] - degree 7, connects to 2 communities
- [[openai_to_anthropic_request()]] - degree 6, connects to 2 communities
- [[test_anthropic_openai_translator.py]] - degree 25, connects to 1 community