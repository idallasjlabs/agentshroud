---
source_file: "gateway/tests/test_a2a_proxy.py"
type: "code"
community: "A2a Proxy"
location: "L61"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/A2a_Proxy
---

# _jsonrpc()

## Connections
- [[test_a2a_proxy.py]] - `contains` [EXTRACTED]
- [[test_parse_jsonrpc_accepts_legacy_path_style_method_alias()]] - `calls` [EXTRACTED]
- [[test_parse_jsonrpc_extracts_callback_url_from_set_push_config()]] - `calls` [EXTRACTED]
- [[test_parse_jsonrpc_extracts_method_and_task_id_from_send_message()]] - `calls` [EXTRACTED]
- [[test_parse_jsonrpc_extracts_task_id_from_get_task()]] - `calls` [EXTRACTED]
- [[test_parse_jsonrpc_unknown_method_raises_value_error()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_allowed_peer_low_risk_forwards()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_binary_part_is_forwarded_unscanned_and_flagged()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_denial_is_also_logged_to_audit_store()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_denied_peer_never_reaches_hermes()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_high_risk_method_without_approval_queue_denied()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_logs_to_audit_store_when_configured()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_missing_auth_is_blocked_and_never_forwarded()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_pii_in_message_is_redacted_before_forwarding()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_task_ownership_violation_blocked()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_unknown_token_is_blocked()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/A2a_Proxy