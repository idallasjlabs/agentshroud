---
source_file: "gateway/security/alert_dispatcher.py"
type: "rationale"
community: "Alert Dispatcher (security)"
location: "L140"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Alert_Dispatcher_security
---

# POST alert to /api/alerts with bounded retry + backoff.          Returns True on

## Connections
- [[._send_notification()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Alert_Dispatcher_security