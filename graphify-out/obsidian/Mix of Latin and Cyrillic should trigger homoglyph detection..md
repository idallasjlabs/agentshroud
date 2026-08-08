---
source_file: "gateway/tests/test_security_hardening.py"
type: "rationale"
community: "PromptGuard Encoding Detection"
location: "L835"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PromptGuard_Encoding_Detection
---

# Mix of Latin and Cyrillic should trigger homoglyph detection.

## Connections
- [[.test_homoglyph_detection()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PromptGuard_Encoding_Detection