---
source_file: "gateway/proxy/gemini_openai_translator.py"
type: "code"
community: "test_gemini_openai_translator.py"
location: "L252"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_gemini_openai_translatorpy
---

# openai_to_gemini_response()

## Connections
- [[LLMProxy._failover_request]] - `calls` [EXTRACTED]
- [[Translate an Ollama OpenAI-compat response to Gemini candidates format.      The]] - `rationale_for` [EXTRACTED]
- [[gemini_openai_translator.py]] - `contains` [EXTRACTED]
- [[openai_to_anthropic_response()]] - `semantically_similar_to` [INFERRED]
- [[test_gemini_openai_translator.py]] - `imports` [EXTRACTED]
- [[test_gemini_to_openai_roundtrip_with_openai_to_gemini_response()]] - `calls` [EXTRACTED]
- [[test_openai_response_empty_choices_yields_empty_text()]] - `calls` [EXTRACTED]
- [[test_openai_response_length_maps_to_max_tokens()]] - `calls` [EXTRACTED]
- [[test_openai_response_to_gemini_candidates()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_gemini_openai_translatorpy