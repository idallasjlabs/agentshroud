---
source_file: "gateway/security/output_canary.py"
type: "rationale"
community: "Output Canary"
location: "L205"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Output_Canary
---

# Check if response contains the session's canary (prompt leakage detected).

## Connections
- [[.check_response()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Output_Canary