---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "WebProxyConfig"
location: "L265"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/WebProxyConfig
---

# TestPIIDetection

## Connections
- [[.test_aws_key_in_response_flagged()]] - `method` [EXTRACTED]
- [[.test_pii_in_response_flagged()]] - `method` [EXTRACTED]
- [[.test_pii_in_url_flagged()]] - `method` [EXTRACTED]
- [[.test_private_key_in_response_flagged()]] - `method` [EXTRACTED]
- [[.test_ssn_in_url_flagged()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/WebProxyConfig