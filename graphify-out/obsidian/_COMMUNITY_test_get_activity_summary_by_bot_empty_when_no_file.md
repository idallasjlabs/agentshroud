---
type: community
members: 2
---

# test_get_activity_summary_by_bot_empty_when_no_file

**Members:** 2 nodes

## Members
- [[get_activity_summary returns empty by_bot when no log file exists.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[test_get_activity_summary_by_bot_empty_when_no_file()]] - code - gateway/tests/test_collaborator_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_get_activity_summary_by_bot_empty_when_no_file
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]

## Top bridge nodes
- [[test_get_activity_summary_by_bot_empty_when_no_file()]] - degree 2, connects to 1 community
