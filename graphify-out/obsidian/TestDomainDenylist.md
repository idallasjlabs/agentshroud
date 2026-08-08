---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "Egress Domain Allowlist"
location: "L47"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress_Domain_Allowlist
---

# TestDomainDenylist

## Connections
- [[.test_allowed_domain_passes()_1]] - `method` [EXTRACTED]
- [[.test_custom_denylist()_1]] - `method` [EXTRACTED]
- [[.test_denied_domain_blocked()]] - `method` [EXTRACTED]
- [[.test_denied_domain_malware()]] - `method` [EXTRACTED]
- [[.test_denied_subdomain_blocked()]] - `method` [EXTRACTED]
- [[.test_domain_not_in_denylist_passes()]] - `method` [EXTRACTED]
- [[.test_github_passes()]] - `method` [EXTRACTED]
- [[.test_stackoverflow_passes()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress_Domain_Allowlist