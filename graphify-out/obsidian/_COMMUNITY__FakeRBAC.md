---
type: community
members: 4
---

# _FakeRBAC

**Members:** 4 nodes

## Members
- [[dot-require()]] - code - gateway/soc/auth.py
- [[Action]] - code - gateway/soc/auth.py
- [[Raise 403 if the caller lacks the required permission.]] - rationale - gateway/soc/auth.py
- [[Resource]] - code - gateway/soc/auth.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_FakeRBAC
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[dot-require()]] - degree 4, connects to 1 community
