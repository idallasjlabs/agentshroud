---
source_file: "gateway/soc/router.py"
type: "code"
community: "Enhanced Approval Queue"
location: "L564"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Enhanced_Approval_Queue
---

# ServiceActionRequest

## Connections
- [[AuditLogEntry]] - `uses` [INFERRED]
- [[AuditResult]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[ContributorManager]] - `uses` [INFERRED]
- [[SCLCaller]] - `uses` [INFERRED]
- [[SCLConfirmationRequired]] - `uses` [INFERRED]
- [[SCLError]] - `uses` [INFERRED]
- [[SCLInterface]] - `uses` [INFERRED]
- [[ServiceManager]] - `uses` [INFERRED]
- [[Severity_2]] - `uses` [INFERRED]
- [[WSEventType]] - `uses` [INFERRED]
- [[killswitch_freeze()]] - `references` [EXTRACTED]
- [[killswitch_shutdown()]] - `references` [EXTRACTED]
- [[rebuild_all_services()]] - `references` [EXTRACTED]
- [[restart_service()_1]] - `references` [EXTRACTED]
- [[rollback_gateway()]] - `references` [EXTRACTED]
- [[router.py_1]] - `contains` [EXTRACTED]
- [[stop_service()_1]] - `references` [EXTRACTED]
- [[update_service()]] - `references` [EXTRACTED]
- [[upgrade_bot()]] - `references` [EXTRACTED]
- [[upgrade_gateway()]] - `references` [EXTRACTED]
- [[upgrade_hermes()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Enhanced_Approval_Queue