---
source_file: "gateway/tests/test_gemini_via_openai_path.py"
type: "code"
community: "test_proxy_gemini_translation_failure_falls_through_gracefully"
location: "L105"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_proxy_gemini_translation_failure_falls_through_gracefully
---

# test_proxy_gemini_translation_failure_falls_through_gracefully()

## Connections
- [[If openai_to_gemini_request raises, the request must still be forwarded…]] - `rationale_for` [EXTRACTED]
- [[LLMProxy]] - `uses` [INFERRED]
- [[_broken_translator()]] - `indirect_call` [INFERRED]
- [[asyncio_25]] - `references` [EXTRACTED]
- [[mock_forward()_16]] - `contains` [EXTRACTED]
- [[mock_forward()_17]] - `indirect_call` [INFERRED]
- [[test_gemini_via_openai_path.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_proxy_gemini_translation_failure_falls_through_gracefully
