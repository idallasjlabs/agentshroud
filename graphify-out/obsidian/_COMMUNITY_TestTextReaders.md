---
type: community
cohesion: 0.40
members: 5
---

# TestTextReaders

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_compose_text_empty_when_absent()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_compose_text_skips_unreadable_then_reads()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_security_scan_sh_empty_when_absent()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_security_scan_sh_read()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestTextReaders]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestTextReaders
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY__w()]]
- 1 edge to [[_COMMUNITY_test_scanner_integration_coverage.py]]

## Top bridge nodes
- [[TestTextReaders]] - degree 5, connects to 1 community
- [[.test_compose_text_skips_unreadable_then_reads()]] - degree 2, connects to 1 community
- [[.test_security_scan_sh_read()]] - degree 2, connects to 1 community