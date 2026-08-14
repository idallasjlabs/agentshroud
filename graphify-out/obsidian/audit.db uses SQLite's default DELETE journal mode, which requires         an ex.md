---
source_file: "gateway/tests/test_audit_archive.py"
type: "rationale"
community: "Architecture Docs"
location: "L196"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Architecture_Docs
---

# audit.db uses SQLite's default DELETE journal mode, which requires         an ex

## Connections
- [[.test_waits_out_a_concurrent_writer_lock_instead_of_failing()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Architecture_Docs