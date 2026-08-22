---
source_file: "gateway/tests/test_a2a_proxy.py"
type: "code"
community: "A2a Proxy"
location: "L53"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/A2a_Proxy
---

# A2AProxy

## Connections
- [[A2AMethod]] - `uses` [INFERRED]
- [[A2APolicyConfig]] - `uses` [INFERRED]
- [[A2APolicyEngine_1]] - `uses` [INFERRED]
- [[A2AProxy]] - `uses` [INFERRED]
- [[A2AProxyResult]] - `uses` [INFERRED]
- [[DifferentialPIIConfig]] - `uses` [INFERRED]
- [[DifferentialPIIDetector]] - `uses` [INFERRED]
- [[proxy()_1]] - `references` [EXTRACTED]
- [[test_agent_card_discovery_is_never_policy_gated()]] - `references` [EXTRACTED]
- [[test_agent_card_discovery_is_still_audited()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_allowed_peer_low_risk_forwards()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_binary_part_is_forwarded_unscanned_and_flagged()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_denial_is_also_logged_to_audit_store()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_denied_peer_never_reaches_hermes()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_high_risk_method_without_approval_queue_denied()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_logs_to_audit_store_when_configured()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_malformed_body_is_blocked()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_missing_auth_is_blocked_and_never_forwarded()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_pii_in_message_is_redacted_before_forwarding()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_task_ownership_violation_blocked()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_unknown_token_is_blocked()]] - `references` [EXTRACTED]
- [[test_resolve_peer_id_from_known_bearer_token()]] - `references` [EXTRACTED]
- [[test_resolve_peer_id_malformed_header_returns_none()]] - `references` [EXTRACTED]
- [[test_resolve_peer_id_missing_header_returns_none()]] - `references` [EXTRACTED]
- [[test_resolve_peer_id_unknown_token_returns_none()]] - `references` [EXTRACTED]
- [[test_resolve_peer_id_uses_constant_time_comparison()]] - `references` [EXTRACTED]
- [[test_resolve_peer_id_whitespace_only_token_returns_none()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/A2a_Proxy