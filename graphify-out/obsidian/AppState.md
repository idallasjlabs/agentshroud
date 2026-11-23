---
source_file: "gateway/ingest_api/state.py"
type: "code"
community: "SecurityPipeline"
location: "L23"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/SecurityPipeline
---

# AppState

## Connections
- [[Container for application-wide state]] - `rationale_for` [EXTRACTED]
- [[DataLedger]] - `uses` [INFERRED]
- [[EgressFilter]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[EventBus]] - `uses` [INFERRED]
- [[GatewayConfig]] - `uses` [INFERRED]
- [[HTTPConnectProxy]] - `uses` [INFERRED]
- [[MCPProxy]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SSHProxy]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[state.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/SecurityPipeline
