---
source_file: "gateway/security/prompt_guard.py"
type: "rationale"
community: "ServiceManager"
location: "L653"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ServiceManager
---

# Check for suspicious base64 content that decodes to injection attempts.

## Connections
- [[._check_encoded_content()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ServiceManager