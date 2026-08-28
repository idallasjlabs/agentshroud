---
type: community
cohesion: 0.05
members: 51
---

# Community 112

**Cohesion:** 0.05 - loosely connected
**Members:** 51 nodes

## Members
- [[.__init__()_80]] - code - gateway/security/falco_monitor.py
- [[.test_categorize_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_categorize_mixed()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_clamav_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[.test_is_agentshroud_rule_false()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_is_agentshroud_rule_true()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_container_info()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_critical_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_empty_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_valid_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_read_alerts_missing_dir()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_clean()_2]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_clean()_3]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_top_rules()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_with_alerts()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_with_rootkit()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_update_db_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_34]] - code - gateway/security/clamav_scanner.py
- [[Any_40]] - code - gateway/security/falco_monitor.py
- [[Categorize alerts by severity.      Args         alerts List of parsed alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Check if a rule is AgentShroud-specific.      Args         rule_name Falco rul]] - rationale - gateway/security/falco_monitor.py
- [[Generate a summary dict suitable for the health report.      Args         alert]] - rationale - gateway/security/falco_monitor.py
- [[Parse a single Falco alert.      Args         raw Raw Falco alert JSON.      R]] - rationale - gateway/security/falco_monitor.py
- [[Path_8]] - code - gateway/security/clamav_scanner.py
- [[Path_11]] - code - gateway/security/falco_monitor.py
- [[Read Falco alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/falco_monitor.py
- [[Run ClamAV scan and return parsed results.      Args         target Directory]] - rationale - gateway/security/clamav_scanner.py
- [[Save a ClamAV report to the log directory.]] - rationale - gateway/security/clamav_scanner.py
- [[TestClamAVRun]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoCategorize]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[TestWazuhSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[Update ClamAV virus database using freshclam.      Args         freshclam_bin]] - rationale - gateway/security/clamav_scanner.py
- [[categorize_alerts()]] - code - gateway/security/falco_monitor.py
- [[datetime_3]] - code - gateway/security/falco_monitor.py
- [[gatewaysecurityclamav_scanner.py]] - code - gateway/security/clamav_scanner.py
- [[gatewaysecurityfalco_monitor.py]] - code - gateway/security/falco_monitor.py
- [[gatewaysecurityhealth_report.py]] - code - gateway/security/health_report.py
- [[gatewaysecuritytrivy_report.py]] - code - gateway/security/trivy_report.py
- [[gatewaysecuritywazuh_client.py]] - code - gateway/security/wazuh_client.py
- [[generate_summary()]] - code - gateway/security/clamav_scanner.py
- [[generate_summary()_1]] - code - gateway/security/falco_monitor.py
- [[is_agentshroud_rule()]] - code - gateway/security/falco_monitor.py
- [[parse_alert()]] - code - gateway/security/falco_monitor.py
- [[read_alerts()]] - code - gateway/security/falco_monitor.py
- [[run_clamscan()]] - code - gateway/security/clamav_scanner.py
- [[save_report()]] - code - gateway/security/clamav_scanner.py
- [[test_security_toolchain.py]] - code - gateway/tests/test_security_toolchain.py
- [[update_virus_db()]] - code - gateway/security/clamav_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_112
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_Security Audit & Drift Detection]]
- 10 edges to [[_COMMUNITY_Community 410]]
- 7 edges to [[_COMMUNITY_Community 347]]
- 6 edges to [[_COMMUNITY_Community 215]]
- 6 edges to [[_COMMUNITY_Community 216]]
- 5 edges to [[_COMMUNITY_Community 579]]
- 3 edges to [[_COMMUNITY_Community 72]]
- 3 edges to [[_COMMUNITY_Community 501]]
- 3 edges to [[_COMMUNITY_Community 632]]
- 2 edges to [[_COMMUNITY_Community 640]]
- 1 edge to [[_COMMUNITY_Community 48]]
- 1 edge to [[_COMMUNITY_Community 665]]
- 1 edge to [[_COMMUNITY_Community 330]]
- 1 edge to [[_COMMUNITY_Community 734]]
- 1 edge to [[_COMMUNITY_Community 590]]

## Top bridge nodes
- [[test_security_toolchain.py]] - degree 47, connects to 9 communities
- [[run_clamscan()]] - degree 10, connects to 5 communities
- [[generate_summary()_1]] - degree 8, connects to 3 communities
- [[read_alerts()]] - degree 10, connects to 2 communities
- [[Any_34]] - degree 6, connects to 2 communities