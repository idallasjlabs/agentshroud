---
source_file: "gateway/proxy/url_analyzer.py"
type: "code"
community: "LLMProxy"
location: "L99"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLMProxy
---

# URLAnalyzer

## Connections
- [[dot-__init__()_201]] - `method` [EXTRACTED]
- [[dot-_check_base64()]] - `method` [EXTRACTED]
- [[dot-_is_private_ip()_2]] - `method` [EXTRACTED]
- [[dot-_is_ssrf()]] - `method` [EXTRACTED]
- [[dot-_resolve_host()]] - `method` [EXTRACTED]
- [[dot-analyze()_1]] - `method` [EXTRACTED]
- [[dot-analyze_and_pin()]] - `method` [EXTRACTED]
- [[Analyze URLs for SSRF, data exfiltration, and suspicious patterns.]] - `rationale_for` [EXTRACTED]
- [[EgressFilter_2]] - `semantically_similar_to` [INFERRED]
- [[TestBase64Heuristic]] - `uses` [INFERRED]
- [[TestDataExfiltration_1]] - `uses` [INFERRED]
- [[TestLegitimateURLsAllowed]] - `uses` [INFERRED]
- [[TestMalformedURLs]] - `uses` [INFERRED]
- [[TestPIIInURLs]] - `uses` [INFERRED]
- [[TestSSRFDetection]] - `uses` [INFERRED]
- [[WebContentScanner]] - `semantically_similar_to` [INFERRED]
- [[analyzer()]] - `calls` [EXTRACTED]
- [[test_url_analyzer.py]] - `imports` [EXTRACTED]
- [[url_analyzer.py_2]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LLMProxy
