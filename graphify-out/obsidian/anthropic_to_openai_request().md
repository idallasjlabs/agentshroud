---
source_file: "gateway/proxy/anthropic_openai_translator.py"
type: "code"
community: "Anthropic Openai Translator"
location: "L103"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Anthropic_Openai_Translator
---

# anthropic_to_openai_request()

## Connections
- [[._failover_request()]] - `calls` [EXTRACTED]
- [[._local_secondary_failover_request()]] - `calls` [EXTRACTED]
- [[Translate an Anthropic Messages request body to OpenAI chat completions format.]] - `rationale_for` [EXTRACTED]
- [[_anthropic_content_to_openai()]] - `calls` [EXTRACTED]
- [[_anthropic_system_to_openai()]] - `calls` [EXTRACTED]
- [[_random_msg_id()_1]] - `calls` [EXTRACTED]
- [[anthropic_openai_translator.py]] - `contains` [EXTRACTED]
- [[gemini_to_openai_request()]] - `semantically_similar_to` [INFERRED]
- [[llm_proxy.py]] - `imports` [EXTRACTED]
- [[test_anthropic_openai_translator.py]] - `imports` [EXTRACTED]
- [[test_translator_anthropic_tool_definitions()]] - `calls` [EXTRACTED]
- [[test_translator_basic_text_message()]] - `calls` [EXTRACTED]
- [[test_translator_no_system_prompt()]] - `calls` [EXTRACTED]
- [[test_translator_non_qwen_target_unchanged()]] - `calls` [EXTRACTED]
- [[test_translator_qwen_target_injects_no_think()]] - `calls` [EXTRACTED]
- [[test_translator_qwen_target_no_system_still_gets_no_think()]] - `calls` [EXTRACTED]
- [[test_translator_system_block_list()]] - `calls` [EXTRACTED]
- [[test_translator_tool_result_becomes_tool_role_message()]] - `calls` [EXTRACTED]
- [[test_translator_tool_use_blocks()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Anthropic_Openai_Translator