---
type: community
cohesion: 0.15
members: 13
---

# TestDataExfiltration

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[.test_base64_in_path_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_base64_in_query_flagged()_1]] - code - gateway/tests/test_url_analyzer.py
- [[.test_base64_in_query_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_base64_in_url_path_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_long_query_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_long_query_string_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_many_params_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_normal_query_not_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_short_base64_not_flagged()_1]] - code - gateway/tests/test_url_analyzer.py
- [[Data exfiltration patterns in URLs — flagged, not blocked.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Short base64 strings are normal (e.g., API tokens in URLs).]] - rationale - gateway/tests/test_url_analyzer.py
- [[TestDataExfiltration_1]] - code - gateway/tests/test_url_analyzer.py
- [[TestDataExfiltration]] - code - gateway/tests/test_web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestDataExfiltration
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_WebProxyConfig]]
- 2 edges to [[_COMMUNITY_WebProxy]]
- 2 edges to [[_COMMUNITY_URLAnalyzer]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[TestDataExfiltration]] - degree 11, connects to 3 communities
- [[TestDataExfiltration_1]] - degree 11, connects to 2 communities