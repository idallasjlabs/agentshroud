---
type: community
cohesion: 0.33
members: 6
---

# Community 1181

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[dot-test_collaborator_archive_exfil_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_cross_user_messaging_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_scheduler_autorun_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Archivebulk-export exfil prompts should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator requests to message other users should be blockedquarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator schedulerautorun requests should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1181
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Telegram Proxy Inbound Tests]]
- 3 edges to [[_COMMUNITY_Telegram Lockdown & Collaborator UX Tests]]

## Top bridge nodes
- [[dot-test_collaborator_cross_user_messaging_request_is_blocked_and_quarantined()]] - degree 8, connects to 2 communities
- [[dot-test_collaborator_scheduler_autorun_request_is_blocked_and_quarantined()]] - degree 8, connects to 2 communities
- [[dot-test_collaborator_archive_exfil_request_is_blocked_and_quarantined()]] - degree 7, connects to 2 communities