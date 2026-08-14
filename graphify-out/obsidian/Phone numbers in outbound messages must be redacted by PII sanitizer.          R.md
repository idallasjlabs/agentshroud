---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Bot Skill Config"
location: "L37"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# Phone numbers in outbound messages must be redacted by PII sanitizer.          R

## Connections
- [[.test_pii_redacted_on_outbound()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Bot_Skill_Config