---
source_file: "gateway/tests/test_anthropic_openai_translator.py"
type: "code"
community: "Anthropic Openai Translator"
location: "L218"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Anthropic_Openai_Translator
---

# _collect_sse()

## Connections
- [[Feed raw SSE bytes into the translator and collect Anthropic events.]] - `rationale_for` [EXTRACTED]
- [[test_anthropic_openai_translator.py]] - `contains` [EXTRACTED]
- [[test_sse_translator_basic_text_stream()]] - `calls` [EXTRACTED]
- [[test_sse_translator_empty_stream_emits_full_sequence()]] - `calls` [EXTRACTED]
- [[test_sse_translator_model_preserved_in_message_start()]] - `calls` [EXTRACTED]
- [[test_sse_translator_stop_reason_propagated()]] - `calls` [EXTRACTED]
- [[test_sse_translator_tool_call_only_starts_at_index_0()]] - `calls` [EXTRACTED]
- [[translate_openai_sse_to_anthropic()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Anthropic_Openai_Translator