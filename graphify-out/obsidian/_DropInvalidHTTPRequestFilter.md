---
source_file: "gateway/ingest_api/lifespan.py"
type: "code"
community: "lifespan.py"
location: "L61"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/lifespanpy
---

# _DropInvalidHTTPRequestFilter

## Connections
- [[.filter()_1]] - `method` [EXTRACTED]
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
- [[test_config_validation.py_1]] - `references` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/lifespanpy