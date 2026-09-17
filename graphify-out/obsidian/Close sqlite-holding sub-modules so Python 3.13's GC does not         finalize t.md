---
source_file: "gateway/tests/test_rbac.py"
type: "rationale"
community: "ingest_api/main.py"
location: "L353"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ingest_api/mainpy
---

# Close sqlite-holding sub-modules so Python 3.13's GC does not         finalize t

## Connections
- [[.teardown_method()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ingest_api/mainpy