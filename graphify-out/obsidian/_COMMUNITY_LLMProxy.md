---
type: community
cohesion: 0.05
members: 61
---

# LLMProxy

**Cohesion:** 0.05 - loosely connected
**Members:** 61 nodes

## Members
- [[.__init__()_80]] - code - gateway/security/falco_monitor.py
- [[.test_categorize_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_categorize_mixed()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_clean_when_installed_not_running()_1]] - code - gateway/tests/test_scanner_integration.py
- [[.test_get_fim_events()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_get_rootkit_events()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_is_agentshroud_rule_false()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_is_agentshroud_rule_true()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_level_to_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_not_run_when_no_alert_dir()_1]] - code - gateway/tests/test_scanner_integration.py
- [[.test_parse_container_info()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_critical_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_empty_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_fim_event()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_rootkit_event()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_valid_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_read_alerts_missing_dir()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_returns_summary_for_empty_dir()_1]] - code - gateway/tests/test_scanner_integration.py
- [[.test_summary_clean()_2]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_clean()_3]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_top_rules()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_with_alerts()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_with_rootkit()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_40]] - code - gateway/security/falco_monitor.py
- [[Any_65]] - code - gateway/security/wazuh_client.py
- [[Categorize alerts by severity.      Args         alerts List of parsed alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Check if a rule is AgentShroud-specific.      Args         rule_name Falco rul]] - rationale - gateway/security/falco_monitor.py
- [[Filter alerts to file integrity monitoring events only.      Args         alert]] - rationale - gateway/security/wazuh_client.py
- [[Filter alerts to rootkit detection events only.      Args         alerts List]] - rationale - gateway/security/wazuh_client.py
- [[Generate a summary dict suitable for the health report.      Args         alert]] - rationale - gateway/security/falco_monitor.py
- [[Map Wazuh alert level to severity string.      Args         level Wazuh alert]] - rationale - gateway/security/wazuh_client.py
- [[Parse a single Falco alert.      Args         raw Raw Falco alert JSON.      R]] - rationale - gateway/security/falco_monitor.py
- [[Parse a single Wazuh alert.      Args         raw Raw Wazuh alert JSON.      R]] - rationale - gateway/security/wazuh_client.py
- [[Path_11]] - code - gateway/security/falco_monitor.py
- [[Path_20]] - code - gateway/security/wazuh_client.py
- [[Read Falco alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/falco_monitor.py
- [[Read Wazuh alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/wazuh_client.py
- [[Return latest Wazuh alert summary from the shared alert volume.      wazuh-agent]] - rationale - gateway/security/scanner_integration.py
- [[TestFalcoCategorize]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[TestGetWazuhSummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestWazuhParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestWazuhSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[categorize_alerts()]] - code - gateway/security/falco_monitor.py
- [[datetime_3]] - code - gateway/security/falco_monitor.py
- [[datetime_5]] - code - gateway/security/wazuh_client.py
- [[generate_summary()]] - code - gateway/security/clamav_scanner.py
- [[generate_summary()_1]] - code - gateway/security/falco_monitor.py
- [[generate_summary()_3]] - code - gateway/security/wazuh_client.py
- [[get_fim_events()]] - code - gateway/security/wazuh_client.py
- [[get_rootkit_events()]] - code - gateway/security/wazuh_client.py
- [[get_wazuh_summary()]] - code - gateway/security/scanner_integration.py
- [[is_agentshroud_rule()]] - code - gateway/security/falco_monitor.py
- [[level_to_severity()]] - code - gateway/security/wazuh_client.py
- [[parse_alert()]] - code - gateway/security/falco_monitor.py
- [[parse_alert()_1]] - code - gateway/security/wazuh_client.py
- [[read_alerts()]] - code - gateway/security/falco_monitor.py
- [[read_alerts()_1]] - code - gateway/security/wazuh_client.py
- [[test_security_toolchain.py]] - code - gateway/tests/test_security_toolchain.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LLMProxy
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_GroupApprovalRouter]]
- 9 edges to [[_COMMUNITY_gateway.security.daily_cve_report]]
- 8 edges to [[_COMMUNITY_test_runtime_engines.py]]
- 8 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 6 edges to [[_COMMUNITY_lifespan.py]]
- 5 edges to [[_COMMUNITY_PrivacyPolicyEnforcer]]
- 4 edges to [[_COMMUNITY_Canvas Skill]]
- 4 edges to [[_COMMUNITY_AgentShroud User Guide]]
- 3 edges to [[_COMMUNITY_Phase 3 MITIGATE (Rollback First!)]]
- 3 edges to [[_COMMUNITY_Step-by-Step Installation]]
- 2 edges to [[_COMMUNITY_A2AMethod]]
- 1 edge to [[_COMMUNITY__wrap_response()]]
- 1 edge to [[_COMMUNITY_agentshroud-bot]]
- 1 edge to [[_COMMUNITY_MCPAuditTrail]]
- 1 edge to [[_COMMUNITY_Startup Sequence]]
- 1 edge to [[_COMMUNITY_Apollo — Audio Systems Producer]]

## Top bridge nodes
- [[test_security_toolchain.py]] - degree 42, connects to 7 communities
- [[generate_summary()_3]] - degree 13, connects to 6 communities
- [[get_wazuh_summary()]] - degree 14, connects to 5 communities
- [[read_alerts()_1]] - degree 9, connects to 3 communities
- [[read_alerts()]] - degree 10, connects to 2 communities