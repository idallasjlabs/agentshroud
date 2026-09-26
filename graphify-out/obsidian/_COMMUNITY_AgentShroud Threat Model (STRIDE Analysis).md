---
type: community
cohesion: 0.24
members: 10
---

# AgentShroud Threat Model (STRIDE Analysis)

**Cohesion:** 0.24 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_argv_shape()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_custom_user()]] - code - gateway/tests/test_multi_host_test.py
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
TABLE source_file, type FROM #community/AgentShroud_Threat_Model_STRIDE_Analysis
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_AgentShroud Red Team Adversarial Tester]]
- 3 edges to [[_COMMUNITY_Required ≥ 4.5 for text, ≥ 3.0 for UI elements]]
- 3 edges to [[_COMMUNITY_SECTION 1 COVER SHEET (Form PTOSB16)]]
- 3 edges to [[_COMMUNITY_TestRunAndSendCveReportImageScans]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]
- 1 edge to [[_COMMUNITY_Hermes — Podcast Production Orchestrator]]
- 1 edge to [[_COMMUNITY_Common Operations]]
- 1 edge to [[_COMMUNITY_TestPatternDetection]]
- 1 edge to [[_COMMUNITY_Development Workflow]]
- 1 edge to [[_COMMUNITY_SECTION 3 DRAWINGS]]

## Top bridge nodes
- [[multi_host_test.py]] - degree 15, connects to 10 communities
- [[TestBuildSshArgv]] - degree 6, connects to 3 communities
- [[build_ssh_argv()]] - degree 6, connects to 1 community
- [[_dry_run_report()]] - degree 4, connects to 1 community
- [[_resolve_command()]] - degree 3, connects to 1 community