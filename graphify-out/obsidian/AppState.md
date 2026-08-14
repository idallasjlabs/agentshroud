---
source_file: "gateway/ingest_api/state.py"
type: "code"
community: "scripts/sync-cve-registry.py"
location: "L23"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/scripts/sync-cve-registrypy
---

# AppState

## Connections
- [[Container for application-wide state]] - `rationale_for` [EXTRACTED]
- [[DataLedger]] - `uses` [INFERRED]
- [[EventBus]] - `uses` [INFERRED]
- [[GatewayConfig_1]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[state.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/scripts/sync-cve-registrypy