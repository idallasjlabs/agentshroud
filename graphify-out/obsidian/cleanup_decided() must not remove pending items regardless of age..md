---
source_file: "gateway/tests/test_approval_queue.py"
type: "rationale"
community: "test_approval_queue.py"
location: "L422"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_approval_queuepy
---

# cleanup_decided() must not remove pending items regardless of age.

## Connections
- [[test_cleanup_decided_keeps_pending_items()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_approval_queuepy