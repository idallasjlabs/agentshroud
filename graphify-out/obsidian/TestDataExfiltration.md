---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "Egress Filter & HTTP Proxy"
location: "L386"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Egress_Filter__HTTP_Proxy
---

# TestDataExfiltration

## Connections
- [[dot-test_base64_in_query_flagged()]] - `method` [EXTRACTED]
- [[dot-test_base64_in_url_path_flagged()]] - `method` [EXTRACTED]
- [[dot-test_long_query_flagged()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[TestDataExfiltration_1]] - `semantically_similar_to` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Egress_Filter__HTTP_Proxy