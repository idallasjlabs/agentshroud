---
type: community
cohesion: 0.12
members: 16
---

# soc/router.py (2)

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[dot-setup_method()_31]] - code - gateway/tests/test_security_hardening.py
- [[dot-teardown_method()_7]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_action_allowed_basic()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_action_denied_high_trust()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_action_unknown_agent()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_failure_decreases_score()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_get_trust()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_get_trust_unknown()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_history()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_register_agent()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_register_idempotent()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_score_never_negative()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_sqlite_persistence()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_success_increases_score()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_violation_large_decrease()]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManager]] - code - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/soc/routerpy_2
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_socrouter.py]]
- 5 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 4 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 3 edges to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 1 edge to [[_COMMUNITY_PromptGuard]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]

## Top bridge nodes
- [[TestTrustManager]] - degree 35, connects to 7 communities
- [[dot-setup_method()_31]] - degree 2, connects to 1 community
- [[dot-test_sqlite_persistence()]] - degree 2, connects to 1 community
