---
type: community
cohesion: 0.18
members: 20
---

# Module Group 228

**Cohesion:** 0.18 - loosely connected
**Members:** 20 nodes

## Members
- [[._patch_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_clean_when_installed_not_running()_1]] - code - gateway/tests/test_scanner_integration.py
- [[.test_not_run_when_no_alert_dir()_1]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_clean_when_all_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_critical_when_any_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_not_configured_when_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_warning_when_high_only()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_summary_for_empty_dir()_1]] - code - gateway/tests/test_scanner_integration.py
- [[.test_scanners_dict_has_all_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_timestamp_present()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_totals_sum_across_scanners()]] - code - gateway/tests/test_scanner_integration.py
- [[Aggregate results from all security scanners into a unified dict.      Returns]] - rationale - gateway/security/scanner_integration.py
- [[Any_51]] - code - gateway/security/scanner_integration.py
- [[Return Fluent Bit log collector status.      Fluent Bit is a log shipper, not a]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Wazuh alert summary from the shared alert volume.      wazuh-agent]] - rationale - gateway/security/scanner_integration.py
- [[TestAggregateResults]] - code - gateway/tests/test_scanner_integration.py
- [[TestGetWazuhSummary]] - code - gateway/tests/test_scanner_integration.py
- [[aggregate_results()]] - code - gateway/security/scanner_integration.py
- [[get_fluent_bit_summary()]] - code - gateway/security/scanner_integration.py
- [[get_wazuh_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_228
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_Scanner Integration Tests]]
- 9 edges to [[_COMMUNITY_Security Scanner Integration]]
- 4 edges to [[_COMMUNITY_Module Group 163]]
- 3 edges to [[_COMMUNITY_Module Group 269]]
- 2 edges to [[_COMMUNITY_Module Group 134]]
- 2 edges to [[_COMMUNITY_Module Group 437]]
- 2 edges to [[_COMMUNITY_Module Group 210]]
- 2 edges to [[_COMMUNITY_Module Group 381]]
- 2 edges to [[_COMMUNITY_Module Group 122]]
- 2 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Module Group 213]]
- 1 edge to [[_COMMUNITY_Module Group 335]]

## Top bridge nodes
- [[Any_51]] - degree 22, connects to 11 communities
- [[aggregate_results()]] - degree 19, connects to 7 communities
- [[get_wazuh_summary()]] - degree 14, connects to 5 communities
- [[._patch_all_not_run()]] - degree 10, connects to 1 community
- [[TestAggregateResults]] - degree 9, connects to 1 community