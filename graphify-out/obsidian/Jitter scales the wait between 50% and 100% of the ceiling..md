---
source_file: "gateway/tests/test_slack_socket_client.py"
type: "rationale"
community: ".proxy_messages()"
location: "L40"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/proxy_messages
---

# Jitter scales the wait between 50% and 100% of the ceiling.

## Connections
- [[.test_jitter_stays_within_half_to_full_ceiling()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/proxy_messages