---
source_file: "gateway/tests/test_sanitizer.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L93"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# Bare 10-digit Telegram UID must pass through unchanged — no <PHONE_NUMBER>.

## Connections
- [[test_telegram_uid_not_redacted_as_phone()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite