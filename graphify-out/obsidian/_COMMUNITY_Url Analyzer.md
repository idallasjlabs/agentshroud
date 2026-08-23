---
type: community
cohesion: 0.22
members: 9
---

# Url Analyzer

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[.test_base64_in_path_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_base64_in_query_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_long_query_string_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_many_params_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_normal_query_not_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[.test_short_base64_not_flagged()_1]] - code - gateway/tests/test_url_analyzer.py
- [[Data exfiltration patterns in URLs — flagged, not blocked.]] - rationale - gateway/tests/test_url_analyzer.py
- [[Short base64 strings are normal (e.g., API tokens in URLs).]] - rationale - gateway/tests/test_url_analyzer.py
- [[TestDataExfiltration]] - code - gateway/tests/test_url_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Url_Analyzer
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Url Analyzer]]
- 1 edge to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Web Proxy]]

## Top bridge nodes
- [[TestDataExfiltration]] - degree 11, connects to 3 communities