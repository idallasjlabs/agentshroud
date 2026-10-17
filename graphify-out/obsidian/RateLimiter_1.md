---
source_file: "gateway/ingest_api/auth.py"
type: "code"
community: "create_auth_dependency"
location: "L30"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/create_auth_dependency
---

# RateLimiter

## Connections
- [[dot-__init__()_49]] - `calls` [EXTRACTED]
- [[dot-__init__()_184]] - `method` [EXTRACTED]
- [[dot-check()_6]] - `method` [EXTRACTED]
- [[Any_83]] - `uses` [INFERRED]
- [[GatewayConfig]] - `uses` [INFERRED]
- [[Simple token-bucket rate limiter      Limits requests per client IP to prevent r]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy_1]] - `uses` [INFERRED]
- [[_OutboundScan]] - `uses` [INFERRED]
- [[auth.py_1]] - `references` [EXTRACTED]
- [[ingest_apiauth.py]] - `contains` [EXTRACTED]
- [[telegram_proxy.py_2]] - `imports` [EXTRACTED]
- [[test_auth.py]] - `imports` [EXTRACTED]
- [[test_rate_limiter()]] - `calls` [EXTRACTED]
- [[test_rate_limiter_allows_requests()]] - `calls` [EXTRACTED]
- [[test_rate_limiter_blocks_excess_requests()]] - `calls` [EXTRACTED]
- [[test_rate_limiter_separate_clients()]] - `calls` [EXTRACTED]
- [[test_rate_limiter_window_cleanup()]] - `calls` [EXTRACTED]
- [[test_security.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/create_auth_dependency
