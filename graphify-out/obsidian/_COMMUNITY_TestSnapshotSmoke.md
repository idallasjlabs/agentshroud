---
type: community
members: 6
---

# TestSnapshotSmoke

**Members:** 6 nodes

## Members
- [[dot-test_hermes_snapshot_zero_new()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_live_registry_is_idempotent_no_new_backlog()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_openclaw_snapshot_registers_backlog_as_under_review()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[Re-running against the LIVE registry adds nothing (backlog already synced).]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestSnapshotSmoke]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[The committed snapshot yields a real backlog, all honest under_review. Diffs…]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSnapshotSmoke
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY__sync]]
- 1 edge to [[_COMMUNITY_test_sync_cve_registry_ghsa.py]]

## Top bridge nodes
- [[TestSnapshotSmoke]] - degree 4, connects to 1 community
- [[dot-test_live_registry_is_idempotent_no_new_backlog()]] - degree 3, connects to 1 community
- [[dot-test_openclaw_snapshot_registers_backlog_as_under_review()]] - degree 3, connects to 1 community
- [[dot-test_hermes_snapshot_zero_new()]] - degree 2, connects to 1 community
