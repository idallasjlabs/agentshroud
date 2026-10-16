---
type: community
cohesion: 0.29
members: 11
---

# TestCollabLockdownNotifications

**Cohesion:** 0.29 - loosely connected
**Members:** 11 nodes

## Members
- [[dot-_setup_proxy_with_capture()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_collab_notified_at_alert_threshold()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_collab_notified_at_escalated_threshold()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_collab_notified_at_suspended_threshold()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_collab_notified_only_once_per_level()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_no_collab_notice_below_alert()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_owner_also_notified_on_threshold()]] - code - gateway/tests/test_progressive_lockdown.py
- [[Owner should receive an escalation notice on the 3rd block.]] - rationale - gateway/tests/test_progressive_lockdown.py
- [[TestCollabLockdownNotifications]] - code - gateway/tests/test_progressive_lockdown.py
- [[The 4th block stays at ALERT but must NOT fire a second notification.]] - rationale - gateway/tests/test_progressive_lockdown.py
- [[Verify _quarantine_blocked_message sends threshold warnings to the collaborator.]] - rationale - gateway/tests/test_progressive_lockdown.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestCollabLockdownNotifications
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_2]]

## Top bridge nodes
- [[TestCollabLockdownNotifications]] - degree 12, connects to 2 communities
- [[dot-_setup_proxy_with_capture()]] - degree 8, connects to 1 community
