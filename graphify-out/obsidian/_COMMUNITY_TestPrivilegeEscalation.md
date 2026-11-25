---
type: community
members: 14
---

# TestPrivilegeEscalation

**Members:** 14 nodes

## Members
- [[dot-test_consent_required_for_sensitive_ops()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_session_cannot_impersonate()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_subagent_monitor_tracks_events()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_trust_cannot_exceed_max()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_unregistered_agent_blocked()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_violation_drops_trust_significantly()]] - code - gateway/tests/test_security_audit_advanced.py
- [[A single violation should meaningfully impact trust.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Consent framework should be available for gating.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Different sessions should have different identities.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Subagent events should be trackable.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test trust boundaries and privilege escalation prevention.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestPrivilegeEscalation]] - code - gateway/tests/test_security_audit_advanced.py
- [[Trust score should have an upper bound.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Unregistered agents should not be trusted.]] - rationale - gateway/tests/test_security_audit_advanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestPrivilegeEscalation
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_Session]]
- 1 edge to [[_COMMUNITY_TestHTTPSecurity]]
- 1 edge to [[_COMMUNITY_test_all_modules_enforce.py]]
- 1 edge to [[_COMMUNITY_ServerConfig]]

## Top bridge nodes
- [[TestPrivilegeEscalation]] - degree 12, connects to 5 communities
- [[dot-test_session_cannot_impersonate()]] - degree 3, connects to 1 community
- [[dot-test_trust_cannot_exceed_max()]] - degree 3, connects to 1 community
- [[dot-test_unregistered_agent_blocked()]] - degree 3, connects to 1 community
- [[dot-test_violation_drops_trust_significantly()]] - degree 3, connects to 1 community
