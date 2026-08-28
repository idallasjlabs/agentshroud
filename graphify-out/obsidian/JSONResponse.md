---
source_file: "gateway/soc/router.py"
type: "code"
community: "SOC Collaborators"
location: "L103"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SOC_Collaborators
---

# JSONResponse

## Connections
- [[AuditLogEntry]] - `uses` [INFERRED]
- [[AuditResult]] - `uses` [INFERRED]
- [[ContributorManager]] - `uses` [INFERRED]
- [[SCLCaller]] - `uses` [INFERRED]
- [[SCLConfirmationRequired]] - `uses` [INFERRED]
- [[SCLInterface]] - `uses` [INFERRED]
- [[ServiceManager]] - `uses` [INFERRED]
- [[_confirmation_required()]] - `calls` [EXTRACTED]
- [[_process_inbound()]] - `calls` [INFERRED]
- [[auth_login()]] - `references` [EXTRACTED]
- [[cors_middleware()]] - `calls` [EXTRACTED]
- [[dashboard_ws_token()]] - `calls` [INFERRED]
- [[email_send()]] - `calls` [INFERRED]
- [[emergency_block_egress()]] - `references` [EXTRACTED]
- [[export_audit()]] - `calls` [EXTRACTED]
- [[get_collaborator_activity()]] - `references` [EXTRACTED]
- [[get_sbom()_1]] - `calls` [EXTRACTED]
- [[global_exception_handler()]] - `calls` [EXTRACTED]
- [[google_api_proxy()]] - `calls` [EXTRACTED]
- [[killswitch_disconnect()]] - `references` [EXTRACTED]
- [[killswitch_freeze()]] - `references` [EXTRACTED]
- [[killswitch_shutdown()]] - `references` [EXTRACTED]
- [[limit_request_body()]] - `calls` [EXTRACTED]
- [[llm_api_proxy()]] - `calls` [EXTRACTED]
- [[mcp_proxy_endpoint()]] - `calls` [EXTRACTED]
- [[ollama_api_proxy()]] - `calls` [EXTRACTED]
- [[rebuild_all_services()]] - `references` [EXTRACTED]
- [[restart_service()_1]] - `references` [EXTRACTED]
- [[rollback_gateway()]] - `references` [EXTRACTED]
- [[security_headers_middleware()]] - `calls` [EXTRACTED]
- [[serve_dashboard()]] - `calls` [INFERRED]
- [[slack_api_proxy()]] - `calls` [EXTRACTED]
- [[ssh_exec()]] - `calls` [EXTRACTED]
- [[stop_service()_1]] - `references` [EXTRACTED]
- [[telegram_api_proxy()]] - `calls` [EXTRACTED]
- [[update_service()]] - `references` [EXTRACTED]
- [[upgrade_bot()]] - `references` [EXTRACTED]
- [[upgrade_gateway()]] - `references` [EXTRACTED]
- [[upgrade_hermes()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SOC_Collaborators