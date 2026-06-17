---
type: community
cohesion: 0.33
members: 6
---

# Module Group 492

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_falco_no_proc_returns_false()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_falco_running_detected()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_falco_zombie_only_returns_false()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_wazuh_agent_absent()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_wazuh_agent_detected()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestProcScans]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_492
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Module Group 131]]
- 1 edge to [[_COMMUNITY_Module Group 170]]

## Top bridge nodes
- [[TestProcScans]] - degree 6, connects to 1 community
- [[.test_falco_running_detected()]] - degree 2, connects to 1 community
- [[.test_falco_zombie_only_returns_false()]] - degree 2, connects to 1 community
- [[.test_wazuh_agent_absent()]] - degree 2, connects to 1 community
- [[.test_wazuh_agent_detected()]] - degree 2, connects to 1 community