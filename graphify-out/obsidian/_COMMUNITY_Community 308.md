---
type: community
members: 27
---

# Community 308

**Members:** 27 nodes

## Members
- [[.test_anthropic_api_error_500_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_anthropic_detection_unchanged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_empty_and_garbage_bodies()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_gemini_invalid_argument_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_gemini_resource_exhausted_stays_quota_territory()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_gemini_unavailable_503()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_gemini_unavailable_http_200()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_http_200_with_overloaded_body()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_http_503_with_overloaded_body()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_http_529_with_overloaded_body()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_mention_in_content_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_non_dict_json_body_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_normal_200_message_body_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_openai_invalid_request_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_openai_overloaded_message_http_200()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_openai_server_error_500_requires_capacity_wording()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_openai_server_error_503()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_openai_server_error_503_without_capacity_wording()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_other_error_types_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_overloaded_word_in_chat_content_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_quota_statuses_not_claimed()]] - code - gateway/tests/test_llm_quota_detector.py
- [[.test_unrecognized_error_shape_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[Return (True, provider_overloaded) for a provider capacity-error     envelop]] - rationale - gateway/proxy/llm_quota_detector.py
- [[SCRUM-60 in-body overload envelopes from OpenAI and Gemini must fail     over e]] - rationale - gateway/tests/test_llm_quota_detector.py
- [[TestIsOverloaded]] - code - gateway/tests/test_llm_quota_detector.py
- [[TestOverloadedMultiProvider]] - code - gateway/tests/test_llm_quota_detector.py
- [[is_overloaded()]] - code - gateway/proxy/llm_quota_detector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_308
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 419]]
- 1 edge to [[_COMMUNITY_Community 126]]
- 1 edge to [[_COMMUNITY_Community 108]]

## Top bridge nodes
- [[is_overloaded()]] - degree 27, connects to 3 communities
- [[TestOverloadedMultiProvider]] - degree 16, connects to 1 community
- [[TestIsOverloaded]] - degree 9, connects to 1 community