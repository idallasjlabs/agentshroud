---
type: community
cohesion: 0.24
members: 10
---

# AgentShroud (system, C4 context) (3)

**Cohesion:** 0.24 - loosely connected
**Members:** 10 nodes

## Members
- [[dot-test_argv_shape()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_custom_user()]] - code - gateway/tests/test_multi_host_test.py
- [[Build the ssh argv for a host. Non-interactive, fail-fast on connect.      ``Bat]] - rationale - gateway/tools/multi_host_test.py
- [[Describe exactly what would run, without executing anything.]] - rationale - gateway/tools/multi_host_test.py
- [[TestBuildSshArgv]] - code - gateway/tests/test_multi_host_test.py
- [[Turn argparse REMAINDER tokens into a command string.      Drops a leading ``--`]] - rationale - gateway/tools/multi_host_test.py
- [[_dry_run_report()]] - code - gateway/tools/multi_host_test.py
- [[_resolve_command()]] - code - gateway/tools/multi_host_test.py
- [[build_ssh_argv()]] - code - gateway/tools/multi_host_test.py
- [[multi_host_test.py]] - code - gateway/tools/multi_host_test.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_system_C4_context_3
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_parse_trivy_output]]
- 3 edges to [[_COMMUNITY_Docker Compose (infra diagram)]]
- 3 edges to [[_COMMUNITY_🎯 High-Value Features (Justify the Effort)]]
- 3 edges to [[_COMMUNITY_VIII. Evaluation]]
- 1 edge to [[_COMMUNITY_Migration Path (SSH → Distributed Node)]]
- 1 edge to [[_COMMUNITY_Red Team Assessment v1.2.0 (2)]]
- 1 edge to [[_COMMUNITY_PermissionLevel (6)]]
- 1 edge to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_LOW Findings]]
- 1 edge to [[_COMMUNITY_AgentShroud™ v0.8.0 Watchtower — Complete Feature List (2)]]

## Top bridge nodes
- [[multi_host_test.py]] - degree 15, connects to 10 communities
- [[TestBuildSshArgv]] - degree 6, connects to 3 communities
- [[build_ssh_argv()]] - degree 6, connects to 1 community
- [[_dry_run_report()]] - degree 4, connects to 1 community
- [[_resolve_command()]] - degree 3, connects to 1 community
