---
type: community
cohesion: 0.09
members: 22
---

# test_security_integration.py

**Cohesion:** 0.09 - loosely connected
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
- [[approval_queue()]] - code - gateway/tests/test_security_integration.py
- [[encrypted_store()]] - code - gateway/tests/test_security_integration.py
- [[prompt_guard()_2]] - code - gateway/tests/test_security_integration.py
- [[sanitizer()_5]] - code - gateway/tests/test_security_integration.py
- [[test_egress_blocks_unauthorized_after_trust_check()]] - code - gateway/tests/test_security_integration.py
- [[test_encrypted_store_in_pipeline()]] - code - gateway/tests/test_security_integration.py
- [[test_full_pipeline_clean_message()]] - code - gateway/tests/test_security_integration.py
- [[test_full_pipeline_pii_message()]] - code - gateway/tests/test_security_integration.py
- [[test_pii_and_prompt_guard_both_trigger()]] - code - gateway/tests/test_security_integration.py
- [[test_pipeline_concurrent_messages()]] - code - gateway/tests/test_security_integration.py
- [[test_response_credential_blocking()]] - code - gateway/tests/test_security_integration.py
- [[test_security_integration.py]] - code - gateway/tests/test_security_integration.py
- [[test_trust_insufficient_action_blocked()]] - code - gateway/tests/test_security_integration.py
- [[trust_manager()_4]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_security_integrationpy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_TrustManager]]
- 8 edges to [[_COMMUNITY_SSHProxy]]
- 4 edges to [[_COMMUNITY_EncryptedStore]]
- 2 edges to [[_COMMUNITY_EgressFilter]]
- 2 edges to [[_COMMUNITY_ApprovalRequest]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_TrustLevel]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_EgressAction]]
- 1 edge to [[_COMMUNITY_EgressPolicy]]

## Top bridge nodes
- [[test_security_integration.py]] - degree 37, connects to 10 communities
- [[approval_queue()]] - degree 3, connects to 2 communities
- [[encrypted_store()]] - degree 2, connects to 1 community
- [[prompt_guard()_2]] - degree 2, connects to 1 community
- [[sanitizer()_5]] - degree 2, connects to 1 community