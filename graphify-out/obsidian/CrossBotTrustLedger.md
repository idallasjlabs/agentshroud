---
source_file: "gateway/security/cross_bot_trust_ledger.py"
type: "code"
community: "TrustManager"
location: "L125"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TrustManager
---

# CrossBotTrustLedger

## Connections
- [[dot-__init__()_105]] - `method` [EXTRACTED]
- [[dot-_propagate()]] - `method` [EXTRACTED]
- [[dot-build_full_mesh()]] - `method` [EXTRACTED]
- [[dot-get_incidents()]] - `method` [EXTRACTED]
- [[dot-incident_count()]] - `method` [EXTRACTED]
- [[dot-peers_of()]] - `method` [EXTRACTED]
- [[dot-record_incident()]] - `method` [EXTRACTED]
- [[dot-register_peer()]] - `method` [EXTRACTED]
- [[dot-register_trust_manager()]] - `method` [EXTRACTED]
- [[dot-test_bot_without_registered_trust_manager_is_skipped()]] - `references` [EXTRACTED]
- [[dot-test_critical_severity_propagates_full_fraction()]] - `references` [EXTRACTED]
- [[dot-test_empty_ledger_has_no_incidents()]] - `references` [EXTRACTED]
- [[dot-test_get_incidents_by_source()]] - `references` [EXTRACTED]
- [[dot-test_get_incidents_with_limit()]] - `references` [EXTRACTED]
- [[dot-test_high_severity_propagates_full_fraction()]] - `references` [EXTRACTED]
- [[dot-test_incident_limit_retained()]] - `references` [EXTRACTED]
- [[dot-test_incident_record_fields()]] - `references` [EXTRACTED]
- [[dot-test_incidents_are_recorded()]] - `references` [EXTRACTED]
- [[dot-test_low_severity_not_propagated()]] - `references` [EXTRACTED]
- [[dot-test_medium_severity_propagates_to_peer()]] - `references` [EXTRACTED]
- [[dot-test_no_self_propagation()]] - `references` [EXTRACTED]
- [[dot-test_propagated_to_is_empty_for_no_peers()]] - `references` [EXTRACTED]
- [[dot-test_propagation_registers_unregistered_peer_agent()]] - `references` [EXTRACTED]
- [[dot-test_register_peer()]] - `references` [EXTRACTED]
- [[dot-test_register_peer_is_bidirectional_by_default()]] - `references` [EXTRACTED]
- [[dot-test_unregistered_bot_has_no_peers()]] - `references` [EXTRACTED]
- [[Shared trust decay channel for multi-bot deployments. Usage ledger =…]] - `rationale_for` [EXTRACTED]
- [[TestBuildFullMesh]] - `uses` [INFERRED]
- [[TestCrossBotTrustLedgerConstruction]] - `uses` [INFERRED]
- [[TestGetIncidentsLimit]] - `uses` [INFERRED]
- [[TestIncidentAudit]] - `uses` [INFERRED]
- [[TestIncidentPropagation]] - `uses` [INFERRED]
- [[TestTrustViolationRecording]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[cross_bot_trust_ledger.py]] - `contains` [EXTRACTED]
- [[ledger()_1]] - `uses` [INFERRED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_cross_bot_trust_ledger.py]] - `imports` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TrustManager
