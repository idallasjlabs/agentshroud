---
source_file: "gateway/tests/test_soc_realtime_coverage.py"
type: "code"
community: "RBAC & SOC Realtime"
location: "L220"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RBAC__SOC_Realtime
---

# TestResolveCaller

## Connections
- [[.test_bearer_header_valid()]] - `method` [EXTRACTED]
- [[.test_cookie_raw_bearer_fallback()]] - `method` [EXTRACTED]
- [[.test_get_caller_passthrough()]] - `method` [EXTRACTED]
- [[.test_no_credentials_raises_401()]] - `method` [EXTRACTED]
- [[.test_session_cookie_valid()]] - `method` [EXTRACTED]
- [[.test_wrong_bearer_raises_401()]] - `method` [EXTRACTED]
- [[.test_x_soc_token_header_valid()]] - `method` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[PermissionResult]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[SOCWebSocketHandler]] - `uses` [INFERRED]
- [[_resolve_caller()]] - `calls` [EXTRACTED]
- [[test_soc_realtime_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/RBAC__SOC_Realtime