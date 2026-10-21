---
type: community
members: 8
---

# test_collaborator_greeter.py (3)

**Members:** 8 nodes

## Members
- [[dot-test_clean_when_installed_not_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_alert_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_summary_for_empty_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[Return True if wazuh-agentd is running as a local process inside this container.]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Wazuh alert summary from the shared alert volume.      wazuh-agent]] - rationale - gateway/security/scanner_integration.py
- [[TestGetWazuhSummary]] - code - gateway/tests/test_scanner_integration.py
- [[_is_wazuh_agent_running()]] - code - gateway/security/scanner_integration.py
- [[get_wazuh_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_collaborator_greeterpy_3
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_test_collaborator_greeter.py (2)]]
- 2 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_AgentTarget (6)]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py (2)]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_Path (3)]]

## Top bridge nodes
- [[get_wazuh_summary()]] - degree 13, connects to 6 communities
- [[_is_wazuh_agent_running()]] - degree 4, connects to 1 community
- [[TestGetWazuhSummary]] - degree 4, connects to 1 community
- [[dot-test_not_run_when_no_alert_dir()]] - degree 3, connects to 1 community
