---
type: community
members: 37
---

# test_security_toolchain.py

**Members:** 37 nodes

## Members
- [[dot-test_categorize_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_categorize_mixed()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_is_agentshroud_rule_false()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_is_agentshroud_rule_true()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_container_info()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_critical_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_valid_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_read_alerts_missing_dir()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_top_rules()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_with_alerts()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_with_rootkit()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_4]] - code
- [[Categorize alerts by severity. Args alerts List of parsed alerts. Returns…]] - rationale - gateway/security/falco_monitor.py
- [[Check if a rule is AgentShroud-specific. Args rule_name Falco rule name.…]] - rationale - gateway/security/falco_monitor.py
- [[Extend AGENTSHROUD_RULES with bot-specific name prefixes. Called at gateway…]] - rationale - gateway/security/falco_monitor.py
- [[Generate a summary dict suitable for the health report. Args alerts List of…]] - rationale - gateway/security/falco_monitor.py
- [[Parse a single Falco alert. Args raw Raw Falco alert JSON. Returns Parsed…]] - rationale - gateway/security/falco_monitor.py
- [[Read Falco alerts from the alert directory. Args alert_dir Directory…]] - rationale - gateway/security/falco_monitor.py
- [[Return recent Falco runtime security alerts with summary.]] - rationale - gateway/ingest_api/main.py
- [[TestFalcoCategorize]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoSummary]] - code - gateway/tests/test_security_toolchain.py
- [[TestWazuhSummary]] - code - gateway/tests/test_security_toolchain.py
- [[Tests for the security toolchain modules. Covers Trivy, ClamAV, Falco, Wazuh,…]] - rationale - gateway/tests/test_security_toolchain.py
- [[categorize_alerts()]] - code - gateway/security/falco_monitor.py
- [[configure_rules()]] - code - gateway/security/falco_monitor.py
- [[datetime]] - code
- [[falco_alerts()]] - code - gateway/ingest_api/main.py
- [[falco_monitor.py]] - code - gateway/security/falco_monitor.py
- [[generate_summary()]] - code - gateway/security/falco_monitor.py
- [[is_agentshroud_rule()]] - code - gateway/security/falco_monitor.py
- [[parse_alert()]] - code - gateway/security/falco_monitor.py
- [[read_alerts()]] - code - gateway/security/falco_monitor.py
- [[test_security_toolchain.py]] - code - gateway/tests/test_security_toolchain.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_security_toolchainpy
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_generate_report]]
- 7 edges to [[_COMMUNITY_parse_trivy_output]]
- 6 edges to [[_COMMUNITY_wazuh_client.py]]
- 5 edges to [[_COMMUNITY_parse_clamscan_output]]
- 5 edges to [[_COMMUNITY_FalcoAlertWatcher]]
- 4 edges to [[_COMMUNITY_run_trivy_scan]]
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_TestStartupScannerKeying]]
- 1 edge to [[_COMMUNITY_TestAlertDispatcher]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_PipelineAction]]

## Top bridge nodes
- [[test_security_toolchain.py]] - degree 49, connects to 10 communities
- [[falco_monitor.py]] - degree 13, connects to 4 communities
- [[read_alerts()]] - degree 11, connects to 2 communities
- [[generate_summary()]] - degree 8, connects to 1 community
- [[falco_alerts()]] - degree 6, connects to 1 community
