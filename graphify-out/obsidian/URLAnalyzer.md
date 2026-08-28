---
source_file: "gateway/proxy/url_analyzer.py"
type: "code"
community: "Community 48"
location: "L99"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_48
---

# URLAnalyzer

## Connections
- [[.__init__()_41]] - `method` [EXTRACTED]
- [[._check_base64()]] - `method` [EXTRACTED]
- [[._is_private_ip()]] - `method` [EXTRACTED]
- [[._is_ssrf()]] - `method` [EXTRACTED]
- [[._resolve_host()]] - `method` [EXTRACTED]
- [[.analyze()]] - `method` [EXTRACTED]
- [[.analyze_and_pin()]] - `method` [EXTRACTED]
- [[Analyze URLs for SSRF, data exfiltration, and suspicious patterns.]] - `rationale_for` [EXTRACTED]
- [[Any_23]] - `uses` [INFERRED]
- [[EgressFilter_1]] - `semantically_similar_to` [INFERRED]
- [[ProxyAction]] - `uses` [INFERRED]
- [[RateLimiter_1]] - `uses` [INFERRED]
- [[TestBase64Heuristic]] - `uses` [INFERRED]
- [[TestDataExfiltration]] - `uses` [INFERRED]
- [[TestLegitimateURLsAllowed]] - `uses` [INFERRED]
- [[TestMalformedURLs]] - `uses` [INFERRED]
- [[TestPIIInURLs]] - `uses` [INFERRED]
- [[TestSSRFDetection]] - `uses` [INFERRED]
- [[URLAnalyzer_1]] - `uses` [INFERRED]
- [[WebContentScanner]] - `semantically_similar_to` [INFERRED]
- [[WebContentScanner_1]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig_1]] - `uses` [INFERRED]
- [[WebProxyResult]] - `uses` [INFERRED]
- [[analyzer()]] - `calls` [EXTRACTED]
- [[test_url_analyzer.py]] - `imports` [EXTRACTED]
- [[url_analyzer.py]] - `contains` [EXTRACTED]
- [[web_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_48