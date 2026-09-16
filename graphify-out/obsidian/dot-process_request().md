---
source_file: "gateway/ingest_api/middleware.py"
type: "code"
community: "Alert Dispatcher & RBAC Reliability"
location: "L496"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Alert_Dispatcher__RBAC_Reliability
---

# .process_request()

## Connections
- [[dot-_check_cross_session_access()]] - `calls` [EXTRACTED]
- [[dot-_check_rbac_permissions()]] - `calls` [EXTRACTED]
- [[dot-_critical_guard_failure()]] - `calls` [EXTRACTED]
- [[dot-_enforce_session_isolation()]] - `calls` [EXTRACTED]
- [[dot-_extract_file_paths()]] - `calls` [EXTRACTED]
- [[dot-_extract_user_id()]] - `calls` [EXTRACTED]
- [[dot-_is_owner()]] - `calls` [EXTRACTED]
- [[dot-_is_path_allowed_for_user()]] - `calls` [EXTRACTED]
- [[dot-_is_tool_call_request()]] - `calls` [EXTRACTED]
- [[Any_2]] - `references` [EXTRACTED]
- [[MiddlewareManager]] - `method` [EXTRACTED]
- [[MiddlewareResult]] - `references` [EXTRACTED]
- [[Process request through all middleware modules.]] - `rationale_for` [EXTRACTED]
- [[RBACConfig_2]] - `calls` [EXTRACTED]
- [[normalize_input()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Alert_Dispatcher__RBAC_Reliability