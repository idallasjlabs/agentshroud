---
type: community
members: 8
---

# .record_activity

**Members:** 8 nodes

## Members
- [[dot-_append_contributor_log()]] - code - gateway/security/collaborator_tracker.py
- [[dot-_normalize_preview()]] - code - gateway/security/collaborator_tracker.py
- [[dot-_normalize_username()]] - code - gateway/security/collaborator_tracker.py
- [[dot-record_activity()]] - code - gateway/security/collaborator_tracker.py
- [[Append one activity entry for any tracked collaborator or the owner. Args…]] - rationale - gateway/security/collaborator_tracker.py
- [[Mirror activity into workspace contributor logs used by daily digests.]] - rationale - gateway/security/collaborator_tracker.py
- [[Normalize previews to single-line safe text for JSONL + markdown mirrors.]] - rationale - gateway/security/collaborator_tracker.py
- [[Normalize username for safe contributor-log tokenization.]] - rationale - gateway/security/collaborator_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/record_activity
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_CollaboratorActivityTracker]]
- 1 edge to [[_COMMUNITY_test_lifespan_prune.py]]

## Top bridge nodes
- [[dot-record_activity()]] - degree 6, connects to 2 communities
- [[dot-_append_contributor_log()]] - degree 3, connects to 1 community
- [[dot-_normalize_preview()]] - degree 3, connects to 1 community
- [[dot-_normalize_username()]] - degree 3, connects to 1 community
