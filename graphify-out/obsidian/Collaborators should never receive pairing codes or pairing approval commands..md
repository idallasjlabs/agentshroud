---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Telegram Outbound Proxy Tests"
location: "L1253"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Outbound_Proxy_Tests
---

# Collaborators should never receive pairing codes or pairing approval commands.

## Connections
- [[.test_collaborator_pairing_code_leakage_is_redacted_json()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Outbound_Proxy_Tests