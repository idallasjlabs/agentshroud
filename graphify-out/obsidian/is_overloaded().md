---
source_file: "gateway/proxy/llm_quota_detector.py"
type: "code"
community: "Planning Docs"
location: "L153"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Planning_Docs
---

# is_overloaded()

## Connections
- [[.proxy_messages()]] - `calls` [EXTRACTED]
- [[.test_anthropic_api_error_500_not_flagged()]] - `calls` [EXTRACTED]
- [[.test_anthropic_detection_unchanged()]] - `calls` [EXTRACTED]
- [[.test_empty_and_garbage_bodies()]] - `calls` [EXTRACTED]
- [[.test_gemini_invalid_argument_not_flagged()]] - `calls` [EXTRACTED]
- [[.test_gemini_resource_exhausted_stays_quota_territory()]] - `calls` [EXTRACTED]
- [[.test_gemini_unavailable_503()]] - `calls` [EXTRACTED]
- [[.test_gemini_unavailable_http_200()]] - `calls` [EXTRACTED]
- [[.test_http_200_with_overloaded_body()]] - `calls` [EXTRACTED]
- [[.test_http_503_with_overloaded_body()]] - `calls` [EXTRACTED]
- [[.test_http_529_with_overloaded_body()]] - `calls` [EXTRACTED]
- [[.test_mention_in_content_not_flagged()]] - `calls` [EXTRACTED]
- [[.test_non_dict_json_body_not_flagged()]] - `calls` [EXTRACTED]
- [[.test_normal_200_message_body_not_flagged()]] - `calls` [EXTRACTED]
- [[.test_openai_invalid_request_not_flagged()]] - `calls` [EXTRACTED]
- [[.test_openai_overloaded_message_http_200()]] - `calls` [EXTRACTED]
- [[.test_openai_server_error_500_requires_capacity_wording()]] - `calls` [EXTRACTED]
- [[.test_openai_server_error_503()]] - `calls` [EXTRACTED]
- [[.test_openai_server_error_503_without_capacity_wording()]] - `calls` [EXTRACTED]
- [[.test_other_error_types_not_flagged()]] - `calls` [EXTRACTED]
- [[.test_overloaded_word_in_chat_content_not_flagged()]] - `calls` [EXTRACTED]
- [[.test_quota_statuses_not_claimed()]] - `calls` [EXTRACTED]
- [[.test_unrecognized_error_shape_not_flagged()]] - `calls` [EXTRACTED]
- [[Return (True, provider_overloaded) for a provider capacity-error     envelop]] - `rationale_for` [EXTRACTED]
- [[llm_proxy.py]] - `imports` [EXTRACTED]
- [[llm_quota_detector.py]] - `contains` [EXTRACTED]
- [[test_llm_quota_detector.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Planning_Docs