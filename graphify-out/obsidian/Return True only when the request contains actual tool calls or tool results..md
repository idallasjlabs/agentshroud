---
source_file: "gateway/ingest_api/middleware.py"
type: "rationale"
community: "Memory Lifecycle & Egress Filtering"
location: "L1247"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Memory_Lifecycle__Egress_Filtering
---

# Return True only when the request contains actual tool calls or tool results.

## Connections
- [[._is_tool_call_request()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Memory_Lifecycle__Egress_Filtering