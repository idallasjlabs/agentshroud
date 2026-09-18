---
source_file: "gateway/security/session_manager.py"
type: "rationale"
community: ".get_or_create_session()"
location: "L259"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/get_or_create_session
---

# Validate and sanitize bot_id to prevent path traversal.          Allows alphanum

## Connections
- [[._validate_bot_id()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/get_or_create_session