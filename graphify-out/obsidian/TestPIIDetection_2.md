---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "Egress Filter & HTTP Proxy"
location: "L265"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress_Filter__HTTP_Proxy
---

# TestPIIDetection

## Connections
- [[dot-test_aws_key_in_response_flagged()]] - `method` [EXTRACTED]
- [[dot-test_pii_in_response_flagged()]] - `method` [EXTRACTED]
- [[dot-test_pii_in_url_flagged()]] - `method` [EXTRACTED]
- [[dot-test_private_key_in_response_flagged()]] - `method` [EXTRACTED]
- [[dot-test_ssn_in_url_flagged()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress_Filter__HTTP_Proxy