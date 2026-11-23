---
source_file: "gateway/security/shared_memory.py"
type: "code"
community: "SharedMemoryManager"
location: "L75"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SharedMemoryManager
---

# ._is_authorized_group_writer()

## Connections
- [[dot-append_to_group_memory()]] - `calls` [EXTRACTED]
- [[dot-get_user_groups_by_id()]] - `indirect_call` [INFERRED]
- [[dot-is_owner()_3]] - `indirect_call` [INFERRED]
- [[dot-test_empty_author_is_denied()]] - `calls` [EXTRACTED]
- [[dot-test_member_authorized()]] - `calls` [EXTRACTED]
- [[dot-test_missing_rbac_is_denied()]] - `calls` [EXTRACTED]
- [[Return True if ``author_id`` may WRITE to ``group_id`` shared memory. RT-5…]] - `rationale_for` [EXTRACTED]
- [[SharedMemoryManager]] - `method` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SharedMemoryManager
