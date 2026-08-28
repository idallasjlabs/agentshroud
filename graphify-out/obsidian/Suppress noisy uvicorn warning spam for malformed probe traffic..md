---
source_file: "gateway/ingest_api/lifespan.py"
type: "rationale"
community: "Memory Lifecycle & Egress Filtering"
location: "L62"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Memory_Lifecycle__Egress_Filtering
---

# Suppress noisy uvicorn warning spam for malformed probe traffic.

## Connections
- [[_DropInvalidHTTPRequestFilter]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Memory_Lifecycle__Egress_Filtering