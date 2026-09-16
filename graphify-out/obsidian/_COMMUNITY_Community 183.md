---
type: community
cohesion: 0.10
members: 38
---

# Community 183

**Cohesion:** 0.10 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-__init__()_76]] - code - gateway/proxy/a2a_proxy.py
- [[dot-__init__()_77]] - code - gateway/tests/test_a2a_proxy.py
- [[dot-_audit()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-_decide()]] - code - gateway/security/a2a_policy.py
- [[dot-_record_trust_violation()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-_tier_for()]] - code - gateway/security/a2a_policy.py
- [[dot-extract_text_for_pii_scan()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-forward()_4]] - code - gateway/proxy/a2a_proxy.py
- [[dot-log_event()_1]] - code - gateway/tests/test_a2a_proxy.py
- [[dot-parse_jsonrpc_request()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-process_agent_card_request()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-process_inbound_request()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-resolve_peer_id()]] - code - gateway/proxy/a2a_proxy.py
- [[A freshly-constructed, un-set result must default to blocked, not     allowed —]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A message with MULTIPLE text parts must not leave a second, unredacted     text]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A2AMethod]] - code - gateway/security/a2a_policy.py
- [[A2APolicyEngine_2]] - code - gateway/proxy/a2a_proxy.py
- [[A2AProxy_1]] - code - gateway/proxy/a2a_proxy.py
- [[A2AProxyResult]] - code - gateway/proxy/a2a_proxy.py
- [[Any_27]] - code - gateway/proxy/a2a_proxy.py
- [[Canonical (v1.0 PascalCase) A2A JSON-RPC methods this engine governs.]] - rationale - gateway/security/a2a_policy.py
- [[Flatten an A2A Message's `parts` array to plain text for PII         scanning.]] - rationale - gateway/proxy/a2a_proxy.py
- [[GET .well-knownagent-card.json — never policy-gated (the A2A         spec requ]] - rationale - gateway/proxy/a2a_proxy.py
- [[Parse a JSON-RPC 2.0 A2A request body into methodtask_id         callback_url.]] - rationale - gateway/proxy/a2a_proxy.py
- [[ParsedA2ARequest]] - code - gateway/proxy/a2a_proxy.py
- [[Record a typed violation against the peer's trust score for the         two A2A-]] - rationale - gateway/proxy/a2a_proxy.py
- [[Resolve peer identity from the Authorization Bearer token.          Never falls]] - rationale - gateway/proxy/a2a_proxy.py
- [[Result of proxying a single inbound A2A request.]] - rationale - gateway/proxy/a2a_proxy.py
- [[Return a copy of raw_body with the first text Part's content replaced     by the]] - rationale - gateway/proxy/a2a_proxy.py
- [[Terminates inbound A2A HTTP requests, enforces policy, forwards.      Usage]] - rationale - gateway/proxy/a2a_proxy.py
- [[Types of security violations.]] - rationale - gateway/security/progressive_trust_config.py
- [[Upstream Hermes Gap 80534 — Peer Identity Resolved From SocketX-Forwarded-For Instead Of Bearer Token]] - concept - gateway/tests/test_a2a_proxy.py
- [[ViolationType]] - code - gateway/security/progressive_trust_config.py
- [[_Event]] - code - gateway/tests/test_a2a_proxy.py
- [[_redact_message_text()]] - code - gateway/proxy/a2a_proxy.py
- [[a2a_proxy.py]] - code - gateway/proxy/a2a_proxy.py
- [[test_proxy_result_defaults_are_safe()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_redact_message_text_clears_all_text_parts_not_just_the_first()]] - code - gateway/tests/test_a2a_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_183
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_Community 131]]
- 21 edges to [[_COMMUNITY_Community 103]]
- 7 edges to [[_COMMUNITY_Community 75]]
- 4 edges to [[_COMMUNITY_Community 109]]
- 4 edges to [[_COMMUNITY_Community 288]]
- 4 edges to [[_COMMUNITY_Community 289]]
- 3 edges to [[_COMMUNITY_Signed Instruction Envelopes & Security Pipeline]]
- 3 edges to [[_COMMUNITY_Voice Gateway STT & Browser Security]]
- 2 edges to [[_COMMUNITY_Community 137]]
- 2 edges to [[_COMMUNITY_Community 46]]
- 1 edge to [[_COMMUNITY_Cross-Bot Trust & A2A Governance]]
- 1 edge to [[_COMMUNITY_Community 689]]

## Top bridge nodes
- [[A2AMethod]] - degree 29, connects to 6 communities
- [[ViolationType]] - degree 20, connects to 5 communities
- [[_Event]] - degree 10, connects to 4 communities
- [[A2AProxy_1]] - degree 38, connects to 3 communities
- [[a2a_proxy.py]] - degree 10, connects to 3 communities