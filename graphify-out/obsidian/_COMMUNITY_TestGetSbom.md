---
type: community
cohesion: 0.40
members: 5
---

# TestGetSbom

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_invalid_json()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_missing_dir()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_no_files()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_valid()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestGetSbom]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestGetSbom
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY__w()]]
- 1 edge to [[_COMMUNITY_test_scanner_integration_coverage.py]]

## Top bridge nodes
- [[TestGetSbom]] - degree 5, connects to 1 community
- [[.test_invalid_json()]] - degree 2, connects to 1 community
- [[.test_valid()]] - degree 2, connects to 1 community