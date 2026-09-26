---
type: community
cohesion: 0.31
members: 11
---

# Common Operations

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
TABLE source_file, type FROM #community/Common_Operations
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Required ≥ 4.5 for text, ≥ 3.0 for UI elements]]
- 2 edges to [[_COMMUNITY_AgentShroud Red Team Adversarial Tester]]
- 1 edge to [[_COMMUNITY_SECTION 1 COVER SHEET (Form PTOSB16)]]
- 1 edge to [[_COMMUNITY_AgentShroud Threat Model (STRIDE Analysis)]]
- 1 edge to [[_COMMUNITY_TestRunAndSendCveReportImageScans]]

## Top bridge nodes
- [[TestParseHosts]] - degree 12, connects to 3 communities
- [[parse_hosts()]] - degree 12, connects to 3 communities