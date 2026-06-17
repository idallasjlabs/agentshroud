---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "HTTP CONNECT Proxy & Egress"
location: "L362"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/HTTP_CONNECT_Proxy__Egress
---

# TestContentTypeFiltering

## Connections
- [[.test_normal_content_type_not_flagged()]] - `method` [EXTRACTED]
- [[.test_suspicious_content_type_flagged()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/HTTP_CONNECT_Proxy__Egress