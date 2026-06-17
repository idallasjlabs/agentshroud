---
type: community
cohesion: 0.12
members: 16
---

# Module Group 285

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[.setup_method()_25]] - code - gateway/tests/test_security_hardening.py
- [[.teardown_method()_5]] - code - gateway/tests/test_security_hardening.py
- [[.test_action_allowed_basic()]] - code - gateway/tests/test_security_hardening.py
- [[.test_action_denied_high_trust()]] - code - gateway/tests/test_security_hardening.py
- [[.test_action_unknown_agent()]] - code - gateway/tests/test_security_hardening.py
- [[.test_failure_decreases_score()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_trust()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_trust_unknown()]] - code - gateway/tests/test_security_hardening.py
- [[.test_history()]] - code - gateway/tests/test_security_hardening.py
- [[.test_register_agent()]] - code - gateway/tests/test_security_hardening.py
- [[.test_register_idempotent()]] - code - gateway/tests/test_security_hardening.py
- [[.test_score_never_negative()]] - code - gateway/tests/test_security_hardening.py
- [[.test_sqlite_persistence()]] - code - gateway/tests/test_security_hardening.py
- [[.test_success_increases_score()]] - code - gateway/tests/test_security_hardening.py
- [[.test_violation_large_decrease()]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManager]] - code - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_285
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 4 edges to [[_COMMUNITY_Module Group 79]]
- 3 edges to [[_COMMUNITY_Agent Isolation & Container Config]]
- 2 edges to [[_COMMUNITY_Alert Dispatcher]]
- 1 edge to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 1 edge to [[_COMMUNITY_Egress Filter & Approval]]
- 1 edge to [[_COMMUNITY_Module Group 88]]
- 1 edge to [[_COMMUNITY_Module Group 71]]
- 1 edge to [[_COMMUNITY_Module Group 66]]
- 1 edge to [[_COMMUNITY_Context Guard & Integrity]]

## Top bridge nodes
- [[TestTrustManager]] - degree 35, connects to 10 communities
- [[.setup_method()_25]] - degree 2, connects to 1 community
- [[.test_sqlite_persistence()]] - degree 2, connects to 1 community