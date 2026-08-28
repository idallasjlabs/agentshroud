---
source_file: "gateway/tests/test_llm_quota_detector.py"
type: "code"
community: "Community 310"
location: "L178"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_310
---

# TestOverloadedMultiProvider

## Connections
- [[.test_anthropic_api_error_500_not_flagged()]] - `method` [EXTRACTED]
- [[.test_anthropic_detection_unchanged()]] - `method` [EXTRACTED]
- [[.test_gemini_invalid_argument_not_flagged()]] - `method` [EXTRACTED]
- [[.test_gemini_resource_exhausted_stays_quota_territory()]] - `method` [EXTRACTED]
- [[.test_gemini_unavailable_503()]] - `method` [EXTRACTED]
- [[.test_gemini_unavailable_http_200()]] - `method` [EXTRACTED]
- [[.test_non_dict_json_body_not_flagged()]] - `method` [EXTRACTED]
- [[.test_openai_invalid_request_not_flagged()]] - `method` [EXTRACTED]
- [[.test_openai_overloaded_message_http_200()]] - `method` [EXTRACTED]
- [[.test_openai_server_error_500_requires_capacity_wording()]] - `method` [EXTRACTED]
- [[.test_openai_server_error_503()]] - `method` [EXTRACTED]
- [[.test_openai_server_error_503_without_capacity_wording()]] - `method` [EXTRACTED]
- [[.test_overloaded_word_in_chat_content_not_flagged()]] - `method` [EXTRACTED]
- [[.test_unrecognized_error_shape_not_flagged()]] - `method` [EXTRACTED]
- [[SCRUM-60 in-body overload envelopes from OpenAI and Gemini must fail     over e]] - `rationale_for` [EXTRACTED]
- [[test_llm_quota_detector.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_310