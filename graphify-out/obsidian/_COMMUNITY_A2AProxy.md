---
type: community
members: 78
---

# A2AProxy

**Members:** 78 nodes

## Members
- [[dot-__init__()_222]] - code - gateway/proxy/a2a_proxy.py
- [[dot-__init__()_223]] - code - gateway/tests/test_a2a_proxy.py
- [[dot-__init__()_224]] - code - gateway/tests/test_a2a_proxy.py
- [[dot-__init__()_225]] - code - gateway/tests/test_a2a_proxy.py
- [[dot-_audit()_1]] - code - gateway/proxy/a2a_proxy.py
- [[dot-_record_trust_violation()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-extract_text_for_pii_scan()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-forward()_2]] - code - gateway/tests/test_a2a_proxy.py
- [[dot-log_event()_2]] - code - gateway/tests/test_a2a_proxy.py
- [[dot-parse_jsonrpc_request()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-process_agent_card_request()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-process_inbound_request()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-resolve_peer_id()]] - code - gateway/proxy/a2a_proxy.py
- [[A SendMessage containing PII must have it redacted in what's forwarded to…]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A filedata Part must not be silently dropped or mis-scanned as text — it's…]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A freshly-constructed, un-set result must default to blocked, not allowed — a…]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A message with MULTIPLE text parts must not leave a second, unredacted text…]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A2AProxy]] - code - gateway/proxy/a2a_proxy.py
- [[A2AProxyResult]] - code - gateway/proxy/a2a_proxy.py
- [[An unparseable request must be rejected through the same…]] - rationale - gateway/tests/test_a2a_proxy.py
- [[Any_88]] - code
- [[Flatten an A2A Message's `parts` array to plain text for PII scanning. Returns…]] - rationale - gateway/proxy/a2a_proxy.py
- [[GET .well-knownagent-card.json must pass through with NO authpeer…]] - rationale - gateway/tests/test_a2a_proxy.py
- [[GET .well-knownagent-card.json — never policy-gated (the A2A spec requires…]] - rationale - gateway/proxy/a2a_proxy.py
- [[Parse a JSON-RPC 2.0 A2A request body into methodtask_id callback_url. Raises…]] - rationale - gateway/proxy/a2a_proxy.py
- [[ParsedA2ARequest]] - code - gateway/proxy/a2a_proxy.py
- [[Pre-1.0 peers send lowercasepath-style method names — Hermes accepts both for…]] - rationale - gateway/tests/test_a2a_proxy.py
- [[Record a typed violation against the peer's trust score for the two…]] - rationale - gateway/proxy/a2a_proxy.py
- [[Records what it was asked to forward; returns a canned response.]] - rationale - gateway/tests/test_a2a_proxy.py
- [[Resolve peer identity from the Authorization Bearer token. Never falls back to…]] - rationale - gateway/proxy/a2a_proxy.py
- [[Result of proxying a single inbound A2A request.]] - rationale - gateway/proxy/a2a_proxy.py
- [[Return a copy of raw_body with the first text Part's content replaced by the…]] - rationale - gateway/proxy/a2a_proxy.py
- [[Terminates inbound A2A HTTP requests, enforces policy, forwards. Usage proxy…]] - rationale - gateway/proxy/a2a_proxy.py
- [[Tests for the A2A (Agent-to-Agent) inbound proxy interceptor (SCRUM-129).…]] - rationale - gateway/tests/test_a2a_proxy.py
- [[Token comparison must not leak timing information — same guarantee as Hermes's…]] - rationale - gateway/tests/test_a2a_proxy.py
- [[_Event]] - code - gateway/tests/test_a2a_proxy.py
- [[_StubAuditStore]] - code - gateway/tests/test_a2a_proxy.py
- [[_StubForwarder_1]] - code - gateway/tests/test_a2a_proxy.py
- [[_base_policy_engine()]] - code - gateway/tests/test_a2a_proxy.py
- [[_jsonrpc()]] - code - gateway/tests/test_a2a_proxy.py
- [[_redact_message_text()]] - code - gateway/proxy/a2a_proxy.py
- [[asyncio_85]] - code
- [[fixture_140]] - code
- [[forwarder()_1]] - code - gateway/tests/test_a2a_proxy.py
- [[proxy()_3]] - code - gateway/tests/test_a2a_proxy.py
- [[test_a2a_proxy.py]] - code - gateway/tests/test_a2a_proxy.py
- [[test_agent_card_discovery_is_never_policy_gated()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_agent_card_discovery_is_still_audited()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_extract_text_concatenates_text_parts()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_extract_text_empty_message_returns_empty_string()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_extract_text_flags_binary_parts_without_scanning_them()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_extract_text_handles_missing_parts_key()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_extract_text_skips_non_dict_entries_in_parts()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_accepts_legacy_path_style_method_alias()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_extracts_callback_url_from_set_push_config()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_extracts_method_and_task_id_from_send_message()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_extracts_task_id_from_get_task()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_missing_method_field_raises_value_error()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_non_dict_body_raises_value_error()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_tolerates_non_dict_params()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_unknown_method_raises_value_error()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_allowed_peer_low_risk_forwards()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_binary_part_is_forwarded_unscanned_and_flagged()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_denial_is_also_logged_to_audit_store()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_high_risk_method_without_approval_queue_denied()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_logs_to_audit_store_when_configured()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_malformed_body_is_blocked()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_missing_auth_is_blocked_and_never_forwarded()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_pii_in_message_is_redacted_before_forwarding()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_unknown_token_is_blocked()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_proxy_result_defaults_are_safe()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_redact_message_text_clears_all_text_parts_not_just_the_first()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_from_known_bearer_token()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_malformed_header_returns_none()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_missing_header_returns_none()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_unknown_token_returns_none()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_uses_constant_time_comparison()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_whitespace_only_token_returns_none()]] - code - gateway/tests/test_a2a_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2AProxy
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_A2APolicyConfig]]
- 13 edges to [[_COMMUNITY_A2APolicyEngine]]
- 3 edges to [[_COMMUNITY_test_differential_pii_detector.py]]
- 3 edges to [[_COMMUNITY_DifferentialPIIDetector]]
- 1 edge to [[_COMMUNITY_ProgressiveTrustConfig]]
- 1 edge to [[_COMMUNITY_test_module_stats.py]]

## Top bridge nodes
- [[test_a2a_proxy.py]] - degree 51, connects to 4 communities
- [[A2AProxy]] - degree 58, connects to 3 communities
- [[_base_policy_engine()]] - degree 10, connects to 2 communities
- [[test_process_inbound_request_pii_in_message_is_redacted_before_forwarding()]] - degree 9, connects to 2 communities
- [[test_process_inbound_request_binary_part_is_forwarded_unscanned_and_flagged()]] - degree 8, connects to 2 communities
