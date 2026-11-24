---
type: community
members: 24
---

# TestAuth

**Members:** 24 nodes

## Members
- [[dot-rotate_session()]] - code - gateway/security/session_security.py
- [[dot-test_agent_registry_module()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_consent_framework_loads()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_oauth_confused_deputy()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_oauth_pkce_violation()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_reject_empty_token()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_reject_garbage_token()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_reject_malformed_jwt()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_reject_none_algorithm()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_session_binding()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_session_different_fingerprints()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_session_rate_limit()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_trust_level_enforcement()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_trust_recovery()]] - code - gateway/tests/test_security_audit.py
- [[Agent registry should be importable.]] - rationale - gateway/tests/test_security_audit.py
- [[Different fingerprints should create different sessions.]] - rationale - gateway/tests/test_security_audit.py
- [[Low-trust agents should be blocked from high-risk actions.]] - rationale - gateway/tests/test_security_audit.py
- [[Reject JWTs with alg=none (classic attack).]] - rationale - gateway/tests/test_security_audit.py
- [[Session]] - code - gateway/security/session_security.py
- [[Session must bind to user identity.]] - rationale - gateway/tests/test_security_audit.py
- [[Test authentication and authorization enforcement.]] - rationale - gateway/tests/test_security_audit.py
- [[TestAuth]] - code - gateway/tests/test_security_audit.py
- [[Trust should recover after good behavior.]] - rationale - gateway/tests/test_security_audit.py
- [[t_session()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAuth
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_TrustManager]]
- 4 edges to [[_COMMUNITY_SessionManager]]
- 4 edges to [[_COMMUNITY_test_security_audit.py]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 1 edge to [[_COMMUNITY_SubagentMonitor]]
- 1 edge to [[_COMMUNITY_ServerConfig]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY_TokenValidator]]

## Top bridge nodes
- [[TestAuth]] - degree 22, connects to 6 communities
- [[Session]] - degree 14, connects to 6 communities
- [[dot-rotate_session()]] - degree 3, connects to 1 community
- [[dot-test_trust_level_enforcement()]] - degree 3, connects to 1 community
- [[dot-test_trust_recovery()]] - degree 3, connects to 1 community
