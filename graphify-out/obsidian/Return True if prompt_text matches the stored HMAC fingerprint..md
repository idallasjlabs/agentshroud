---
source_file: "gateway/security/prompt_guard.py"
type: "rationale"
community: "._get_hmac_key()"
location: "L631"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_get_hmac_key
---

# Return True if prompt_text matches the stored HMAC fingerprint.

## Connections
- [[.verify_system_prompt()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_get_hmac_key