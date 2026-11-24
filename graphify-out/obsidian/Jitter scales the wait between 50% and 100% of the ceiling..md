---
source_file: "gateway/tests/test_slack_socket_client.py"
type: "rationale"
community: ".test_events_api_envelope_dispatches_handle_event"
location: "L40"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_events_api_envelope_dispatches_handle_event
---

# Jitter scales the wait between 50% and 100% of the ceiling.

## Connections
- [[dot-test_jitter_stays_within_half_to_full_ceiling()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_events_api_envelope_dispatches_handle_event
