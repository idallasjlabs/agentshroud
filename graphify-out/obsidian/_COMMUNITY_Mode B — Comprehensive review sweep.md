---
type: community
cohesion: 0.50
members: 4
---

# Mode B — Comprehensive review sweep

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_empty_files_skipped()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_invalid_then_valid()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_missing_dir_returns_none()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestLoadLatestJson_1]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Mode_B__Comprehensive_review_sweep
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_TestMultilingualInjection]]
- 1 edge to [[_COMMUNITY_wazuh_client.py]]

## Top bridge nodes
- [[TestLoadLatestJson_1]] - degree 4, connects to 1 community
- [[.test_empty_files_skipped()]] - degree 2, connects to 1 community
- [[.test_invalid_then_valid()]] - degree 2, connects to 1 community