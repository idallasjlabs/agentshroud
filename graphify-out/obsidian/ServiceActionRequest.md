---
source_file: "gateway/soc/router.py"
type: "code"
community: "SOC Correlation & Router"
location: "L564"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SOC_Correlation__Router
---

# ServiceActionRequest

## Connections
- [[AuditLogEntry]] - `uses` [INFERRED]
- [[AuditResult_1]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[ContributorManager]] - `uses` [INFERRED]
- [[SCLCaller_1]] - `uses` [INFERRED]
- [[SCLConfirmationRequired]] - `uses` [INFERRED]
- [[SCLInterface_1]] - `uses` [INFERRED]
- [[ServiceManager]] - `uses` [INFERRED]
- [[killswitch_freeze()]] - `references` [EXTRACTED]
- [[killswitch_shutdown()]] - `references` [EXTRACTED]
- [[rebuild_all_services()]] - `references` [EXTRACTED]
- [[restart_service()]] - `references` [EXTRACTED]
- [[rollback_gateway()]] - `references` [EXTRACTED]
- [[socrouter.py]] - `contains` [EXTRACTED]
- [[stop_service()]] - `references` [EXTRACTED]
- [[update_service()]] - `references` [EXTRACTED]
- [[upgrade_bot()]] - `references` [EXTRACTED]
- [[upgrade_gateway()]] - `references` [EXTRACTED]
- [[upgrade_hermes()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SOC_Correlation__Router