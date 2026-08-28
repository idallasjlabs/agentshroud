---
source_file: "gateway/tests/test_a2a_proxy.py"
type: "code"
community: "Community 110"
location: "L29"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_110
---

# _StubForwarder

## Connections
- [[.__init__()_137]] - `method` [EXTRACTED]
- [[.forward()_2]] - `method` [EXTRACTED]
- [[A2AMethod]] - `uses` [INFERRED]
- [[A2APolicyConfig]] - `uses` [INFERRED]
- [[A2APolicyEngine_1]] - `uses` [INFERRED]
- [[A2AProxy]] - `uses` [INFERRED]
- [[A2AProxyResult]] - `uses` [INFERRED]
- [[DifferentialPIIConfig]] - `uses` [INFERRED]
- [[DifferentialPIIDetector]] - `uses` [INFERRED]
- [[Records what it was asked to forward; returns a canned response.]] - `rationale_for` [EXTRACTED]
- [[forwarder()]] - `references` [EXTRACTED]
- [[proxy()_1]] - `references` [EXTRACTED]
- [[test_a2a_proxy.py]] - `contains` [EXTRACTED]
- [[test_agent_card_discovery_is_never_policy_gated()]] - `references` [EXTRACTED]
- [[test_agent_card_discovery_is_still_audited()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_allowed_peer_low_risk_forwards()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_binary_part_is_forwarded_unscanned_and_flagged()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_denial_is_also_logged_to_audit_store()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_denied_peer_never_reaches_hermes()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_high_risk_method_without_approval_queue_denied()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_logs_to_audit_store_when_configured()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_malformed_body_is_blocked()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_missing_auth_is_blocked_and_never_forwarded()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_pii_in_message_is_redacted_before_forwarding()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_task_ownership_violation_blocked()]] - `references` [EXTRACTED]
- [[test_process_inbound_request_unknown_token_is_blocked()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_110