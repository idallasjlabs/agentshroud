---
source_file: "gateway/soc/auth.py"
type: "code"
community: "SOC Authentication"
location: "L171"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SOC_Authentication
---

# _resolve_caller()

## Connections
- [[.test_bearer_header_valid()]] - `calls` [EXTRACTED]
- [[.test_cookie_raw_bearer_fallback()]] - `calls` [EXTRACTED]
- [[.test_no_credentials_raises_401()]] - `calls` [EXTRACTED]
- [[.test_session_cookie_valid()]] - `calls` [EXTRACTED]
- [[.test_wrong_bearer_raises_401()]] - `calls` [EXTRACTED]
- [[.test_x_soc_token_header_valid()]] - `calls` [EXTRACTED]
- [[FastAPI dependency resolve Bearercookie token → user_id → role.]] - `rationale_for` [EXTRACTED]
- [[SCLCaller]] - `references` [EXTRACTED]
- [[_get_config_token()]] - `calls` [EXTRACTED]
- [[_get_rbac_manager()]] - `calls` [EXTRACTED]
- [[_verify_bearer()]] - `calls` [EXTRACTED]
- [[_verify_session_token()]] - `calls` [EXTRACTED]
- [[auth.py_1]] - `contains` [EXTRACTED]
- [[test_soc_realtime_coverage.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SOC_Authentication