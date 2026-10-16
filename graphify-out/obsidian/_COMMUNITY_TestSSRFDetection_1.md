---
type: community
cohesion: 0.17
members: 17
---

# TestSSRFDetection

**Cohesion:** 0.17 - loosely connected
**Members:** 17 nodes

## Members
- [[dot-_check_base64()]] - code - gateway/proxy/url_analyzer.py
- [[dot-_is_private_ip()_1]] - code - gateway/proxy/url_analyzer.py
- [[dot-_is_ssrf()]] - code - gateway/proxy/url_analyzer.py
- [[dot-_resolve_host()]] - code - gateway/proxy/url_analyzer.py
- [[dot-analyze()_1]] - code - gateway/proxy/url_analyzer.py
- [[dot-analyze_and_pin()]] - code - gateway/proxy/url_analyzer.py
- [[dot-flagged()_2]] - code - gateway/proxy/url_analyzer.py
- [[A single finding from URL analysis.]] - rationale - gateway/proxy/url_analyzer.py
- [[Analyze URL and pin resolved IP to mitigate DNS rebinding TOCTOU.          When]] - rationale - gateway/proxy/url_analyzer.py
- [[Analyze a URL for security issues.          Returns URLAnalysisResult with verdi]] - rationale - gateway/proxy/url_analyzer.py
- [[Check for base64-encoded data in URL path and query values.]] - rationale - gateway/proxy/url_analyzer.py
- [[Check if an IP address is privatereservedloopback.]] - rationale - gateway/proxy/url_analyzer.py
- [[Check if hostname is a privatereserved address (SSRF attempt).]] - rationale - gateway/proxy/url_analyzer.py
- [[Resolve hostname to IP. Returns None on failure.          NOTE DNS rebinding at]] - rationale - gateway/proxy/url_analyzer.py
- [[Result of analyzing a URL.]] - rationale - gateway/proxy/url_analyzer.py
- [[URLAnalysisResult_1]] - code - gateway/proxy/url_analyzer.py
- [[URLFinding]] - code - gateway/proxy/url_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSSRFDetection
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_TestSSRFDetection_2]]
- 2 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 1 edge to [[_COMMUNITY_TestSSRFDetection_5]]

## Top bridge nodes
- [[dot-_check_base64()]] - degree 6, connects to 2 communities
- [[dot-analyze()_1]] - degree 9, connects to 1 community
- [[dot-analyze_and_pin()]] - degree 7, connects to 1 community
- [[URLAnalysisResult_1]] - degree 6, connects to 1 community
- [[dot-_is_private_ip()_1]] - degree 5, connects to 1 community
