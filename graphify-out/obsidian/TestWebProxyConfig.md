---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "HTTP CONNECT Proxy & Egress"
location: "L498"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTP_CONNECT_Proxy__Egress
---

# TestWebProxyConfig

## Connections
- [[.test_domain_denied()]] - `method` [EXTRACTED]
- [[.test_get_domain_settings_custom()]] - `method` [EXTRACTED]
- [[.test_get_domain_settings_default()]] - `method` [EXTRACTED]
- [[.test_passthrough_mode_default_off()]] - `method` [EXTRACTED]
- [[.test_wildcard_domain_settings()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTP_CONNECT_Proxy__Egress