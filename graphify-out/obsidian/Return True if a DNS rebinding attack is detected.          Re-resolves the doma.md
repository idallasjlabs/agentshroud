---
source_file: "gateway/security/dns_filter.py"
type: "rationale"
community: "Memory Lifecycle & Egress Filtering"
location: "L196"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Memory_Lifecycle__Egress_Filtering
---

# Return True if a DNS rebinding attack is detected.          Re-resolves the doma

## Connections
- [[.check_rebinding()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Memory_Lifecycle__Egress_Filtering