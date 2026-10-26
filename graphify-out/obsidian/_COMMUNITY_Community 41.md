---
type: community
members: 86
---

# Community 41

**Members:** 86 nodes

## Members
- [[.__init__()_102]] - code - gateway/security/oauth_security.py
- [[.check_state_reuse()]] - code - gateway/security/oauth_security.py
- [[.create_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[.record_state_used()]] - code - gateway/security/oauth_security.py
- [[.register_known_shared_ids()]] - code - gateway/security/oauth_security.py
- [[.test_cookie_custom_max_age_expires_sooner()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_expired_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_tamper_detected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_within_max_age_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_wrong_client_fails()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_wrong_scope_fails()]] - code - gateway/tests/test_oauth_security.py
- [[.test_create_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[.test_credit_card_amex()]] - code - gateway/tests/test_security_audit.py
- [[.test_credit_card_no_dashes()]] - code - gateway/tests/test_security_audit.py
- [[.test_credit_card_visa()]] - code - gateway/tests/test_security_audit.py
- [[.test_different_uri_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_email_standard()]] - code - gateway/tests/test_security_audit.py
- [[.test_email_with_plus()]] - code - gateway/tests/test_security_audit.py
- [[.test_empty_and_none_input()]] - code - gateway/tests/test_security_audit.py
- [[.test_empty_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_empty_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_exact_match_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_http_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_multiple_pii_single_message()]] - code - gateway/tests/test_security_audit.py
- [[.test_no_false_positive_on_dates()]] - code - gateway/tests/test_security_audit.py
- [[.test_no_false_positive_on_zip()]] - code - gateway/tests/test_security_audit.py
- [[.test_path_traversal_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_phone_international()]] - code - gateway/tests/test_security_audit.py
- [[.test_phone_us_standard()]] - code - gateway/tests/test_security_audit.py
- [[.test_pii_boundary_handling()]] - code - gateway/tests/test_security_audit.py
- [[.test_pii_in_code_block()]] - code - gateway/tests/test_security_audit.py
- [[.test_pii_in_json()]] - code - gateway/tests/test_security_audit.py
- [[.test_pii_with_obfuscation_attempt()]] - code - gateway/tests/test_security_audit.py
- [[.test_pkce_plain_rejected_when_s256_required()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_required_missing_challenge()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_s256_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_verifier_validation()]] - code - gateway/tests/test_oauth_security.py
- [[.test_short_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_ssn_no_dashes()]] - code - gateway/tests/test_security_audit.py
- [[.test_ssn_space_separated()]] - code - gateway/tests/test_security_audit.py
- [[.test_ssn_standard_format()]] - code - gateway/tests/test_security_audit.py
- [[.test_state_replay_detected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_static_shared_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_unicode_pii()]] - code - gateway/tests/test_security_audit.py
- [[.test_unique_client_id_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_valid_state_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_validate_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[.validate_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[.validate_redirect_uri()]] - code - gateway/security/oauth_security.py
- [[.validate_request()]] - code - gateway/security/oauth_security.py
- [[.verify_pkce()]] - code - gateway/security/oauth_security.py
- [[Amex card 378282246310005 (15 digits starting with 37).]] - rationale - gateway/tests/test_security_audit.py
- [[Attempt to hide PII with zero-width chars.]] - rationale - gateway/tests/test_security_audit.py
- [[Card without dashes 4111111111111111.]] - rationale - gateway/tests/test_security_audit.py
- [[ConfusedDeputyError]] - code - gateway/security/oauth_security.py
- [[Dates should not be flagged as SSNphone.]] - rationale - gateway/tests/test_security_audit.py
- [[Edge case empty string.]] - rationale - gateway/tests/test_security_audit.py
- [[Email with plus addressing user+tag@gmail.com.]] - rationale - gateway/tests/test_security_audit.py
- [[International phone +1-555-867-5309.]] - rationale - gateway/tests/test_security_audit.py
- [[Multiple PII entities in one message.]] - rationale - gateway/tests/test_security_audit.py
- [[OAuthError]] - code - gateway/security/oauth_security.py
- [[OAuthRequest]] - code - gateway/security/oauth_security.py
- [[OAuthSecurityValidator]] - code - gateway/security/oauth_security.py
- [[PII at message start and end.]] - rationale - gateway/tests/test_security_audit.py
- [[PII embedded in JSON.]] - rationale - gateway/tests/test_security_audit.py
- [[PII in codemarkdown blocks.]] - rationale - gateway/tests/test_security_audit.py
- [[PII with Unicode characters nearby.]] - rationale - gateway/tests/test_security_audit.py
- [[PKCEViolation]] - code - gateway/security/oauth_security.py
- [[RedirectMismatch]] - code - gateway/security/oauth_security.py
- [[SSN in standard XXX-XX-XXXX format.]] - rationale - gateway/tests/test_security_audit.py
- [[SSN with spaces 123 45 6789.]] - rationale - gateway/tests/test_security_audit.py
- [[SSN without dashes 123456789 — Presidio+spaCy only (regex needs dashes).]] - rationale - gateway/tests/test_security_audit.py
- [[Standard email address.]] - rationale - gateway/tests/test_security_audit.py
- [[Test PII sanitization — works with Presidio (Python ≤3.13) or regex fallback (3.]] - rationale - gateway/tests/test_security_audit.py
- [[TestClientValidation]] - code - gateway/tests/test_oauth_security.py
- [[TestConsentCookieBinding]] - code - gateway/tests/test_oauth_security.py
- [[TestPIIDetection_1]] - code - gateway/tests/test_security_audit.py
- [[TestPKCE]] - code - gateway/tests/test_oauth_security.py
- [[TestRedirectURI]] - code - gateway/tests/test_oauth_security.py
- [[TestStateValidation]] - code - gateway/tests/test_oauth_security.py
- [[US phone (555) 867-5309.]] - rationale - gateway/tests/test_security_audit.py
- [[Visa card 4111-1111-1111-1111.]] - rationale - gateway/tests/test_security_audit.py
- [[ZIP codes should not be flagged as SSNphoneCC.]] - rationale - gateway/tests/test_security_audit.py
- [[oauth_security.py]] - code - gateway/security/oauth_security.py
- [[test_oauth_security.py]] - code - gateway/tests/test_oauth_security.py
- [[validator()]] - code - gateway/tests/test_oauth_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_41
SORT file.name ASC
```

## Connections to other communities
- 41 edges to [[_COMMUNITY_Community 0]]
- 12 edges to [[_COMMUNITY_Community 72]]
- 8 edges to [[_COMMUNITY_Community 431]]
- 3 edges to [[_COMMUNITY_Community 196]]
- 3 edges to [[_COMMUNITY_Community 509]]
- 2 edges to [[_COMMUNITY_Community 108]]
- 2 edges to [[_COMMUNITY_Community 7]]
- 2 edges to [[_COMMUNITY_Community 24]]
- 2 edges to [[_COMMUNITY_Community 76]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 52]]
- 1 edge to [[_COMMUNITY_Community 152]]
- 1 edge to [[_COMMUNITY_Community 146]]
- 1 edge to [[_COMMUNITY_Community 93]]
- 1 edge to [[_COMMUNITY_Community 477]]
- 1 edge to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Community 70]]
- 1 edge to [[_COMMUNITY_Community 71]]
- 1 edge to [[_COMMUNITY_Community 22]]
- 1 edge to [[_COMMUNITY_Community 434]]
- 1 edge to [[_COMMUNITY_Community 5]]
- 1 edge to [[_COMMUNITY_Community 11]]

## Top bridge nodes
- [[TestPIIDetection_1]] - degree 55, connects to 16 communities
- [[OAuthSecurityValidator]] - degree 32, connects to 4 communities
- [[ConfusedDeputyError]] - degree 21, connects to 4 communities
- [[PKCEViolation]] - degree 21, connects to 4 communities
- [[RedirectMismatch]] - degree 21, connects to 4 communities