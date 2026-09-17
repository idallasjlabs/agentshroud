---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "TestOutboundClassifierHelpers"
location: "L4096"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestOutboundClassifierHelpers
---

# Our own protected notices must never be double-filtered.

## Connections
- [[.test_contains_high_risk_leakage_skips_protected_header_text()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestOutboundClassifierHelpers