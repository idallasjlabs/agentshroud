---
source_file: "gateway/proxy/a2a_proxy.py"
type: "code"
community: "A2AProxy"
location: "L123"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/A2AProxy
---

# A2AProxy

## Connections
- [[dot-__init__()_222]] - `method` [EXTRACTED]
- [[dot-_audit()_1]] - `method` [EXTRACTED]
- [[dot-_record_trust_violation()]] - `method` [EXTRACTED]
- [[dot-extract_text_for_pii_scan()]] - `method` [EXTRACTED]
- [[dot-parse_jsonrpc_request()]] - `method` [EXTRACTED]
- [[dot-process_agent_card_request()]] - `method` [EXTRACTED]
- [[dot-process_inbound_request()]] - `method` [EXTRACTED]
- [[dot-resolve_peer_id()]] - `method` [EXTRACTED]
- [[A2AMethod]] - `uses` [INFERRED]
- [[A2APolicyEngine]] - `uses` [INFERRED]
- [[Terminates inbound A2A HTTP requests, enforces policy, forwards. Usage proxy…]] - `rationale_for` [EXTRACTED]
- [[ViolationType]] - `uses` [INFERRED]
- [[a2a_proxy.py]] - `contains` [EXTRACTED]
- [[proxy()_3]] - `uses` [INFERRED]
- [[test_a2a_integration.py]] - `imports` [EXTRACTED]
- [[test_a2a_proxy.py]] - `imports` [EXTRACTED]
- [[test_a2a_trust_scoring.py]] - `imports` [EXTRACTED]
- [[test_adversarial_ssrf_callback_bypass_attempts_over_real_http()]] - `uses` [INFERRED]
- [[test_adversarial_task_ownership_hijack_attempt_over_real_http()]] - `uses` [INFERRED]
- [[test_agent_card_discovery_is_never_policy_gated()]] - `uses` [INFERRED]
- [[test_agent_card_discovery_is_still_audited()]] - `uses` [INFERRED]
- [[test_extract_text_concatenates_text_parts()]] - `uses` [INFERRED]
- [[test_extract_text_empty_message_returns_empty_string()]] - `uses` [INFERRED]
- [[test_extract_text_flags_binary_parts_without_scanning_them()]] - `uses` [INFERRED]
- [[test_extract_text_handles_missing_parts_key()]] - `uses` [INFERRED]
- [[test_extract_text_skips_non_dict_entries_in_parts()]] - `uses` [INFERRED]
- [[test_full_round_trip_allowed_request_reaches_the_peer()]] - `uses` [INFERRED]
- [[test_full_round_trip_denied_request_never_reaches_the_peer()]] - `uses` [INFERRED]
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - `uses` [INFERRED]
- [[test_legitimate_callback_url_is_forwarded_over_real_http()]] - `uses` [INFERRED]
- [[test_parse_jsonrpc_accepts_legacy_path_style_method_alias()]] - `uses` [INFERRED]
- [[test_parse_jsonrpc_extracts_callback_url_from_set_push_config()]] - `uses` [INFERRED]
- [[test_parse_jsonrpc_extracts_method_and_task_id_from_send_message()]] - `uses` [INFERRED]
- [[test_parse_jsonrpc_extracts_task_id_from_get_task()]] - `uses` [INFERRED]
- [[test_parse_jsonrpc_missing_method_field_raises_value_error()]] - `uses` [INFERRED]
- [[test_parse_jsonrpc_non_dict_body_raises_value_error()]] - `uses` [INFERRED]
- [[test_parse_jsonrpc_tolerates_non_dict_params()]] - `uses` [INFERRED]
- [[test_parse_jsonrpc_unknown_method_raises_value_error()]] - `uses` [INFERRED]
- [[test_process_inbound_request_allowed_peer_low_risk_forwards()]] - `uses` [INFERRED]
- [[test_process_inbound_request_binary_part_is_forwarded_unscanned_and_flagged()]] - `uses` [INFERRED]
- [[test_process_inbound_request_denial_is_also_logged_to_audit_store()]] - `uses` [INFERRED]
- [[test_process_inbound_request_denied_peer_never_reaches_hermes()]] - `uses` [INFERRED]
- [[test_process_inbound_request_high_risk_method_without_approval_queue_denied()]] - `uses` [INFERRED]
- [[test_process_inbound_request_logs_to_audit_store_when_configured()]] - `uses` [INFERRED]
- [[test_process_inbound_request_malformed_body_is_blocked()]] - `uses` [INFERRED]
- [[test_process_inbound_request_missing_auth_is_blocked_and_never_forwarded()]] - `uses` [INFERRED]
- [[test_process_inbound_request_pii_in_message_is_redacted_before_forwarding()]] - `uses` [INFERRED]
- [[test_process_inbound_request_task_ownership_violation_blocked()]] - `uses` [INFERRED]
- [[test_process_inbound_request_unknown_token_is_blocked()]] - `uses` [INFERRED]
- [[test_proxy_without_trust_manager_does_not_raise()]] - `calls` [EXTRACTED]
- [[test_resolve_peer_id_from_known_bearer_token()]] - `uses` [INFERRED]
- [[test_resolve_peer_id_malformed_header_returns_none()]] - `uses` [INFERRED]
- [[test_resolve_peer_id_missing_header_returns_none()]] - `uses` [INFERRED]
- [[test_resolve_peer_id_unknown_token_returns_none()]] - `uses` [INFERRED]
- [[test_resolve_peer_id_uses_constant_time_comparison()]] - `uses` [INFERRED]
- [[test_resolve_peer_id_whitespace_only_token_returns_none()]] - `uses` [INFERRED]
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - `uses` [INFERRED]
- [[test_task_ownership_violation_records_a2a_violation_type()]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/A2AProxy
