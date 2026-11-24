---
source_file: "gateway/tests/test_security_fixes.py"
type: "code"
community: "GatewayConfig"
location: "L397"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/GatewayConfig
---

# .test_client_disconnect_returns_499()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[TestTelegramProxyClientDisconnect]] - `method` [EXTRACTED]
- [[When body() raises ClientDisconnect the handler returns 499 without crashing.]] - `rationale_for` [EXTRACTED]
- [[asyncio_40]] - `references` [EXTRACTED]
- [[telegram_api_proxy()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/GatewayConfig
