---
source_file: "gateway/tests/test_slack_socket_client.py"
type: "rationale"
community: "Slack Socket Client"
location: "L204"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Slack_Socket_Client
---

# hello messages are silently consumed without calling handle_event.

## Connections
- [[.test_hello_message_not_dispatched()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Slack_Socket_Client