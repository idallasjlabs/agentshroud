---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "docs/redteam"
location: "L4359"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/docs/redteam
---

# PII redaction must not strip parse_mode for the whole message (owner, fallback p

## Connections
- [[.test_parse_mode_preserved_and_placeholder_escaped_email_fallback_path()]] - `rationale_for` [EXTRACTED]
- [[.test_parse_mode_preserved_and_placeholder_escaped_phone_fallback_path()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/docs/redteam