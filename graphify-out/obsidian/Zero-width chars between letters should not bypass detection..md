---
source_file: "gateway/tests/test_security_hardening.py"
type: "rationale"
community: "PromptGuard Encoding Detection"
location: "L804"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PromptGuard_Encoding_Detection
---

# Zero-width chars between letters should not bypass detection.

## Connections
- [[.test_zero_width_evasion()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PromptGuard_Encoding_Detection