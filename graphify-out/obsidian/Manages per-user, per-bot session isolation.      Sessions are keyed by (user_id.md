---
source_file: "gateway/security/session_manager.py"
type: "rationale"
community: "Middleware & Session Isolation"
location: "L122"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Middleware__Session_Isolation
---

# Manages per-user, per-bot session isolation.      Sessions are keyed by (user_id

## Connections
- [[UserSessionManager]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Middleware__Session_Isolation