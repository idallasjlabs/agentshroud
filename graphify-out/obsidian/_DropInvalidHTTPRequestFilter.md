---
source_file: "gateway/ingest_api/lifespan.py"
type: "code"
community: "Security Audit & Watchtower Tests"
location: "L61"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Audit__Watchtower_Tests
---

# _DropInvalidHTTPRequestFilter

## Connections
- [[.filter()]] - `method` [EXTRACTED]
- [[.test_lifespan_uvicorn_warning_filter_drops_invalid_http_noise()]] - `calls` [EXTRACTED]
- [[AlertTelegramRelay]] - `uses` [INFERRED]
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

#graphify/code #graphify/INFERRED #community/Security_Audit__Watchtower_Tests