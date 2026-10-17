---
source_file: "gateway/ingest_api/lifespan.py"
type: "code"
community: "ToolResultSanitizer"
location: "L61"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ToolResultSanitizer
---

# _DropInvalidHTTPRequestFilter

## Connections
- [[dot-filter()_1]] - `method` [EXTRACTED]
- [[dot-test_lifespan_uvicorn_warning_filter_drops_invalid_http_noise()]] - `calls` [EXTRACTED]
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
- [[test_config_validation.py]] - `references` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/ToolResultSanitizer
