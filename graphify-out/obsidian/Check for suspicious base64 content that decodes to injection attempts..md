---
source_file: "gateway/security/prompt_guard.py"
type: "rationale"
community: "Audit Export Pipeline"
location: "L653"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Audit_Export_Pipeline
---

# Check for suspicious base64 content that decodes to injection attempts.

## Connections
- [[._check_encoded_content()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Audit_Export_Pipeline