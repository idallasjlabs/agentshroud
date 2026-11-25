---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "._extract_first_egress_target"
location: "L4096"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_extract_first_egress_target
---

# Our own protected notices must never be double-filtered.

## Connections
- [[dot-test_contains_high_risk_leakage_skips_protected_header_text()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_extract_first_egress_target
