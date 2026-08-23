---
type: community
cohesion: 0.11
members: 19
---

# Security Hardening

**Cohesion:** 0.11 - loosely connected
**Members:** 19 nodes

## Members
- [[.setup_method()_28]] - code - gateway/tests/test_security_hardening.py
- [[.teardown_method()_6]] - code - gateway/tests/test_security_hardening.py
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
- [[.test_trust_escalation_attack()]] - code - gateway/tests/test_security_hardening.py
- [[.test_trust_level_progression()]] - code - gateway/tests/test_security_hardening.py
- [[.test_violation_large_decrease()]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManager]] - code - gateway/tests/test_security_hardening.py
- [[Verify you can't jump from UNTRUSTED to FULL in one step.]] - rationale - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Security_Hardening
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Security Hardening]]
- 5 edges to [[_COMMUNITY_Security Regressions V1 2]]
- 3 edges to [[_COMMUNITY_Cross Bot Trust Ledger]]
- 2 edges to [[_COMMUNITY_Security Hardening]]
- 2 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 2 edges to [[_COMMUNITY_Egress Filter]]
- 1 edge to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Egress Filter]]
- 1 edge to [[_COMMUNITY_Egress Filter (security)]]
- 1 edge to [[_COMMUNITY_Pipeline Unit]]
- 1 edge to [[_COMMUNITY_Progressive Trust Integration]]

## Top bridge nodes
- [[TestTrustManager]] - degree 35, connects to 11 communities
- [[.test_trust_escalation_attack()]] - degree 4, connects to 2 communities
- [[.test_trust_level_progression()]] - degree 3, connects to 2 communities
- [[.setup_method()_28]] - degree 2, connects to 1 community
- [[.test_sqlite_persistence()]] - degree 2, connects to 1 community