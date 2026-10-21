---
source_file: "gateway/tests/test_security_fixes.py"
type: "rationale"
community: "telegram_api_proxy (/telegram-api/{path})"
location: "L398"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/telegram_api_proxy_/telegram-api/path
---

# When body() raises ClientDisconnect the handler returns 499 without crashing.

## Connections
- [[dot-test_client_disconnect_returns_499()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/telegram_api_proxy_/telegram-api/path
