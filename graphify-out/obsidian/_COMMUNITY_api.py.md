---
type: community
members: 92
---

# api.py

**Members:** 92 nodes

## Members
- [[dot-__init__()_135]] - code - gateway/security/a2a_governance.py
- [[dot-_check_message_size()]] - code - gateway/security/a2a_governance.py
- [[dot-_check_peer()]] - code - gateway/security/a2a_governance.py
- [[dot-_check_rate_limit()]] - code - gateway/security/a2a_governance.py
- [[dot-_check_task_concurrency()]] - code - gateway/security/a2a_governance.py
- [[dot-_finalize()]] - code - gateway/security/a2a_governance.py
- [[dot-_process()]] - code - gateway/security/a2a_governance.py
- [[dot-_sanitize_message()]] - code - gateway/security/a2a_governance.py
- [[dot-complete_task()]] - code - gateway/security/a2a_governance.py
- [[dot-fingerprint()]] - code - gateway/security/a2a_governance.py
- [[dot-get_events()_1]] - code - gateway/security/a2a_governance.py
- [[dot-get_peer()]] - code - gateway/security/a2a_governance.py
- [[dot-get_summary()]] - code - gateway/security/a2a_governance.py
- [[dot-is_trusted()]] - code - gateway/security/a2a_governance.py
- [[dot-process_inbound()_9]] - code - gateway/security/a2a_governance.py
- [[dot-process_outbound()_7]] - code - gateway/security/a2a_governance.py
- [[dot-register_peer()]] - code - gateway/security/a2a_governance.py
- [[dot-test_api_key_sanitized()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_clean_payload_not_sanitized()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_complete_task_frees_slot()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_disabled_allows_all()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_fingerprint_deterministic()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_fingerprint_differs_for_different_payloads()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_get_events_filtered()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_normal_size_allowed()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_outbound_to_trusted_peer()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_outbound_to_unknown_quarantined()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_oversized_denied()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_peer_stats_updated()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_rate_limit_exceeded()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_register_peer()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_ssn_sanitized()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_summary()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_task_limit_exceeded()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_task_within_limit()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_trust_clamped()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_trusted_peer_allowed()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_unknown_peer_quarantined()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_unregister_peer()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_untrusted_peer_allowed_in_monitor()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_untrusted_peer_denied()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_update_trust()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-test_within_rate_limit()]] - code - gateway/tests/test_a2a_governance.py
- [[dot-to_dict()_8]] - code - gateway/security/a2a_governance.py
- [[dot-unregister_peer()]] - code - gateway/security/a2a_governance.py
- [[dot-update_peer_trust()]] - code - gateway/security/a2a_governance.py
- [[A2A protocol message types (based on A2A v1.0 spec).]] - rationale - gateway/security/a2a_governance.py
- [[A2ADecision]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceConfig]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceEvent]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy]] - code - gateway/security/a2a_governance.py
- [[A2AMessage]] - code - gateway/security/a2a_governance.py
- [[A2AMessageType]] - code - gateway/security/a2a_governance.py
- [[A2APeer]] - code - gateway/security/a2a_governance.py
- [[An A2A protocol message passing through the governance proxy.]] - rationale - gateway/security/a2a_governance.py
- [[Apply final decision and log governance event.]] - rationale - gateway/security/a2a_governance.py
- [[Audit event for A2A governance decisions.]] - rationale - gateway/security/a2a_governance.py
- [[Check concurrent task limit for task_request messages.]] - rationale - gateway/security/a2a_governance.py
- [[Check message payload size.]] - rationale - gateway/security/a2a_governance.py
- [[Check per-peer rate limit.]] - rationale - gateway/security/a2a_governance.py
- [[Configuration for the A2A governance proxy.]] - rationale - gateway/security/a2a_governance.py
- [[Content hash for deduplication and audit.]] - rationale - gateway/security/a2a_governance.py
- [[Core message processing pipeline.]] - rationale - gateway/security/a2a_governance.py
- [[Get governance proxy summary.]] - rationale - gateway/security/a2a_governance.py
- [[Governance decision for an A2A message.]] - rationale - gateway/security/a2a_governance.py
- [[Governance proxy for Agent-to-Agent communication.      Sits between local agent]] - rationale - gateway/security/a2a_governance.py
- [[Look up a registered peer.]] - rationale - gateway/security/a2a_governance.py
- [[Mark a delegated task as complete (decrements active task counter).]] - rationale - gateway/security/a2a_governance.py
- [[Register a known A2A peer agent.]] - rationale - gateway/security/a2a_governance.py
- [[Registered A2A peer agent.]] - rationale - gateway/security/a2a_governance.py
- [[Remove a peer from the registry.]] - rationale - gateway/security/a2a_governance.py
- [[Sanitize PII from A2A message payload. Returns list of sanitizations applied.]] - rationale - gateway/security/a2a_governance.py
- [[TestDisabledProxy]] - code - gateway/tests/test_a2a_governance.py
- [[TestInboundProcessing]] - code - gateway/tests/test_a2a_governance.py
- [[TestMessageFingerprint]] - code - gateway/tests/test_a2a_governance.py
- [[TestMessageSize]] - code - gateway/tests/test_a2a_governance.py
- [[TestOutboundProcessing]] - code - gateway/tests/test_a2a_governance.py
- [[TestPIISanitization]] - code - gateway/tests/test_a2a_governance.py
- [[TestPeerManagement]] - code - gateway/tests/test_a2a_governance.py
- [[TestRateLimiting_2]] - code - gateway/tests/test_a2a_governance.py
- [[TestReporting]] - code - gateway/tests/test_a2a_governance.py
- [[TestTaskConcurrency]] - code - gateway/tests/test_a2a_governance.py
- [[Update a peer's trust score (called by TrustManager integration).]] - rationale - gateway/security/a2a_governance.py
- [[Validate and govern an inbound A2A message from a remote peer.]] - rationale - gateway/security/a2a_governance.py
- [[Validate that the peer is registered and trusted.]] - rationale - gateway/security/a2a_governance.py
- [[_msg()]] - code - gateway/tests/test_a2a_governance.py
- [[a2a_governance.py]] - code - gateway/security/a2a_governance.py
- [[monitor_proxy()]] - code - gateway/tests/test_a2a_governance.py
- [[proxy()_3]] - code - gateway/tests/test_a2a_governance.py
- [[test_a2a_governance.py]] - code - gateway/tests/test_a2a_governance.py
- [[trusted_peer()]] - code - gateway/tests/test_a2a_governance.py
- [[untrusted_peer()]] - code - gateway/tests/test_a2a_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/apipy
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_Path (3)]]
- 1 edge to [[_COMMUNITY_TestCanvasAuthHelpers]]

## Top bridge nodes
- [[A2ADecision]] - degree 26, connects to 2 communities
- [[A2AGovernanceProxy]] - degree 43, connects to 1 community
- [[A2AMessageType]] - degree 15, connects to 1 community
- [[a2a_governance.py]] - degree 8, connects to 1 community
- [[dot-get_events()_1]] - degree 4, connects to 1 community
