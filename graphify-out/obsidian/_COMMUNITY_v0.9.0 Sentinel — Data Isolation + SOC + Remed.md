---
type: community
cohesion: 0.22
members: 9
---

# v0.9.0 "Sentinel" — Data Isolation + SOC + Remed

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[.test_clean_params_no_findings()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_fake_system_prompt_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_identity_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_low_confidence_not_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_nested_injection_caught()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_normal_text_not_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_prompt_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_special_token_injection()]] - code - gateway/tests/test_mcp_proxy.py
- [[TestInjectionDetection]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/v090_Sentinel__Data_Isolation__SOC__Remed
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 3 edges to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_brand-guidelines]]
- 1 edge to [[_COMMUNITY_TestParanoidConfig]]
- 1 edge to [[_COMMUNITY_test_voice_gateway.py]]
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_AgentShroud v0.9.0 — Human Interface Testing Gui]]

## Top bridge nodes
- [[TestInjectionDetection]] - degree 22, connects to 7 communities