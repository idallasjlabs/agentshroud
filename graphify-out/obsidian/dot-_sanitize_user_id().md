---
source_file: "gateway/security/path_isolation.py"
type: "code"
community: "Alert Dispatcher & RBAC Reliability"
location: "L110"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Alert_Dispatcher__RBAC_Reliability
---

# ._sanitize_user_id()

## Connections
- [[dot-_check_cross_user_access()]] - `calls` [EXTRACTED]
- [[dot-_get_user_temp_dir()]] - `calls` [EXTRACTED]
- [[dot-cleanup_abandoned_directories()]] - `calls` [EXTRACTED]
- [[PathIsolationManager]] - `method` [EXTRACTED]
- [[Sanitize user ID to prevent path traversal attacks.]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Alert_Dispatcher__RBAC_Reliability