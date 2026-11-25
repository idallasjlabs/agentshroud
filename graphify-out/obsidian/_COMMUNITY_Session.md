---
type: community
members: 7
---

# Session

**Members:** 7 nodes

## Members
- [[dot-test_session_binding()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_session_different_fingerprints()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_session_rate_limit()]] - code - gateway/tests/test_security_audit.py
- [[Different fingerprints should create different sessions.]] - rationale - gateway/tests/test_security_audit.py
- [[Session]] - code - gateway/security/session_security.py
- [[Session must bind to user identity.]] - rationale - gateway/tests/test_security_audit.py
- [[t_session()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Session
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_SessionManager]]
- 3 edges to [[_COMMUNITY_TestAuth]]
- 2 edges to [[_COMMUNITY_TestPrivilegeEscalation]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[Session]] - degree 14, connects to 7 communities
- [[dot-test_session_binding()]] - degree 3, connects to 1 community
- [[dot-test_session_different_fingerprints()]] - degree 3, connects to 1 community
- [[t_session()]] - degree 2, connects to 1 community
- [[dot-test_session_rate_limit()]] - degree 2, connects to 1 community
