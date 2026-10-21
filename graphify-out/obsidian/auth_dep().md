---
source_file: "gateway/ingest_api/main.py"
type: "code"
community: "WebContentScanner"
location: "L191"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/WebContentScanner
---

# auth_dep()

## Connections
- [[dot-teardown_method()]] - `indirect_call` [INFERRED]
- [[dot-test_discard_blocked_message_not_found_returns_error()]] - `indirect_call` [INFERRED]
- [[dot-test_quarantine_summary_counts_inbound_and_outbound()]] - `indirect_call` [INFERRED]
- [[dot-test_release_blocked_outbound_marks_item_released()]] - `indirect_call` [INFERRED]
- [[Authentication dependency for protected endpoints]] - `rationale_for` [EXTRACTED]
- [[Request_4]] - `references` [EXTRACTED]
- [[TestOpProxyEndpoint]] - `references` [EXTRACTED]
- [[ingest_apimain.py]] - `contains` [EXTRACTED]
- [[test_channel_ownership.py]] - `imports` [EXTRACTED]
- [[test_email_owner_bypasses_pii.py]] - `imports` [EXTRACTED]
- [[test_forward_stream.py]] - `imports` [EXTRACTED]
- [[test_gateway_email_service.py]] - `imports` [EXTRACTED]
- [[test_main_endpoints.py]] - `imports` [EXTRACTED]
- [[test_op_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/WebContentScanner
