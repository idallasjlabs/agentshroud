---
type: community
cohesion: 0.05
members: 60
---

# LLMProxy.proxy_messages (non-streaming)

**Cohesion:** 0.05 - loosely connected
**Members:** 60 nodes

## Members
- [[dot-_handle_critical()]] - code - gateway/security/falco_monitor.py
- [[dot-_process_new_alerts()]] - code - gateway/security/falco_monitor.py
- [[dot-test_categorize_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_categorize_mixed()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_get_fim_events()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_get_rootkit_events()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_is_agentshroud_rule_false()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_is_agentshroud_rule_true()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_level_to_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_container_info()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_critical_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_fim_event()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_rootkit_event()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_valid_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_read_alerts_missing_dir()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_top_rules()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_with_alerts()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_with_rootkit()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_4]] - code - gateway/security/falco_monitor.py
- [[Any_5]] - code - gateway/security/wazuh_client.py
- [[Categorize alerts by severity.      Args         alerts List of parsed alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Check if a rule is AgentShroud-specific.      Args         rule_name Falco rul]] - rationale - gateway/security/falco_monitor.py
- [[Extend AGENTSHROUD_RULES with bot-specific name prefixes.      Called at gateway]] - rationale - gateway/security/falco_monitor.py
- [[Filter alerts to file integrity monitoring events only.      Args         alert]] - rationale - gateway/security/wazuh_client.py
- [[Filter alerts to rootkit detection events only.      Args         alerts List]] - rationale - gateway/security/wazuh_client.py
- [[Generate a summary dict suitable for the health report.      Args         alert]] - rationale - gateway/security/falco_monitor.py
- [[Map Wazuh alert level to severity string.      Args         level Wazuh alert]] - rationale - gateway/security/wazuh_client.py
- [[Parse a single Falco alert.      Args         raw Raw Falco alert JSON.      R]] - rationale - gateway/security/falco_monitor.py
- [[Parse a single Wazuh alert.      Args         raw Raw Wazuh alert JSON.      R]] - rationale - gateway/security/wazuh_client.py
- [[Path_2]] - code - gateway/security/wazuh_client.py
- [[Read Falco alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/falco_monitor.py
- [[Read Wazuh alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/wazuh_client.py
- [[TestFalcoCategorize]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoSummary]] - code - gateway/tests/test_security_toolchain.py
- [[TestWazuhParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestWazuhSummary]] - code - gateway/tests/test_security_toolchain.py
- [[categorize_alerts()]] - code - gateway/security/falco_monitor.py
- [[configure_rules()]] - code - gateway/security/falco_monitor.py
- [[datetime]] - code - gateway/security/falco_monitor.py
- [[datetime_1]] - code - gateway/security/wazuh_client.py
- [[falco-rules]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[falco_monitor.py]] - code - gateway/security/falco_monitor.py
- [[generate_summary()_1]] - code - gateway/security/falco_monitor.py
- [[generate_summary()_2]] - code - gateway/security/wazuh_client.py
- [[get_fim_events()]] - code - gateway/security/wazuh_client.py
- [[get_rootkit_events()]] - code - gateway/security/wazuh_client.py
- [[is_agentshroud_rule()]] - code - gateway/security/falco_monitor.py
- [[level_to_severity()]] - code - gateway/security/wazuh_client.py
- [[parse_alert()]] - code - gateway/security/falco_monitor.py
- [[parse_alert()_1]] - code - gateway/security/wazuh_client.py
- [[read_alerts()]] - code - gateway/security/falco_monitor.py
- [[read_alerts()_1]] - code - gateway/security/wazuh_client.py
- [[test_security_toolchain.py]] - code - gateway/tests/test_security_toolchain.py
- [[wazuh-ossec]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[wazuh_client.py]] - code - gateway/security/wazuh_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LLMProxyproxy_messages_non-streaming
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_system-requirements]]
- 9 edges to [[_COMMUNITY_Skill Project Management (PM) (3)]]
- 8 edges to [[_COMMUNITY_ContextGuard]]
- 7 edges to [[_COMMUNITY_Common Queries]]
- 5 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming) (2)]]
- 4 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_UserSessionManager (3) (2)]]
- 2 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 2 edges to [[_COMMUNITY_PipelineAction (2)]]
- 2 edges to [[_COMMUNITY_OpenClaw Skill Metadata Schema (frontmatter convention)]]
- 2 edges to [[_COMMUNITY_parse_clamscan_output]]
- 2 edges to [[_COMMUNITY_AgentTarget (2)]]
- 1 edge to [[_COMMUNITY_falco-rules.yaml]]
- 1 edge to [[_COMMUNITY_wazuh-ossec.conf]]
- 1 edge to [[_COMMUNITY_SubagentMonitor]]
- 1 edge to [[_COMMUNITY__load_latest_json]]
- 1 edge to [[_COMMUNITY_ADR-001 Transparent Proxy vs Agent Modification]]
- 1 edge to [[_COMMUNITY_AgentShroud™ v0.8.0 Watchtower — Complete Feature List]]

## Top bridge nodes
- [[generate_summary()_2]] - degree 13, connects to 7 communities
- [[test_security_toolchain.py]] - degree 42, connects to 6 communities
- [[falco_monitor.py]] - degree 15, connects to 5 communities
- [[wazuh_client.py]] - degree 13, connects to 4 communities
- [[read_alerts()_1]] - degree 9, connects to 3 communities
