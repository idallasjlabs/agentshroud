---
source_file: "gateway/tests/test_anthropic_openai_translator.py"
type: "code"
community: "Gateway Test Suite"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# test_anthropic_openai_translator.py

## Connections
- [[_collect_sse()]] - `contains` [EXTRACTED]
- [[anthropic_to_openai_request()]] - `imports` [EXTRACTED]
- [[openai_to_anthropic_response()]] - `imports` [EXTRACTED]
- [[test_sse_translator_basic_text_stream()]] - `contains` [EXTRACTED]
- [[test_sse_translator_empty_stream_emits_full_sequence()]] - `contains` [EXTRACTED]
- [[test_sse_translator_model_preserved_in_message_start()]] - `contains` [EXTRACTED]
- [[test_sse_translator_stop_reason_propagated()]] - `contains` [EXTRACTED]
- [[test_sse_translator_tool_call_only_starts_at_index_0()]] - `contains` [EXTRACTED]
- [[test_translator_anthropic_tool_definitions()]] - `contains` [EXTRACTED]
- [[test_translator_basic_text_message()]] - `contains` [EXTRACTED]
- [[test_translator_empty_choices_yields_nonempty_content()]] - `contains` [EXTRACTED]
- [[test_translator_empty_string_content_yields_nonempty_content()]] - `contains` [EXTRACTED]
- [[test_translator_max_tokens_finish_reason()]] - `contains` [EXTRACTED]
- [[test_translator_no_system_prompt()]] - `contains` [EXTRACTED]
- [[test_translator_non_qwen_target_unchanged()]] - `contains` [EXTRACTED]
- [[test_translator_null_content_no_tool_calls_yields_nonempty_content()]] - `contains` [EXTRACTED]
- [[test_translator_openai_to_anthropic_basic()]] - `contains` [EXTRACTED]
- [[test_translator_preserves_original_model()]] - `contains` [EXTRACTED]
- [[test_translator_qwen_target_injects_no_think()]] - `contains` [EXTRACTED]
- [[test_translator_qwen_target_no_system_still_gets_no_think()]] - `contains` [EXTRACTED]
- [[test_translator_system_block_list()]] - `contains` [EXTRACTED]
- [[test_translator_tool_calls_to_tool_use()]] - `contains` [EXTRACTED]
- [[test_translator_tool_result_becomes_tool_role_message()]] - `contains` [EXTRACTED]
- [[test_translator_tool_use_blocks()]] - `contains` [EXTRACTED]
- [[translate_openai_sse_to_anthropic()]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite