---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Bot Skill Config"
location: "L6232"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# Internal/non-routable pseudo-TLDs should not enter approval queue.

## Connections
- [[.test_non_owner_internal_suffix_domain_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]
- [[.test_non_owner_numeric_tld_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Bot_Skill_Config