---
type: community
cohesion: 0.08
members: 49
---

# test_a2a_proxy.py

**Cohesion:** 0.08 - loosely connected
**Members:** 49 nodes

## Members
- [[.__init__()_24]] - code - gateway/tests/test_a2a_proxy.py
- [[.__init__()_25]] - code - gateway/tests/test_a2a_proxy.py
- [[.forward()]] - code - gateway/tests/test_a2a_proxy.py
- [[A filedata Part must not be silently dropped or mis-scanned as text —     it's]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A2APolicyEngine]] - code - gateway/tests/test_a2a_proxy.py
- [[A2AProxy]] - code - gateway/tests/test_a2a_proxy.py
- [[An unparseable request must be rejected through the same     process_inbound_req]] - rationale - gateway/tests/test_a2a_proxy.py
- [[GET .well-knownagent-card.json must pass through with NO authpeer     require]] - rationale - gateway/tests/test_a2a_proxy.py
- [[Pre-1.0 peers send lowercasepath-style method names — Hermes accepts     both f]] - rationale - gateway/tests/test_a2a_proxy.py
- [[Records what it was asked to forward; returns a canned response.]] - rationale - gateway/tests/test_a2a_proxy.py
- [[Token comparison must not leak timing information — same guarantee as     Hermes]] - rationale - gateway/tests/test_a2a_proxy.py
- [[Upstream Hermes Gap 80534 — Peer Identity Resolved From SocketX-Forwarded-For Instead Of Bearer Token]] - concept - gateway/tests/test_a2a_proxy.py
- [[_StubAuditStore]] - code - gateway/tests/test_a2a_proxy.py
- [[_StubForwarder]] - code - gateway/tests/test_a2a_proxy.py
- [[_base_policy_engine()]] - code - gateway/tests/test_a2a_proxy.py
- [[_jsonrpc()]] - code - gateway/tests/test_a2a_proxy.py
- [[forwarder()]] - code - gateway/tests/test_a2a_proxy.py
- [[proxy()]] - code - gateway/tests/test_a2a_proxy.py
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
- [[test_process_inbound_request_denial_is_also_logged_to_audit_store()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_denied_peer_never_reaches_hermes()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_high_risk_method_without_approval_queue_denied()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_logs_to_audit_store_when_configured()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_malformed_body_is_blocked()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_missing_auth_is_blocked_and_never_forwarded()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_task_ownership_violation_blocked()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_unknown_token_is_blocked()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_from_known_bearer_token()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_malformed_header_returns_none()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_missing_header_returns_none()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_unknown_token_returns_none()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_uses_constant_time_comparison()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_whitespace_only_token_returns_none()]] - code - gateway/tests/test_a2a_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_a2a_proxypy
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_DifferentialPIIDetector]]
- 12 edges to [[_COMMUNITY_A2APolicyEngine]]
- 10 edges to [[_COMMUNITY_A2AProxyResult]]
- 10 edges to [[_COMMUNITY_A2AMethod]]

## Top bridge nodes
- [[test_a2a_proxy.py]] - degree 50, connects to 4 communities
- [[A2AProxy]] - degree 27, connects to 4 communities
- [[_StubForwarder]] - degree 26, connects to 4 communities
- [[_StubAuditStore]] - degree 12, connects to 4 communities
- [[A2APolicyEngine]] - degree 10, connects to 4 communities