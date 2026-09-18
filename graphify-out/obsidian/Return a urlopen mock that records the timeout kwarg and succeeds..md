---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "TestForwardToTelegramTimeouts"
location: "L4480"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestForwardToTelegramTimeouts
---

# Return a urlopen mock that records the timeout kwarg and succeeds.

## Connections
- [[._fake_urlopen_factory()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestForwardToTelegramTimeouts