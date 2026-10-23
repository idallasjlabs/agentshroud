---
type: community
cohesion: 0.36
members: 8
---

# _looks_like_base64()

**Cohesion:** 0.36 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-test_actual_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_all_lowercase_not_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_non_base64_chars()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_short_string_not_base64()]] - code - gateway/tests/test_url_analyzer.py
- [[Heuristic does this string look like base64-encoded data]] - rationale - gateway/proxy/url_analyzer.py
- [[Test the _looks_like_base64 helper.]] - rationale - gateway/tests/test_url_analyzer.py
- [[TestBase64Heuristic]] - code - gateway/tests/test_url_analyzer.py
- [[_looks_like_base64()]] - code - gateway/proxy/url_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_looks_like_base64
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_URLAnalyzer]]
- 2 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_LLMProxy]]

## Top bridge nodes
- [[_looks_like_base64()]] - degree 8, connects to 3 communities
- [[TestBase64Heuristic]] - degree 8, connects to 2 communities
