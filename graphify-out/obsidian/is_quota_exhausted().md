---
source_file: "gateway/proxy/llm_quota_detector.py"
type: "code"
community: "Gateway Test Suite"
location: "L114"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# is_quota_exhausted()

## Connections
- [[.proxy_messages()]] - `calls` [EXTRACTED]
- [[LLMProxy.proxy_messages()]] - `calls` [EXTRACTED]
- [[Return (True, token) if the response indicates a billingquota wall.      The st]] - `rationale_for` [EXTRACTED]
- [[_is_anthropic_quota()]] - `calls` [EXTRACTED]
- [[_is_google_quota()]] - `calls` [EXTRACTED]
- [[_is_openai_quota()]] - `calls` [EXTRACTED]
- [[llm_proxy.py]] - `imports` [EXTRACTED]
- [[llm_quota_detector.py]] - `contains` [EXTRACTED]
- [[test_200_never_triggers()]] - `calls` [EXTRACTED]
- [[test_400_without_quota_substring_not_flagged()]] - `calls` [EXTRACTED]
- [[test_500_never_triggers()]] - `calls` [EXTRACTED]
- [[test_detect_anthropic_400_oauth_extra_usage()]] - `calls` [EXTRACTED]
- [[test_detect_anthropic_credit_balance_substring()]] - `calls` [EXTRACTED]
- [[test_detect_anthropic_extra_usage()]] - `calls` [EXTRACTED]
- [[test_detect_anthropic_rate_limit_type_quota_message()]] - `calls` [EXTRACTED]
- [[test_detect_anthropic_settings_url()]] - `calls` [EXTRACTED]
- [[test_detect_google_resource_exhausted()]] - `calls` [EXTRACTED]
- [[test_detect_openai_insufficient_quota()]] - `calls` [EXTRACTED]
- [[test_llm_quota_detector.py]] - `imports` [EXTRACTED]
- [[test_no_false_positive_on_anthropic_request_rate_limit()]] - `calls` [EXTRACTED]
- [[test_non_json_body_anthropic_429_no_substring_match()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite