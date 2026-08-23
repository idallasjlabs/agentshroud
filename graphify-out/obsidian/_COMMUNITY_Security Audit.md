---
type: community
cohesion: 0.05
members: 41
---

# Security Audit

**Cohesion:** 0.05 - loosely connected
**Members:** 41 nodes

## Members
- [[.sanitizer()_1]] - code - gateway/tests/test_security_audit.py
- [[.test_credit_card_amex()]] - code - gateway/tests/test_security_audit.py
- [[.test_credit_card_no_dashes()]] - code - gateway/tests/test_security_audit.py
- [[.test_credit_card_visa()]] - code - gateway/tests/test_security_audit.py
- [[.test_email_standard()]] - code - gateway/tests/test_security_audit.py
- [[.test_email_with_plus()]] - code - gateway/tests/test_security_audit.py
- [[.test_empty_and_none_input()]] - code - gateway/tests/test_security_audit.py
- [[.test_multiple_pii_single_message()]] - code - gateway/tests/test_security_audit.py
- [[.test_no_false_positive_on_dates()]] - code - gateway/tests/test_security_audit.py
- [[.test_no_false_positive_on_zip()]] - code - gateway/tests/test_security_audit.py
- [[.test_phone_international()]] - code - gateway/tests/test_security_audit.py
- [[.test_phone_us_standard()]] - code - gateway/tests/test_security_audit.py
- [[.test_pii_boundary_handling()]] - code - gateway/tests/test_security_audit.py
- [[.test_pii_in_code_block()]] - code - gateway/tests/test_security_audit.py
- [[.test_pii_in_json()]] - code - gateway/tests/test_security_audit.py
- [[.test_pii_with_obfuscation_attempt()]] - code - gateway/tests/test_security_audit.py
- [[.test_ssn_no_dashes()]] - code - gateway/tests/test_security_audit.py
- [[.test_ssn_space_separated()]] - code - gateway/tests/test_security_audit.py
- [[.test_ssn_standard_format()]] - code - gateway/tests/test_security_audit.py
- [[.test_unicode_pii()]] - code - gateway/tests/test_security_audit.py
- [[Amex card 378282246310005 (15 digits starting with 37).]] - rationale - gateway/tests/test_security_audit.py
- [[Attempt to hide PII with zero-width chars.]] - rationale - gateway/tests/test_security_audit.py
- [[Card without dashes 4111111111111111.]] - rationale - gateway/tests/test_security_audit.py
- [[Dates should not be flagged as SSNphone.]] - rationale - gateway/tests/test_security_audit.py
- [[Edge case empty string.]] - rationale - gateway/tests/test_security_audit.py
- [[Email with plus addressing user+tag@gmail.com.]] - rationale - gateway/tests/test_security_audit.py
- [[International phone +1-555-867-5309.]] - rationale - gateway/tests/test_security_audit.py
- [[Multiple PII entities in one message.]] - rationale - gateway/tests/test_security_audit.py
- [[PII at message start and end.]] - rationale - gateway/tests/test_security_audit.py
- [[PII embedded in JSON.]] - rationale - gateway/tests/test_security_audit.py
- [[PII in codemarkdown blocks.]] - rationale - gateway/tests/test_security_audit.py
- [[PII with Unicode characters nearby.]] - rationale - gateway/tests/test_security_audit.py
- [[SSN in standard XXX-XX-XXXX format.]] - rationale - gateway/tests/test_security_audit.py
- [[SSN with spaces 123 45 6789.]] - rationale - gateway/tests/test_security_audit.py
- [[SSN without dashes 123456789 — Presidio+spaCy only (regex needs dashes).]] - rationale - gateway/tests/test_security_audit.py
- [[Standard email address.]] - rationale - gateway/tests/test_security_audit.py
- [[Test PII sanitization — works with Presidio (Python ≤3.13) or regex fallback (3.]] - rationale - gateway/tests/test_security_audit.py
- [[TestPIIDetection_1]] - code - gateway/tests/test_security_audit.py
- [[US phone (555) 867-5309.]] - rationale - gateway/tests/test_security_audit.py
- [[Visa card 4111-1111-1111-1111.]] - rationale - gateway/tests/test_security_audit.py
- [[ZIP codes should not be flagged as SSNphoneCC.]] - rationale - gateway/tests/test_security_audit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Security_Audit
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 5 edges to [[_COMMUNITY_OAuth & Metadata Guard]]
- 2 edges to [[_COMMUNITY_Security Hardening]]
- 2 edges to [[_COMMUNITY_Git Guard (security)]]
- 2 edges to [[_COMMUNITY_Privilege Separation & File Sandbox]]
- 2 edges to [[_COMMUNITY_Key Vault]]
- 2 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 2 edges to [[_COMMUNITY_Resource Guard & Local Model Parity]]
- 2 edges to [[_COMMUNITY_Subagent Monitor]]
- 1 edge to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Browser Security]]
- 1 edge to [[_COMMUNITY_Dns Filter]]
- 1 edge to [[_COMMUNITY_Egress Filter]]
- 1 edge to [[_COMMUNITY_Egress Monitor]]
- 1 edge to [[_COMMUNITY_Security Regressions V1 2]]

## Top bridge nodes
- [[TestPIIDetection_1]] - degree 55, connects to 15 communities
- [[.sanitizer()_1]] - degree 2, connects to 1 community