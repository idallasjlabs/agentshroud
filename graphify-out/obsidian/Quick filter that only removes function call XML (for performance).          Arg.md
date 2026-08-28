---
source_file: "gateway/security/xml_leak_filter.py"
type: "rationale"
community: "Memory Lifecycle & Egress Filtering"
location: "L172"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Memory_Lifecycle__Egress_Filtering
---

# Quick filter that only removes function call XML (for performance).          Arg

## Connections
- [[.filter_function_calls_only()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Memory_Lifecycle__Egress_Filtering