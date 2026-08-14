---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "HTTP Forwarder"
location: "L4466"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTP_Forwarder
---

# TestForwardToTelegramTimeouts

## Connections
- [[._fake_urlopen_factory()]] - `method` [EXTRACTED]
- [[.test_long_poll_timeout_remains_60s()]] - `method` [EXTRACTED]
- [[.test_non_long_poll_timeout_is_15s()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[Tests that _forward_to_telegram uses correct urlopen timeouts.      Regression g]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTP_Forwarder