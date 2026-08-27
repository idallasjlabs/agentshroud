---
source_file: "gateway/tests/test_a2a_proxy.py"
type: "code"
community: "Community 107"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_107
---

# test_a2a_proxy.py

## Connections
- [[A2AMethod]] - `imports` [EXTRACTED]
- [[A2APolicyConfig]] - `imports` [EXTRACTED]
- [[A2APolicyEngine_1]] - `imports` [EXTRACTED]
- [[A2AProxy]] - `imports` [EXTRACTED]
- [[A2AProxyResult]] - `imports` [EXTRACTED]
- [[DifferentialPIIConfig]] - `imports` [EXTRACTED]
- [[DifferentialPIIDetector]] - `imports` [EXTRACTED]
- [[Upstream Hermes Gap 80534 — Peer Identity Resolved From SocketX-Forwarded-For Instead Of Bearer Token]] - `references` [EXTRACTED]
- [[_Event]] - `contains` [EXTRACTED]
- [[_StubAuditStore]] - `contains` [EXTRACTED]
- [[_StubForwarder]] - `contains` [EXTRACTED]
- [[_base_policy_engine()]] - `contains` [EXTRACTED]
- [[_jsonrpc()_1]] - `contains` [EXTRACTED]
- [[_redact_message_text()]] - `imports` [EXTRACTED]
- [[forwarder()]] - `contains` [EXTRACTED]
- [[proxy()_1]] - `contains` [EXTRACTED]
- [[test_agent_card_discovery_is_never_policy_gated()]] - `contains` [EXTRACTED]
- [[test_agent_card_discovery_is_still_audited()]] - `contains` [EXTRACTED]
- [[test_extract_text_concatenates_text_parts()]] - `contains` [EXTRACTED]
- [[test_extract_text_empty_message_returns_empty_string()]] - `contains` [EXTRACTED]
- [[test_extract_text_flags_binary_parts_without_scanning_them()]] - `contains` [EXTRACTED]
- [[test_extract_text_handles_missing_parts_key()]] - `contains` [EXTRACTED]
- [[test_extract_text_skips_non_dict_entries_in_parts()]] - `contains` [EXTRACTED]
- [[test_parse_jsonrpc_accepts_legacy_path_style_method_alias()]] - `contains` [EXTRACTED]
- [[test_parse_jsonrpc_extracts_callback_url_from_set_push_config()]] - `contains` [EXTRACTED]
- [[test_parse_jsonrpc_extracts_method_and_task_id_from_send_message()]] - `contains` [EXTRACTED]
- [[test_parse_jsonrpc_extracts_task_id_from_get_task()]] - `contains` [EXTRACTED]
- [[test_parse_jsonrpc_missing_method_field_raises_value_error()]] - `contains` [EXTRACTED]
- [[test_parse_jsonrpc_non_dict_body_raises_value_error()]] - `contains` [EXTRACTED]
- [[test_parse_jsonrpc_tolerates_non_dict_params()]] - `contains` [EXTRACTED]
- [[test_parse_jsonrpc_unknown_method_raises_value_error()]] - `contains` [EXTRACTED]
- [[test_process_inbound_request_allowed_peer_low_risk_forwards()]] - `contains` [EXTRACTED]
- [[test_process_inbound_request_binary_part_is_forwarded_unscanned_and_flagged()]] - `contains` [EXTRACTED]
- [[test_process_inbound_request_denial_is_also_logged_to_audit_store()]] - `contains` [EXTRACTED]
- [[test_process_inbound_request_denied_peer_never_reaches_hermes()]] - `contains` [EXTRACTED]
- [[test_process_inbound_request_high_risk_method_without_approval_queue_denied()]] - `contains` [EXTRACTED]
- [[test_process_inbound_request_logs_to_audit_store_when_configured()]] - `contains` [EXTRACTED]
- [[test_process_inbound_request_malformed_body_is_blocked()]] - `contains` [EXTRACTED]
- [[test_process_inbound_request_missing_auth_is_blocked_and_never_forwarded()]] - `contains` [EXTRACTED]
- [[test_process_inbound_request_pii_in_message_is_redacted_before_forwarding()]] - `contains` [EXTRACTED]
- [[test_process_inbound_request_task_ownership_violation_blocked()]] - `contains` [EXTRACTED]
- [[test_process_inbound_request_unknown_token_is_blocked()]] - `contains` [EXTRACTED]
- [[test_proxy_result_defaults_are_safe()]] - `contains` [EXTRACTED]
- [[test_redact_message_text_clears_all_text_parts_not_just_the_first()]] - `contains` [EXTRACTED]
- [[test_resolve_peer_id_from_known_bearer_token()]] - `contains` [EXTRACTED]
- [[test_resolve_peer_id_malformed_header_returns_none()]] - `contains` [EXTRACTED]
- [[test_resolve_peer_id_missing_header_returns_none()]] - `contains` [EXTRACTED]
- [[test_resolve_peer_id_unknown_token_returns_none()]] - `contains` [EXTRACTED]
- [[test_resolve_peer_id_uses_constant_time_comparison()]] - `contains` [EXTRACTED]
- [[test_resolve_peer_id_whitespace_only_token_returns_none()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_107