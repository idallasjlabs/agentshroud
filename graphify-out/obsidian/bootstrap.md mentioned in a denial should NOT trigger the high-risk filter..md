---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "TestOutboundClassifierHelpers"
location: "L4091"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestOutboundClassifierHelpers
---

# bootstrap.md mentioned in a denial should NOT trigger the high-risk filter.

## Connections
- [[.test_contains_high_risk_leakage_skips_bootstrap_md_in_denial_context()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestOutboundClassifierHelpers