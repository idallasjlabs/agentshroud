---
source_file: "gateway/tests/test_oauth_security.py"
type: "code"
community: "test_security_audit.py"
location: "L69"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_security_auditpy
---

# TestStateValidation

## Connections
- [[.test_empty_state_rejected()]] - `method` [EXTRACTED]
- [[.test_short_state_rejected()]] - `method` [EXTRACTED]
- [[.test_state_replay_detected()]] - `method` [EXTRACTED]
- [[.test_valid_state_accepted()]] - `method` [EXTRACTED]
- [[ConfusedDeputyError]] - `uses` [INFERRED]
- [[OAuthError]] - `uses` [INFERRED]
- [[OAuthRequest]] - `uses` [INFERRED]
- [[OAuthSecurityValidator]] - `uses` [INFERRED]
- [[PKCEViolation]] - `uses` [INFERRED]
- [[RedirectMismatch]] - `uses` [INFERRED]
- [[test_oauth_security.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/test_security_auditpy