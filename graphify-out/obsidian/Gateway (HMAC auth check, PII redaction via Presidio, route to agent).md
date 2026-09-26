---
source_file: "docs/diagrams/images/diagram-15-sequence-telegram.svg"
type: "concept"
community: "test_alert_dispatcher_retry.py"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/test_alert_dispatcher_retrypy
---

# Gateway (HMAC auth check, PII redaction via Presidio, route to agent)

## Connections
- [[Bot Container (agent decides reply + tool call)]] - `calls` [EXTRACTED]
- [[Telegram API]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/test_alert_dispatcher_retrypy