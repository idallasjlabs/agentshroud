---
source_file: "gateway/soc/auth.py"
type: "code"
community: "Ingest API & RBAC Core"
location: "L170"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Ingest_API__RBAC_Core
---

# _resolve_caller()

## Connections
- [[dot-test_bearer_header_valid()]] - `calls` [EXTRACTED]
- [[dot-test_cookie_raw_bearer_fallback()]] - `calls` [EXTRACTED]
- [[dot-test_no_credentials_raises_401()]] - `calls` [EXTRACTED]
- [[dot-test_session_cookie_valid()]] - `calls` [EXTRACTED]
- [[dot-test_wrong_bearer_raises_401()]] - `calls` [EXTRACTED]
- [[dot-test_x_soc_token_header_valid()]] - `calls` [EXTRACTED]
- [[FastAPI dependency resolve Bearercookie token → user_id → role.]] - `rationale_for` [EXTRACTED]
- [[SCLCaller_1]] - `references` [EXTRACTED]
- [[TestResolveCaller]] - `calls` [EXTRACTED]
- [[_get_config_token()]] - `calls` [EXTRACTED]
- [[_get_rbac_manager()]] - `calls` [EXTRACTED]
- [[_verify_bearer()]] - `calls` [EXTRACTED]
- [[_verify_session_token()]] - `calls` [EXTRACTED]
- [[socauth.py]] - `contains` [EXTRACTED]
- [[test_soc_realtime_coverage.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Ingest_API__RBAC_Core