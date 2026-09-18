---
source_file: "gateway/tests/test_shared_memory_write_acl.py"
type: "rationale"
community: "TestUserMemoryWriteACL"
location: "L167"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestUserMemoryWriteACL
---

# A non-owner author cannot write into another user's private memory.

## Connections
- [[.test_foreign_writer_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestUserMemoryWriteACL