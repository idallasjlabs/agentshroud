---
type: community
members: 19
---

# CrossBotTrustLedger (2)

**Members:** 19 nodes

## Members
- [[dot-setup_method()_27]] - code - gateway/tests/test_security_hardening.py
- [[dot-teardown_method()_6]] - code - gateway/tests/test_security_hardening.py
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
- [[dot-test_trust_level_progression()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_violation_large_decrease()]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManager]] - code - gateway/tests/test_security_hardening.py
- [[Verify you can't jump from UNTRUSTED to FULL in one step.]] - rationale - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CrossBotTrustLedger_2
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_EgressFilterConfig]]
- 6 edges to [[_COMMUNITY_TrustConfig]]
- 3 edges to [[_COMMUNITY_AgentRegistry]]
- 3 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 2 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_outbound.py]]

## Top bridge nodes
- [[TestTrustManager]] - degree 35, connects to 9 communities
- [[dot-test_trust_escalation_attack()]] - degree 4, connects to 2 communities
- [[dot-test_trust_level_progression()]] - degree 3, connects to 2 communities
- [[dot-setup_method()_27]] - degree 2, connects to 1 community
- [[dot-test_sqlite_persistence()]] - degree 2, connects to 1 community
