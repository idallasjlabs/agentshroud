---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Bot Skill Config"
location: "L6301"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# Approval preflight should reject domains with non-alphabetic TLDs.

## Connections
- [[.test_non_owner_numeric_tld_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]
- [[.test_non_owner_punycode_domain_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Bot_Skill_Config