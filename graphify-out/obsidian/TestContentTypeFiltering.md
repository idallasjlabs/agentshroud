---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "Egress Filter & HTTP Proxy"
location: "L362"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Egress_Filter__HTTP_Proxy
---

# TestContentTypeFiltering

## Connections
- [[dot-test_normal_content_type_not_flagged()]] - `method` [EXTRACTED]
- [[dot-test_suspicious_content_type_flagged()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Egress_Filter__HTTP_Proxy