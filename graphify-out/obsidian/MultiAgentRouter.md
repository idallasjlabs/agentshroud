---
source_file: "gateway/ingest_api/router.py"
type: "code"
community: "SSHProxy"
location: "L42"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SSHProxy
---

# MultiAgentRouter

## Connections
- [[.__init__()_32]] - `method` [EXTRACTED]
- [[._build_forward_payload()]] - `method` [EXTRACTED]
- [[.disabled_client()]] - `calls` [EXTRACTED]
- [[.forward_to_agent()]] - `method` [EXTRACTED]
- [[.forward_to_agent_stream()]] - `method` [EXTRACTED]
- [[.health_check()_1]] - `method` [EXTRACTED]
- [[.list_targets()]] - `method` [EXTRACTED]
- [[.no_approval_client()]] - `calls` [EXTRACTED]
- [[.register_bots()]] - `method` [EXTRACTED]
- [[.resolve_target()]] - `method` [EXTRACTED]
- [[AgentTarget_1]] - `uses` [INFERRED]
- [[AppState]] - `uses` [INFERRED]
- [[FastAPI_1]] - `uses` [INFERRED]
- [[ForwardRequest_1]] - `uses` [INFERRED]
- [[HTTPForwarder]] - `semantically_similar_to` [INFERRED]
- [[LogRecord_2]] - `uses` [INFERRED]
- [[RouterConfig]] - `uses` [INFERRED]
- [[Routes content to appropriate agent containers      Routing priority     1. Exp]] - `rationale_for` [EXTRACTED]
- [[TestSSHDisabledEndpoint]] - `uses` [INFERRED]
- [[TestSSHExec]] - `uses` [INFERRED]
- [[TestSSHHistory]] - `uses` [INFERRED]
- [[TestSSHHosts]] - `uses` [INFERRED]
- [[TestSSHProxyValidateWriteFile]] - `uses` [INFERRED]
- [[TestSSHProxyWriteFileTransport]] - `uses` [INFERRED]
- [[TestSSHRequireApprovalFalse]] - `uses` [INFERRED]
- [[TestSSHValidateCwd]] - `uses` [INFERRED]
- [[TestSSHWriteFileEndpoint]] - `uses` [INFERRED]
- [[TestSSHWriteFileLedgerAudit]] - `uses` [INFERRED]
- [[TestSSHWriteFileShellMetacharacterContentRoundTrip]] - `uses` [INFERRED]
- [[_DropInvalidHTTPRequestFilter]] - `uses` [INFERRED]
- [[client()_19]] - `calls` [EXTRACTED]
- [[client()_20]] - `calls` [EXTRACTED]
- [[ingest_apirouter.py]] - `contains` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[main.py]] - `references` [EXTRACTED]
- [[router()]] - `calls` [EXTRACTED]
- [[router()_1]] - `calls` [EXTRACTED]
- [[router()_2]] - `calls` [EXTRACTED]
- [[state.py]] - `imports` [EXTRACTED]
- [[test_hermes_and_openclaw_coexist()]] - `calls` [EXTRACTED]
- [[test_resolves_hermes_target()]] - `calls` [EXTRACTED]
- [[test_router.py]] - `imports` [EXTRACTED]
- [[test_router_openai_translation.py]] - `imports` [EXTRACTED]
- [[test_router_streaming.py]] - `imports` [EXTRACTED]
- [[test_ssh_endpoints.py]] - `imports` [EXTRACTED]
- [[test_ssh_write_file_endpoint.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SSHProxy