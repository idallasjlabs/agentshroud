---
source_file: "gateway/security/session_manager.py"
type: "rationale"
community: "KeyVaultConfig"
location: "L259"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/KeyVaultConfig
---

# Validate and sanitize bot_id to prevent path traversal.          Allows alphanum

## Connections
- [[._validate_bot_id()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/KeyVaultConfig