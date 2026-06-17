---
source_file: "gateway/proxy/web_proxy.py"
type: "code"
community: "HTTP CONNECT Proxy & Egress"
location: "L38"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/HTTP_CONNECT_Proxy__Egress
---

# ProxyAction

## Connections
- [[Enum]] - `inherits` [EXTRACTED]
- [[MockDNSVerdict]] - `uses` [INFERRED]
- [[MockEgressChannel]] - `uses` [INFERRED]
- [[MockEgressEvent]] - `uses` [INFERRED]
- [[MockThreatLevel]] - `uses` [INFERRED]
- [[MockURLResult]] - `uses` [INFERRED]
- [[TestAllowlistMode]] - `uses` [INFERRED]
- [[TestAuditChain_1]] - `uses` [INFERRED]
- [[TestContentTypeFiltering]] - `uses` [INFERRED]
- [[TestDataExfiltration_1]] - `uses` [INFERRED]
- [[TestDomainDenylist]] - `uses` [INFERRED]
- [[TestEncodedPayloads]] - `uses` [INFERRED]
- [[TestHiddenContent]] - `uses` [INFERRED]
- [[TestIsDomainAllowed]] - `uses` [INFERRED]
- [[TestPIIDetection_2]] - `uses` [INFERRED]
- [[TestPassthroughMode_1]] - `uses` [INFERRED]
- [[TestPromptInjectionDetection]] - `uses` [INFERRED]
- [[TestRateLimiting_3]] - `uses` [INFERRED]
- [[TestResponseSizeLimits]] - `uses` [INFERRED]
- [[TestSSRFBlocking]] - `uses` [INFERRED]
- [[TestStats_1]] - `uses` [INFERRED]
- [[TestWebProxyConfig]] - `uses` [INFERRED]
- [[TestWebProxySecurityIntegration]] - `uses` [INFERRED]
- [[TestZeroWidthAttacks]] - `uses` [INFERRED]
- [[URLAnalyzer]] - `uses` [INFERRED]
- [[WebContentScanner]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[str]] - `inherits` [EXTRACTED]
- [[test_web_proxy.py]] - `imports` [EXTRACTED]
- [[test_web_proxy_security.py]] - `imports` [EXTRACTED]
- [[web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/HTTP_CONNECT_Proxy__Egress