---
source_file: "gateway/tests/test_cross_bot_trust_ledger.py"
type: "code"
community: "Gateway Test Suite"
location: "L43"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# CrossBotTrustLedger

## Connections
- [[.test_bot_without_registered_trust_manager_is_skipped()]] - `references` [EXTRACTED]
- [[.test_critical_severity_propagates_full_fraction()]] - `references` [EXTRACTED]
- [[.test_default_policy_is_sane()]] - `calls` [EXTRACTED]
- [[.test_empty_ledger_has_no_incidents()]] - `references` [EXTRACTED]
- [[.test_get_incidents_by_source()]] - `references` [EXTRACTED]
- [[.test_get_incidents_with_limit()]] - `references` [EXTRACTED]
- [[.test_high_severity_propagates_full_fraction()]] - `references` [EXTRACTED]
- [[.test_incident_limit_retained()]] - `references` [EXTRACTED]
- [[.test_incident_record_fields()]] - `references` [EXTRACTED]
- [[.test_incidents_are_recorded()]] - `references` [EXTRACTED]
- [[.test_low_severity_not_propagated()]] - `references` [EXTRACTED]
- [[.test_medium_severity_propagates_to_peer()]] - `references` [EXTRACTED]
- [[.test_no_self_propagation()]] - `references` [EXTRACTED]
- [[.test_propagated_to_is_empty_for_no_peers()]] - `references` [EXTRACTED]
- [[.test_propagation_limited_to_max_depth()]] - `calls` [EXTRACTED]
- [[.test_propagation_registers_unregistered_peer_agent()]] - `references` [EXTRACTED]
- [[.test_register_peer()]] - `references` [EXTRACTED]
- [[.test_register_peer_is_bidirectional_by_default()]] - `references` [EXTRACTED]
- [[.test_unregistered_bot_has_no_peers()]] - `references` [EXTRACTED]
- [[BotIncidentSeverity]] - `uses` [INFERRED]
- [[CrossBotTrustLedger]] - `uses` [INFERRED]
- [[IncidentRecord]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustDecayPolicy]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[ledger()_1]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite