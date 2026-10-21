---
type: community
members: 48
---

# LLMProxy.proxy_messages (non-streaming)

**Members:** 48 nodes

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
- [[dot-test_summary_top_rules()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_with_alerts()]] - code - gateway/tests/test_security_toolchain.py
- [[Alert Levels]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Any_12]] - code - gateway/security/falco_monitor.py
- [[Categorize alerts by severity.      Args         alerts List of parsed alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Check if a rule is AgentShroud-specific.      Args         rule_name Falco rul]] - rationale - gateway/security/falco_monitor.py
- [[Extend AGENTSHROUD_RULES with bot-specific name prefixes.      Called at gateway]] - rationale - gateway/security/falco_monitor.py
- [[Generate a summary dict suitable for the health report.      Args         alert]] - rationale - gateway/security/falco_monitor.py
- [[Integration_1]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Integration with Gateway]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Key OSSEC Config Sections (Inferred)]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Network Enforcement]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Parse a single Falco alert.      Args         raw Raw Falco alert JSON.      R]] - rationale - gateway/security/falco_monitor.py
- [[Priority Levels]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Purpose_61]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Purpose_62]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Read Falco alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/falco_monitor.py
- [[Related Notes_23]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Related Notes_24]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Relationship to Other Security Modules]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Rules Defined]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Shell Spawning Exceptions]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[TestFalcoCategorize]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[What Wazuh Monitors in AgentShroud]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[categorize_alerts()]] - code - gateway/security/falco_monitor.py
- [[configure_rules()]] - code - gateway/security/falco_monitor.py
- [[datetime]] - code - gateway/security/falco_monitor.py
- [[falco-rules]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[falco-rules.yaml]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[falco_monitor.py]] - code - gateway/security/falco_monitor.py
- [[generate_summary()_1]] - code - gateway/security/falco_monitor.py
- [[is_agentshroud_rule()]] - code - gateway/security/falco_monitor.py
- [[parse_alert()]] - code - gateway/security/falco_monitor.py
- [[read_alerts()]] - code - gateway/security/falco_monitor.py
- [[wazuh-ossec.conf]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[wazuh-ossec]] - document - docs/vault/03 - Configuration/wazuh-ossec.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LLMProxyproxy_messages_non-streaming
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_TestVersionRoutes]]
- 4 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming) (2)]]
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_system-requirements]]
- 2 edges to [[_COMMUNITY_test_playback_state.c]]
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY__wrap_response()]]
- 1 edge to [[_COMMUNITY_UserSessionManager (3) (2)]]
- 1 edge to [[_COMMUNITY_MCPPolicyEngine]]

## Top bridge nodes
- [[falco_monitor.py]] - degree 15, connects to 6 communities
- [[read_alerts()]] - degree 10, connects to 3 communities
- [[generate_summary()_1]] - degree 8, connects to 3 communities
- [[wazuh-ossec]] - degree 6, connects to 3 communities
- [[TestFalcoParser]] - degree 8, connects to 2 communities
