---
source_file: "gateway/ingest_api/lifespan.py"
type: "code"
community: "Approval Routing & Event Bus"
location: "L61"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Approval_Routing__Event_Bus
---

# _DropInvalidHTTPRequestFilter

## Connections
- [[dot-filter()_1]] - `method` [EXTRACTED]
- [[AlertTelegramRelay]] - `uses` [INFERRED]
- [[DataLedger]] - `uses` [INFERRED]
- [[EventBus]] - `uses` [INFERRED]
- [[GroupRegistry]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[RBACConfig_2]] - `uses` [INFERRED]
- [[Suppress noisy uvicorn warning spam for malformed probe traffic.]] - `rationale_for` [EXTRACTED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[_install_uvicorn_warning_filter()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Approval_Routing__Event_Bus