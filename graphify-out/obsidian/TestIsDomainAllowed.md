---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "HTTP CONNECT Proxy & Egress"
location: "L576"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTP_CONNECT_Proxy__Egress
---

# TestIsDomainAllowed

## Connections
- [[.test_case_insensitive()_2]] - `method` [EXTRACTED]
- [[.test_empty_allowlist_blocks_everything()]] - `method` [EXTRACTED]
- [[.test_exact_match()_1]] - `method` [EXTRACTED]
- [[.test_wildcard_does_not_match_other_root()]] - `method` [EXTRACTED]
- [[.test_wildcard_matches_root_domain()]] - `method` [EXTRACTED]
- [[.test_wildcard_matches_subdomain()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[Unit tests for WebProxyConfig.is_domain_allowed().]] - `rationale_for` [EXTRACTED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTP_CONNECT_Proxy__Egress