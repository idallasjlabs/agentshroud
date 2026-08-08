---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "Egress Domain Allowlist"
location: "L386"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Egress_Domain_Allowlist
---

# TestDataExfiltration

## Connections
- [[.test_base64_in_query_flagged()_1]] - `method` [EXTRACTED]
- [[.test_base64_in_url_path_flagged()]] - `method` [EXTRACTED]
- [[.test_long_query_flagged()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Egress_Domain_Allowlist