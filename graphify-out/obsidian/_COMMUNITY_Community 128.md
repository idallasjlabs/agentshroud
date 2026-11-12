---
type: community
members: 41
---

# Community 128

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
TABLE source_file, type FROM #community/Community_128
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 41]]
- 4 edges to [[_COMMUNITY_Community 7]]
- 4 edges to [[_COMMUNITY_Community 0]]
- 3 edges to [[_COMMUNITY_Community 162]]
- 2 edges to [[_COMMUNITY_Community 72]]
- 2 edges to [[_COMMUNITY_Community 684]]
- 2 edges to [[_COMMUNITY_Community 5]]
- 2 edges to [[_COMMUNITY_Community 146]]
- 1 edge to [[_COMMUNITY_Community 557]]
- 1 edge to [[_COMMUNITY_Community 166]]
- 1 edge to [[_COMMUNITY_Community 93]]
- 1 edge to [[_COMMUNITY_Community 108]]
- 1 edge to [[_COMMUNITY_Community 477]]
- 1 edge to [[_COMMUNITY_Community 235]]
- 1 edge to [[_COMMUNITY_Community 32]]
- 1 edge to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Community 809]]
- 1 edge to [[_COMMUNITY_Community 365]]
- 1 edge to [[_COMMUNITY_Community 71]]

## Top bridge nodes
- [[TestPIIDetection_1]] - degree 55, connects to 19 communities
- [[.sanitizer()_1]] - degree 2, connects to 1 community