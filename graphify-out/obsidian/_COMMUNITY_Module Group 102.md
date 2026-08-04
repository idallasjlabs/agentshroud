---
type: community
cohesion: 0.10
members: 42
---

# Module Group 102

**Cohesion:** 0.10 - loosely connected
**Members:** 42 nodes

## Members
- [[.__init__()_52]] - code - gateway/security/consent_framework.py
- [[.add_to_blacklist()]] - code - gateway/security/consent_framework.py
- [[.add_to_whitelist()]] - code - gateway/security/consent_framework.py
- [[.get_blacklist()]] - code - gateway/security/consent_framework.py
- [[.get_whitelist()]] - code - gateway/security/consent_framework.py
- [[.remove_from_blacklist()]] - code - gateway/security/consent_framework.py
- [[.remove_from_whitelist()]] - code - gateway/security/consent_framework.py
- [[.test_add_and_remove_blacklist()]] - code - gateway/tests/test_consent_framework.py
- [[.test_add_and_remove_whitelist()]] - code - gateway/tests/test_consent_framework.py
- [[.test_blacklisted_command_rejected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_decision_approved()]] - code - gateway/tests/test_consent_framework.py
- [[.test_decision_denied()]] - code - gateway/tests/test_consent_framework.py
- [[.test_decision_has_timestamp()]] - code - gateway/tests/test_consent_framework.py
- [[.test_empty_command_rejected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_env_with_path_manipulation()]] - code - gateway/tests/test_consent_framework.py
- [[.test_env_with_secrets_in_value_warned()]] - code - gateway/tests/test_consent_framework.py
- [[.test_known_dangerous_patterns_detected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_multiple_configs_validated()]] - code - gateway/tests/test_consent_framework.py
- [[.test_safe_env_no_warnings()]] - code - gateway/tests/test_consent_framework.py
- [[.test_shell_injection_backtick_detected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_shell_injection_curl_detected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_shell_injection_dollar_paren()]] - code - gateway/tests/test_consent_framework.py
- [[.test_shell_injection_pipe_to_sh()]] - code - gateway/tests/test_consent_framework.py
- [[.test_shell_injection_rm_rf_detected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_shell_injection_wget_detected()]] - code - gateway/tests/test_consent_framework.py
- [[.test_valid_config_passes()]] - code - gateway/tests/test_consent_framework.py
- [[.test_whitelisted_command_auto_approved()]] - code - gateway/tests/test_consent_framework.py
- [[.validate_config()]] - code - gateway/security/consent_framework.py
- [[.validate_configs()]] - code - gateway/security/consent_framework.py
- [[ConfigValidationError]] - code - gateway/security/consent_framework.py
- [[ConsentDecision]] - code - gateway/security/consent_framework.py
- [[ConsentFramework]] - code - gateway/security/consent_framework.py
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
TABLE source_file, type FROM #community/Module_Group_102
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 9 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 4 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 3 edges to [[_COMMUNITY_Alert Dispatcher]]
- 2 edges to [[_COMMUNITY_Module Group 110]]
- 1 edge to [[_COMMUNITY_Module Group 113]]
- 1 edge to [[_COMMUNITY_Module Group 258]]
- 1 edge to [[_COMMUNITY_Module Group 257]]
- 1 edge to [[_COMMUNITY_Subagent Monitor]]
- 1 edge to [[_COMMUNITY_Module Group 66]]
- 1 edge to [[_COMMUNITY_Module Group 137]]

## Top bridge nodes
- [[ConsentDecision]] - degree 33, connects to 9 communities
- [[ConsentFramework]] - degree 25, connects to 1 community
- [[ConfigValidationError]] - degree 3, connects to 1 community
