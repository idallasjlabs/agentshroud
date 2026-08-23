---
type: community
cohesion: 0.28
members: 9
---

# Observatory Mode

**Cohesion:** 0.28 - loosely connected
**Members:** 9 nodes

## Members
- [[.test_auto_revert_restores_enforce()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_revert_task_created_on_put()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_second_put_cancels_previous_task()]] - code - gateway/tests/test_observatory_mode.py
- [[A revert task is created (and is an asyncio.Task).]] - rationale - gateway/tests/test_observatory_mode.py
- [[Auto-revert task sets mode back to enforce after delay.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Second PUT cancels the first revert task.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Set AGENTSHROUD_MODE at runtime with automatic revert to 'enforce'.]] - rationale - gateway/web/api.py
- [[TestAutoRevert]] - code - gateway/tests/test_observatory_mode.py
- [[set_mode()_1]] - code - gateway/web/api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Observatory_Mode
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Killswitch Monitor & Observatory Mode]]
- 5 edges to [[_COMMUNITY_Web Api Coverage]]
- 1 edge to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 1 edge to [[_COMMUNITY_Api (web)]]

## Top bridge nodes
- [[TestAutoRevert]] - degree 8, connects to 3 communities
- [[set_mode()_1]] - degree 7, connects to 3 communities
- [[.test_revert_task_created_on_put()]] - degree 5, connects to 2 communities
- [[.test_auto_revert_restores_enforce()]] - degree 4, connects to 1 community
- [[.test_second_put_cancels_previous_task()]] - degree 4, connects to 1 community