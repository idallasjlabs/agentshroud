---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L4454"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
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

#graphify/code #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline