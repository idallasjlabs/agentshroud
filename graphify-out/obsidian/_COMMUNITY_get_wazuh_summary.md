---
type: community
members: 8
---

# get_wazuh_summary

**Members:** 8 nodes

## Members
- [[dot-test_clean_when_installed_not_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_alert_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_summary_for_empty_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[Return True if wazuh-agentd is running as a local process inside this container.]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Wazuh alert summary from the shared alert volume. wazuh-agentd…]] - rationale - gateway/security/scanner_integration.py
- [[TestGetWazuhSummary]] - code - gateway/tests/test_scanner_integration.py
- [[_is_wazuh_agent_running()]] - code - gateway/security/scanner_integration.py
- [[get_wazuh_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_wazuh_summary
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_generate_summary]]
- 2 edges to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_aggregate_results]]
- 1 edge to [[_COMMUNITY_compute_scorecard]]
- 1 edge to [[_COMMUNITY_Any]]
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[get_wazuh_summary()]] - degree 13, connects to 7 communities
- [[TestGetWazuhSummary]] - degree 4, connects to 1 community
- [[_is_wazuh_agent_running()]] - degree 3, connects to 1 community
