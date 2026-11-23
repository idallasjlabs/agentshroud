---
type: community
members: 30
---

# test_security_integration.py

**Members:** 30 nodes

## Members
- [[Agent with low trust cannot perform elevated actions.]] - rationale - gateway/tests/test_security_integration.py
- [[Clean message flows through entire pipeline without issues.]] - rationale - gateway/tests/test_security_integration.py
- [[Even if trust allows an action, egress filter blocks unauthorized destinations.]] - rationale - gateway/tests/test_security_integration.py
- [[Message with PII gets sanitized and logged correctly.]] - rationale - gateway/tests/test_security_integration.py
- [[Multiple messages through pipeline concurrently — thread safety.]] - rationale - gateway/tests/test_security_integration.py
- [[Outbound responses have credentials blocked for untrusted sources.]] - rationale - gateway/tests/test_security_integration.py
- [[Security Module Integration Tests — full pipeline end-to-end.]] - rationale - gateway/tests/test_security_integration.py
- [[Sensitive audit data can be encrypted at rest.]] - rationale - gateway/tests/test_security_integration.py
- [[When both PII sanitizer and prompt guard detect issues.]] - rationale - gateway/tests/test_security_integration.py
- [[approval_queue()_1]] - code - gateway/tests/test_security_integration.py
- [[asyncio_64]] - code
- [[encrypted_store()]] - code - gateway/tests/test_security_integration.py
- [[fixture_107]] - code
- [[ledger()_2]] - code - gateway/tests/test_security_integration.py
- [[parametrize_19]] - code
- [[process_message()]] - code - gateway/tests/test_security_integration.py
- [[prompt_guard()_2]] - code - gateway/tests/test_security_integration.py
- [[sanitizer()_5]] - code - gateway/tests/test_security_integration.py
- [[sk- key families with hyphensunderscores were missed by a-zA-Z0-9{20,}.]] - rationale - gateway/tests/test_security_integration.py
- [[test_egress_blocks_unauthorized_after_trust_check()]] - code - gateway/tests/test_security_integration.py
- [[test_encrypted_store_in_pipeline()]] - code - gateway/tests/test_security_integration.py
- [[test_full_pipeline_clean_message()]] - code - gateway/tests/test_security_integration.py
- [[test_full_pipeline_pii_message()]] - code - gateway/tests/test_security_integration.py
- [[test_hyphenated_sk_keys_are_blocked()]] - code - gateway/tests/test_security_integration.py
- [[test_pii_and_prompt_guard_both_trigger()]] - code - gateway/tests/test_security_integration.py
- [[test_pipeline_concurrent_messages()]] - code - gateway/tests/test_security_integration.py
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
- 13 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 6 edges to [[_COMMUNITY_PIIConfig]]
- 6 edges to [[_COMMUNITY_EgressFilter]]
- 4 edges to [[_COMMUNITY_EgressPolicy]]
- 4 edges to [[_COMMUNITY_ContainerSnapshot]]
- 3 edges to [[_COMMUNITY_EncryptedStore]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_EnhancedApprovalQueue]]
- 2 edges to [[_COMMUNITY_PromptGuard]]
- 1 edge to [[_COMMUNITY_deep_security_test]]
- 1 edge to [[_COMMUNITY_prompt_guard.py]]

## Top bridge nodes
- [[test_security_integration.py]] - degree 50, connects to 11 communities
- [[fixture_107]] - degree 8, connects to 2 communities
- [[approval_queue()_1]] - degree 4, connects to 2 communities
- [[encrypted_store()]] - degree 4, connects to 2 communities
- [[ledger()_2]] - degree 4, connects to 1 community
