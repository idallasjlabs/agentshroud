---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Bot Skill Config"
location: "L6370"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# Punycode/IDN domains should not enter preflight approval queue.

## Connections
- [[.test_non_owner_punycode_domain_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]
- [[.test_non_owner_scheme_relative_url_queues_https_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Bot_Skill_Config