---
source_file: "gateway/security/output_canary.py"
type: "rationale"
community: "TestOutputCanary"
location: "L205"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestOutputCanary
---

# Check if response contains the session's canary (prompt leakage detected).

## Connections
- [[.check_response()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestOutputCanary