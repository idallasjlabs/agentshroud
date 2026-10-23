---
type: community
cohesion: 0.50
members: 4
---

# ._run_and_read (2)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[dot-test_multiline_parenthesised_value_consumed()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[dot-test_unterminated_field_returns_end()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[TestConsumeFieldEdge]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[_consume_field]] - code - scripts/triage-cve-mitigations.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_run_and_read_2
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Path]]
- 1 edge to [[_COMMUNITY_dot-_run_and_read]]

## Top bridge nodes
- [[TestConsumeFieldEdge]] - degree 4, connects to 1 community
- [[dot-test_multiline_parenthesised_value_consumed()]] - degree 2, connects to 1 community
- [[dot-test_unterminated_field_returns_end()]] - degree 2, connects to 1 community
- [[_consume_field]] - degree 2, connects to 1 community
