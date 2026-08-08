---
source_file: "gateway/tests/test_security_hardening.py"
type: "rationale"
community: "PromptGuard Encoding Detection"
location: "L909"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PromptGuard_Encoding_Detection
---

# Unknown event types should not inject SQL.

## Connections
- [[.test_event_type_validation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PromptGuard_Encoding_Detection