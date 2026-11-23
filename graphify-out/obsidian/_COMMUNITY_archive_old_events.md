---
type: community
members: 43
---

# archive_old_events

**Members:** 43 nodes

## Members
- [[dot-db()]] - code - gateway/inbound_edge/store.py
- [[dot-test_archived_rows_preserved_verbatim()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_archives_only_events_older_than_cutoff()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_idempotent_rerun_finds_nothing_left()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_live_forward_chain_still_valid_after_archival()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_missing_db_is_reported_not_raised()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_missing_db_reported_not_raised()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_no_events_to_archive_is_a_noop()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_no_matching_rows_is_a_clean_noop()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_no_vacuum_flag_skips_vacuum()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_processes_in_multiple_batches()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_purges_only_matching_event_type_and_severity()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_running_twice_is_idempotent()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_vacuum_failure_does_not_discard_a_successful_archive()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_vacuum_reduces_file_size_after_bulk_delete()]] - code - gateway/tests/test_audit_archive.py
- [[dot-test_waits_out_a_concurrent_writer_lock_instead_of_failing()]] - code - gateway/tests/test_audit_archive.py
- [[A full disk (or any VACUUM-specific OperationalError) must not raise past a…]] - rationale - gateway/tests/test_audit_archive.py
- [[Archive+delete ALL rows matching (event_type, severity), regardless of age. For…]] - rationale - gateway/security/audit_archive.py
- [[Build n chained events, oldest first, spaced spacing_days apart ending at…]] - rationale - gateway/tests/test_audit_archive.py
- [[Connection_2]] - code
- [[Move audit_events older than cutoff_days into archive_path, then delete +…]] - rationale - gateway/security/audit_archive.py
- [[Path_43]] - code
- [[TestArchiveOldEvents]] - code - gateway/tests/test_audit_archive.py
- [[TestPurgeLowValueEvents]] - code - gateway/tests/test_audit_archive.py
- [[The remaining live rows' own internal chain (row N's prev_hash == row N-1's…]] - rationale - gateway/tests/test_audit_archive.py
- [[_chain_events()]] - code - gateway/tests/test_audit_archive.py
- [[_cli()]] - code - gateway/security/audit_archive.py
- [[_make_live_db()]] - code - gateway/tests/test_audit_archive.py
- [[_make_mixed_live_db()]] - code - gateway/tests/test_audit_archive.py
- [[archive_old_events()]] - code - gateway/security/audit_archive.py
- [[audit.db uses SQLite's default DELETE journal mode, which requires an exclusive…]] - rationale - gateway/tests/test_audit_archive.py
- [[audit_archive.py]] - code - gateway/security/audit_archive.py
- [[datetime_5]] - code
- [[events list of (event_id, timestamp, prev_hash, entry_hash).]] - rationale - gateway/tests/test_audit_archive.py
- [[execute()]] - code - gateway/tests/test_audit_archive.py
- [[failing_vacuum_connect()]] - code - gateway/tests/test_audit_archive.py
- [[fixture_97]] - code
- [[hold_write_lock()]] - code - gateway/tests/test_audit_archive.py
- [[n_noisy events of (egress_filter, INFO); n_denies of (egress_filter, HIGH);…]] - rationale - gateway/tests/test_audit_archive.py
- [[now()_8]] - code - gateway/tests/test_audit_archive.py
- [[purge_low_value_events()]] - code - gateway/security/audit_archive.py
- [[release_after_delay()]] - code - gateway/tests/test_audit_archive.py
- [[test_audit_archive.py]] - code - gateway/tests/test_audit_archive.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/archive_old_events
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_EdgeStore]]

## Top bridge nodes
- [[dot-db()]] - degree 3, connects to 1 community
