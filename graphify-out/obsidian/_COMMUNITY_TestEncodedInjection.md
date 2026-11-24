---
type: community
members: 4
---

# TestEncodedInjection

**Members:** 4 nodes

## Members
- [[dot-test_base64_clean_content_not_flagged()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_base64_encoded_injection()_1]] - code - gateway/tests/test_tool_result_injection.py
- [[Benign base64 content should not trigger encoded injection.]] - rationale - gateway/tests/test_tool_result_injection.py
- [[TestEncodedInjection]] - code - gateway/tests/test_tool_result_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestEncodedInjection
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ToolResultInjectionScanner]]

## Top bridge nodes
- [[TestEncodedInjection]] - degree 3, connects to 1 community
