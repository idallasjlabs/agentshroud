---
source_file: "gateway/soc/models.py"
type: "code"
community: "Soc Bots"
location: "L109"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Soc_Bots
---

# SecurityEvent

## Connections
- [[.test_filters_egress_log_by_bot_id()]] - `calls` [EXTRACTED]
- [[.test_filters_events_by_exact_bot_id()]] - `calls` [EXTRACTED]
- [[.test_minimal_construction()]] - `calls` [EXTRACTED]
- [[.test_no_bot_id_returns_all_events()]] - `calls` [EXTRACTED]
- [[.test_optional_fields_default_none()]] - `calls` [EXTRACTED]
- [[Any_66]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[SecurityEvent]] - `uses` [INFERRED]
- [[Severity_1]] - `uses` [INFERRED]
- [[_renderSecurityTable()]] - `shares_data_with` [INFERRED]
- [[event_adapter.py]] - `imports` [EXTRACTED]
- [[from_anomaly_alert()]] - `calls` [EXTRACTED]
- [[from_audit_chain_entry()]] - `calls` [EXTRACTED]
- [[from_dict()]] - `calls` [EXTRACTED]
- [[from_egress_attempt()]] - `calls` [EXTRACTED]
- [[from_pipeline_result()]] - `calls` [EXTRACTED]
- [[models.py_1]] - `contains` [EXTRACTED]
- [[test_soc_bots.py]] - `imports` [EXTRACTED]
- [[test_soc_models.py]] - `imports` [EXTRACTED]
- [[test_soc_realtime_coverage.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Soc_Bots