---
source_file: "gateway/tests/test_security_fixes.py"
type: "rationale"
community: "Slack API Proxy"
location: "L398"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Slack_API_Proxy
---

# When body() raises ClientDisconnect the handler returns 499 without crashing.

## Connections
- [[.test_client_disconnect_returns_499()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Slack_API_Proxy