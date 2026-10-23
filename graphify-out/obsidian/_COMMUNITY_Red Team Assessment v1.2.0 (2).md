---
type: community
cohesion: 0.40
members: 6
---

# Red Team Assessment v1.2.0 (2)

**Cohesion:** 0.40 - moderately connected
**Members:** 6 nodes

## Members
- [[dot-test_ssh_runner_none_streams()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_ssh_runner_uses_subprocess()]] - code - gateway/tests/test_multi_host_test.py
- [[HostRunner]] - code - gateway/tools/multi_host_test.py
- [[Return a HostRunner that executes the command on the host over SSH.      SSH con]] - rationale - gateway/tools/multi_host_test.py
- [[TestSshRunner]] - code - gateway/tests/test_multi_host_test.py
- [[ssh_runner()]] - code - gateway/tools/multi_host_test.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Red_Team_Assessment_v120_2
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_🎯 High-Value Features (Justify the Effort)]]
- 2 edges to [[_COMMUNITY_VIII. Evaluation]]
- 2 edges to [[_COMMUNITY_parse_trivy_output]]
- 1 edge to [[_COMMUNITY_Docker Compose (infra diagram)]]
- 1 edge to [[_COMMUNITY_LOW Findings]]
- 1 edge to [[_COMMUNITY_AgentShroud (system, C4 context) (3)]]

## Top bridge nodes
- [[ssh_runner()]] - degree 7, connects to 3 communities
- [[TestSshRunner]] - degree 6, connects to 3 communities
- [[HostRunner]] - degree 3, connects to 2 communities
