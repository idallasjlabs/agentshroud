---
type: community
cohesion: 0.33
members: 6
---

# AgentShroud v0.7.0 Blue Team Security Audit Report

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
TABLE source_file, type FROM #community/AgentShroud_v070_Blue_Team_Security_Audit_Report
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_SessionManager]]
- 3 edges to [[_COMMUNITY_SessionManager_1]]
- 1 edge to [[_COMMUNITY_AgentShroud v0.7.0 Blue Team Security Audit Report_2]]

## Top bridge nodes
- [[TestSessionValidation]] - degree 12, connects to 3 communities
- [[dot-test_expired_session_rejected()]] - degree 2, connects to 1 community
