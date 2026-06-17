---
type: community
cohesion: 0.09
members: 22
---

# Module Group 216

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
- [[egress_filter()_1]] - code - gateway/tests/test_security_integration.py
- [[encrypted_store()]] - code - gateway/tests/test_security_integration.py
- [[prompt_guard()_2]] - code - gateway/tests/test_security_integration.py
- [[sanitizer()_4]] - code - gateway/tests/test_security_integration.py
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
TABLE source_file, type FROM #community/Module_Group_216
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 3 edges to [[_COMMUNITY_Ledger Config & Test Infra]]
- 3 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 3 edges to [[_COMMUNITY_Alert Dispatcher]]
- 3 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 2 edges to [[_COMMUNITY_Approval Queue Core]]
- 2 edges to [[_COMMUNITY_Egress Filter & Approval]]
- 2 edges to [[_COMMUNITY_Module Group 88]]
- 2 edges to [[_COMMUNITY_Module Group 71]]
- 2 edges to [[_COMMUNITY_Module Group 66]]
- 2 edges to [[_COMMUNITY_Context Guard & Integrity]]
- 1 edge to [[_COMMUNITY_Enhanced Approval Queue]]
- 1 edge to [[_COMMUNITY_Module Group 79]]

## Top bridge nodes
- [[test_security_integration.py]] - degree 37, connects to 13 communities
- [[egress_filter()_1]] - degree 4, connects to 3 communities
- [[encrypted_store()]] - degree 2, connects to 1 community
- [[prompt_guard()_2]] - degree 2, connects to 1 community
- [[sanitizer()_4]] - degree 2, connects to 1 community