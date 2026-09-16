---
type: community
cohesion: 0.33
members: 6
---

# Community 1175

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[dot-test_falco_no_proc_returns_false()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_falco_running_detected()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_falco_zombie_only_returns_false()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_wazuh_agent_absent()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_wazuh_agent_detected()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestProcScans]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1175
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 200]]
- 1 edge to [[_COMMUNITY_Community 297]]

## Top bridge nodes
- [[TestProcScans]] - degree 6, connects to 1 community
- [[dot-test_falco_running_detected()]] - degree 2, connects to 1 community
- [[dot-test_falco_zombie_only_returns_false()]] - degree 2, connects to 1 community
- [[dot-test_wazuh_agent_absent()]] - degree 2, connects to 1 community
- [[dot-test_wazuh_agent_detected()]] - degree 2, connects to 1 community