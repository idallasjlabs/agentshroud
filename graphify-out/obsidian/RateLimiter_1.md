---
source_file: "gateway/ingest_api/auth.py"
type: "code"
community: "telegram_proxy.py"
location: "L30"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/telegram_proxypy
---

# RateLimiter

## Connections
- [[dot-__init__()_164]] - `calls` [EXTRACTED]
- [[dot-__init__()_163]] - `method` [EXTRACTED]
- [[dot-check()_2]] - `method` [EXTRACTED]
- [[Any_42]] - `uses` [INFERRED]
- [[GatewayConfig_4]] - `uses` [INFERRED]
- [[Simple token-bucket rate limiter      Limits requests per client IP to prevent r]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy_2]] - `uses` [INFERRED]
- [[_OutboundScan]] - `uses` [INFERRED]
- [[auth.py]] - `references` [EXTRACTED]
- [[ingest_apiauth.py]] - `contains` [EXTRACTED]
- [[telegram_proxy.py]] - `imports` [EXTRACTED]
- [[test_auth.py]] - `imports` [EXTRACTED]
- [[test_rate_limiter()]] - `calls` [EXTRACTED]
- [[test_rate_limiter_allows_requests()]] - `calls` [EXTRACTED]
- [[test_rate_limiter_blocks_excess_requests()]] - `calls` [EXTRACTED]
- [[test_rate_limiter_separate_clients()]] - `calls` [EXTRACTED]
- [[test_rate_limiter_window_cleanup()]] - `calls` [EXTRACTED]
- [[test_security.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/telegram_proxypy
