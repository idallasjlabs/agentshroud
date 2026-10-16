---
type: community
cohesion: 0.13
members: 25
---

# test_anthropic_openai_translator.py

**Cohesion:** 0.13 - loosely connected
**Members:** 25 nodes

## Members
- [[Failover reply with choices (e.g. rate-limit stub) must not return content]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Failover reply with empty-string content must not return content.]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Failover reply with null content and no tool_calls must not return content.]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Failover to a qwen-family model must disable thinking mode Qwen3's     think]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Translate an Anthropic Messages request body to OpenAI chat completions format.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Translate an Ollama OpenAI-compat response to Anthropic Messages API format.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[anthropic_to_openai_request()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[openai_to_anthropic_response()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[test_anthropic_openai_translator.py]] - code - gateway/tests/test_anthropic_openai_translator.py
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
TABLE source_file, type FROM #community/test_anthropic_openai_translatorpy
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_anthropic_openai_translator.py_2]]
- 6 edges to [[_COMMUNITY_test_anthropic_openai_translator.py_1]]
- 1 edge to [[_COMMUNITY_test_gemini_openai_translator.py_2]]
- 1 edge to [[_COMMUNITY_test_gemini_openai_translator.py]]

## Top bridge nodes
- [[anthropic_to_openai_request()]] - degree 16, connects to 2 communities
- [[openai_to_anthropic_response()]] - degree 12, connects to 2 communities
- [[test_anthropic_openai_translator.py]] - degree 25, connects to 1 community
