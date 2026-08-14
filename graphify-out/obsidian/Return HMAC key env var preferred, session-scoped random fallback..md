---
source_file: "gateway/security/prompt_guard.py"
type: "rationale"
community: "Audit Export Pipeline"
location: "L605"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Audit_Export_Pipeline
---

# Return HMAC key: env var preferred, session-scoped random fallback.

## Connections
- [[._get_hmac_key()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Audit_Export_Pipeline