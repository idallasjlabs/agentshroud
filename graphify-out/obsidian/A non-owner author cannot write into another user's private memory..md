---
source_file: "gateway/tests/test_shared_memory_write_acl.py"
type: "rationale"
community: "File Sandbox"
location: "L167"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/File_Sandbox
---

# A non-owner author cannot write into another user's private memory.

## Connections
- [[.test_foreign_writer_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/File_Sandbox