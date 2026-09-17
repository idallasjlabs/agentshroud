---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "Egress Filter & HTTP Proxy"
location: "L47"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress_Filter__HTTP_Proxy
---

# TestDomainDenylist

## Connections
- [[dot-test_allowed_domain_passes()]] - `method` [EXTRACTED]
- [[dot-test_custom_denylist()_1]] - `method` [EXTRACTED]
- [[dot-test_denied_domain_blocked()]] - `method` [EXTRACTED]
- [[dot-test_denied_domain_malware()]] - `method` [EXTRACTED]
- [[dot-test_denied_subdomain_blocked()]] - `method` [EXTRACTED]
- [[dot-test_domain_not_in_denylist_passes()]] - `method` [EXTRACTED]
- [[dot-test_github_passes()]] - `method` [EXTRACTED]
- [[dot-test_stackoverflow_passes()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress_Filter__HTTP_Proxy