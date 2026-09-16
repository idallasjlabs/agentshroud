---
source_file: "gateway/proxy/a2a_proxy.py"
type: "code"
community: "Community 183"
location: "L123"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_183
---

# A2AProxy

## Connections
- [[dot-__init__()_76]] - `method` [EXTRACTED]
- [[dot-_audit()]] - `method` [EXTRACTED]
- [[dot-_record_trust_violation()]] - `method` [EXTRACTED]
- [[dot-extract_text_for_pii_scan()]] - `method` [EXTRACTED]
- [[dot-parse_jsonrpc_request()]] - `method` [EXTRACTED]
- [[dot-process_agent_card_request()]] - `method` [EXTRACTED]
- [[dot-process_inbound_request()]] - `method` [EXTRACTED]
- [[dot-resolve_peer_id()]] - `method` [EXTRACTED]
- [[A2AMethod]] - `uses` [INFERRED]
- [[A2APeerTestDouble]] - `uses` [INFERRED]
- [[A2APolicyEngine]] - `uses` [INFERRED]
- [[A2APolicyEngine_1]] - `uses` [INFERRED]
- [[A2AProxy]] - `uses` [INFERRED]
- [[HermesA2AForwarder]] - `calls` [EXTRACTED]
- [[Request_2]] - `uses` [INFERRED]
- [[Response_1]] - `uses` [INFERRED]
- [[Terminates inbound A2A HTTP requests, enforces policy, forwards.      Usage]] - `rationale_for` [EXTRACTED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[TrustManager]] - `calls` [EXTRACTED]
- [[Upstream Hermes Gap 80534 — Peer Identity Resolved From SocketX-Forwarded-For Instead Of Bearer Token]] - `implements` [EXTRACTED]
- [[ViolationType]] - `uses` [INFERRED]
- [[_Event]] - `uses` [INFERRED]
- [[_StubAuditStore]] - `uses` [INFERRED]
- [[_StubForwarder]] - `uses` [INFERRED]
- [[_StubForwarder_2]] - `uses` [INFERRED]
- [[a2a_proxy.py]] - `contains` [EXTRACTED]
- [[test_a2a_integration.py]] - `imports` [EXTRACTED]
- [[test_a2a_proxy.py]] - `imports` [EXTRACTED]
- [[test_a2a_trust_scoring.py]] - `imports` [EXTRACTED]
- [[test_adversarial_ssrf_callback_bypass_attempts_over_real_http()]] - `calls` [EXTRACTED]
- [[test_adversarial_task_ownership_hijack_attempt_over_real_http()]] - `calls` [EXTRACTED]
- [[test_full_round_trip_allowed_request_reaches_the_peer()]] - `calls` [EXTRACTED]
- [[test_full_round_trip_denied_request_never_reaches_the_peer()]] - `calls` [EXTRACTED]
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - `calls` [EXTRACTED]
- [[test_legitimate_callback_url_is_forwarded_over_real_http()]] - `calls` [EXTRACTED]
- [[test_proxy_without_trust_manager_does_not_raise()]] - `calls` [EXTRACTED]
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - `calls` [EXTRACTED]
- [[test_task_ownership_violation_records_a2a_violation_type()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_183