---
type: community
cohesion: 0.10
members: 25
---

# A2AProxyResult

**Cohesion:** 0.10 - loosely connected
**Members:** 25 nodes

## Members
- [[.__init__()_77]] - code - gateway/tests/test_a2a_proxy.py
- [[._audit()]] - code - gateway/proxy/a2a_proxy.py
- [[._record_trust_violation()]] - code - gateway/proxy/a2a_proxy.py
- [[.extract_text_for_pii_scan()]] - code - gateway/proxy/a2a_proxy.py
- [[.forward()_4]] - code - gateway/proxy/a2a_proxy.py
- [[.log_event()_1]] - code - gateway/tests/test_a2a_proxy.py
- [[.parse_jsonrpc_request()]] - code - gateway/proxy/a2a_proxy.py
- [[.process_agent_card_request()]] - code - gateway/proxy/a2a_proxy.py
- [[.process_inbound_request()]] - code - gateway/proxy/a2a_proxy.py
- [[.resolve_peer_id()]] - code - gateway/proxy/a2a_proxy.py
- [[A freshly-constructed, un-set result must default to blocked, not     allowed —]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A message with MULTIPLE text parts must not leave a second, unredacted     text]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A2AProxyResult]] - code - gateway/proxy/a2a_proxy.py
- [[Any_26]] - code - gateway/proxy/a2a_proxy.py
- [[Flatten an A2A Message's `parts` array to plain text for PII         scanning.]] - rationale - gateway/proxy/a2a_proxy.py
- [[GET .well-knownagent-card.json — never policy-gated (the A2A         spec requ]] - rationale - gateway/proxy/a2a_proxy.py
- [[Parse a JSON-RPC 2.0 A2A request body into methodtask_id         callback_url.]] - rationale - gateway/proxy/a2a_proxy.py
- [[Record a typed violation against the peer's trust score for the         two A2A-]] - rationale - gateway/proxy/a2a_proxy.py
- [[Resolve peer identity from the Authorization Bearer token.          Never falls]] - rationale - gateway/proxy/a2a_proxy.py
- [[Result of proxying a single inbound A2A request.]] - rationale - gateway/proxy/a2a_proxy.py
- [[Return a copy of raw_body with the first text Part's content replaced     by the]] - rationale - gateway/proxy/a2a_proxy.py
- [[_Event]] - code - gateway/tests/test_a2a_proxy.py
- [[_redact_message_text()]] - code - gateway/proxy/a2a_proxy.py
- [[test_proxy_result_defaults_are_safe()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_redact_message_text_clears_all_text_parts_not_just_the_first()]] - code - gateway/tests/test_a2a_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2AProxyResult
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_A2APolicyEngine]]
- 10 edges to [[_COMMUNITY_test_a2a_proxy.py]]
- 5 edges to [[_COMMUNITY_A2AMethod]]
- 2 edges to [[_COMMUNITY_PipelineAction]]
- 2 edges to [[_COMMUNITY_DifferentialPIIDetector]]
- 1 edge to [[_COMMUNITY_record_decision]]

## Top bridge nodes
- [[A2AProxyResult]] - degree 15, connects to 4 communities
- [[_Event]] - degree 10, connects to 4 communities
- [[Any_26]] - degree 8, connects to 3 communities
- [[.parse_jsonrpc_request()]] - degree 6, connects to 2 communities
- [[_redact_message_text()]] - degree 6, connects to 2 communities