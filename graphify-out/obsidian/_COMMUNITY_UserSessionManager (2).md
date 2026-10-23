---
type: community
cohesion: 0.09
members: 31
---

# UserSessionManager (2)

**Cohesion:** 0.09 - loosely connected
**Members:** 31 nodes

## Members
- [[dot-__init__()_110]] - code - gateway/proxy/a2a_proxy.py
- [[dot-__init__()_111]] - code - gateway/tests/test_a2a_proxy.py
- [[dot-_audit()_1]] - code - gateway/proxy/a2a_proxy.py
- [[dot-_record_trust_violation()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-extract_text_for_pii_scan()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-forward()_2]] - code - gateway/proxy/a2a_proxy.py
- [[dot-log_event()_1]] - code - gateway/tests/test_a2a_proxy.py
- [[dot-parse_jsonrpc_request()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-process_agent_card_request()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-process_inbound_request()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-resolve_peer_id()]] - code - gateway/proxy/a2a_proxy.py
- [[A freshly-constructed, un-set result must default to blocked, not     allowed —]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A message with MULTIPLE text parts must not leave a second, unredacted     text]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A2AMethod_1]] - code - gateway/security/a2a_policy.py
- [[A2APolicyEngine_3]] - code - gateway/proxy/a2a_proxy.py
- [[A2AProxyResult]] - code - gateway/proxy/a2a_proxy.py
- [[Any_39]] - code - gateway/proxy/a2a_proxy.py
- [[Canonical (v1.0 PascalCase) A2A JSON-RPC methods this engine governs.]] - rationale - gateway/security/a2a_policy.py
- [[Flatten an A2A Message's `parts` array to plain text for PII         scanning.]] - rationale - gateway/proxy/a2a_proxy.py
- [[GET .well-knownagent-card.json — never policy-gated (the A2A         spec requ]] - rationale - gateway/proxy/a2a_proxy.py
- [[Parse a JSON-RPC 2.0 A2A request body into methodtask_id         callback_url.]] - rationale - gateway/proxy/a2a_proxy.py
- [[ParsedA2ARequest]] - code - gateway/proxy/a2a_proxy.py
- [[Record a typed violation against the peer's trust score for the         two A2A-]] - rationale - gateway/proxy/a2a_proxy.py
- [[Resolve peer identity from the Authorization Bearer token.          Never falls]] - rationale - gateway/proxy/a2a_proxy.py
- [[Result of proxying a single inbound A2A request.]] - rationale - gateway/proxy/a2a_proxy.py
- [[Return a copy of raw_body with the first text Part's content replaced     by the]] - rationale - gateway/proxy/a2a_proxy.py
- [[_Event]] - code - gateway/tests/test_a2a_proxy.py
- [[_redact_message_text()]] - code - gateway/proxy/a2a_proxy.py
- [[a2a_proxy.py]] - code - gateway/proxy/a2a_proxy.py
- [[test_proxy_result_defaults_are_safe()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_redact_message_text_clears_all_text_parts_not_just_the_first()]] - code - gateway/tests/test_a2a_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/UserSessionManager_2
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_UserSessionManager]]
- 16 edges to [[_COMMUNITY_ReportStore]]
- 7 edges to [[_COMMUNITY_record_decision()]]
- 5 edges to [[_COMMUNITY_socrouter.py]]
- 5 edges to [[_COMMUNITY_A2APolicyConfig]]
- 4 edges to [[_COMMUNITY_hermesskillsi-bsREADME]]
- 2 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]

## Top bridge nodes
- [[A2AMethod_1]] - degree 29, connects to 6 communities
- [[_Event]] - degree 10, connects to 4 communities
- [[A2AProxyResult]] - degree 15, connects to 3 communities
- [[a2a_proxy.py]] - degree 10, connects to 3 communities
- [[Any_39]] - degree 8, connects to 2 communities
