---
type: community
members: 21
---

# Community 419

**Members:** 21 nodes

## Members
- [[Anthropic returns the Claude.ai OAuth quota copy with HTTP 400     (wrapped as i]] - rationale - gateway/tests/test_llm_quota_detector.py
- [[Generic 400 validation errors must NOT trigger failover.]] - rationale - gateway/tests/test_llm_quota_detector.py
- [[Return (True, token) if the response indicates a billingquota wall.      The st]] - rationale - gateway/proxy/llm_quota_detector.py
- [[_is_anthropic_quota()]] - code - gateway/proxy/llm_quota_detector.py
- [[_is_google_quota()]] - code - gateway/proxy/llm_quota_detector.py
- [[_is_openai_quota()]] - code - gateway/proxy/llm_quota_detector.py
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
TABLE source_file, type FROM #community/Community_419
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 308]]
- 1 edge to [[_COMMUNITY_Community 126]]
- 1 edge to [[_COMMUNITY_Community 108]]
- 1 edge to [[_COMMUNITY_Community 979]]

## Top bridge nodes
- [[is_quota_exhausted()]] - degree 20, connects to 2 communities
- [[llm_quota_detector.py]] - degree 7, connects to 2 communities
- [[test_llm_quota_detector.py]] - degree 17, connects to 1 community