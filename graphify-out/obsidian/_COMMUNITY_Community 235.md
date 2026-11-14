---
type: community
members: 77
---

# Community 235

**Members:** 77 nodes

## Members
- [[.__init__()_94]] - code - gateway/security/env_guard.py
- [[._contains_env_access_patterns()]] - code - gateway/security/env_guard.py
- [[._looks_like_credential()]] - code - gateway/security/env_guard.py
- [[._make_record()]] - code - gateway/tests/test_security_audit.py
- [[._record_leakage()]] - code - gateway/security/env_guard.py
- [[.check_command_execution()]] - code - gateway/security/env_guard.py
- [[.check_file_access()]] - code - gateway/security/env_guard.py
- [[.clear_detected_leakages()]] - code - gateway/security/env_guard.py
- [[.export_leakage_report()]] - code - gateway/security/env_guard.py
- [[.get_leakage_summary()]] - code - gateway/security/env_guard.py
- [[.monitor_environment_access()]] - code - gateway/security/env_guard.py
- [[.scrub_command_output()]] - code - gateway/security/env_guard.py
- [[.test_allows_file_named_environ_elsewhere()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_allows_plain_command()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_allows_unrelated_file()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_aws_key_redaction()]] - code - gateway/tests/test_security_audit.py
- [[.test_aws_key_redaction_via_pattern()]] - code - gateway/tests/test_security_audit.py
- [[.test_base64_padding_is_credential()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_blocks_cat_proc_environ_pattern()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_blocks_env_command()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_blocks_exact_proc_self_environ()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_blocks_indirect_var_expansion()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_blocks_printenv()_1]] - code - gateway/tests/test_env_guard_class.py
- [[.test_blocks_wildcard_proc_pid_environ()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_clean_output_unchanged_and_no_leakage()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_clear_resets_leakages()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_credit_card_in_logs()]] - code - gateway/tests/test_security_audit.py
- [[.test_critical_leakage_yields_critical_risk()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_empty_command_is_allowed()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_env_guard_command_check()]] - code - gateway/tests/test_security_audit.py
- [[.test_env_guard_detects_data_access()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_env_guard_monitoring()]] - code - gateway/tests/test_security_audit.py
- [[.test_env_guard_scrub_output()]] - code - gateway/tests/test_security_audit.py
- [[.test_export_writes_valid_json_report()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_git_guard_scan_repo()]] - code - gateway/tests/test_security_audit.py
- [[.test_github_token_redaction()]] - code - gateway/tests/test_security_audit.py
- [[.test_jwt_redaction()]] - code - gateway/tests/test_security_audit.py
- [[.test_long_alphanumeric_is_credential()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_many_medium_yields_medium_risk()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_multiple_high_yields_high_risk()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_named_var_with_short_value_uses_redacted_marker()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_natural_language_question_is_allowed()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_no_activity_is_low_risk()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_plain_word_is_not_credential()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_scrubs_credential_looking_value_for_unknown_var()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_scrubs_named_credential_env_var()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_scrubs_openai_key_pattern()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_short_value_is_not_credential()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_ssn_redaction_in_logs()]] - code - gateway/tests/test_security_audit.py
- [[.test_summary_aggregates_by_severity_and_method()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_unparseable_text_is_allowed()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_unparseable_text_is_allowed()_1]] - code - gateway/tests/test_round2_hardening.py
- [[Any_49]] - code - gateway/security/env_guard.py
- [[Check if a value looks like a credential.]] - rationale - gateway/security/env_guard.py
- [[Check if command contains patterns that could access environment.]] - rationale - gateway/security/env_guard.py
- [[Check if command execution should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Check if file access should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Clear the list of detected leakages.]] - rationale - gateway/security/env_guard.py
- [[Environment guard should monitor data access patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[EnvironmentGuard]] - code - gateway/security/env_guard.py
- [[Export leakage findings to a report file.]] - rationale - gateway/security/env_guard.py
- [[Get summary of all detected leakages.]] - rationale - gateway/security/env_guard.py
- [[Guard against environment variable leakage and unauthorized access.]] - rationale - gateway/security/env_guard.py
- [[Monitor an agent's environment access attempts.          Args             agent]] - rationale - gateway/security/env_guard.py
- [[Record a detected environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Scrub environment variables and API keys from command output.          Args]] - rationale - gateway/security/env_guard.py
- [[Test log sanitization and information leakage prevention.]] - rationale - gateway/tests/test_security_audit.py
- [[TestCheckCommandExecution]] - code - gateway/tests/test_env_guard_class.py
- [[TestCheckFileAccess]] - code - gateway/tests/test_env_guard_class.py
- [[TestEnvGuardFailOpen]] - code - gateway/tests/test_round2_hardening.py
- [[TestLoggingSecurity]] - code - gateway/tests/test_security_audit.py
- [[TestLooksLikeCredential]] - code - gateway/tests/test_env_guard_class.py
- [[TestMonitorEnvironmentAccess]] - code - gateway/tests/test_env_guard_class.py
- [[TestScrubCommandOutput]] - code - gateway/tests/test_env_guard_class.py
- [[TestSummaryAndExport]] - code - gateway/tests/test_env_guard_class.py
- [[guard()_2]] - code - gateway/tests/test_env_guard_class.py
- [[test_env_guard_class.py]] - code - gateway/tests/test_env_guard_class.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_235
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Community 0]]
- 13 edges to [[_COMMUNITY_Community 72]]
- 12 edges to [[_COMMUNITY_Community 121]]
- 8 edges to [[_COMMUNITY_Community 41]]
- 5 edges to [[_COMMUNITY_Community 5]]
- 4 edges to [[_COMMUNITY_Community 162]]
- 4 edges to [[_COMMUNITY_Community 362]]
- 4 edges to [[_COMMUNITY_Community 365]]
- 3 edges to [[_COMMUNITY_Community 7]]
- 2 edges to [[_COMMUNITY_Community 477]]
- 2 edges to [[_COMMUNITY_Community 684]]
- 2 edges to [[_COMMUNITY_Community 809]]
- 2 edges to [[_COMMUNITY_Community 146]]
- 1 edge to [[_COMMUNITY_Community 978]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 14]]
- 1 edge to [[_COMMUNITY_Community 557]]
- 1 edge to [[_COMMUNITY_Community 166]]
- 1 edge to [[_COMMUNITY_Community 17]]
- 1 edge to [[_COMMUNITY_Community 93]]
- 1 edge to [[_COMMUNITY_Community 108]]
- 1 edge to [[_COMMUNITY_Community 148]]
- 1 edge to [[_COMMUNITY_Community 196]]
- 1 edge to [[_COMMUNITY_Community 128]]
- 1 edge to [[_COMMUNITY_Community 479]]
- 1 edge to [[_COMMUNITY_Community 32]]
- 1 edge to [[_COMMUNITY_Community 71]]

## Top bridge nodes
- [[TestLoggingSecurity]] - degree 47, connects to 18 communities
- [[EnvironmentGuard]] - degree 74, connects to 15 communities
- [[TestEnvGuardFailOpen]] - degree 9, connects to 5 communities
- [[._record_leakage()]] - degree 6, connects to 1 community
- [[.check_command_execution()]] - degree 5, connects to 1 community