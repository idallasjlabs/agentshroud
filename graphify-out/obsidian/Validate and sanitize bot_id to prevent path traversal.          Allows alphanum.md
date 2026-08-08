---
source_file: "gateway/security/session_manager.py"
type: "rationale"
community: "URL/Domain Validation Tests"
location: "L259"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/URL/Domain_Validation_Tests
---

# Validate and sanitize bot_id to prevent path traversal.          Allows alphanum

## Connections
- [[._validate_bot_id()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/URL/Domain_Validation_Tests