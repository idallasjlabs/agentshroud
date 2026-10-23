---
type: community
cohesion: 0.36
members: 8
---

# Docker Compose (infra diagram)

**Cohesion:** 0.36 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-test_255_is_unreachable()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_nonzero_is_fail()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_zero_is_pass()]] - code - gateway/tests/test_multi_host_test.py
- [[HostStatus]] - code - gateway/tools/multi_host_test.py
- [[Map a runner exit code to a HostStatus.]] - rationale - gateway/tools/multi_host_test.py
- [[Outcome classification for a single host.]] - rationale - gateway/tools/multi_host_test.py
- [[TestClassify_1]] - code - gateway/tests/test_multi_host_test.py
- [[classify()_1]] - code - gateway/tools/multi_host_test.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Docker_Compose_infra_diagram
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_VIII. Evaluation]]
- 4 edges to [[_COMMUNITY_parse_trivy_output]]
- 3 edges to [[_COMMUNITY_AgentShroud (system, C4 context) (3)]]
- 2 edges to [[_COMMUNITY_LOW Findings]]
- 2 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_🎯 High-Value Features (Justify the Effort)]]
- 1 edge to [[_COMMUNITY_AgentShroud™ v0.8.0 Watchtower — Complete Feature List (2)]]
- 1 edge to [[_COMMUNITY_PermissionLevel (6)]]
- 1 edge to [[_COMMUNITY_Red Team Assessment v1.2.0 (2)]]
- 1 edge to [[_COMMUNITY_Migration Path (SSH → Distributed Node)]]

## Top bridge nodes
- [[HostStatus]] - degree 18, connects to 10 communities
- [[classify()_1]] - degree 8, connects to 3 communities
- [[TestClassify_1]] - degree 7, connects to 2 communities
