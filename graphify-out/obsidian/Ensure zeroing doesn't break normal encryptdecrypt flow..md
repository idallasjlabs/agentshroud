---
source_file: "gateway/tests/test_security_hardening.py"
type: "rationale"
community: "PromptGuard Encoding Detection"
location: "L783"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PromptGuard_Encoding_Detection
---

# Ensure zeroing doesn't break normal encrypt/decrypt flow.

## Connections
- [[.test_encrypt_decrypt_still_works_after_zeroing()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PromptGuard_Encoding_Detection