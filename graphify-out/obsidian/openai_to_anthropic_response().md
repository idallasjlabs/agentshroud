---
source_file: "gateway/proxy/anthropic_openai_translator.py"
type: "code"
community: "Gateway Test Suite"
location: "L344"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# openai_to_anthropic_response()

## Connections
- [[._failover_request()]] - `calls` [EXTRACTED]
- [[LLMProxy._failover_request()]] - `calls` [EXTRACTED]
- [[Translate an Ollama OpenAI-compat response to Anthropic Messages API format.]] - `rationale_for` [EXTRACTED]
- [[_random_msg_id()_1]] - `calls` [EXTRACTED]
- [[anthropic_openai_translator.py]] - `contains` [EXTRACTED]
- [[llm_proxy.py]] - `imports` [EXTRACTED]
- [[openai_to_gemini_response()]] - `semantically_similar_to` [INFERRED]
- [[test_anthropic_openai_translator.py]] - `imports` [EXTRACTED]
- [[test_translator_empty_choices_yields_nonempty_content()]] - `calls` [EXTRACTED]
- [[test_translator_empty_string_content_yields_nonempty_content()]] - `calls` [EXTRACTED]
- [[test_translator_max_tokens_finish_reason()]] - `calls` [EXTRACTED]
- [[test_translator_null_content_no_tool_calls_yields_nonempty_content()]] - `calls` [EXTRACTED]
- [[test_translator_openai_to_anthropic_basic()]] - `calls` [EXTRACTED]
- [[test_translator_preserves_original_model()]] - `calls` [EXTRACTED]
- [[test_translator_tool_calls_to_tool_use()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite