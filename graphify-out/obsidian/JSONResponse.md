---
source_file: "gateway/soc/router.py"
type: "code"
community: "soc/router.py"
location: "L103"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/soc/routerpy
---

# JSONResponse

## Connections
- [[AuditLogEntry]] - `uses` [INFERRED]
- [[AuditResult_1]] - `uses` [INFERRED]
- [[ContributorManager]] - `uses` [INFERRED]
- [[SCLCaller_1]] - `uses` [INFERRED]
- [[SCLConfirmationRequired]] - `uses` [INFERRED]
- [[SCLInterface_1]] - `uses` [INFERRED]
- [[ServiceManager]] - `uses` [INFERRED]
- [[_confirmation_required()]] - `calls` [EXTRACTED]
- [[_process_inbound()]] - `calls` [INFERRED]
- [[auth_login()]] - `references` [EXTRACTED]
- [[dashboard_ws_token()]] - `calls` [INFERRED]
- [[email_send()]] - `calls` [INFERRED]
- [[emergency_block_egress()]] - `references` [EXTRACTED]
- [[export_audit()]] - `calls` [EXTRACTED]
- [[get_collaborator_activity()]] - `references` [EXTRACTED]
- [[get_sbom()]] - `calls` [EXTRACTED]
- [[killswitch_disconnect()]] - `references` [EXTRACTED]
- [[killswitch_freeze()]] - `references` [EXTRACTED]
- [[killswitch_shutdown()]] - `references` [EXTRACTED]
- [[rebuild_all_services()]] - `references` [EXTRACTED]
- [[restart_service()]] - `references` [EXTRACTED]
- [[rollback_gateway()]] - `references` [EXTRACTED]
- [[serve_dashboard()]] - `calls` [INFERRED]
- [[stop_service()]] - `references` [EXTRACTED]
- [[update_service()]] - `references` [EXTRACTED]
- [[upgrade_bot()]] - `references` [EXTRACTED]
- [[upgrade_gateway()]] - `references` [EXTRACTED]
- [[upgrade_hermes()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/soc/routerpy
