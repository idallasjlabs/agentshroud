---
source_file: "gateway/proxy/web_config.py"
type: "code"
community: "Egress Filter & HTTP Proxy"
location: "L21"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Egress_Filter__HTTP_Proxy
---

# DomainSettings

## Connections
- [[dot-get_domain_settings()]] - `references` [EXTRACTED]
- [[dot-test_custom_domain_size_limit()]] - `calls` [EXTRACTED]
- [[dot-test_get_domain_settings_custom()]] - `calls` [EXTRACTED]
- [[dot-test_wildcard_domain_settings()]] - `calls` [EXTRACTED]
- [[Per-domain configuration overrides.]] - `rationale_for` [EXTRACTED]
- [[TestAllowlistMode]] - `uses` [INFERRED]
- [[TestAuditChain_1]] - `uses` [INFERRED]
- [[TestContentTypeFiltering]] - `uses` [INFERRED]
- [[TestDataExfiltration]] - `uses` [INFERRED]
- [[TestDomainDenylist]] - `uses` [INFERRED]
- [[TestEncodedPayloads]] - `uses` [INFERRED]
- [[TestHiddenContent]] - `uses` [INFERRED]
- [[TestIsDomainAllowed]] - `uses` [INFERRED]
- [[TestPIIDetection_2]] - `uses` [INFERRED]
- [[TestPassthroughMode]] - `uses` [INFERRED]
- [[TestPromptInjectionDetection]] - `uses` [INFERRED]
- [[TestRateLimiting]] - `uses` [INFERRED]
- [[TestResponseSizeLimits]] - `uses` [INFERRED]
- [[TestSSRFBlocking]] - `uses` [INFERRED]
- [[TestStats_1]] - `uses` [INFERRED]
- [[TestWebProxyConfig]] - `uses` [INFERRED]
- [[TestZeroWidthAttacks]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `imports` [EXTRACTED]
- [[web_config.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Egress_Filter__HTTP_Proxy