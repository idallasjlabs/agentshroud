---
type: community
members: 48
---

# is_overloaded

**Members:** 48 nodes

## Members
- [[dot-test_anthropic_api_error_500_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_anthropic_detection_unchanged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_empty_and_garbage_bodies()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_gemini_invalid_argument_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_gemini_resource_exhausted_stays_quota_territory()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_gemini_unavailable_503()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_gemini_unavailable_http_200()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_http_200_with_overloaded_body()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_http_503_with_overloaded_body()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_http_529_with_overloaded_body()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_mention_in_content_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_non_dict_json_body_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_normal_200_message_body_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_openai_invalid_request_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_openai_overloaded_message_http_200()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_openai_server_error_500_requires_capacity_wording()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_openai_server_error_503()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_openai_server_error_503_without_capacity_wording()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_other_error_types_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_overloaded_word_in_chat_content_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_quota_statuses_not_claimed()]] - code - gateway/tests/test_llm_quota_detector.py
- [[dot-test_unrecognized_error_shape_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[Anthropic returns the Claude.ai OAuth quota copy with HTTP 400     (wrapped as i]] - rationale - gateway/tests/test_llm_quota_detector.py
- [[Generic 400 validation errors must NOT trigger failover.]] - rationale - gateway/tests/test_llm_quota_detector.py
- [[Return (True, provider_overloaded) for a provider capacity-error     envelop]] - rationale - gateway/proxy/llm_quota_detector.py
- [[Return (True, token) if the response indicates a billingquota wall.      The st]] - rationale - gateway/proxy/llm_quota_detector.py
- [[SCRUM-60 in-body overload envelopes from OpenAI and Gemini must fail     over e]] - rationale - gateway/tests/test_llm_quota_detector.py
- [[TestIsOverloaded]] - code - gateway/tests/test_llm_quota_detector.py
- [[TestOverloadedMultiProvider]] - code - gateway/tests/test_llm_quota_detector.py
- [[_is_anthropic_quota()]] - code - gateway/proxy/llm_quota_detector.py
- [[_is_google_quota()]] - code - gateway/proxy/llm_quota_detector.py
- [[_is_openai_quota()]] - code - gateway/proxy/llm_quota_detector.py
- [[is_overloaded()]] - code - gateway/proxy/llm_quota_detector.py
- [[is_quota_exhausted()]] - code - gateway/proxy/llm_quota_detector.py
- [[llm_quota_detector.py]] - code - gateway/proxy/llm_quota_detector.py
- [[test_200_never_triggers()]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_400_without_quota_substring_not_flagged()]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_500_never_triggers()]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_detect_anthropic_400_oauth_extra_usage()]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_detect_anthropic_credit_balance_substring()]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_detect_anthropic_extra_usage()]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_detect_anthropic_rate_limit_type_quota_message()]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_detect_anthropic_settings_url()]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_detect_google_resource_exhausted()]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_detect_openai_insufficient_quota()]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_llm_quota_detector.py]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_no_false_positive_on_anthropic_request_rate_limit()]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_non_json_body_anthropic_429_no_substring_match()]] - code - gateway/tests/test_llm_quota_detector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/is_overloaded
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_is_rate_limited_post_retry]]

## Top bridge nodes
- [[llm_quota_detector.py]] - degree 7, connects to 1 community
