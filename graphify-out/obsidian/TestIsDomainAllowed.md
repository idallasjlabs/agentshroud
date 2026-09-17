---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "Egress Filter & HTTP Proxy"
location: "L576"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress_Filter__HTTP_Proxy
---

# TestIsDomainAllowed

## Connections
- [[dot-test_case_insensitive()_1]] - `method` [EXTRACTED]
- [[dot-test_empty_allowlist_blocks_everything()]] - `method` [EXTRACTED]
- [[dot-test_exact_match()_1]] - `method` [EXTRACTED]
- [[dot-test_wildcard_does_not_match_other_root()]] - `method` [EXTRACTED]
- [[dot-test_wildcard_matches_root_domain()]] - `method` [EXTRACTED]
- [[dot-test_wildcard_matches_subdomain()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[Unit tests for WebProxyConfig.is_domain_allowed().]] - `rationale_for` [EXTRACTED]
- [[WebProxy]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress_Filter__HTTP_Proxy