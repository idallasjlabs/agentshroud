---
source_file: "gateway/security/tool_result_sanitizer_enhanced.py"
type: "rationale"
community: "Memory Lifecycle & Egress Filtering"
location: "L169"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Memory_Lifecycle__Egress_Filtering
---

# Remove or warn about markdown images pointing to non-allowlisted domains.

## Connections
- [[.sanitize_images()]] - `rationale_for` [EXTRACTED]
- [[.sanitize_links()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Memory_Lifecycle__Egress_Filtering