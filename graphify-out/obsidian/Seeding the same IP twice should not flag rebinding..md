---
source_file: "gateway/tests/test_dns_filter.py"
type: "rationale"
community: "Memory Lifecycle & Egress Filtering"
location: "L218"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Memory_Lifecycle__Egress_Filtering
---

# Seeding the same IP twice should not flag rebinding.

## Connections
- [[.test_stable_resolution_passes()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Memory_Lifecycle__Egress_Filtering