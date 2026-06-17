---
source_file: "gateway/ingest_api/lifespan.py"
type: "code"
community: "Gateway Config & Lifespan"
location: "L55"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Gateway_Config__Lifespan
---

# _DropInvalidHTTPRequestFilter

## Connections
- [[.filter()]] - `method` [EXTRACTED]
- [[.test_lifespan_uvicorn_warning_filter_drops_invalid_http_noise()]] - `calls` [EXTRACTED]
- [[DataLedger]] - `uses` [INFERRED]
- [[EventBus]] - `uses` [INFERRED]
- [[GroupRegistry]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Suppress noisy uvicorn warning spam for malformed probe traffic.]] - `rationale_for` [EXTRACTED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[_install_uvicorn_warning_filter()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `contains` [EXTRACTED]
- [[test_config_validation.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Gateway_Config__Lifespan