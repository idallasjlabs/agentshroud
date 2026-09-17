---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Tool Result Sanitizer & XML Injection Filtering"
location: "L4678"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Tool_Result_Sanitizer__XML_Injection_Filtering
---

# _contains_internal_approval_banner must only fire on real egress banners.

## Connections
- [[TestInternalBannerMatcher]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Tool_Result_Sanitizer__XML_Injection_Filtering