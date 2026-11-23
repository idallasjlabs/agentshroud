---
source_file: "gateway/tests/test_slack_socket_client.py"
type: "rationale"
community: "compute_backoff"
location: "L35"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/compute_backoff
---

# Backoff never exceeds the cap, even for huge attempt counts.

## Connections
- [[dot-test_capped_at_cap_for_large_attempts()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/compute_backoff
