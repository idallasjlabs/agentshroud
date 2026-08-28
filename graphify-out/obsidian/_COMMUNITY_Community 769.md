---
type: community
cohesion: 0.30
members: 12
---

# Community 769

**Cohesion:** 0.30 - loosely connected
**Members:** 12 nodes

## Members
- [[.test_idempotent_rerun_finds_nothing_left()]] - code - gateway/tests/test_audit_archive.py
- [[.test_missing_db_reported_not_raised()]] - code - gateway/tests/test_audit_archive.py
- [[.test_no_matching_rows_is_a_clean_noop()]] - code - gateway/tests/test_audit_archive.py
- [[.test_processes_in_multiple_batches()]] - code - gateway/tests/test_audit_archive.py
- [[.test_purges_only_matching_event_type_and_severity()]] - code - gateway/tests/test_audit_archive.py
- [[Archive+delete ALL rows matching (event_type, severity), regardless of age.]] - rationale - gateway/security/audit_archive.py
- [[TestPurgeLowValueEvents]] - code - gateway/tests/test_audit_archive.py
- [[_make_mixed_live_db()]] - code - gateway/tests/test_audit_archive.py
- [[n_noisy events of (egress_filter, INFO); n_denies of (egress_filter, HIGH);]] - rationale - gateway/tests/test_audit_archive.py
- [[now()]] - code - gateway/tests/test_audit_archive.py
- [[purge_low_value_events()]] - code - gateway/security/audit_archive.py
- [[test_audit_archive.py]] - code - gateway/tests/test_audit_archive.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_769
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Community 359]]

## Top bridge nodes
- [[purge_low_value_events()]] - degree 10, connects to 1 community
- [[test_audit_archive.py]] - degree 8, connects to 1 community