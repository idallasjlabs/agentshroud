---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: ".test_owner_revoke_command_requires_target_user_id"
location: "L677"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_owner_revoke_command_requires_target_user_id
---

# /revoke must persist through pause_collaborator() so the pause survives

## Connections
- [[dot-test_owner_revoke_command_persists_pause_to_disk()]] - `rationale_for` [EXTRACTED]
- [[dot-test_owner_revoke_command_requires_target_user_id()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_owner_revoke_command_requires_target_user_id
