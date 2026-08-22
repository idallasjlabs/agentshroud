---
source_file: "gateway/tests/test_audit_archive.py"
type: "rationale"
community: "Audit Archive"
location: "L237"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Audit_Archive
---

# A full disk (or any VACUUM-specific OperationalError) must not         raise pas

## Connections
- [[.test_vacuum_failure_does_not_discard_a_successful_archive()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Audit_Archive