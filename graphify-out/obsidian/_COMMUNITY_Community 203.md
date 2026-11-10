---
type: community
members: 46
---

# Community 203

**Members:** 46 nodes

## Members
- [[._check_message_size()]] - code - gateway/security/a2a_governance.py
- [[._check_peer()]] - code - gateway/security/a2a_governance.py
- [[._check_rate_limit()]] - code - gateway/security/a2a_governance.py
- [[._check_task_concurrency()]] - code - gateway/security/a2a_governance.py
- [[._finalize()]] - code - gateway/security/a2a_governance.py
- [[._process()]] - code - gateway/security/a2a_governance.py
- [[._sanitize_message()]] - code - gateway/security/a2a_governance.py
- [[.complete_task()]] - code - gateway/security/a2a_governance.py
- [[.fingerprint()]] - code - gateway/security/a2a_governance.py
- [[.get_events()_1]] - code - gateway/security/a2a_governance.py
- [[.get_peer()]] - code - gateway/security/a2a_governance.py
- [[.get_summary()]] - code - gateway/security/a2a_governance.py
- [[.process_inbound()_1]] - code - gateway/security/a2a_governance.py
- [[.process_outbound()_1]] - code - gateway/security/a2a_governance.py
- [[.register_peer()]] - code - gateway/security/a2a_governance.py
- [[.test_fingerprint_deterministic()]] - code - gateway/tests/test_a2a_governance.py
- [[.test_fingerprint_differs_for_different_payloads()]] - code - gateway/tests/test_a2a_governance.py
- [[.to_dict()_3]] - code - gateway/security/a2a_governance.py
- [[.unregister_peer()]] - code - gateway/security/a2a_governance.py
- [[.update_peer_trust()]] - code - gateway/security/a2a_governance.py
- [[A2ADecision]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceEvent]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy]] - code - gateway/security/a2a_governance.py
- [[A2AMessage]] - code - gateway/security/a2a_governance.py
- [[An A2A protocol message passing through the governance proxy.]] - rationale - gateway/security/a2a_governance.py
- [[Apply final decision and log governance event.]] - rationale - gateway/security/a2a_governance.py
- [[Audit event for A2A governance decisions.]] - rationale - gateway/security/a2a_governance.py
- [[Check concurrent task limit for task_request messages.]] - rationale - gateway/security/a2a_governance.py
- [[Check message payload size.]] - rationale - gateway/security/a2a_governance.py
- [[Check per-peer rate limit.]] - rationale - gateway/security/a2a_governance.py
- [[Content hash for deduplication and audit.]] - rationale - gateway/security/a2a_governance.py
- [[Core message processing pipeline.]] - rationale - gateway/security/a2a_governance.py
- [[Get governance proxy summary.]] - rationale - gateway/security/a2a_governance.py
- [[Governance decision for an A2A message.]] - rationale - gateway/security/a2a_governance.py
- [[Governance proxy for Agent-to-Agent communication.      Sits between local agent]] - rationale - gateway/security/a2a_governance.py
- [[Look up a registered peer.]] - rationale - gateway/security/a2a_governance.py
- [[Mark a delegated task as complete (decrements active task counter).]] - rationale - gateway/security/a2a_governance.py
- [[Register a known A2A peer agent.]] - rationale - gateway/security/a2a_governance.py
- [[Remove a peer from the registry.]] - rationale - gateway/security/a2a_governance.py
- [[Sanitize PII from A2A message payload. Returns list of sanitizations applied.]] - rationale - gateway/security/a2a_governance.py
- [[TestMessageFingerprint]] - code - gateway/tests/test_a2a_governance.py
- [[Update a peer's trust score (called by TrustManager integration).]] - rationale - gateway/security/a2a_governance.py
- [[Validate and govern an inbound A2A message from a remote peer.]] - rationale - gateway/security/a2a_governance.py
- [[Validate and govern an outbound A2A message to a remote peer.]] - rationale - gateway/security/a2a_governance.py
- [[Validate that the peer is registered and trusted.]] - rationale - gateway/security/a2a_governance.py
- [[a2a_governance.py]] - code - gateway/security/a2a_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_203
SORT file.name ASC
```

## Connections to other communities
- 52 edges to [[_COMMUNITY_Community 44]]
- 3 edges to [[_COMMUNITY_Community 8]]
- 1 edge to [[_COMMUNITY_Community 261]]
- 1 edge to [[_COMMUNITY_Community 11]]
- 1 edge to [[_COMMUNITY_Community 1209]]

## Top bridge nodes
- [[A2ADecision]] - degree 26, connects to 3 communities
- [[A2AGovernanceProxy]] - degree 43, connects to 2 communities
- [[a2a_governance.py]] - degree 8, connects to 2 communities
- [[A2AMessage]] - degree 27, connects to 1 community
- [[TestMessageFingerprint]] - degree 9, connects to 1 community