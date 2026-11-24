---
source_file: "gateway/tests/test_rbac.py"
type: "rationale"
community: "TestRBACIntegration"
location: "L353"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestRBACIntegration
---

# Close sqlite-holding sub-modules so Python 3.13's GC does not finalize them…

## Connections
- [[dot-teardown_method()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestRBACIntegration
