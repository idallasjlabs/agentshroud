---
type: community
cohesion: 0.22
members: 9
---

# TestSSRFDetection

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[dot-test_api_endpoint_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_docs_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_github_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_https_allowed()_1]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_news_site_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_public_ip_allowed()_1]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_stackoverflow_allowed()]] - code - gateway/tests/test_url_analyzer.py
- [[Ensure normal browsing URLs pass through.]] - rationale - gateway/tests/test_url_analyzer.py
- [[TestLegitimateURLsAllowed]] - code - gateway/tests/test_url_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSSRFDetection
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_TestSSRFDetection_2]]
- 1 edge to [[_COMMUNITY_TestToolChainAnalyzer]]

## Top bridge nodes
- [[TestLegitimateURLsAllowed]] - degree 11, connects to 2 communities
