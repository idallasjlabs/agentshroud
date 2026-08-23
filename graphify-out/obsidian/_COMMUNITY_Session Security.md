---
type: community
cohesion: 0.33
members: 6
---

# Session Security

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_expired_session_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_unknown_session_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_valid_session_accepted()]] - code - gateway/tests/test_session_security.py
- [[.test_wrong_ip_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_wrong_user_agent_rejected()]] - code - gateway/tests/test_session_security.py
- [[TestSessionValidation]] - code - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Session_Security
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Session Security]]
- 2 edges to [[_COMMUNITY_Session Security (security)]]

## Top bridge nodes
- [[TestSessionValidation]] - degree 12, connects to 2 communities
- [[.test_expired_session_rejected()]] - degree 2, connects to 1 community