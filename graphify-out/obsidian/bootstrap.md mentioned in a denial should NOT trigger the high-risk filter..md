---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "._extract_first_egress_target"
location: "L4091"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_extract_first_egress_target
---

# bootstrap.md mentioned in a denial should NOT trigger the high-risk filter.

## Connections
- [[dot-test_contains_high_risk_leakage_skips_bootstrap_md_in_denial_context()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_extract_first_egress_target
