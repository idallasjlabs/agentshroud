---
type: community
cohesion: 0.12
members: 36
---

# Audit Archive

**Cohesion:** 0.12 - loosely connected
**Members:** 36 nodes

## Members
- [[.test_archived_rows_preserved_verbatim()]] - code - gateway/tests/test_audit_archive.py
- [[.test_archives_only_events_older_than_cutoff()]] - code - gateway/tests/test_audit_archive.py
- [[.test_idempotent_rerun_finds_nothing_left()]] - code - gateway/tests/test_audit_archive.py
- [[.test_live_forward_chain_still_valid_after_archival()]] - code - gateway/tests/test_audit_archive.py
- [[.test_missing_db_is_reported_not_raised()]] - code - gateway/tests/test_audit_archive.py
- [[.test_missing_db_reported_not_raised()]] - code - gateway/tests/test_audit_archive.py
- [[.test_no_events_to_archive_is_a_noop()]] - code - gateway/tests/test_audit_archive.py
- [[.test_no_matching_rows_is_a_clean_noop()]] - code - gateway/tests/test_audit_archive.py
- [[.test_no_vacuum_flag_skips_vacuum()]] - code - gateway/tests/test_audit_archive.py
- [[.test_processes_in_multiple_batches()]] - code - gateway/tests/test_audit_archive.py
- [[.test_purges_only_matching_event_type_and_severity()]] - code - gateway/tests/test_audit_archive.py
- [[.test_running_twice_is_idempotent()]] - code - gateway/tests/test_audit_archive.py
- [[.test_vacuum_failure_does_not_discard_a_successful_archive()]] - code - gateway/tests/test_audit_archive.py
- [[.test_vacuum_reduces_file_size_after_bulk_delete()]] - code - gateway/tests/test_audit_archive.py
- [[.test_waits_out_a_concurrent_writer_lock_instead_of_failing()]] - code - gateway/tests/test_audit_archive.py
- [[A full disk (or any VACUUM-specific OperationalError) must not         raise pas]] - rationale - gateway/tests/test_audit_archive.py
- [[Archive+delete ALL rows matching (event_type, severity), regardless of age.]] - rationale - gateway/security/audit_archive.py
- [[Build n chained events, oldest first, spaced spacing_days apart ending at `start]] - rationale - gateway/tests/test_audit_archive.py
- [[Move audit_events older than cutoff_days into archive_path, then delete + VACUUM]] - rationale - gateway/security/audit_archive.py
- [[Path_6]] - code - gateway/security/audit_archive.py
- [[TestArchiveOldEvents]] - code - gateway/tests/test_audit_archive.py
- [[TestPurgeLowValueEvents]] - code - gateway/tests/test_audit_archive.py
- [[The remaining live rows' own internal chain (row N's prev_hash ==         row N-]] - rationale - gateway/tests/test_audit_archive.py
- [[_chain_events()]] - code - gateway/tests/test_audit_archive.py
- [[_cli()]] - code - gateway/security/audit_archive.py
- [[_make_live_db()]] - code - gateway/tests/test_audit_archive.py
- [[_make_mixed_live_db()]] - code - gateway/tests/test_audit_archive.py
- [[archive_old_events()]] - code - gateway/security/audit_archive.py
- [[audit.db uses SQLite's default DELETE journal mode, which requires         an ex]] - rationale - gateway/tests/test_audit_archive.py
- [[audit_archive.py]] - code - gateway/security/audit_archive.py
- [[datetime_1]] - code - gateway/security/audit_archive.py
- [[events list of (event_id, timestamp, prev_hash, entry_hash).]] - rationale - gateway/tests/test_audit_archive.py
- [[n_noisy events of (egress_filter, INFO); n_denies of (egress_filter, HIGH);]] - rationale - gateway/tests/test_audit_archive.py
- [[now()]] - code - gateway/tests/test_audit_archive.py
- [[purge_low_value_events()]] - code - gateway/security/audit_archive.py
- [[test_audit_archive.py]] - code - gateway/tests/test_audit_archive.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Audit_Archive
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Audit Export]]

## Top bridge nodes
- [[archive_old_events()]] - degree 17, connects to 1 community