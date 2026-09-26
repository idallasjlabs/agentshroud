---
type: community
cohesion: 0.05
members: 72
---

# ProgressiveLockdown

**Cohesion:** 0.05 - loosely connected
**Members:** 72 nodes

## Members
- [[.__init__()_102]] - code - gateway/security/oauth_security.py
- [[.check_state_reuse()]] - code - gateway/security/oauth_security.py
- [[.create_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[.record_state_used()]] - code - gateway/security/oauth_security.py
- [[.register_known_shared_ids()]] - code - gateway/security/oauth_security.py
- [[.test_base64_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_clean_message_not_blocked()]] - code - gateway/tests/test_security_audit.py
- [[.test_clean_technical_message()]] - code - gateway/tests/test_security_audit.py
- [[.test_cookie_custom_max_age_expires_sooner()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_expired_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_tamper_detected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_within_max_age_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_wrong_client_fails()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_wrong_scope_fails()]] - code - gateway/tests/test_oauth_security.py
- [[.test_create_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[.test_dan_jailbreak()]] - code - gateway/tests/test_security_audit.py
- [[.test_different_uri_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_empty_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_empty_input()_2]] - code - gateway/tests/test_security_audit.py
- [[.test_empty_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_exact_match_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_http_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_ignore_previous_instructions()]] - code - gateway/tests/test_security_audit.py
- [[.test_indirect_injection_url()]] - code - gateway/tests/test_security_audit.py
- [[.test_instruction_override()]] - code - gateway/tests/test_security_audit.py
- [[.test_multilingual_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_path_traversal_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_plain_rejected_when_s256_required()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_required_missing_challenge()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_s256_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_verifier_validation()]] - code - gateway/tests/test_oauth_security.py
- [[.test_prompt_leaking_via_markdown()]] - code - gateway/tests/test_security_audit.py
- [[.test_repeated_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_role_reassignment()]] - code - gateway/tests/test_security_audit.py
- [[.test_short_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_state_replay_detected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_static_shared_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_system_prompt_extraction()]] - code - gateway/tests/test_security_audit.py
- [[.test_token_smuggling()]] - code - gateway/tests/test_security_audit.py
- [[.test_unique_client_id_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_valid_state_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_validate_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[.test_xml_injection()]] - code - gateway/tests/test_security_audit.py
- [[.validate_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[.validate_redirect_uri()]] - code - gateway/security/oauth_security.py
- [[.validate_request()]] - code - gateway/security/oauth_security.py
- [[.verify_pkce()]] - code - gateway/security/oauth_security.py
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
- [[Wang et al. 2026 (arXiv2602.08412) — Confused Deputy  Event Injection Attacks]] - paper - docs/vault/02 - Modules/Security Modules/oauth_security.py.md
- [[oauth_security.py]] - code - gateway/security/oauth_security.py
- [[test_oauth_security.py]] - code - gateway/tests/test_oauth_security.py
- [[validator()]] - code - gateway/tests/test_oauth_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ProgressiveLockdown
SORT file.name ASC
```

## Connections to other communities
- 48 edges to [[_COMMUNITY_lifespan.py]]
- 16 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_test_llm_proxy_failover.py]]
- 2 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 2 edges to [[_COMMUNITY_test_dashboard.py]]
- 2 edges to [[_COMMUNITY_ServiceManager]]
- 2 edges to [[_COMMUNITY_climain.py]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_test_filter_xml_blocks.py]]
- 1 edge to [[_COMMUNITY_EgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_apply-patches.js (OpenClaw)]]
- 1 edge to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_TestAuth]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Value Proposition - REVISED]]
- 1 edge to [[_COMMUNITY_voice_task]]
- 1 edge to [[_COMMUNITY_rbac_config.py]]
- 1 edge to [[_COMMUNITY_MemoryIntegrityMonitor]]

## Top bridge nodes
- [[TestPromptGuard]] - degree 51, connects to 16 communities
- [[oauth_security.py]] - degree 12, connects to 4 communities
- [[OAuthSecurityValidator]] - degree 32, connects to 2 communities
- [[ConfusedDeputyError]] - degree 21, connects to 2 communities
- [[PKCEViolation]] - degree 21, connects to 2 communities