---
type: community
members: 33
---

# is_quota_exhausted

**Members:** 33 nodes

## Members
- [[A 429 that escaped the retry loop must trigger local failover.]] - rationale - gateway/tests/test_rate_limit_failover.py
- [[Anthropic returns the Claude.ai OAuth quota copy with HTTP 400 (wrapped as…]] - rationale - gateway/tests/test_llm_quota_detector.py
- [[Generic 400 validation errors must NOT trigger failover.]] - rationale - gateway/tests/test_llm_quota_detector.py
- [[Post-retry rate-limit failover. Observed 2026-06-131415 Anthropic returned…]] - rationale - gateway/tests/test_rate_limit_failover.py
- [[Quota-exhaustion detector for cloud LLM providers. Pure-function module — no…]] - rationale - gateway/proxy/llm_quota_detector.py
- [[Return (True, anthropic_rate_limitopenai_rate_limit...) for a persistent…]] - rationale - gateway/proxy/llm_quota_detector.py
- [[Return (True, token) if the response indicates a billingquota wall. The stable…]] - rationale - gateway/proxy/llm_quota_detector.py
- [[_is_anthropic_quota()]] - code - gateway/proxy/llm_quota_detector.py
- [[_is_google_quota()]] - code - gateway/proxy/llm_quota_detector.py
- [[_is_openai_quota()]] - code - gateway/proxy/llm_quota_detector.py
- [[asyncio_53]] - code
- [[is_quota_exhausted()]] - code - gateway/proxy/llm_quota_detector.py
- [[is_rate_limited_post_retry()]] - code - gateway/proxy/llm_quota_detector.py
- [[llm_quota_detector.py]] - code - gateway/proxy/llm_quota_detector.py
- [[mock_forward()_18]] - code - gateway/tests/test_rate_limit_failover.py
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
- [[test_detector_empty_body_still_fires_as_generic_cloud()]] - code - gateway/tests/test_rate_limit_failover.py
- [[test_detector_fires_on_plain_429()]] - code - gateway/tests/test_rate_limit_failover.py
- [[test_detector_skips_non_429()]] - code - gateway/tests/test_rate_limit_failover.py
- [[test_llm_quota_detector.py]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_no_false_positive_on_anthropic_request_rate_limit()]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_non_json_body_anthropic_429_no_substring_match()]] - code - gateway/tests/test_llm_quota_detector.py
- [[test_proxy_failover_on_post_retry_429()]] - code - gateway/tests/test_rate_limit_failover.py
- [[test_rate_limit_failover.py]] - code - gateway/tests/test_rate_limit_failover.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/is_quota_exhausted
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_LLMProxy]]
- 4 edges to [[_COMMUNITY_is_overloaded]]
- 4 edges to [[_COMMUNITY_test_anthropic_openai_translator.py]]

## Top bridge nodes
- [[is_quota_exhausted()]] - degree 21, connects to 2 communities
- [[llm_quota_detector.py]] - degree 10, connects to 2 communities
- [[test_rate_limit_failover.py]] - degree 9, connects to 2 communities
- [[is_rate_limited_post_retry()]] - degree 8, connects to 2 communities
- [[test_llm_quota_detector.py]] - degree 17, connects to 1 community
