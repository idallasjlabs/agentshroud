---
type: community
cohesion: 0.05
members: 71
---

# AlertDispatcher

**Cohesion:** 0.05 - loosely connected
**Members:** 71 nodes

## Members
- [[dot-__init__()_144]] - code - gateway/security/oauth_security.py
- [[dot-check_state_reuse()]] - code - gateway/security/oauth_security.py
- [[dot-create_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[dot-record_state_used()]] - code - gateway/security/oauth_security.py
- [[dot-register_known_shared_ids()]] - code - gateway/security/oauth_security.py
- [[dot-test_base64_injection()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_clean_message_not_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_clean_technical_message()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_cookie_custom_max_age_expires_sooner()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_expired_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_tamper_detected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_within_max_age_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_wrong_client_fails()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_wrong_scope_fails()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_create_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_dan_jailbreak()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_different_uri_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_empty_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_empty_input()_2]] - code - gateway/tests/test_security_audit.py
- [[dot-test_empty_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_exact_match_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_http_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_ignore_previous_instructions()_1]] - code - gateway/tests/test_security_audit.py
- [[dot-test_indirect_injection_url()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_instruction_override()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_multilingual_injection()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_path_traversal_rejected()_1]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_plain_rejected_when_s256_required()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_required_missing_challenge()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_s256_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_verifier_validation()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_prompt_leaking_via_markdown()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_repeated_injection()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_role_reassignment()_1]] - code - gateway/tests/test_security_audit.py
- [[dot-test_short_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_state_replay_detected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_static_shared_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_system_prompt_extraction()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_token_smuggling()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_unique_client_id_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_valid_state_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_validate_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_xml_injection()]] - code - gateway/tests/test_security_audit.py
- [[dot-validate_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[dot-validate_redirect_uri()]] - code - gateway/security/oauth_security.py
- [[dot-validate_request()]] - code - gateway/security/oauth_security.py
- [[dot-verify_pkce()]] - code - gateway/security/oauth_security.py
- [[Base64 encoded instruction.]] - rationale - gateway/tests/test_security_audit.py
- [[ConfusedDeputyError]] - code - gateway/security/oauth_security.py
- [[Injection in another language.]] - rationale - gateway/tests/test_security_audit.py
- [[Markdown-based injection.]] - rationale - gateway/tests/test_security_audit.py
- [[Normal messages should pass.]] - rationale - gateway/tests/test_security_audit.py
- [[OAuthError]] - code - gateway/security/oauth_security.py
- [[OAuthRequest]] - code - gateway/security/oauth_security.py
- [[OAuthSecurityValidator]] - code - gateway/security/oauth_security.py
- [[PKCEViolation]] - code - gateway/security/oauth_security.py
- [[RedirectMismatch]] - code - gateway/security/oauth_security.py
- [[Same injection multiple times shouldn't bypass.]] - rationale - gateway/tests/test_security_audit.py
- [[Technical discussion mentioning 'system' shouldn't trigger.]] - rationale - gateway/tests/test_security_audit.py
- [[Test prompt injection detection with adversarial payloads.]] - rationale - gateway/tests/test_security_audit.py
- [[TestClientValidation]] - code - gateway/tests/test_oauth_security.py
- [[TestConsentCookieBinding]] - code - gateway/tests/test_oauth_security.py
- [[TestPKCE]] - code - gateway/tests/test_oauth_security.py
- [[TestPromptGuard]] - code - gateway/tests/test_security_audit.py
- [[TestRedirectURI]] - code - gateway/tests/test_oauth_security.py
- [[TestStateValidation]] - code - gateway/tests/test_oauth_security.py
- [[Token boundary attack.]] - rationale - gateway/tests/test_security_audit.py
- [[URL-based indirect injection.]] - rationale - gateway/tests/test_security_audit.py
- [[oauth_security.py]] - code - gateway/security/oauth_security.py
- [[test_oauth_security.py]] - code - gateway/tests/test_oauth_security.py
- [[validator()]] - code - gateway/tests/test_oauth_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AlertDispatcher
SORT file.name ASC
```

## Connections to other communities
- 42 edges to [[_COMMUNITY_AlertDispatcher]]
- 10 edges to [[_COMMUNITY_MiddlewareManager]]
- 5 edges to [[_COMMUNITY_ResourceGuard]]
- 4 edges to [[_COMMUNITY_KillSwitchMonitor_1]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig_6]]
- 2 edges to [[_COMMUNITY_AgentTarget_2]]
- 2 edges to [[_COMMUNITY_SessionManager]]
- 2 edges to [[_COMMUNITY_TrustConfig_1]]
- 2 edges to [[_COMMUNITY_ConsentFramework_1]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_ResourceGuard_1]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_1]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_3]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig_1]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_outbound.py_1]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]
- 1 edge to [[_COMMUNITY_validate_network_security]]

## Top bridge nodes
- [[TestPromptGuard]] - degree 51, connects to 16 communities
- [[ConfusedDeputyError]] - degree 21, connects to 4 communities
- [[PKCEViolation]] - degree 21, connects to 4 communities
- [[RedirectMismatch]] - degree 21, connects to 4 communities
- [[OAuthSecurityValidator]] - degree 30, connects to 3 communities
