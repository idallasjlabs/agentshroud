---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "Egress Filter & HTTP Proxy"
location: "L528"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress_Filter__HTTP_Proxy
---

# TestAllowlistMode

## Connections
- [[dot-allowlist_config()]] - `method` [EXTRACTED]
- [[dot-allowlist_proxy()]] - `method` [EXTRACTED]
- [[dot-test_default_mode_is_denylist()]] - `method` [EXTRACTED]
- [[dot-test_denylist_mode_still_works()]] - `method` [EXTRACTED]
- [[dot-test_listed_domain_passes()]] - `method` [EXTRACTED]
- [[dot-test_ssrf_blocked_before_allowlist_check()]] - `method` [EXTRACTED]
- [[dot-test_unlisted_domain_blocked()]] - `method` [EXTRACTED]
- [[dot-test_wildcard_deeper_subdomain_passes()]] - `method` [EXTRACTED]
- [[dot-test_wildcard_subdomain_passes()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[Default-deny allowlist unlisted domains are blocked.]] - `rationale_for` [EXTRACTED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress_Filter__HTTP_Proxy