---
source_file: "gateway/ingest_api/middleware.py"
type: "rationale"
community: "Memory Lifecycle & Egress Filtering"
location: "L460"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Memory_Lifecycle__Egress_Filtering
---

# Record a guard __init__ exception so the request path can fail closed.

## Connections
- [[._record_guard_init_failure()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Memory_Lifecycle__Egress_Filtering