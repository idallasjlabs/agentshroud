---
type: community
cohesion: 0.04
members: 74
---

# _wrap_response()

**Cohesion:** 0.04 - loosely connected
**Members:** 74 nodes

## Members
- [[dot-check_state_reuse()]] - code - gateway/security/oauth_security.py
- [[dot-monitor_sandbox()]] - code - gateway/tests/test_security_audit.py
- [[dot-sandbox()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_absolute_path_to_sensitive_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_app_read_allowed()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_basic_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_cookie_custom_max_age_expires_sooner()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_expired_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_tamper_detected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_within_max_age_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_wrong_client_fails()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_wrong_scope_fails()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_create_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_different_uri_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_double_encoded_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_empty_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_empty_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_enforce_vs_monitor_contrast()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_exact_match_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_http_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_monitor_mode_allows_everything()_1]] - code - gateway/tests/test_security_audit.py
- [[dot-test_null_byte_injection_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_path_traversal_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_plain_rejected_when_s256_required()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_required_missing_challenge()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_s256_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_verifier_validation()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_proc_meminfo_allowed()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_proc_self_environ_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_short_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_staging_detection()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_state_replay_detected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_static_shared_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_symlink_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_tmp_read_allowed()_1]] - code - gateway/tests/test_security_audit.py
- [[dot-test_unique_client_id_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_valid_state_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_validate_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_windows_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_outside_allowed_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_pii_detection()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_to_app_data_allowed()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_to_system_dir_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_to_tmp_allowed()]] - code - gateway/tests/test_security_audit.py
- [[dot-validate_redirect_uri()]] - code - gateway/security/oauth_security.py
- [[dot-validate_request()]] - code - gateway/security/oauth_security.py
- [[Access to procselfenviron exposes env vars — must be blocked.]] - rationale - gateway/tests/test_security_audit.py
- [[Allowed read path should pass.]] - rationale - gateway/tests/test_security_audit.py
- [[ConfusedDeputyError]] - code - gateway/security/oauth_security.py
- [[Detect data staging patterns.]] - rationale - gateway/tests/test_security_audit.py
- [[Monitor mode flags but allows — verify difference from enforce.]] - rationale - gateway/tests/test_security_audit.py
- [[Monitor-mode sandbox for comparison testing.]] - rationale - gateway/tests/test_security_audit.py
- [[OAuthError]] - code - gateway/security/oauth_security.py
- [[OAuthRequest]] - code - gateway/security/oauth_security.py
- [[PKCEViolation]] - code - gateway/security/oauth_security.py
- [[Reading from app should be allowed.]] - rationale - gateway/tests/test_security_audit.py
- [[RedirectMismatch]] - code - gateway/security/oauth_security.py
- [[Same path, different modes — enforce blocks, monitor allows.]] - rationale - gateway/tests/test_security_audit.py
- [[Symlink-based escape attempt blocked.]] - rationale - gateway/tests/test_security_audit.py
- [[Test file system sandboxing in enforce mode — blocks unauthorized access.]] - rationale - gateway/tests/test_security_audit.py
- [[TestClientValidation]] - code - gateway/tests/test_oauth_security.py
- [[TestConsentCookieBinding]] - code - gateway/tests/test_oauth_security.py
- [[TestFileSandbox]] - code - gateway/tests/test_security_audit.py
- [[TestPKCE]] - code - gateway/tests/test_oauth_security.py
- [[TestRedirectURI]] - code - gateway/tests/test_oauth_security.py
- [[TestStateValidation]] - code - gateway/tests/test_oauth_security.py
- [[Wang et al. 2026 (arXiv2602.08412) — Confused Deputy  Event Injection Attacks]] - paper - docs/vault/02 - Modules/Security Modules/oauth_security.py.md
- [[Writing PII should be flagged even to allowed paths.]] - rationale - gateway/tests/test_security_audit.py
- [[Writing outside allowed paths must be blocked.]] - rationale - gateway/tests/test_security_audit.py
- [[Writing to appdata should be allowed.]] - rationale - gateway/tests/test_security_audit.py
- [[Writing to tmp should be allowed.]] - rationale - gateway/tests/test_security_audit.py
- [[oauth_security.py_2]] - code - gateway/security/oauth_security.py
- [[test_oauth_security.py]] - code - gateway/tests/test_oauth_security.py
- [[validator()]] - code - gateway/tests/test_oauth_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_wrap_response
SORT file.name ASC
```

## Connections to other communities
- 48 edges to [[_COMMUNITY_ContextGuard]]
- 12 edges to [[_COMMUNITY_Any]]
- 8 edges to [[_COMMUNITY_dot-_make_proxy()]]
- 3 edges to [[_COMMUNITY_FileSandbox]]
- 2 edges to [[_COMMUNITY_SubagentMonitor]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy (2)]]
- 2 edges to [[_COMMUNITY_AgentShroud™ README]]
- 1 edge to [[_COMMUNITY_KeyVault]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_SessionManager]]
- 1 edge to [[_COMMUNITY_SecureBrowser (3)]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 1 edge to [[_COMMUNITY_PromptGuard]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]
- 1 edge to [[_COMMUNITY_test_a2a_policy.py]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager]]
- 1 edge to [[_COMMUNITY_WebProxy]]
- 1 edge to [[_COMMUNITY_NetworkSecurityFinding]]

## Top bridge nodes
- [[TestFileSandbox]] - degree 55, connects to 15 communities
- [[oauth_security.py_2]] - degree 11, connects to 4 communities
- [[ConfusedDeputyError]] - degree 21, connects to 2 communities
- [[PKCEViolation]] - degree 21, connects to 2 communities
- [[RedirectMismatch]] - degree 21, connects to 2 communities
