---
source_file: "gateway/security/prompt_guard.py"
type: "rationale"
community: "PromptGuard Encoding Detection"
location: "L653"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PromptGuard_Encoding_Detection
---

# Check for suspicious base64 content that decodes to injection attempts.

## Connections
- [[._check_encoded_content()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PromptGuard_Encoding_Detection