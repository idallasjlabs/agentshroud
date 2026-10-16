---
type: community
cohesion: 0.08
members: 45
---

# ConsentFramework

**Cohesion:** 0.08 - loosely connected
**Members:** 45 nodes

## Members
- [[dot-__init__()_55]] - code - gateway/security/consent_framework.py
- [[dot-add_to_blacklist()]] - code - gateway/security/consent_framework.py
- [[dot-add_to_whitelist()]] - code - gateway/security/consent_framework.py
- [[dot-get_blacklist()]] - code - gateway/security/consent_framework.py
- [[dot-get_whitelist()]] - code - gateway/security/consent_framework.py
- [[dot-remove_from_blacklist()]] - code - gateway/security/consent_framework.py
- [[dot-remove_from_whitelist()]] - code - gateway/security/consent_framework.py
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
- [[Chen et al. 2026 — Agent configuration vulnerabilities  session hijacking (arXiv2602.14364)]] - paper - gateway/security/consent_framework.py
- [[ConfigValidationError]] - code - gateway/security/consent_framework.py
- [[ConsentFramework]] - code - gateway/security/consent_framework.py
- [[Maloyan & Namiot 2026 (arXiv2601.17548) — Malicious MCP server configuration attacks]] - paper - docs/vault/02 - Modules/Security Modules/consent_framework.py.md
- [[Maloyan & Namiot 2026 — MCP security analysis (arXiv2601.17548)]] - paper - gateway/security/consent_framework.py
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
TABLE source_file, type FROM #community/ConsentFramework
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_AlertDispatcher]]
- 10 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_ConsentFramework_1]]
- 2 edges to [[_COMMUNITY_SessionManager_1]]
- 1 edge to [[_COMMUNITY_ResourceGuard_1]]
- 1 edge to [[_COMMUNITY_AlertDispatcher_1]]

## Top bridge nodes
- [[ConsentFramework]] - degree 31, connects to 4 communities
- [[consent_framework.py]] - degree 10, connects to 3 communities
- [[TestServerConfigValidation]] - degree 13, connects to 1 community
- [[TestEnvironmentValidation]] - degree 10, connects to 1 community
- [[TestWhitelistBlacklist]] - degree 9, connects to 1 community
