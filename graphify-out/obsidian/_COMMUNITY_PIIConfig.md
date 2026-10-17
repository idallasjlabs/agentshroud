---
type: community
members: 22
---

# PIIConfig

**Members:** 22 nodes

## Members
- [[Agent with low trust cannot perform elevated actions.]] - rationale - gateway/tests/test_security_integration.py
- [[Clean message flows through entire pipeline without issues.]] - rationale - gateway/tests/test_security_integration.py
- [[Even if trust allows an action, egress filter blocks unauthorized destinations.]] - rationale - gateway/tests/test_security_integration.py
- [[Message with PII gets sanitized and logged correctly.]] - rationale - gateway/tests/test_security_integration.py
- [[Multiple messages through pipeline concurrently — thread safety.]] - rationale - gateway/tests/test_security_integration.py
- [[Outbound responses have credentials blocked for untrusted sources.]] - rationale - gateway/tests/test_security_integration.py
- [[Sensitive audit data can be encrypted at rest.]] - rationale - gateway/tests/test_security_integration.py
- [[When both PII sanitizer and prompt guard detect issues.]] - rationale - gateway/tests/test_security_integration.py
- [[egress_filter()_1]] - code - gateway/tests/test_security_integration.py
- [[encrypted_store()]] - code - gateway/tests/test_security_integration.py
- [[prompt_guard()_1]] - code - gateway/tests/test_security_integration.py
- [[sanitizer()_3]] - code - gateway/tests/test_security_integration.py
- [[test_egress_blocks_unauthorized_after_trust_check()]] - code - gateway/tests/test_security_integration.py
- [[test_encrypted_store_in_pipeline()]] - code - gateway/tests/test_security_integration.py
- [[test_full_pipeline_clean_message()]] - code - gateway/tests/test_security_integration.py
- [[test_full_pipeline_pii_message()]] - code - gateway/tests/test_security_integration.py
- [[test_pii_and_prompt_guard_both_trigger()]] - code - gateway/tests/test_security_integration.py
- [[test_pipeline_concurrent_messages()]] - code - gateway/tests/test_security_integration.py
- [[test_response_credential_blocking()]] - code - gateway/tests/test_security_integration.py
- [[test_security_integration.py]] - code - gateway/tests/test_security_integration.py
- [[test_trust_insufficient_action_blocked()]] - code - gateway/tests/test_security_integration.py
- [[trust_manager()_2]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PIIConfig
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 5 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig]]
- 3 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig (3)]]
- 2 edges to [[_COMMUNITY_UserSessionManager (2)_1]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (2)]]

## Top bridge nodes
- [[test_security_integration.py]] - degree 37, connects to 11 communities
- [[egress_filter()_1]] - degree 4, connects to 3 communities
- [[prompt_guard()_1]] - degree 2, connects to 1 community
- [[encrypted_store()]] - degree 2, connects to 1 community
- [[sanitizer()_3]] - degree 2, connects to 1 community
