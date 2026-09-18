---
type: community
cohesion: 0.17
members: 12
---

# TestWebSocketHandshakeAuth

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[.test_ws_activity_rejects_bad_token()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_activity_rejects_no_token()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_approvals_rejects_bad_token()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_approvals_rejects_master_token()]] - code - gateway/tests/test_security_fixes.py
- [[.test_ws_approvals_rejects_no_token()]] - code - gateway/tests/test_security_fixes.py
- [[TestWebSocketHandshakeAuth]] - code - gateway/tests/test_security_fixes.py
- [[WS wsactivity closes immediately without token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsactivity closes with bad token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsapprovals closes immediately without token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsapprovals closes with bad token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsapprovals rejects the master auth token -- R3-L4 removed the         mast]] - rationale - gateway/tests/test_security_fixes.py
- [[WebSocket endpoints must validate token during handshake, not first message]] - rationale - gateway/tests/test_security_fixes.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestWebSocketHandshakeAuth
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_SSHProxy]]
- 2 edges to [[_COMMUNITY_test_dashboard.py]]

## Top bridge nodes
- [[TestWebSocketHandshakeAuth]] - degree 12, connects to 2 communities