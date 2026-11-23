---
source_file: "gateway/security/session_security.py"
type: "code"
community: "TestAuth"
location: "L45"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestAuth
---

# Session

## Connections
- [[dot-create_session()]] - `calls` [EXTRACTED]
- [[dot-rotate_session()]] - `calls` [EXTRACTED]
- [[dot-test_session_binding()]] - `calls` [EXTRACTED]
- [[dot-test_session_cannot_impersonate()]] - `calls` [INFERRED]
- [[dot-test_session_different_fingerprints()]] - `calls` [EXTRACTED]
- [[dot-test_session_rate_limit()]] - `calls` [EXTRACTED]
- [[TestAuth_1]] - `uses` [INFERRED]
- [[TestPrivilegeEscalation]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[deep_security_test()]] - `uses` [INFERRED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[session_security.py_2]] - `contains` [EXTRACTED]
- [[t_session()]] - `calls` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TestAuth
