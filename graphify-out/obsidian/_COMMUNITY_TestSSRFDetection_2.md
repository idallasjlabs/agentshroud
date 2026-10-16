---
type: community
cohesion: 0.22
members: 11
---

# TestSSRFDetection

**Cohesion:** 0.22 - loosely connected
**Members:** 11 nodes

## Members
- [[dot-__init__()_191]] - code - gateway/proxy/url_analyzer.py
- [[dot-test_empty_url()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_no_scheme()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_weird_scheme()]] - code - gateway/tests/test_url_analyzer.py
- [[Analyze URLs for SSRF, data exfiltration, and suspicious patterns.]] - rationale - gateway/proxy/url_analyzer.py
- [[Args             resolve_dns If True, resolve hostnames to IPs and check those]] - rationale - gateway/proxy/url_analyzer.py
- [[Edge cases and malformed URLs.]] - rationale - gateway/tests/test_url_analyzer.py
- [[TestMalformedURLs]] - code - gateway/tests/test_url_analyzer.py
- [[URLAnalyzer_1]] - code - gateway/proxy/url_analyzer.py
- [[analyzer()]] - code - gateway/tests/test_url_analyzer.py
- [[test_url_analyzer.py]] - code - gateway/tests/test_url_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSSRFDetection
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_TestSSRFDetection_1]]
- 3 edges to [[_COMMUNITY_TestSSRFDetection_5]]
- 3 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_TestSSRFDetection_6]]
- 2 edges to [[_COMMUNITY_TestSSRFDetection]]
- 2 edges to [[_COMMUNITY_TestSSRFDetection_3]]
- 2 edges to [[_COMMUNITY_TestSSRFDetection_4]]
- 1 edge to [[_COMMUNITY_WebContentScanner]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]

## Top bridge nodes
- [[URLAnalyzer_1]] - degree 19, connects to 9 communities
- [[test_url_analyzer.py]] - degree 10, connects to 6 communities
- [[TestMalformedURLs]] - degree 7, connects to 1 community
