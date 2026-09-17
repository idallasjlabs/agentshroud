---
source_file: "gateway/proxy/gemini_openai_translator.py"
type: "code"
community: "test_gemini_openai_translator.py"
location: "L215"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_gemini_openai_translatorpy
---

# gemini_to_openai_response()

## Connections
- [[LLMProxy.proxy_messages]] - `calls` [EXTRACTED]
- [[Translate a Gemini generateContent response to OpenAI chatcompletions     shape]] - `rationale_for` [EXTRACTED]
- [[_parts_to_text()]] - `calls` [EXTRACTED]
- [[gemini_openai_translator.py]] - `contains` [EXTRACTED]
- [[test_gemini_openai_translator.py]] - `imports` [EXTRACTED]
- [[test_gemini_to_openai_response_empty_candidates_yields_empty_text()]] - `calls` [EXTRACTED]
- [[test_gemini_to_openai_response_envelope()]] - `calls` [EXTRACTED]
- [[test_gemini_to_openai_response_max_tokens_finish_reason()]] - `calls` [EXTRACTED]
- [[test_gemini_to_openai_roundtrip_with_openai_to_gemini_response()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_gemini_openai_translatorpy