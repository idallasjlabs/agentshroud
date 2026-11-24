---
type: community
members: 8
---

# get_falco_summary

**Members:** 8 nodes

## Members
- [[dot-test_clean_when_installed_not_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_alert_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_summary_for_empty_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[Return True if a non-zombie falco process is running inside this container.]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Falco alert summary from the local alert directory. CC-20 If…]] - rationale - gateway/security/scanner_integration.py
- [[TestGetFalcoSummary]] - code - gateway/tests/test_scanner_integration.py
- [[_is_falco_running()]] - code - gateway/security/scanner_integration.py
- [[get_falco_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_falco_summary
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_Any_1]]
- 1 edge to [[_COMMUNITY_compute_scorecard]]
- 1 edge to [[_COMMUNITY_wazuh_client.py]]

## Top bridge nodes
- [[get_falco_summary()]] - degree 12, connects to 5 communities
- [[TestGetFalcoSummary]] - degree 4, connects to 1 community
- [[_is_falco_running()]] - degree 3, connects to 1 community
