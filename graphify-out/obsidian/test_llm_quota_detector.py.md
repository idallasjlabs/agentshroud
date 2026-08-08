---
source_file: "gateway/tests/test_llm_quota_detector.py"
type: "code"
community: "Gateway Test Suite"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# test_llm_quota_detector.py

## Connections
- [[TestIsOverloaded]] - `contains` [EXTRACTED]
- [[TestOverloadedMultiProvider]] - `contains` [EXTRACTED]
- [[is_overloaded()]] - `imports` [EXTRACTED]
- [[is_quota_exhausted()]] - `imports` [EXTRACTED]
- [[llm_quota_detector.py]] - `references` [EXTRACTED]
- [[test_200_never_triggers()]] - `contains` [EXTRACTED]
- [[test_400_without_quota_substring_not_flagged()]] - `contains` [EXTRACTED]
- [[test_500_never_triggers()]] - `contains` [EXTRACTED]
- [[test_detect_anthropic_400_oauth_extra_usage()]] - `contains` [EXTRACTED]
- [[test_detect_anthropic_credit_balance_substring()]] - `contains` [EXTRACTED]
- [[test_detect_anthropic_extra_usage()]] - `contains` [EXTRACTED]
- [[test_detect_anthropic_rate_limit_type_quota_message()]] - `contains` [EXTRACTED]
- [[test_detect_anthropic_settings_url()]] - `contains` [EXTRACTED]
- [[test_detect_google_resource_exhausted()]] - `contains` [EXTRACTED]
- [[test_detect_openai_insufficient_quota()]] - `contains` [EXTRACTED]
- [[test_no_false_positive_on_anthropic_request_rate_limit()]] - `contains` [EXTRACTED]
- [[test_non_json_body_anthropic_429_no_substring_match()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite