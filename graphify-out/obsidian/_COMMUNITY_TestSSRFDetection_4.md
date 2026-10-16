---
type: community
cohesion: 0.22
members: 9
---

# TestSSRFDetection

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[dot-test_base64_in_path_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_base64_in_query_flagged()_1]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_long_query_string_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_many_params_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_normal_query_not_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_short_base64_not_flagged()_1]] - code - gateway/tests/test_url_analyzer.py
- [[Data exfiltration patterns in URLs — flagged, not blocked.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Short base64 strings are normal (e.g., API tokens in URLs).]] - rationale - gateway/tests/test_url_analyzer.py
- [[TestDataExfiltration_1]] - code - gateway/tests/test_url_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSSRFDetection
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_TestSSRFDetection_2]]
- 1 edge to [[_COMMUNITY_TestToolChainAnalyzer]]
- 1 edge to [[_COMMUNITY_WebProxyConfig]]

## Top bridge nodes
- [[TestDataExfiltration_1]] - degree 11, connects to 3 communities
