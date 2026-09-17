---
source_file: "gateway/security/session_manager.py"
type: "rationale"
community: ".get_or_create_group_session()"
location: "L244"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/get_or_create_group_session
---

# Validate and sanitize user_id to prevent path traversal.          Only allows al

## Connections
- [[._validate_user_id()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/get_or_create_group_session