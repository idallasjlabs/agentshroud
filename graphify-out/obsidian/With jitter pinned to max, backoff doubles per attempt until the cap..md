---
source_file: "gateway/tests/test_slack_socket_client.py"
type: "rationale"
community: ".proxy_messages()"
location: "L30"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/proxy_messages
---

# With jitter pinned to max, backoff doubles per attempt until the cap.

## Connections
- [[.test_grows_exponentially_with_attempt()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/proxy_messages