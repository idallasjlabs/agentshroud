---
source_file: "gateway/tests/test_slack_proxy.py"
type: "rationale"
community: "input_normalizer.py"
location: "L511"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/input_normalizerpy
---

# handle_event ignores message events with no user field.

## Connections
- [[.test_event_without_user_ignored()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/input_normalizerpy