---
source_file: "gateway/tests/test_rbac.py"
type: "rationale"
community: "Ingest API & RBAC Core"
location: "L353"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Ingest_API__RBAC_Core
---

# Close sqlite-holding sub-modules so Python 3.13's GC does not         finalize t

## Connections
- [[dot-teardown_method()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Ingest_API__RBAC_Core