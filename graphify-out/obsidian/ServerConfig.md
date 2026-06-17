---
source_file: "gateway/security/consent_framework.py"
type: "code"
community: "Module Group 102"
location: "L32"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Module_Group_102
---

# ServerConfig

## Connections
- [[.test_blacklisted_command_rejected()]] - `calls` [EXTRACTED]
- [[.test_empty_command_rejected()]] - `calls` [EXTRACTED]
- [[.test_env_with_path_manipulation()]] - `calls` [EXTRACTED]
- [[.test_env_with_secrets_in_value_warned()]] - `calls` [EXTRACTED]
- [[.test_known_dangerous_patterns_detected()]] - `calls` [EXTRACTED]
- [[.test_multiple_configs_validated()]] - `calls` [EXTRACTED]
- [[.test_safe_env_no_warnings()]] - `calls` [EXTRACTED]
- [[.test_shell_injection_backtick_detected()]] - `calls` [EXTRACTED]
- [[.test_shell_injection_curl_detected()]] - `calls` [EXTRACTED]
- [[.test_shell_injection_dollar_paren()]] - `calls` [EXTRACTED]
- [[.test_shell_injection_pipe_to_sh()]] - `calls` [EXTRACTED]
- [[.test_shell_injection_rm_rf_detected()]] - `calls` [EXTRACTED]
- [[.test_shell_injection_wget_detected()]] - `calls` [EXTRACTED]
- [[.test_valid_config_passes()]] - `calls` [EXTRACTED]
- [[.test_whitelisted_command_auto_approved()]] - `calls` [EXTRACTED]
- [[.validate_config()]] - `references` [EXTRACTED]
- [[.validate_configs()]] - `references` [EXTRACTED]
- [[TestConsentDecision]] - `uses` [INFERRED]
- [[TestEnvironmentValidation]] - `uses` [INFERRED]
- [[TestServerConfigValidation]] - `uses` [INFERRED]
- [[TestWhitelistBlacklist]] - `uses` [INFERRED]
- [[consent_framework.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Module_Group_102