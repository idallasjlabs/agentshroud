---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "Gateway Test Suite"
location: "L528"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# TestAllowlistMode

## Connections
- [[.allowlist_config()]] - `method` [EXTRACTED]
- [[.allowlist_proxy()]] - `method` [EXTRACTED]
- [[.test_default_mode_is_denylist()]] - `method` [EXTRACTED]
- [[.test_denylist_mode_still_works()]] - `method` [EXTRACTED]
- [[.test_listed_domain_passes()]] - `method` [EXTRACTED]
- [[.test_ssrf_blocked_before_allowlist_check()]] - `method` [EXTRACTED]
- [[.test_unlisted_domain_blocked()_1]] - `method` [EXTRACTED]
- [[.test_wildcard_deeper_subdomain_passes()]] - `method` [EXTRACTED]
- [[.test_wildcard_subdomain_passes()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[Default-deny allowlist unlisted domains are blocked.]] - `rationale_for` [EXTRACTED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite