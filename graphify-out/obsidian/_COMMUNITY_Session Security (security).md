---
type: community
cohesion: 0.14
members: 20
---

# Session Security (security)

**Cohesion:** 0.14 - loosely connected
**Members:** 20 nodes

## Members
- [[.__init__()_116]] - code - gateway/security/session_security.py
- [[._fingerprint()]] - code - gateway/security/session_security.py
- [[.cleanup_expired()_3]] - code - gateway/security/session_security.py
- [[.create_session()]] - code - gateway/security/session_security.py
- [[.destroy_session()]] - code - gateway/security/session_security.py
- [[.generate_instruction_nonce()]] - code - gateway/security/session_security.py
- [[.register_event_source()]] - code - gateway/security/session_security.py
- [[.rotate_session()]] - code - gateway/security/session_security.py
- [[.test_cleanup_expired()]] - code - gateway/tests/test_session_security.py
- [[.test_different_ips_not_rate_limited()]] - code - gateway/tests/test_session_security.py
- [[.test_rate_limit_exceeded()_1]] - code - gateway/tests/test_session_security.py
- [[.test_rate_limit_resets_after_window()]] - code - gateway/tests/test_session_security.py
- [[.validate_nonce()]] - code - gateway/security/session_security.py
- [[.validate_session()]] - code - gateway/security/session_security.py
- [[Chen et al. 2026 — Agent configuration vulnerabilities  session hijacking (arXiv2602.14364)]] - paper - gateway/security/consent_framework.py
- [[Generate a single-use, time-bound nonce for an instruction.          Format ``]] - rationale - gateway/security/session_security.py
- [[Return True if the nonce is valid (not replayed, within 5-min window).]] - rationale - gateway/security/session_security.py
- [[SessionManager]] - code - gateway/security/session_security.py
- [[TestRateLimiting_3]] - code - gateway/tests/test_session_security.py
- [[Wang et al. 2026 — Event injection attacks (arXiv2602.08412)]] - paper - gateway/security/session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Session_Security_security
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Session Security]]
- 11 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 2 edges to [[_COMMUNITY_Browser Security]]
- 2 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 2 edges to [[_COMMUNITY_Session Security]]
- 2 edges to [[_COMMUNITY_Session Security]]

## Top bridge nodes
- [[SessionManager]] - degree 40, connects to 5 communities
- [[.create_session()]] - degree 5, connects to 2 communities
- [[TestRateLimiting_3]] - degree 10, connects to 1 community
- [[.validate_session()]] - degree 6, connects to 1 community
- [[.rotate_session()]] - degree 3, connects to 1 community