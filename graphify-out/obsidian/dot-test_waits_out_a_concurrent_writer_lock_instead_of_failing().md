---
source_file: "gateway/tests/test_audit_archive.py"
type: "code"
community: "archive_old_events"
location: "L195"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/archive_old_events
---

# .test_waits_out_a_concurrent_writer_lock_instead_of_failing()

## Connections
- [[TestArchiveOldEvents]] - `method` [EXTRACTED]
- [[_chain_events()]] - `calls` [EXTRACTED]
- [[_make_live_db()]] - `calls` [EXTRACTED]
- [[archive_old_events()]] - `calls` [EXTRACTED]
- [[audit.db uses SQLite's default DELETE journal mode, which requires an exclusive…]] - `rationale_for` [EXTRACTED]
- [[hold_write_lock()]] - `indirect_call` [INFERRED]
- [[release_after_delay()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/archive_old_events
