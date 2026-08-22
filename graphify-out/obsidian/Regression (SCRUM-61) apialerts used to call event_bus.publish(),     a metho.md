---
source_file: "gateway/tests/test_alert_telegram_relay.py"
type: "rationale"
community: "Middleware & Session Isolation"
location: "L127"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Middleware__Session_Isolation
---

# Regression (SCRUM-61): /api/alerts used to call event_bus.publish(),     a metho

## Connections
- [[test_api_alerts_endpoint_emits_bus_event()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Middleware__Session_Isolation