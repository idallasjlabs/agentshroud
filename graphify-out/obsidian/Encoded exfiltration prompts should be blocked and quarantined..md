---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Proxy Inbound"
location: "L4052"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Inbound
---

# Encoded exfiltration prompts should be blocked and quarantined.

## Connections
- [[.test_collaborator_encoded_exfil_request_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]
- [[.test_collaborator_plugin_discovery_request_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Proxy_Inbound