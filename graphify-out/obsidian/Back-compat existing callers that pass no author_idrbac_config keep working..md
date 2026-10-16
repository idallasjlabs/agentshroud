---
source_file: "gateway/tests/test_shared_memory_write_acl.py"
type: "rationale"
community: "ApprovalQueueConfig"
location: "L200"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ApprovalQueueConfig
---

# Back-compat: existing callers that pass no author_id/rbac_config keep working.

## Connections
- [[dot-test_legacy_no_author_write_still_appends()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ApprovalQueueConfig
