---
type: community
cohesion: 0.29
members: 7
---

# Discovery Strategy

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.test_basic_spawn()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_depth_exceeded_allowed_in_monitor()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_depth_exceeded_denied()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_depth_penalty_reduces_trust()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_disabled_always_allows()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_strict_inheritance_caps_trust()]] - code - gateway/tests/test_subagent_governance.py
- [[TestSpawnAuthorization]] - code - gateway/tests/test_subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Discovery_Strategy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Quick Reference — AgentShroud]]
- 2 edges to [[_COMMUNITY_TestCanvasAuthHelpers]]

## Top bridge nodes
- [[TestSpawnAuthorization]] - degree 12, connects to 2 communities