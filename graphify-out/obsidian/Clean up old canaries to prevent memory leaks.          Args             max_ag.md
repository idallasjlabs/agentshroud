---
source_file: "gateway/security/output_canary.py"
type: "rationale"
community: "Memory Lifecycle & Egress Filtering"
location: "L351"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Memory_Lifecycle__Egress_Filtering
---

# Clean up old canaries to prevent memory leaks.          Args:             max_ag

## Connections
- [[.cleanup_expired_canaries()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Memory_Lifecycle__Egress_Filtering