---
type: community
cohesion: 0.13
members: 26
---

# test_collaborator_greeter.py

**Cohesion:** 0.13 - loosely connected
**Members:** 26 nodes

## Members
- [[dot-_patch_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_clean_report()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_clean_when_installed_not_running()_2]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_critical_on_critical_findings()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_alert_dir()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_report()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_critical_when_any_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_not_configured_when_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_warning_when_high_only()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_summary_for_empty_dir()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_scanners_dict_has_all_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_timestamp_present()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_totals_sum_across_scanners()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_warning_on_failures()]] - code - gateway/tests/test_scanner_integration.py
- [[Aggregate results from all security scanners into a unified dict.      Returns]] - rationale - gateway/security/scanner_integration.py
- [[Any_64]] - code - gateway/security/scanner_integration.py
- [[Return Fluent Bit log collector status.      Fluent Bit is a log shipper, not a]] - rationale - gateway/security/scanner_integration.py
- [[Return latest OpenSCAP compliance summary from saved reports.]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Wazuh alert summary from the shared alert volume.      wazuh-agent]] - rationale - gateway/security/scanner_integration.py
- [[TestAggregateResults_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestGetOpenscapSummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestGetWazuhSummary]] - code - gateway/tests/test_scanner_integration.py
- [[aggregate_results()]] - code - gateway/security/scanner_integration.py
- [[get_fluent_bit_summary()]] - code - gateway/security/scanner_integration.py
- [[get_openscap_summary()]] - code - gateway/security/scanner_integration.py
- [[get_wazuh_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_collaborator_greeterpy
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 10 edges to [[_COMMUNITY_scanner_integration.py]]
- 5 edges to [[_COMMUNITY_Path_2]]
- 4 edges to [[_COMMUNITY__load_latest_json]]
- 4 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 3 edges to [[_COMMUNITY_AgentTarget_4]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_test_soc_bots.py]]
- 1 edge to [[_COMMUNITY_get_trivy_summary]]

## Top bridge nodes
- [[Any_64]] - degree 22, connects to 9 communities
- [[aggregate_results()]] - degree 19, connects to 6 communities
- [[get_wazuh_summary()]] - degree 14, connects to 5 communities
- [[get_openscap_summary()]] - degree 11, connects to 4 communities
- [[dot-_patch_all_not_run()]] - degree 10, connects to 1 community
