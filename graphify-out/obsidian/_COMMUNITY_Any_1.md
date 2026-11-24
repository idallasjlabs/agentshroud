---
type: community
members: 23
---

# Any

**Members:** 23 nodes

## Members
- [[dot-_patch_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_clean_report()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_critical_on_critical_findings()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_report()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_clean_when_all_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_critical_when_any_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_not_configured_when_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_warning_when_high_only()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_scanners_dict_has_all_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_timestamp_present()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_totals_sum_across_scanners()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_warning_on_failures()]] - code - gateway/tests/test_scanner_integration.py
- [[Aggregate results from all security scanners into a unified dict. Returns Dict…]] - rationale - gateway/security/scanner_integration.py
- [[Any_60]] - code
- [[Return Fluent Bit log collector status. Fluent Bit is a log shipper, not a…]] - rationale - gateway/security/scanner_integration.py
- [[Return True if fluent-bit pidfile tmpfluent-bit.pid exists with a live PID.]] - rationale - gateway/security/scanner_integration.py
- [[Return latest OpenSCAP compliance summary from saved reports.]] - rationale - gateway/security/scanner_integration.py
- [[TestAggregateResults_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestGetOpenscapSummary]] - code - gateway/tests/test_scanner_integration.py
- [[_is_fluent_bit_running()]] - code - gateway/security/scanner_integration.py
- [[aggregate_results()]] - code - gateway/security/scanner_integration.py
- [[get_fluent_bit_summary()]] - code - gateway/security/scanner_integration.py
- [[get_openscap_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Any
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 8 edges to [[_COMMUNITY_scanner_integration.py]]
- 4 edges to [[_COMMUNITY__score_compliance_auditing]]
- 4 edges to [[_COMMUNITY_get_trivy_summary]]
- 4 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 3 edges to [[_COMMUNITY__score_image_integrity]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_get_falco_summary]]
- 2 edges to [[_COMMUNITY_get_wazuh_summary]]
- 2 edges to [[_COMMUNITY_compute_scorecard]]
- 1 edge to [[_COMMUNITY_get_sbom]]
- 1 edge to [[_COMMUNITY_Any]]
- 1 edge to [[_COMMUNITY_test_soc_bots.py]]

## Top bridge nodes
- [[Any_60]] - degree 22, connects to 12 communities
- [[aggregate_results()]] - degree 19, connects to 6 communities
- [[get_openscap_summary()]] - degree 11, connects to 4 communities
- [[dot-test_overall_clean_when_all_clean()]] - degree 7, connects to 4 communities
- [[dot-_patch_all_not_run()]] - degree 10, connects to 3 communities
