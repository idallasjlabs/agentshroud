---
type: community
members: 36
---

# UserSessionManager (2)

**Members:** 36 nodes

## Members
- [[dot-__init__()_87]] - code - gateway/proxy/a2a_proxy.py
- [[dot-__init__()_88]] - code - gateway/tests/test_a2a_proxy.py
- [[dot-_audit()_1]] - code - gateway/proxy/a2a_proxy.py
- [[dot-_decide()]] - code - gateway/security/a2a_policy.py
- [[dot-_record_trust_violation()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-_tier_for()]] - code - gateway/security/a2a_policy.py
- [[dot-extract_text_for_pii_scan()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-forward()_1]] - code - gateway/proxy/a2a_proxy.py
- [[dot-log_event()]] - code - gateway/tests/test_a2a_proxy.py
- [[dot-parse_jsonrpc_request()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-process_agent_card_request()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-process_inbound_request()]] - code - gateway/proxy/a2a_proxy.py
- [[dot-resolve_peer_id()]] - code - gateway/proxy/a2a_proxy.py
- [[A freshly-constructed, un-set result must default to blocked, not     allowed —]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A message with MULTIPLE text parts must not leave a second, unredacted     text]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A2AMethod]] - code - gateway/security/a2a_policy.py
- [[A2APolicyEngine_1]] - code - gateway/proxy/a2a_proxy.py
- [[A2AProxyResult]] - code - gateway/proxy/a2a_proxy.py
- [[Any_27]] - code - gateway/proxy/a2a_proxy.py
- [[Canonical (v1.0 PascalCase) A2A JSON-RPC methods this engine governs.]] - rationale - gateway/security/a2a_policy.py
- [[Ergonomic recorder for enforcement points — never raises.      ``sanitized=True`]] - rationale - gateway/security/module_stats.py
- [[Flatten an A2A Message's `parts` array to plain text for PII         scanning.]] - rationale - gateway/proxy/a2a_proxy.py
- [[GET .well-knownagent-card.json — never policy-gated (the A2A         spec requ]] - rationale - gateway/proxy/a2a_proxy.py
- [[Parse a JSON-RPC 2.0 A2A request body into methodtask_id         callback_url.]] - rationale - gateway/proxy/a2a_proxy.py
- [[ParsedA2ARequest]] - code - gateway/proxy/a2a_proxy.py
- [[Record a typed violation against the peer's trust score for the         two A2A-]] - rationale - gateway/proxy/a2a_proxy.py
- [[Resolve peer identity from the Authorization Bearer token.          Never falls]] - rationale - gateway/proxy/a2a_proxy.py
- [[Result of proxying a single inbound A2A request.]] - rationale - gateway/proxy/a2a_proxy.py
- [[Return a copy of raw_body with the first text Part's content replaced     by the]] - rationale - gateway/proxy/a2a_proxy.py
- [[SOC Per-Module Enforcement Heat-Map (SCRUM-80)]] - document - docker/README.md
- [[_Event]] - code - gateway/tests/test_a2a_proxy.py
- [[_redact_message_text()]] - code - gateway/proxy/a2a_proxy.py
- [[a2a_proxy.py]] - code - gateway/proxy/a2a_proxy.py
- [[record_decision()]] - code - gateway/security/module_stats.py
- [[test_proxy_result_defaults_are_safe()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_redact_message_text_clears_all_text_parts_not_just_the_first()]] - code - gateway/tests/test_a2a_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/UserSessionManager_2
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_UserSessionManager]]
- 15 edges to [[_COMMUNITY_ReportStore]]
- 8 edges to [[_COMMUNITY_hermesskillsi-bsREADME]]
- 6 edges to [[_COMMUNITY_Security Module Inventory]]
- 5 edges to [[_COMMUNITY_socrouter.py]]
- 5 edges to [[_COMMUNITY_ADR-006 Multi-Runtime Container Support]]
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 2 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_TestMultilingualInjection]]
- 1 edge to [[_COMMUNITY_First iteration ingests + records; second sees dedup and skips. (2)]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_test_hermes_model_resolver.py (2)]]

## Top bridge nodes
- [[record_decision()]] - degree 20, connects to 7 communities
- [[A2AMethod]] - degree 29, connects to 5 communities
- [[A2AProxyResult]] - degree 15, connects to 3 communities
- [[a2a_proxy.py]] - degree 10, connects to 3 communities
- [[_Event]] - degree 10, connects to 3 communities
