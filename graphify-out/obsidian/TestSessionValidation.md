---
source_file: "gateway/tests/test_session_security.py"
type: "code"
community: "Community 1133"
location: "L50"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_1133
---

# TestSessionValidation

## Connections
- [[.test_expired_session_rejected()]] - `method` [EXTRACTED]
- [[.test_unknown_session_rejected()]] - `method` [EXTRACTED]
- [[.test_valid_session_accepted()]] - `method` [EXTRACTED]
- [[.test_wrong_ip_rejected()]] - `method` [EXTRACTED]
- [[.test_wrong_user_agent_rejected()]] - `method` [EXTRACTED]
- [[EventInjectionError]] - `uses` [INFERRED]
- [[RateLimitExceeded]] - `uses` [INFERRED]
- [[SessionBindingError]] - `uses` [INFERRED]
- [[SessionError]] - `uses` [INFERRED]
- [[SessionExpired]] - `uses` [INFERRED]
- [[SessionManager]] - `uses` [INFERRED]
- [[test_session_security.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_1133