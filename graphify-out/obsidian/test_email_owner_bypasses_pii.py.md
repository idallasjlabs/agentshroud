---
source_file: "gateway/tests/test_email_owner_bypasses_pii.py"
type: "code"
community: "TestPatternDetection"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestPatternDetection
---

# test_email_owner_bypasses_pii.py

## Connections
- [[PIISanitizer_2]] - `calls` [EXTRACTED]
- [[TestOwnerEmailBypassesPii]] - `contains` [EXTRACTED]
- [[auth_dep()]] - `imports` [EXTRACTED]
- [[auth_dep()_4]] - `imports` [EXTRACTED]
- [[bypass_auth()_1]] - `contains` [EXTRACTED]
- [[client()_4]] - `contains` [EXTRACTED]
- [[email_send()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TestPatternDetection
