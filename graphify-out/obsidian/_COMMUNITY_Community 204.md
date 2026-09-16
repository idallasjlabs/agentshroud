---
type: community
cohesion: 0.11
members: 36
---

# Community 204

**Cohesion:** 0.11 - loosely connected
**Members:** 36 nodes

## Members
- [[dot-test_add_and_remove_blacklist()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_add_and_remove_whitelist()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_blacklisted_command_rejected()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_decision_approved()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_decision_denied()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_decision_has_timestamp()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_empty_command_rejected()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_env_with_path_manipulation()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_env_with_secrets_in_value_warned()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_known_dangerous_patterns_detected()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_multiple_configs_validated()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_safe_env_no_warnings()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_shell_injection_backtick_detected()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_shell_injection_curl_detected()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_shell_injection_dollar_paren()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_shell_injection_pipe_to_sh()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_shell_injection_rm_rf_detected()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_shell_injection_wget_detected()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_valid_config_passes()]] - code - gateway/tests/test_consent_framework.py
- [[dot-test_whitelisted_command_auto_approved()]] - code - gateway/tests/test_consent_framework.py
- [[dot-validate_config()]] - code - gateway/security/consent_framework.py
- [[dot-validate_configs()]] - code - gateway/security/consent_framework.py
- [[Chen et al. 2026 (arXiv2602.14364) — MCP config shell injection  secret exfiltration]] - paper - docs/vault/02 - Modules/Security Modules/consent_framework.py.md
- [[ConfigValidationError]] - code - gateway/security/consent_framework.py
- [[ConsentDecision]] - code - gateway/security/consent_framework.py
- [[Maloyan & Namiot 2026 (arXiv2601.17548) — Malicious MCP server configuration attacks]] - paper - docs/vault/02 - Modules/Security Modules/consent_framework.py.md
- [[ServerConfig]] - code - gateway/security/consent_framework.py
- [[ShellInjectionDetected]] - code - gateway/security/consent_framework.py
- [[TestConsentDecision]] - code - gateway/tests/test_consent_framework.py
- [[TestEnvironmentValidation]] - code - gateway/tests/test_consent_framework.py
- [[TestServerConfigValidation]] - code - gateway/tests/test_consent_framework.py
- [[TestWhitelistBlacklist]] - code - gateway/tests/test_consent_framework.py
- [[Validate a server configuration before execution.]] - rationale - gateway/security/consent_framework.py
- [[consent_framework.py]] - code - gateway/security/consent_framework.py
- [[framework()]] - code - gateway/tests/test_consent_framework.py
- [[test_consent_framework.py]] - code - gateway/tests/test_consent_framework.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_204
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Alert Dispatcher & RBAC Reliability]]
- 10 edges to [[_COMMUNITY_Session Manager & PIIContext Guard]]
- 10 edges to [[_COMMUNITY_P3 Infrastructure Security Modules]]
- 2 edges to [[_COMMUNITY_Voice Gateway STT & Browser Security]]
- 1 edge to [[_COMMUNITY_Community 52]]
- 1 edge to [[_COMMUNITY_File Sandbox & Privilege Separation Tests]]
- 1 edge to [[_COMMUNITY_Community 48]]

## Top bridge nodes
- [[ConsentDecision]] - degree 33, connects to 5 communities
- [[consent_framework.py]] - degree 11, connects to 4 communities
- [[TestServerConfigValidation]] - degree 13, connects to 1 community
- [[TestEnvironmentValidation]] - degree 10, connects to 1 community
- [[TestWhitelistBlacklist]] - degree 9, connects to 1 community