---
type: community
cohesion: 0.33
members: 6
---

# TestSessionValidation

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[dot-test_expired_session_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_unknown_session_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_valid_session_accepted()]] - code - gateway/tests/test_session_security.py
- [[dot-test_wrong_ip_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_wrong_user_agent_rejected()]] - code - gateway/tests/test_session_security.py
- [[TestSessionValidation]] - code - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSessionValidation
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_SessionError]]
- 2 edges to [[_COMMUNITY_SessionManager]]

## Top bridge nodes
- [[TestSessionValidation]] - degree 12, connects to 2 communities
- [[dot-test_expired_session_rejected()]] - degree 2, connects to 1 community
