---
type: community
cohesion: 0.12
members: 16
---

# TrustConfig

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[dot-setup_method()_36]] - code - gateway/tests/test_security_hardening.py
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
TABLE source_file, type FROM #community/TrustConfig
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_PIIConfig]]
- 6 edges to [[_COMMUNITY_EgressFilterConfig]]
- 4 edges to [[_COMMUNITY_AlertDispatcher]]
- 3 edges to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_AuditChain]]

## Top bridge nodes
- [[TestTrustManager]] - degree 35, connects to 6 communities
- [[dot-setup_method()_36]] - degree 2, connects to 1 community
- [[dot-test_sqlite_persistence()]] - degree 2, connects to 1 community
