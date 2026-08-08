---
source_file: "gateway/tests/test_rbac.py"
type: "rationale"
community: "Auth & Exception Types"
location: "L354"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Auth__Exception_Types
---

# Close sqlite-holding sub-modules so Python 3.13's GC does not         finalize t

## Connections
- [[.teardown_method()_4]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Auth__Exception_Types