---
source_file: "gateway/security/session_security.py"
type: "code"
community: "Session Security"
location: "L24"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Session_Security
---

# SessionError

## Connections
- [[.register_event_source()]] - `calls` [EXTRACTED]
- [[.validate_event()]] - `calls` [EXTRACTED]
- [[.validate_session()]] - `calls` [EXTRACTED]
- [[EventInjectionError]] - `inherits` [EXTRACTED]
- [[Exception]] - `inherits` [EXTRACTED]
- [[RateLimitExceeded]] - `inherits` [EXTRACTED]
- [[SessionBindingError]] - `inherits` [EXTRACTED]
- [[SessionExpired]] - `inherits` [EXTRACTED]
- [[TestEventInjection]] - `uses` [INFERRED]
- [[TestInstructionNonce]] - `uses` [INFERRED]
- [[TestRateLimiting_3]] - `uses` [INFERRED]
- [[TestSessionCleanup]] - `uses` [INFERRED]
- [[TestSessionCreation]] - `uses` [INFERRED]
- [[TestSessionRotation]] - `uses` [INFERRED]
- [[TestSessionValidation]] - `uses` [INFERRED]
- [[session_security.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Session_Security