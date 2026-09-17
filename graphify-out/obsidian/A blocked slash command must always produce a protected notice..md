---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "TestNoResponseGuarantee"
location: "L7953"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestNoResponseGuarantee
---

# A blocked slash command must always produce a protected notice.

## Connections
- [[.test_collaborator_blocked_command_always_gets_notice()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestNoResponseGuarantee