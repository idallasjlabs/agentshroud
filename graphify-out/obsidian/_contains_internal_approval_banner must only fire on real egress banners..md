---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "HTTP Forwarder"
location: "L4678"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/HTTP_Forwarder
---

# _contains_internal_approval_banner must only fire on real egress banners.

## Connections
- [[TestInternalBannerMatcher]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/HTTP_Forwarder