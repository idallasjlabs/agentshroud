---
source_file: "gateway/tests/test_security_fixes.py"
type: "rationale"
community: "AsyncMock"
location: "L398"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AsyncMock
---

# When body() raises ClientDisconnect the handler returns 499 without crashing.

## Connections
- [[dot-test_client_disconnect_returns_499()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AsyncMock
