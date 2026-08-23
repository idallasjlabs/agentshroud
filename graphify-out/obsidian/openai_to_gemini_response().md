---
source_file: "gateway/proxy/gemini_openai_translator.py"
type: "code"
community: "Gemini Openai Translator"
location: "L252"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gemini_Openai_Translator
---

# openai_to_gemini_response()

## Connections
- [[._failover_request()]] - `calls` [EXTRACTED]
- [[Translate an Ollama OpenAI-compat response to Gemini candidates format.      The]] - `rationale_for` [EXTRACTED]
- [[gemini_openai_translator.py]] - `contains` [EXTRACTED]
- [[llm_proxy.py]] - `imports` [EXTRACTED]
- [[openai_to_anthropic_response()]] - `semantically_similar_to` [INFERRED]
- [[test_gemini_openai_translator.py]] - `imports` [EXTRACTED]
- [[test_gemini_to_openai_roundtrip_with_openai_to_gemini_response()]] - `calls` [EXTRACTED]
- [[test_openai_response_empty_choices_yields_empty_text()]] - `calls` [EXTRACTED]
- [[test_openai_response_length_maps_to_max_tokens()]] - `calls` [EXTRACTED]
- [[test_openai_response_to_gemini_candidates()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gemini_Openai_Translator