---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "Egress Domain Allowlist"
location: "L298"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Egress_Domain_Allowlist
---

# TestResponseSizeLimits

## Connections
- [[.test_custom_domain_size_limit()]] - `method` [EXTRACTED]
- [[.test_large_response_flagged()]] - `method` [EXTRACTED]
- [[.test_normal_response_not_flagged_for_size()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Egress_Domain_Allowlist