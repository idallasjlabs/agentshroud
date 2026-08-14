---
source_file: "gateway/security/audit_archive.py"
type: "code"
community: "Architecture Docs"
location: "L46"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Architecture_Docs
---

# archive_old_events()

## Connections
- [[.test_archived_rows_preserved_verbatim()]] - `calls` [EXTRACTED]
- [[.test_archives_only_events_older_than_cutoff()]] - `calls` [EXTRACTED]
- [[.test_live_forward_chain_still_valid_after_archival()]] - `calls` [EXTRACTED]
- [[.test_missing_db_is_reported_not_raised()]] - `calls` [EXTRACTED]
- [[.test_no_events_to_archive_is_a_noop()]] - `calls` [EXTRACTED]
- [[.test_no_vacuum_flag_skips_vacuum()]] - `calls` [EXTRACTED]
- [[.test_running_twice_is_idempotent()]] - `calls` [EXTRACTED]
- [[.test_vacuum_failure_does_not_discard_a_successful_archive()]] - `calls` [EXTRACTED]
- [[.test_vacuum_reduces_file_size_after_bulk_delete()]] - `calls` [EXTRACTED]
- [[.test_waits_out_a_concurrent_writer_lock_instead_of_failing()]] - `calls` [EXTRACTED]
- [[Move audit_events older than cutoff_days into archive_path, then delete + VACUUM]] - `rationale_for` [EXTRACTED]
- [[Path_6]] - `references` [EXTRACTED]
- [[_cli()]] - `calls` [EXTRACTED]
- [[audit_archive.py]] - `contains` [EXTRACTED]
- [[datetime_1]] - `references` [EXTRACTED]
- [[test_audit_archive.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Architecture_Docs