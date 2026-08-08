---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "Egress Domain Allowlist"
location: "L407"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Egress_Domain_Allowlist
---

# TestPassthroughMode

## Connections
- [[.test_passthrough_adds_header()]] - `method` [EXTRACTED]
- [[.test_passthrough_allows_everything()_1]] - `method` [EXTRACTED]
- [[.test_passthrough_skips_content_scan()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Egress_Domain_Allowlist