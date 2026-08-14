---
type: community
members: 9
---

# .github/ISSUE_TEMPLATE

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
TABLE source_file, type FROM #community/github/ISSUE_TEMPLATE
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_PromptGuard Encoding Detection]]
- 3 edges to [[_COMMUNITY_Collaborator Prompt Safety]]
- 3 edges to [[_COMMUNITY_SOC Dashboard]]
- 1 edge to [[_COMMUNITY_Setup Docs]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]

## Top bridge nodes
- [[TestInjectionDetection]] - degree 22, connects to 5 communities