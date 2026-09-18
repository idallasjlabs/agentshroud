---
type: community
cohesion: 0.33
members: 6
---

# .test_collaborator_cross_user_messaging_request_

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_collaborator_archive_exfil_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_cross_user_messaging_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_scheduler_autorun_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Archivebulk-export exfil prompts should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator requests to message other users should be blockedquarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator schedulerautorun requests should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_collaborator_cross_user_messaging_request_
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 3 edges to [[_COMMUNITY__wrap_response()]]

## Top bridge nodes
- [[.test_collaborator_cross_user_messaging_request_is_blocked_and_quarantined()]] - degree 8, connects to 2 communities
- [[.test_collaborator_scheduler_autorun_request_is_blocked_and_quarantined()]] - degree 8, connects to 2 communities
- [[.test_collaborator_archive_exfil_request_is_blocked_and_quarantined()]] - degree 7, connects to 2 communities