---
source_file: "gateway/tests/test_slack_socket_client.py"
type: "rationale"
community: "compute_backoff"
location: "L30"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/compute_backoff
---

# With jitter pinned to max, backoff doubles per attempt until the cap.

## Connections
- [[dot-test_grows_exponentially_with_attempt()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/compute_backoff
