---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: ".test_unknown_user_always_gets_pending_or_rate_limit_notice()"
location: "L7971"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_unknown_user_always_gets_pending_or_rate_limit_notice
---

# A blocked slash command must always produce a protected notice.

## Connections
- [[dot-test_collaborator_blocked_command_always_gets_notice()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_unknown_user_always_gets_pending_or_rate_limit_notice
