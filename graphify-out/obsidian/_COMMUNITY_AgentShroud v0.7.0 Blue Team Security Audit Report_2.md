---
type: community
cohesion: 0.33
members: 6
---

# AgentShroud v0.7.0 Blue Team Security Audit Report

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[dot-test_unknown_event_source_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_unregistered_session_event_rejected()]] - code - gateway/tests/test_session_security.py
- [[dot-test_valid_event_source_accepted()]] - code - gateway/tests/test_session_security.py
- [[TestEventInjection]] - code - gateway/tests/test_session_security.py
- [[manager()]] - code - gateway/tests/test_session_security.py
- [[test_session_security.py]] - code - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_v070_Blue_Team_Security_Audit_Report
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_SessionManager]]
- 5 edges to [[_COMMUNITY_SessionManager_1]]
- 1 edge to [[_COMMUNITY_TestInstructionNonce]]
- 1 edge to [[_COMMUNITY_AgentShroud v0.7.0 Blue Team Security Audit Report_3]]
- 1 edge to [[_COMMUNITY_test_prompt_guard.py_1]]

## Top bridge nodes
- [[test_session_security.py]] - degree 10, connects to 5 communities
- [[TestEventInjection]] - degree 10, connects to 2 communities
- [[manager()]] - degree 2, connects to 1 community
