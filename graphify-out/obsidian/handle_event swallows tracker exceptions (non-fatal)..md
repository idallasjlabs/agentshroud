---
source_file: "gateway/tests/test_slack_proxy.py"
type: "rationale"
community: "TestHandleEvent"
location: "L526"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestHandleEvent
---

# handle_event swallows tracker exceptions (non-fatal).

## Connections
- [[.test_tracker_error_does_not_propagate()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestHandleEvent