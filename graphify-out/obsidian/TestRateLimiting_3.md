---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "Egress Domain Allowlist"
location: "L326"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Egress_Domain_Allowlist
---

# TestRateLimiting

## Connections
- [[.test_different_domains_independent()]] - `method` [EXTRACTED]
- [[.test_rate_limit_blocks_excess()]] - `method` [EXTRACTED]
- [[.test_rate_limiter_reset()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Egress_Domain_Allowlist