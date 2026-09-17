---
type: community
cohesion: 0.12
members: 30
---

# A2AMessage

**Cohesion:** 0.12 - loosely connected
**Members:** 30 nodes

## Members
- [[._check_message_size()]] - code - gateway/security/a2a_governance.py
- [[._check_peer()]] - code - gateway/security/a2a_governance.py
- [[._check_rate_limit()]] - code - gateway/security/a2a_governance.py
- [[._check_task_concurrency()]] - code - gateway/security/a2a_governance.py
- [[._finalize()]] - code - gateway/security/a2a_governance.py
- [[._process()]] - code - gateway/security/a2a_governance.py
- [[._sanitize_message()]] - code - gateway/security/a2a_governance.py
- [[.get_events()]] - code - gateway/security/a2a_governance.py
- [[.process_inbound()]] - code - gateway/security/a2a_governance.py
- [[.process_outbound()]] - code - gateway/security/a2a_governance.py
- [[.test_fingerprint_deterministic()]] - code - gateway/tests/test_a2a_governance.py
- [[.test_fingerprint_differs_for_different_payloads()]] - code - gateway/tests/test_a2a_governance.py
- [[A2ADecision]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceEvent]] - code - gateway/security/a2a_governance.py
- [[A2AMessage]] - code - gateway/security/a2a_governance.py
- [[An A2A protocol message passing through the governance proxy.]] - rationale - gateway/security/a2a_governance.py
- [[Apply final decision and log governance event.]] - rationale - gateway/security/a2a_governance.py
- [[Audit event for A2A governance decisions.]] - rationale - gateway/security/a2a_governance.py
- [[Check concurrent task limit for task_request messages.]] - rationale - gateway/security/a2a_governance.py
- [[Check message payload size.]] - rationale - gateway/security/a2a_governance.py
- [[Check per-peer rate limit.]] - rationale - gateway/security/a2a_governance.py
- [[Core message processing pipeline.]] - rationale - gateway/security/a2a_governance.py
- [[Enum_2]] - code
- [[Governance decision for an A2A message.]] - rationale - gateway/security/a2a_governance.py
- [[Retrieve governance events with optional filters.]] - rationale - gateway/security/a2a_governance.py
- [[Sanitize PII from A2A message payload. Returns list of sanitizations applied.]] - rationale - gateway/security/a2a_governance.py
- [[TestMessageFingerprint]] - code - gateway/tests/test_a2a_governance.py
- [[Validate and govern an inbound A2A message from a remote peer.]] - rationale - gateway/security/a2a_governance.py
- [[Validate that the peer is registered and trusted.]] - rationale - gateway/security/a2a_governance.py
- [[a2a_governance.py]] - code - gateway/security/a2a_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2AMessage
SORT file.name ASC
```

## Connections to other communities
- 38 edges to [[_COMMUNITY_A2AGovernanceProxy]]
- 14 edges to [[_COMMUNITY_A2AGovernanceProxy]]
- 2 edges to [[_COMMUNITY_A2APeer]]
- 2 edges to [[_COMMUNITY_TestPeerManagement]]
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[A2AMessage]] - degree 26, connects to 3 communities
- [[A2ADecision]] - degree 24, connects to 2 communities
- [[TestMessageFingerprint]] - degree 9, connects to 2 communities
- [[a2a_governance.py]] - degree 8, connects to 2 communities
- [[Retrieve governance events with optional filters.]] - degree 3, connects to 2 communities