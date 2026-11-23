---
source_file: "gateway/tests/test_security_fixes.py"
type: "rationale"
community: "asyncio"
location: "L398"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/asyncio
---

# When body() raises ClientDisconnect the handler returns 499 without crashing.

## Connections
- [[dot-test_client_disconnect_returns_499()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/asyncio
