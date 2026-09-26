---
type: community
cohesion: 0.13
members: 26
---

# Canvas Skill

**Cohesion:** 0.13 - loosely connected
**Members:** 26 nodes

## Members
- [[._patch_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_clean_report()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_clean_when_installed_not_running()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_critical_on_critical_findings()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_not_run_when_no_alert_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_not_run_when_no_report()_1]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_critical_when_any_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_not_configured_when_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_warning_when_high_only()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_summary_for_empty_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_scanners_dict_has_all_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_timestamp_present()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_totals_sum_across_scanners()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_warning_on_failures()]] - code - gateway/tests/test_scanner_integration.py
- [[Aggregate results from all security scanners into a unified dict.      Returns]] - rationale - gateway/security/scanner_integration.py
- [[Any_58]] - code - gateway/security/scanner_integration.py
- [[Return Fluent Bit log collector status.      Fluent Bit is a log shipper, not a]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Falco alert summary from the local alert directory.      CC-20 If]] - rationale - gateway/security/scanner_integration.py
- [[Return latest OpenSCAP compliance summary from saved reports.]] - rationale - gateway/security/scanner_integration.py
- [[TestAggregateResults]] - code - gateway/tests/test_scanner_integration.py
- [[TestGetFalcoSummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestGetOpenscapSummary]] - code - gateway/tests/test_scanner_integration.py
- [[aggregate_results()]] - code - gateway/security/scanner_integration.py
- [[get_falco_summary()]] - code - gateway/security/scanner_integration.py
- [[get_fluent_bit_summary()]] - code - gateway/security/scanner_integration.py
- [[get_openscap_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Canvas_Skill
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_A2AMethod]]
- 10 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 5 edges to [[_COMMUNITY_Step-by-Step Installation]]
- 4 edges to [[_COMMUNITY_agentshroud-bot]]
- 4 edges to [[_COMMUNITY_LLMProxy]]
- 3 edges to [[_COMMUNITY_MCPAuditTrail]]
- 2 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_AgentShroud Dev Environment — Raspberry Pi 4 (8G]]
- 1 edge to [[_COMMUNITY_🟢 INFO (nice to have)]]
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[Any_58]] - degree 22, connects to 9 communities
- [[aggregate_results()]] - degree 19, connects to 7 communities
- [[get_falco_summary()]] - degree 13, connects to 4 communities
- [[get_openscap_summary()]] - degree 11, connects to 4 communities
- [[._patch_all_not_run()]] - degree 10, connects to 1 community