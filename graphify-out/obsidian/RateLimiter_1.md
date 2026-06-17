---
source_file: "gateway/proxy/web_proxy.py"
type: "code"
community: "HTTP CONNECT Proxy & Egress"
location: "L95"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/HTTP_CONNECT_Proxy__Egress
---

# RateLimiter

## Connections
- [[.__init__()_34]] - `method` [EXTRACTED]
- [[.__init__()_35]] - `calls` [EXTRACTED]
- [[.check()_1]] - `method` [EXTRACTED]
- [[.reset()]] - `method` [EXTRACTED]
- [[.test_rate_limiter_reset()]] - `calls` [EXTRACTED]
- [[Simple in-memory per-domain rate limiter using sliding window.]] - `rationale_for` [EXTRACTED]
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
- [[TestZeroWidthAttacks]] - `uses` [INFERRED]
- [[URLAnalyzer]] - `uses` [INFERRED]
- [[WebContentScanner]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy.py]] - `imports` [EXTRACTED]
- [[web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/HTTP_CONNECT_Proxy__Egress