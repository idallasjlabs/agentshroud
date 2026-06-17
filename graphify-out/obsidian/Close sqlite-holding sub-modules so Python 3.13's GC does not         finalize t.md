---
source_file: "gateway/tests/test_rbac.py"
type: "rationale"
community: "RBAC Configuration"
location: "L357"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/RBAC_Configuration
---

# Close sqlite-holding sub-modules so Python 3.13's GC does not         finalize t

## Connections
- [[.teardown_method()_3]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/RBAC_Configuration