---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "HTTP CONNECT Proxy & Egress"
location: "L265"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTP_CONNECT_Proxy__Egress
---

# TestPIIDetection

## Connections
- [[.test_aws_key_in_response_flagged()]] - `method` [EXTRACTED]
- [[.test_pii_in_response_flagged()]] - `method` [EXTRACTED]
- [[.test_pii_in_url_flagged()]] - `method` [EXTRACTED]
- [[.test_private_key_in_response_flagged()]] - `method` [EXTRACTED]
- [[.test_ssn_in_url_flagged()_1]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTP_CONNECT_Proxy__Egress