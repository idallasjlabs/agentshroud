---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "lifespan.py"
location: "L344"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/lifespanpy
---

# Different sessions should not share state unsafely.

## Connections
- [[.test_session_isolation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/lifespanpy