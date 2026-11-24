---
source_file: "gateway/tests/test_slack_socket_client.py"
type: "rationale"
community: ".test_events_api_envelope_dispatches_handle_event"
location: "L35"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_events_api_envelope_dispatches_handle_event
---

# Backoff never exceeds the cap, even for huge attempt counts.

## Connections
- [[dot-test_capped_at_cap_for_large_attempts()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_events_api_envelope_dispatches_handle_event
