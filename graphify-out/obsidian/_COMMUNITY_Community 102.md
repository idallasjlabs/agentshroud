---
type: community
members: 56
---

# Community 102

**Members:** 56 nodes

## Members
- [[.test_categorize_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_categorize_mixed()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_get_fim_events()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_get_rootkit_events()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_is_agentshroud_rule_false()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_is_agentshroud_rule_true()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_level_to_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_container_info()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_critical_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_empty_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_fim_event()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_rootkit_event()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_valid_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_read_alerts_missing_dir()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_clean()_2]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_clean()_3]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_top_rules()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_with_alerts()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_with_rootkit()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_40]] - code - gateway/security/falco_monitor.py
- [[Any_65]] - code - gateway/security/wazuh_client.py
- [[Categorize alerts by severity.      Args         alerts List of parsed alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Check if a rule is AgentShroud-specific.      Args         rule_name Falco rul]] - rationale - gateway/security/falco_monitor.py
- [[Extend AGENTSHROUD_RULES with bot-specific name prefixes.      Called at gateway]] - rationale - gateway/security/falco_monitor.py
- [[Filter alerts to file integrity monitoring events only.      Args         alert]] - rationale - gateway/security/wazuh_client.py
- [[Filter alerts to rootkit detection events only.      Args         alerts List]] - rationale - gateway/security/wazuh_client.py
- [[Generate a summary dict suitable for the health report.      Args         alert]] - rationale - gateway/security/falco_monitor.py
- [[Map Wazuh alert level to severity string.      Args         level Wazuh alert]] - rationale - gateway/security/wazuh_client.py
- [[Parse a single Falco alert.      Args         raw Raw Falco alert JSON.      R]] - rationale - gateway/security/falco_monitor.py
- [[Parse a single Wazuh alert.      Args         raw Raw Wazuh alert JSON.      R]] - rationale - gateway/security/wazuh_client.py
- [[Path_20]] - code - gateway/security/wazuh_client.py
- [[Read Falco alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/falco_monitor.py
- [[Read Wazuh alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/wazuh_client.py
- [[TestFalcoCategorize]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[TestWazuhParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestWazuhSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[categorize_alerts()]] - code - gateway/security/falco_monitor.py
- [[configure_rules()]] - code - gateway/security/falco_monitor.py
- [[datetime_3]] - code - gateway/security/falco_monitor.py
- [[datetime_5]] - code - gateway/security/wazuh_client.py
- [[falco_monitor.py]] - code - gateway/security/falco_monitor.py
- [[generate_summary()_1]] - code - gateway/security/falco_monitor.py
- [[generate_summary()_3]] - code - gateway/security/wazuh_client.py
- [[get_fim_events()]] - code - gateway/security/wazuh_client.py
- [[get_rootkit_events()]] - code - gateway/security/wazuh_client.py
- [[is_agentshroud_rule()]] - code - gateway/security/falco_monitor.py
- [[level_to_severity()]] - code - gateway/security/wazuh_client.py
- [[parse_alert()]] - code - gateway/security/falco_monitor.py
- [[parse_alert()_1]] - code - gateway/security/wazuh_client.py
- [[read_alerts()]] - code - gateway/security/falco_monitor.py
- [[read_alerts()_1]] - code - gateway/security/wazuh_client.py
- [[test_security_toolchain.py]] - code - gateway/tests/test_security_toolchain.py
- [[wazuh_client.py]] - code - gateway/security/wazuh_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_102
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Community 185]]
- 9 edges to [[_COMMUNITY_Community 131]]
- 8 edges to [[_COMMUNITY_Community 0]]
- 7 edges to [[_COMMUNITY_Community 148]]
- 4 edges to [[_COMMUNITY_Community 531]]
- 4 edges to [[_COMMUNITY_Community 29]]
- 2 edges to [[_COMMUNITY_Community 72]]
- 2 edges to [[_COMMUNITY_Community 978]]
- 2 edges to [[_COMMUNITY_Community 219]]
- 2 edges to [[_COMMUNITY_Community 49]]
- 2 edges to [[_COMMUNITY_Community 1969]]
- 2 edges to [[_COMMUNITY_Community 943]]
- 1 edge to [[_COMMUNITY_Community 146]]
- 1 edge to [[_COMMUNITY_Community 842]]
- 1 edge to [[_COMMUNITY_Community 311]]
- 1 edge to [[_COMMUNITY_Community 363]]
- 1 edge to [[_COMMUNITY_Community 793]]
- 1 edge to [[_COMMUNITY_Community 625]]

## Top bridge nodes
- [[falco_monitor.py]] - degree 17, connects to 8 communities
- [[generate_summary()_3]] - degree 13, connects to 8 communities
- [[test_security_toolchain.py]] - degree 42, connects to 6 communities
- [[wazuh_client.py]] - degree 15, connects to 6 communities
- [[read_alerts()_1]] - degree 9, connects to 3 communities