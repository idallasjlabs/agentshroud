---
source_file: "gateway/tests/test_redteam_probes.py"
type: "rationale"
community: "test_approval_queue.py"
location: "L285"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_approval_queuepy
---

# One agent's session data must not leak to another.

## Connections
- [[test_session_isolation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_approval_queuepy