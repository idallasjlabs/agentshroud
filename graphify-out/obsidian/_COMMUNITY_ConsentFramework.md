---
type: community
cohesion: 0.04
members: 85
---

# ConsentFramework

**Cohesion:** 0.04 - loosely connected
**Members:** 85 nodes

## Members
- [[.__init__()_15]] - code - gateway/security/consent_framework.py
- [[.add_to_blacklist()]] - code - gateway/security/consent_framework.py
- [[.add_to_whitelist()]] - code - gateway/security/consent_framework.py
- [[.analyze_content()]] - code - gateway/security/browser_security.py
- [[.analyze_screenshot()]] - code - gateway/security/browser_security.py
- [[.can_enter_credentials()]] - code - gateway/security/browser_security.py
- [[.check_url_reputation()]] - code - gateway/security/browser_security.py
- [[.get_blacklist()]] - code - gateway/security/consent_framework.py
- [[.get_whitelist()]] - code - gateway/security/consent_framework.py
- [[.remove_from_blacklist()]] - code - gateway/security/consent_framework.py
- [[.remove_from_whitelist()]] - code - gateway/security/consent_framework.py
- [[.test_add_and_remove_blacklist()]] - code - gateway/tests/test_consent_framework.py
- [[.test_add_and_remove_whitelist()]] - code - gateway/tests/test_consent_framework.py
- [[.test_blacklisted_command_rejected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_data_uri_blocked()]] - code - gateway/tests/test_browser_security.py
- [[.test_decision_approved()]] - code - gateway/tests/test_consent_framework.py
- [[.test_decision_denied()]] - code - gateway/tests/test_consent_framework.py
- [[.test_decision_has_timestamp()]] - code - gateway/tests/test_consent_framework.py
- [[.test_empty_command_rejected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_env_with_path_manipulation()]] - code - gateway/tests/test_consent_framework.py
- [[.test_env_with_secrets_in_value_warned()]] - code - gateway/tests/test_consent_framework.py
- [[.test_excessive_subdomains()]] - code - gateway/tests/test_browser_security.py
- [[.test_fake_captcha()]] - code - gateway/tests/test_browser_security.py
- [[.test_fake_dialog_detected()]] - code - gateway/tests/test_browser_security.py
- [[.test_fake_windows_alert()]] - code - gateway/tests/test_browser_security.py
- [[.test_homograph_attack()]] - code - gateway/tests/test_browser_security.py
- [[.test_hook_can_flag_threat()]] - code - gateway/tests/test_browser_security.py
- [[.test_http_blocked()]] - code - gateway/tests/test_browser_security.py
- [[.test_https_allowed()]] - code - gateway/tests/test_browser_security.py
- [[.test_ip_address_url()]] - code - gateway/tests/test_browser_security.py
- [[.test_ip_blocked_for_credentials()]] - code - gateway/tests/test_browser_security.py
- [[.test_known_dangerous_patterns_detected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_known_phishing_pattern()]] - code - gateway/tests/test_browser_security.py
- [[.test_legitimate_url()]] - code - gateway/tests/test_browser_security.py
- [[.test_localhost_allowed()]] - code - gateway/tests/test_browser_security.py
- [[.test_multiple_configs_validated()]] - code - gateway/tests/test_consent_framework.py
- [[.test_multiple_threats_aggregated()]] - code - gateway/tests/test_browser_security.py
- [[.test_no_hook_returns_none_threat()]] - code - gateway/tests/test_browser_security.py
- [[.test_safe_content_passes()]] - code - gateway/tests/test_browser_security.py
- [[.test_safe_env_no_warnings()]] - code - gateway/tests/test_consent_framework.py
- [[.test_screenshot_hook_registered()]] - code - gateway/tests/test_browser_security.py
- [[.test_shell_injection_backtick_detected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_shell_injection_curl_detected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_shell_injection_dollar_paren()]] - code - gateway/tests/test_consent_framework.py
- [[.test_shell_injection_pipe_to_sh()]] - code - gateway/tests/test_consent_framework.py
- [[.test_shell_injection_rm_rf_detected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_shell_injection_wget_detected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_suspicious_domain_blocked()]] - code - gateway/tests/test_browser_security.py
- [[.test_suspicious_subdomain()]] - code - gateway/tests/test_browser_security.py
- [[.test_tech_support_scam()]] - code - gateway/tests/test_browser_security.py
- [[.test_urgent_action_required()]] - code - gateway/tests/test_browser_security.py
- [[.test_valid_config_passes()]] - code - gateway/tests/test_consent_framework.py
- [[.test_whitelisted_command_auto_approved()]] - code - gateway/tests/test_consent_framework.py
- [[.validate_config()]] - code - gateway/security/consent_framework.py
- [[.validate_configs()]] - code - gateway/security/consent_framework.py
- [[Chen et al. 2026 (arXiv2602.14364) — MCP config shell injection  secret exfiltration]] - paper - docs/vault/02 - Modules/Security Modules/consent_framework.py.md
- [[Chen et al. 2026 — Agent configuration vulnerabilities  session hijacking (arXiv2602.14364)]] - paper - gateway/security/consent_framework.py
- [[ConfigValidationError]] - code - gateway/security/consent_framework.py
- [[ConsentFramework]] - code - gateway/security/consent_framework.py
- [[CredentialEntryBlocked]] - code - gateway/security/browser_security.py
- [[Exception_4]] - code
- [[Maloyan & Namiot 2026 (arXiv2601.17548) — Malicious MCP server configuration attacks]] - paper - docs/vault/02 - Modules/Security Modules/consent_framework.py.md
- [[Maloyan & Namiot 2026 — MCP security analysis (arXiv2601.17548)]] - paper - gateway/security/consent_framework.py
- [[PhishingURLDetected]] - code - gateway/security/browser_security.py
- [[ServerConfig]] - code - gateway/security/consent_framework.py
- [[ShellInjectionDetected]] - code - gateway/security/consent_framework.py
- [[SocialEngineeringDetected]] - code - gateway/security/browser_security.py
- [[TestConsentDecision]] - code - gateway/tests/test_consent_framework.py
- [[TestCredentialProtection]] - code - gateway/tests/test_browser_security.py
- [[TestEnvironmentValidation]] - code - gateway/tests/test_consent_framework.py
- [[TestScreenshotAnalysis]] - code - gateway/tests/test_browser_security.py
- [[TestServerConfigValidation]] - code - gateway/tests/test_consent_framework.py
- [[TestSocialEngineeringDetection]] - code - gateway/tests/test_browser_security.py
- [[TestURLReputation]] - code - gateway/tests/test_browser_security.py
- [[TestWhitelistBlacklist]] - code - gateway/tests/test_consent_framework.py
- [[ThreatAssessment]] - code - gateway/security/browser_security.py
- [[ThreatLevel]] - code - gateway/security/browser_security.py
- [[Validate a server configuration before execution.]] - rationale - gateway/security/consent_framework.py
- [[Wu et al. 2026 (arXiv2601.07263) — Browser-based agent social engineering attacks]] - paper - docs/vault/02 - Modules/Security Modules/browser_security.py.md
- [[browser_security.py]] - code - gateway/security/browser_security.py
- [[consent_framework.py]] - code - gateway/security/consent_framework.py
- [[framework()]] - code - gateway/tests/test_consent_framework.py
- [[guard()_4]] - code - gateway/tests/test_browser_security.py
- [[test_browser_security.py]] - code - gateway/tests/test_browser_security.py
- [[test_consent_framework.py]] - code - gateway/tests/test_consent_framework.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ConsentFramework
SORT file.name ASC
```

## Connections to other communities
- 35 edges to [[_COMMUNITY_lifespan.py]]
- 7 edges to [[_COMMUNITY_test_security_audit.py]]
- 4 edges to [[_COMMUNITY_SessionManager]]
- 2 edges to [[_COMMUNITY_AgentTarget]]
- 2 edges to [[_COMMUNITY_EncryptedStore]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY__make_token()]]
- 1 edge to [[_COMMUNITY_test_voice_gateway.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_IntelReportStore]]
- 1 edge to [[_COMMUNITY_SecureBrowser]]
- 1 edge to [[_COMMUNITY_SecureBrowser]]
- 1 edge to [[_COMMUNITY_SecureBrowser]]
- 1 edge to [[_COMMUNITY_SecureBrowser]]
- 1 edge to [[_COMMUNITY_TestAuth]]
- 1 edge to [[_COMMUNITY_TestFileSandbox]]
- 1 edge to [[_COMMUNITY_DraftEntry]]
- 1 edge to [[_COMMUNITY_test_approval_queue.py]]
- 1 edge to [[_COMMUNITY_WebProxy]]

## Top bridge nodes
- [[Exception_4]] - degree 18, connects to 13 communities
- [[ThreatAssessment]] - degree 22, connects to 6 communities
- [[ConsentFramework]] - degree 31, connects to 4 communities
- [[browser_security.py]] - degree 13, connects to 4 communities
- [[consent_framework.py]] - degree 11, connects to 3 communities