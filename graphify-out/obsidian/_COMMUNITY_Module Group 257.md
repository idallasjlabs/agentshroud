---
type: community
cohesion: 0.11
members: 18
---

# Module Group 257

**Cohesion:** 0.11 - loosely connected
**Members:** 18 nodes

## Members
- [[.test_crlf_in_prompt_guard()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_deeply_nested_json()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_json_injection_in_context()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_null_byte_in_prompt()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_oversized_json_payload()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_polyglot_payload()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_unicode_normalization_bypass()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_xml_entity_expansion()]] - code - gateway/tests/test_security_audit_advanced.py
- [[CRLF injection in prompt shouldn't bypass detection.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Deeply nested JSON shouldn't cause stack overflow.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[JSON injection in message shouldn't manipulate context.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Null bytes shouldn't bypass prompt guard.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Polyglot (valid as multiple formats) shouldn't bypass checks.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test HTTP-level security CRLF, header injection, content types.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestHTTPSecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[Unicode tricks shouldn't bypass PII detection.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Very large JSON shouldn't crash the parser.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[XXE-style payloads shouldn't crash processing.]] - rationale - gateway/tests/test_security_audit_advanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_257
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
- [[TestHTTPSecurity]] - degree 33, connects to 14 communities
- [[.test_json_injection_in_context()]] - degree 3, connects to 1 community
- [[.test_oversized_json_payload()]] - degree 3, connects to 1 community
