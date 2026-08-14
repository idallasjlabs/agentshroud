---
source_file: "gateway/tests/test_audit_archive.py"
type: "code"
community: "Architecture Docs"
location: "L66"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Architecture_Docs
---

# TestArchiveOldEvents

## Connections
- [[.test_archived_rows_preserved_verbatim()]] - `method` [EXTRACTED]
- [[.test_archives_only_events_older_than_cutoff()]] - `method` [EXTRACTED]
- [[.test_live_forward_chain_still_valid_after_archival()]] - `method` [EXTRACTED]
- [[.test_missing_db_is_reported_not_raised()]] - `method` [EXTRACTED]
- [[.test_no_events_to_archive_is_a_noop()]] - `method` [EXTRACTED]
- [[.test_no_vacuum_flag_skips_vacuum()]] - `method` [EXTRACTED]
- [[.test_running_twice_is_idempotent()]] - `method` [EXTRACTED]
- [[.test_vacuum_failure_does_not_discard_a_successful_archive()]] - `method` [EXTRACTED]
- [[.test_vacuum_reduces_file_size_after_bulk_delete()]] - `method` [EXTRACTED]
- [[.test_waits_out_a_concurrent_writer_lock_instead_of_failing()]] - `method` [EXTRACTED]
- [[test_audit_archive.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Architecture_Docs