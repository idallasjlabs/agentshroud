---
type: community
cohesion: 0.07
members: 27
---

# Community 322

**Cohesion:** 0.07 - loosely connected
**Members:** 27 nodes

## Members
- [[Agent with low trust cannot perform elevated actions.]] - rationale - gateway/tests/test_security_integration.py
- [[Clean message flows through entire pipeline without issues.]] - rationale - gateway/tests/test_security_integration.py
- [[Config with all security modules enabled.]] - rationale - gateway/tests/test_security_integration.py
- [[Drift detector catches container config changes during operation.]] - rationale - gateway/tests/test_security_integration.py
- [[Even if trust allows an action, egress filter blocks unauthorized destinations.]] - rationale - gateway/tests/test_security_integration.py
- [[Message with PII gets sanitized and logged correctly.]] - rationale - gateway/tests/test_security_integration.py
- [[Multiple messages through pipeline concurrently — thread safety.]] - rationale - gateway/tests/test_security_integration.py
- [[Outbound responses have credentials blocked for untrusted sources.]] - rationale - gateway/tests/test_security_integration.py
- [[Pipeline with all modules disabled acts as passthrough.]] - rationale - gateway/tests/test_security_integration.py
- [[Pipeline with only PII enabled, prompt guard disabled.]] - rationale - gateway/tests/test_security_integration.py
- [[Sensitive audit data can be encrypted at rest.]] - rationale - gateway/tests/test_security_integration.py
- [[When both PII sanitizer and prompt guard detect issues.]] - rationale - gateway/tests/test_security_integration.py
- [[approval_queue()]] - code - gateway/tests/test_security_integration.py
- [[full_pipeline_config()]] - code - gateway/tests/test_security_integration.py
- [[sanitizer()_5]] - code - gateway/tests/test_security_integration.py
- [[test_drift_detection_in_pipeline()]] - code - gateway/tests/test_security_integration.py
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

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_322
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Tool Result Sanitizer & XML Injection Filtering]]
- 4 edges to [[_COMMUNITY_Gateway Config & PII Sanitizer]]
- 4 edges to [[_COMMUNITY_Encrypted Store & Drift Detector]]
- 4 edges to [[_COMMUNITY_PII Sanitizer & Redaction]]
- 4 edges to [[_COMMUNITY_Approval Queue (WebSocket)]]
- 3 edges to [[_COMMUNITY_Cross-Bot Trust & A2A Governance]]
- 3 edges to [[_COMMUNITY_Prompt Guard & Context Integrity]]
- 3 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 2 edges to [[_COMMUNITY_Alert Dispatcher & RBAC Reliability]]
- 2 edges to [[_COMMUNITY_Multi-Agent Router & Chat UI]]
- 2 edges to [[_COMMUNITY_Community 185]]
- 1 edge to [[_COMMUNITY_Community 52]]
- 1 edge to [[_COMMUNITY_Community 167]]
- 1 edge to [[_COMMUNITY_Community 182]]

## Top bridge nodes
- [[test_security_integration.py]] - degree 37, connects to 14 communities
- [[full_pipeline_config()]] - degree 7, connects to 5 communities
- [[test_pipeline_all_modules_disabled()]] - degree 5, connects to 3 communities
- [[test_drift_detection_in_pipeline()]] - degree 4, connects to 2 communities
- [[test_pipeline_selective_modules()]] - degree 4, connects to 2 communities