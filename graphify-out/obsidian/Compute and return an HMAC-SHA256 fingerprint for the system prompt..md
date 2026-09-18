---
source_file: "gateway/security/prompt_guard.py"
type: "rationale"
community: "._get_hmac_key()"
location: "L616"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_get_hmac_key
---

# Compute and return an HMAC-SHA256 fingerprint for the system prompt.

## Connections
- [[.register_system_prompt()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_get_hmac_key