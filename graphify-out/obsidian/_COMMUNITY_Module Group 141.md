---
type: community
cohesion: 0.09
members: 34
---

# Module Group 141

**Cohesion:** 0.09 - loosely connected
**Members:** 34 nodes

## Members
- [[.test_categorize_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_categorize_mixed()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_is_agentshroud_rule_false()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_is_agentshroud_rule_true()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_container_info()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_critical_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_empty_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_valid_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_read_alerts_missing_dir()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_clean()_2]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_clean()_3]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_top_rules()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_with_alerts()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_with_rootkit()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_35]] - code - gateway/security/falco_monitor.py
- [[Categorize alerts by severity.      Args         alerts List of parsed alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Check if a rule is AgentShroud-specific.      Args         rule_name Falco rul]] - rationale - gateway/security/falco_monitor.py
- [[Extend AGENTSHROUD_RULES with bot-specific name prefixes.      Called at gateway]] - rationale - gateway/security/falco_monitor.py
- [[Generate a summary dict suitable for the health report.      Args         alert]] - rationale - gateway/security/falco_monitor.py
- [[Parse a single Falco alert.      Args         raw Raw Falco alert JSON.      R]] - rationale - gateway/security/falco_monitor.py
- [[Read Falco alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/falco_monitor.py
- [[TestFalcoCategorize]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[TestWazuhSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[categorize_alerts()]] - code - gateway/security/falco_monitor.py
- [[configure_rules()]] - code - gateway/security/falco_monitor.py
- [[datetime_1]] - code - gateway/security/falco_monitor.py
- [[falco_monitor.py]] - code - gateway/security/falco_monitor.py
- [[generate_summary()_1]] - code - gateway/security/falco_monitor.py
- [[is_agentshroud_rule()]] - code - gateway/security/falco_monitor.py
- [[parse_alert()]] - code - gateway/security/falco_monitor.py
- [[read_alerts()]] - code - gateway/security/falco_monitor.py
- [[test_security_toolchain.py]] - code - gateway/tests/test_security_toolchain.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_141
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Module Group 114]]
- 7 edges to [[_COMMUNITY_Module Group 155]]
- 6 edges to [[_COMMUNITY_Module Group 163]]
- 5 edges to [[_COMMUNITY_Alert Dispatcher]]
- 5 edges to [[_COMMUNITY_Module Group 153]]
- 4 edges to [[_COMMUNITY_Module Group 242]]
- 3 edges to [[_COMMUNITY_Module Group 176]]
- 2 edges to [[_COMMUNITY_Security Scanner Integration]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 1 edge to [[_COMMUNITY_Module Group 324]]
- 1 edge to [[_COMMUNITY_Module Group 286]]

## Top bridge nodes
- [[test_security_toolchain.py]] - degree 42, connects to 8 communities
- [[falco_monitor.py]] - degree 11, connects to 4 communities
- [[read_alerts()]] - degree 10, connects to 2 communities
- [[TestFalcoParser]] - degree 8, connects to 1 community
- [[generate_summary()_1]] - degree 7, connects to 1 community
