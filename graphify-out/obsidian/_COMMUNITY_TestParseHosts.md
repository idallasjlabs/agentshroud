---
type: community
cohesion: 0.31
members: 11
---

# TestParseHosts

**Cohesion:** 0.31 - loosely connected
**Members:** 11 nodes

## Members
- [[.test_comma_separated()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_custom_default()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_dedup_preserves_first_order()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_empty_string_returns_defaults()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_mixed_separators_and_stripping()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_none_returns_defaults()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_only_separators_falls_back_to_default()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_whitespace_separated()]] - code - gateway/tests/test_multi_host_test.py
- [[Parse a commawhitespace-separated host list into a de-duplicated list.      Emp]] - rationale - gateway/tools/multi_host_test.py
- [[TestParseHosts]] - code - gateway/tests/test_multi_host_test.py
- [[parse_hosts()]] - code - gateway/tools/multi_host_test.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestParseHosts
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MultiHostResult]]
- 2 edges to [[_COMMUNITY_test_multi_host_test.py]]
- 1 edge to [[_COMMUNITY_HostStatus]]
- 1 edge to [[_COMMUNITY_main()]]
- 1 edge to [[_COMMUNITY_multi_host_test.py]]

## Top bridge nodes
- [[TestParseHosts]] - degree 12, connects to 3 communities
- [[parse_hosts()]] - degree 12, connects to 3 communities