---
type: community
cohesion: 0.08
members: 26
---

# test_security_integration.py

**Cohesion:** 0.08 - loosely connected
**Members:** 26 nodes

## Members
- [[Agent with low trust cannot perform elevated actions.]] - rationale - gateway/tests/test_security_integration.py
- [[Clean message flows through entire pipeline without issues.]] - rationale - gateway/tests/test_security_integration.py
- [[Even if trust allows an action, egress filter blocks unauthorized destinations.]] - rationale - gateway/tests/test_security_integration.py
- [[Message with PII gets sanitized and logged correctly.]] - rationale - gateway/tests/test_security_integration.py
- [[Multiple messages through pipeline concurrently — thread safety.]] - rationale - gateway/tests/test_security_integration.py
- [[Outbound responses have credentials blocked for untrusted sources.]] - rationale - gateway/tests/test_security_integration.py
- [[Pipeline with all modules disabled acts as passthrough.]] - rationale - gateway/tests/test_security_integration.py
- [[Pipeline with only PII enabled, prompt guard disabled.]] - rationale - gateway/tests/test_security_integration.py
- [[Sensitive audit data can be encrypted at rest.]] - rationale - gateway/tests/test_security_integration.py
- [[When both PII sanitizer and prompt guard detect issues.]] - rationale - gateway/tests/test_security_integration.py
- [[approval_queue()]] - code - gateway/tests/test_security_integration.py
- [[encrypted_store()]] - code - gateway/tests/test_security_integration.py
- [[prompt_guard()_1]] - code - gateway/tests/test_security_integration.py
- [[sanitizer()_1]] - code - gateway/tests/test_security_integration.py
- [[test_egress_blocks_unauthorized_after_trust_check()]] - code - gateway/tests/test_security_integration.py
- [[test_encrypted_store_in_pipeline()]] - code - gateway/tests/test_security_integration.py
- [[test_full_pipeline_clean_message()]] - code - gateway/tests/test_security_integration.py
- [[test_full_pipeline_pii_message()]] - code - gateway/tests/test_security_integration.py
- [[test_pii_and_prompt_guard_both_trigger()]] - code - gateway/tests/test_security_integration.py
- [[test_pipeline_all_modules_disabled()]] - code - gateway/tests/test_security_integration.py
- [[test_pipeline_concurrent_messages()]] - code - gateway/tests/test_security_integration.py
- [[test_pipeline_selective_modules()]] - code - gateway/tests/test_security_integration.py
- [[test_response_credential_blocking()]] - code - gateway/tests/test_security_integration.py
- [[test_security_integration.py]] - code - gateway/tests/test_security_integration.py
- [[test_trust_insufficient_action_blocked()]] - code - gateway/tests/test_security_integration.py
- [[trust_manager()_5]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_security_integrationpy
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_MCPPermissionManager]]
- 5 edges to [[_COMMUNITY_ContextGuard]]
- 4 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 3 edges to [[_COMMUNITY_PromptGuard]]
- 3 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]

## Top bridge nodes
- [[test_security_integration.py]] - degree 37, connects to 8 communities
- [[test_pipeline_all_modules_disabled()]] - degree 5, connects to 3 communities
- [[test_pipeline_selective_modules()]] - degree 4, connects to 2 communities
- [[approval_queue()]] - degree 3, connects to 2 communities
- [[encrypted_store()]] - degree 2, connects to 1 community
