---
source_file: "gateway/tests/test_email_owner_bypasses_pii.py"
type: "code"
community: "Forward (routes)"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Forward_routes
---

# test_email_owner_bypasses_pii.py

## Connections
- [[FastAPI app instance]] - `calls` [EXTRACTED]
- [[PIISanitizer]] - `calls` [EXTRACTED]
- [[TestOwnerEmailBypassesPii]] - `contains` [EXTRACTED]
- [[auth_dep()]] - `imports` [EXTRACTED]
- [[auth_dep()_3]] - `imports` [EXTRACTED]
- [[bypass_auth()_1]] - `contains` [EXTRACTED]
- [[client()_7]] - `contains` [EXTRACTED]
- [[email_send()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Forward_routes