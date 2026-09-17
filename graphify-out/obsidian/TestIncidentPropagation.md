---
source_file: "gateway/tests/test_cross_bot_trust_ledger.py"
type: "code"
community: "TrustConfig"
location: "L105"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TrustConfig
---

# TestIncidentPropagation

## Connections
- [[.test_bot_without_registered_trust_manager_is_skipped()]] - `method` [EXTRACTED]
- [[.test_critical_severity_propagates_full_fraction()]] - `method` [EXTRACTED]
- [[.test_high_severity_propagates_full_fraction()]] - `method` [EXTRACTED]
- [[.test_low_severity_not_propagated()]] - `method` [EXTRACTED]
- [[.test_medium_severity_propagates_to_peer()]] - `method` [EXTRACTED]
- [[.test_no_self_propagation()]] - `method` [EXTRACTED]
- [[.test_propagation_limited_to_max_depth()]] - `method` [EXTRACTED]
- [[BotIncidentSeverity]] - `uses` [INFERRED]
- [[CrossBotTrustLedger_1]] - `uses` [INFERRED]
- [[IncidentRecord]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustDecayPolicy]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_cross_bot_trust_ledger.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TrustConfig