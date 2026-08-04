---
type: community
cohesion: 0.11
members: 18
---

# Module Group 258

**Cohesion:** 0.11 - loosely connected
**Members:** 18 nodes

## Members
- [[.test_binary_data_in_text_fields()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_deeply_nested_context_attacks()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_empty_inputs_everywhere()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_many_pii_entities()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_rapid_fire_scans()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_regex_redos_email()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_regex_redos_ssn()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_very_long_message()]] - code - gateway/tests/test_security_audit_advanced.py
- [[Binary data in text fields shouldn't crash.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Email regex should not be vulnerable to ReDoS.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Empty strings shouldn't crash any module.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Message with hundreds of PII entities should complete.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Nested context attacks shouldn't cause stack overflow.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Rapid scanning shouldn't degrade or crash.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[SSN regex should not be vulnerable to ReDoS.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test resilience against denial of service patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestDoSPrevention]] - code - gateway/tests/test_security_audit_advanced.py
- [[Very long messages should be handled without crash.]] - rationale - gateway/tests/test_security_audit_advanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_258
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 4 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 3 edges to [[_COMMUNITY_Alert Dispatcher]]
- 2 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 2 edges to [[_COMMUNITY_Subagent Monitor]]
- 1 edge to [[_COMMUNITY_Tool Result Sanitizer]]
- 1 edge to [[_COMMUNITY_Module Group 102]]
- 1 edge to [[_COMMUNITY_DNS Filter & Tunneling Detection]]
- 1 edge to [[_COMMUNITY_Module Group 88]]
- 1 edge to [[_COMMUNITY_Module Group 66]]
- 1 edge to [[_COMMUNITY_Module Group 80]]
- 1 edge to [[_COMMUNITY_Module Group 110]]
- 1 edge to [[_COMMUNITY_Context Guard & Integrity]]
- 1 edge to [[_COMMUNITY_Progressive Trust Levels]]

## Top bridge nodes
- [[TestDoSPrevention]] - degree 33, connects to 14 communities
- [[.test_deeply_nested_context_attacks()]] - degree 3, connects to 1 community
- [[.test_empty_inputs_everywhere()]] - degree 3, connects to 1 community
