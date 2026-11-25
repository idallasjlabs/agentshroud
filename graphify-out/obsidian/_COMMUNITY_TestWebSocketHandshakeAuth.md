---
type: community
members: 16
---

# TestWebSocketHandshakeAuth

**Members:** 16 nodes

## Members
- [[dot-test_ws_activity_accepts_valid_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_activity_rejects_bad_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_activity_rejects_no_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_approvals_accepts_valid_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_approvals_rejects_bad_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_approvals_rejects_master_token()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_ws_approvals_rejects_no_token()]] - code - gateway/tests/test_security_fixes.py
- [[TestWebSocketHandshakeAuth]] - code - gateway/tests/test_security_fixes.py
- [[WS wsactivity accepts valid scoped WS token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsactivity closes immediately without token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsactivity closes with bad token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsapprovals accepts valid scoped WS token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsapprovals closes immediately without token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsapprovals closes with bad token]] - rationale - gateway/tests/test_security_fixes.py
- [[WS wsapprovals rejects the master auth token -- R3-L4 removed the master-…]] - rationale - gateway/tests/test_security_fixes.py
- [[WebSocket endpoints must validate token during handshake, not first message]] - rationale - gateway/tests/test_security_fixes.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestWebSocketHandshakeAuth
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_ingest_apiconfig.py]]

## Top bridge nodes
- [[TestWebSocketHandshakeAuth]] - degree 9, connects to 1 community
- [[dot-test_ws_activity_accepts_valid_token()]] - degree 3, connects to 1 community
- [[dot-test_ws_approvals_accepts_valid_token()]] - degree 3, connects to 1 community
