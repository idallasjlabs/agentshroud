---
source_file: "gateway/security/session_security.py"
type: "code"
community: "SessionManager"
location: "L40"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/SessionManager
---

# RateLimitExceeded

## Connections
- [[.create_session()]] - `calls` [EXTRACTED]
- [[SessionError]] - `inherits` [EXTRACTED]
- [[TestEventInjection]] - `uses` [INFERRED]
- [[TestInstructionNonce]] - `uses` [INFERRED]
- [[TestRateLimiting_2]] - `uses` [INFERRED]
- [[TestSessionCleanup]] - `uses` [INFERRED]
- [[TestSessionCreation]] - `uses` [INFERRED]
- [[TestSessionRotation]] - `uses` [INFERRED]
- [[TestSessionValidation]] - `uses` [INFERRED]
- [[session_security.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/SessionManager