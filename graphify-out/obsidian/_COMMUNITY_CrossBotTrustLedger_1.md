---
type: community
cohesion: 0.11
members: 18
---

# CrossBotTrustLedger

**Cohesion:** 0.11 - loosely connected
**Members:** 18 nodes

## Members
- [[dot-setup_method()_37]] - code - gateway/tests/test_security_hardening.py
- [[dot-teardown_method()_7]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_action_allowed_basic()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_action_denied_high_trust()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_action_unknown_agent()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_failure_decreases_score()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_get_trust()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_get_trust_unknown()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_history()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_register_agent()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_register_idempotent()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_score_never_negative()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_sqlite_persistence()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_success_increases_score()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_trust_escalation_attack()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_violation_large_decrease()]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManager]] - code - gateway/tests/test_security_hardening.py
- [[Verify you can't jump from UNTRUSTED to FULL in one step.]] - rationale - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CrossBotTrustLedger
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_TrustConfig]]
- 5 edges to [[_COMMUNITY_EgressFilterConfig]]
- 3 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor_1]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig_1]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_outbound.py_1]]
- 1 edge to [[_COMMUNITY_AuditChain]]

## Top bridge nodes
- [[TestTrustManager]] - degree 35, connects to 9 communities
- [[dot-test_trust_escalation_attack()]] - degree 4, connects to 1 community
- [[dot-setup_method()_37]] - degree 2, connects to 1 community
- [[dot-test_sqlite_persistence()]] - degree 2, connects to 1 community
