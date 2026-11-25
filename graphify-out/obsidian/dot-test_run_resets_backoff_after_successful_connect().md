---
source_file: "gateway/tests/test_slack_socket_client.py"
type: "code"
community: ".test_events_api_envelope_dispatches_handle_event"
location: "L53"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_events_api_envelope_dispatches_handle_event
---

# .test_run_resets_backoff_after_successful_connect()

## Connections
- [[A successful WSS connection resets the attempt counter to 0.]] - `rationale_for` [EXTRACTED]
- [[TestComputeBackoff]] - `method` [EXTRACTED]
- [[_make_client()]] - `calls` [EXTRACTED]
- [[asyncio_17]] - `references` [EXTRACTED]
- [[fake_backoff()]] - `indirect_call` [INFERRED]
- [[fake_connect_and_handle()]] - `indirect_call` [INFERRED]
- [[fake_get_wss_url()]] - `indirect_call` [INFERRED]
- [[fake_sleep()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_events_api_envelope_dispatches_handle_event
