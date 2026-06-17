---
source_file: "gateway/tests/test_web_proxy.py"
type: "code"
community: "HTTP CONNECT Proxy & Egress"
location: "L196"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTP_CONNECT_Proxy__Egress
---

# TestHiddenContent

## Connections
- [[.test_clean_comment_not_flagged()]] - `method` [EXTRACTED]
- [[.test_injection_in_hidden_div()]] - `method` [EXTRACTED]
- [[.test_injection_in_html_comment()]] - `method` [EXTRACTED]
- [[.test_injection_in_invisible_text()]] - `method` [EXTRACTED]
- [[.test_injection_in_meta_tag()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[DomainSettings]] - `uses` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTP_CONNECT_Proxy__Egress