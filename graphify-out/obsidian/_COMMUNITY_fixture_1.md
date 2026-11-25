---
type: community
members: 4
---

# fixture

**Members:** 4 nodes

## Members
- [[Use a temporary DB for all tests.]] - rationale - gateway/tests/test_version_routes.py
- [[client()_11]] - code - gateway/tests/test_version_routes.py
- [[fixture_55]] - code
- [[tmp_version_db()]] - code - gateway/tests/test_version_routes.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/fixture
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_version_routes.py]]
- 1 edge to [[_COMMUNITY_app]]

## Top bridge nodes
- [[tmp_version_db()]] - degree 3, connects to 1 community
- [[fixture_55]] - degree 3, connects to 1 community
- [[client()_11]] - degree 2, connects to 1 community
