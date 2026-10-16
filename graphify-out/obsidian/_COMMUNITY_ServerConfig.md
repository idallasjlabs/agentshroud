---
type: community
cohesion: 0.23
members: 16
---

# ServerConfig

**Cohesion:** 0.23 - loosely connected
**Members:** 16 nodes

## Members
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
- [[ServerConfig]] - code - gateway/security/consent_framework.py
- [[TestEnvironmentValidation]] - code - gateway/tests/test_consent_framework.py
- [[TestServerConfigValidation]] - code - gateway/tests/test_consent_framework.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ServerConfig
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_ConsentFramework]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]

## Top bridge nodes
- [[TestServerConfigValidation]] - degree 13, connects to 2 communities
- [[TestEnvironmentValidation]] - degree 10, connects to 2 communities
- [[ServerConfig]] - degree 22, connects to 1 community
