---
source_file: "gateway/tests/test_alert_telegram_relay.py"
type: "code"
community: "test_api_alerts_endpoint_emits_bus_event"
location: "L126"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_api_alerts_endpoint_emits_bus_event
---

# test_api_alerts_endpoint_emits_bus_event()

## Connections
- [[EventBus]] - `uses` [INFERRED]
- [[Regression (SCRUM-61) apialerts used to call event_bus.publish(), a method…]] - `rationale_for` [EXTRACTED]
- [[_capture()_7]] - `indirect_call` [INFERRED]
- [[asyncio_67]] - `references` [EXTRACTED]
- [[json()_1]] - `contains` [EXTRACTED]
- [[receive_security_alert()]] - `calls` [EXTRACTED]
- [[test_alert_telegram_relay.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_api_alerts_endpoint_emits_bus_event
