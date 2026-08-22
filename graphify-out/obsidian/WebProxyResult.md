---
source_file: "gateway/proxy/web_proxy.py"
type: "code"
community: "Web Proxy Security"
location: "L45"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Web_Proxy_Security
---

# WebProxyResult

## Connections
- [[.check_request()]] - `references` [EXTRACTED]
- [[.flagged()_2]] - `method` [EXTRACTED]
- [[.scan_response()]] - `references` [EXTRACTED]
- [[.to_dict()_2]] - `method` [EXTRACTED]
- [[MockDNSVerdict]] - `uses` [INFERRED]
- [[MockEgressChannel]] - `uses` [INFERRED]
- [[MockEgressEvent]] - `uses` [INFERRED]
- [[MockThreatLevel]] - `uses` [INFERRED]
- [[MockURLResult]] - `uses` [INFERRED]
- [[Result of proxying a web request.]] - `rationale_for` [EXTRACTED]
- [[TestWebProxySecurityIntegration]] - `uses` [INFERRED]
- [[URLAnalyzer]] - `uses` [INFERRED]
- [[WebContentScanner]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_web_proxy_security.py]] - `imports` [EXTRACTED]
- [[web_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Web_Proxy_Security