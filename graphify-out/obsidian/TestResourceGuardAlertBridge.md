---
source_file: "gateway/tests/test_resource_guard_wiring.py"
type: "code"
community: "PII Sanitizer & Resource Guard"
location: "L52"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PII_Sanitizer__Resource_Guard
---

# TestResourceGuardAlertBridge

## Connections
- [[._build_bridge()]] - `method` [EXTRACTED]
- [[.test_bridge_registered_via_add_alert_callback_fires_through()]] - `method` [EXTRACTED]
- [[.test_missing_timestamp_falls_back_to_zero()]] - `method` [EXTRACTED]
- [[.test_non_spike_alert_dispatched_with_medium_severity()]] - `method` [EXTRACTED]
- [[.test_spike_alert_dispatched_with_high_severity()]] - `method` [EXTRACTED]
- [[ResourceGuard]] - `uses` [INFERRED]
- [[ResourceLimits]] - `uses` [INFERRED]
- [[The lifespan bridges ResourceGuard's native callback payload to AlertDispatcher.]] - `rationale_for` [EXTRACTED]
- [[test_resource_guard_wiring.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PII_Sanitizer__Resource_Guard
