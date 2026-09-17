---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "TestInternalBannerMatcher"
location: "L4677"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestInternalBannerMatcher
---

# TestInternalBannerMatcher

## Connections
- [[.test_false_on_empty_string()]] - `method` [EXTRACTED]
- [[.test_false_on_non_string()]] - `method` [EXTRACTED]
- [[.test_no_false_positive_on_domain_mention()]] - `method` [EXTRACTED]
- [[.test_no_false_positive_on_generic_llm_response()]] - `method` [EXTRACTED]
- [[.test_true_on_callback_token()]] - `method` [EXTRACTED]
- [[.test_true_on_deny_token()]] - `method` [EXTRACTED]
- [[.test_true_on_real_egress_banner_header()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker_1]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[TelegramAPIProxy_2]] - `uses` [INFERRED]
- [[_contains_internal_approval_banner must only fire on real egress banners.]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TestInternalBannerMatcher