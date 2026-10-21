---
type: community
members: 9
---

# FalcoAlertWatcher (2)

**Members:** 9 nodes

## Members
- [[dot-test_is_agentshroud_rule_false()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_is_agentshroud_rule_true()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_container_info()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_critical_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_valid_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[Check if a rule is AgentShroud-specific.      Args         rule_name Falco rul]] - rationale - gateway/security/falco_monitor.py
- [[TestFalcoParser]] - code - gateway/tests/test_security_toolchain.py
- [[is_agentshroud_rule()]] - code - gateway/security/falco_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FalcoAlertWatcher_2
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 2 edges to [[_COMMUNITY_FalcoAlertWatcher]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]

## Top bridge nodes
- [[TestFalcoParser]] - degree 8, connects to 2 communities
- [[is_agentshroud_rule()]] - degree 7, connects to 2 communities
