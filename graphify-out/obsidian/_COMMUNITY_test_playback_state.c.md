---
type: community
members: 82
---

# test_playback_state.c

**Members:** 82 nodes

## Members
- [[dot-__init__()_149]] - code - gateway/security/env_guard.py
- [[dot-_contains_env_access_patterns()]] - code - gateway/security/env_guard.py
- [[dot-_looks_like_credential()]] - code - gateway/security/env_guard.py
- [[dot-_make_record()]] - code - gateway/tests/test_security_audit.py
- [[dot-_record_leakage()]] - code - gateway/security/env_guard.py
- [[dot-check_command_execution()]] - code - gateway/security/env_guard.py
- [[dot-check_file_access()]] - code - gateway/security/env_guard.py
- [[dot-clear_detected_leakages()]] - code - gateway/security/env_guard.py
- [[dot-export_leakage_report()]] - code - gateway/security/env_guard.py
- [[dot-get_leakage_summary()]] - code - gateway/security/env_guard.py
- [[dot-monitor_environment_access()]] - code - gateway/security/env_guard.py
- [[dot-scrub_command_output()]] - code - gateway/security/env_guard.py
- [[dot-test_allows_file_named_environ_elsewhere()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_allows_plain_command()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_allows_unrelated_file()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_aws_key_redaction()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_aws_key_redaction_via_pattern()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_base64_padding_is_credential()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_blocks_cat_proc_environ_pattern()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_blocks_env_command()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_blocks_exact_proc_self_environ()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_blocks_indirect_var_expansion()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_blocks_printenv()_1]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_blocks_wildcard_proc_pid_environ()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_clean_output_unchanged_and_no_leakage()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_clear_resets_leakages()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_credit_card_in_logs()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_critical_leakage_yields_critical_risk()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_empty_command_is_allowed()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_env_guard_command_check()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_env_guard_monitoring()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_env_guard_scrub_output()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_export_writes_valid_json_report()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_github_token_redaction()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_jwt_redaction()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_long_alphanumeric_is_credential()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_many_medium_yields_medium_risk()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_multiple_high_yields_high_risk()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_named_var_with_short_value_uses_redacted_marker()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_natural_language_question_is_allowed()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_no_activity_is_low_risk()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_plain_word_is_not_credential()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_scrubs_credential_looking_value_for_unknown_var()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_scrubs_named_credential_env_var()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_scrubs_openai_key_pattern()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_short_value_is_not_credential()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_ssn_redaction_in_logs()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_summary_aggregates_by_severity_and_method()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_unparseable_text_is_allowed()]] - code - gateway/tests/test_env_guard_class.py
- [[dot-test_unparseable_text_is_allowed()_1]] - code - gateway/tests/test_round2_hardening.py
- [[Any_55]] - code - gateway/security/env_guard.py
- [[Check if a value looks like a credential.]] - rationale - gateway/security/env_guard.py
- [[Check if command contains patterns that could access environment.]] - rationale - gateway/security/env_guard.py
- [[Check if command execution should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Check if file access should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Clear the list of detected leakages.]] - rationale - gateway/security/env_guard.py
- [[Detected environment variable leakage.]] - rationale - gateway/security/env_guard.py
- [[EnvironmentGuard]] - code - gateway/security/env_guard.py
- [[EnvironmentLeakage]] - code - gateway/security/env_guard.py
- [[Export leakage findings to a report file.]] - rationale - gateway/security/env_guard.py
- [[Get summary of all detected leakages.]] - rationale - gateway/security/env_guard.py
- [[Get the global environment guard instance.]] - rationale - gateway/security/env_guard.py
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
- [[alert_dispatcher.py]] - code - gateway/security/alert_dispatcher.py
- [[canary.py]] - code - gateway/security/canary.py
- [[encrypted_store.py]] - code - gateway/security/encrypted_store.py
- [[env_guard.py_2]] - code - gateway/security/env_guard.py
- [[get_env_guard()]] - code - gateway/security/env_guard.py
- [[guard()_4]] - code - gateway/tests/test_env_guard_class.py
- [[test_env_guard_class.py]] - code - gateway/tests/test_env_guard_class.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_playback_statec
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_MiddlewareManager]]
- 12 edges to [[_COMMUNITY__wrap_response()]]
- 11 edges to [[_COMMUNITY_SessionManager]]
- 9 edges to [[_COMMUNITY__wrap_response() (2)_1]]
- 6 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 6 edges to [[_COMMUNITY_PortManager]]
- 5 edges to [[_COMMUNITY_dot-_make_proxy()]]
- 4 edges to [[_COMMUNITY_check_command]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]
- 4 edges to [[_COMMUNITY__wrap_response() (4)]]
- 3 edges to [[_COMMUNITY_AgentTarget (2)_1]]
- 3 edges to [[_COMMUNITY_NetworkSecurityFinding]]
- 3 edges to [[_COMMUNITY_DelegationManager]]
- 3 edges to [[_COMMUNITY__wrap_response() (3)_1]]
- 2 edges to [[_COMMUNITY_asyncio]]
- 2 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 2 edges to [[_COMMUNITY_Common Queries]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy (2)_1]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig (2)]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_SecureBrowser (3)]]
- 1 edge to [[_COMMUNITY_AgentShroud™ README]]
- 1 edge to [[_COMMUNITY_KeyRotationManager (2)]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_system-requirements]]
- 1 edge to [[_COMMUNITY__wrap_response() (5)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_WebProxy]]
- 1 edge to [[_COMMUNITY_test_a2a_policy.py]]

## Top bridge nodes
- [[TestLoggingSecurity]] - degree 47, connects to 21 communities
- [[EnvironmentGuard]] - degree 73, connects to 12 communities
- [[alert_dispatcher.py]] - degree 10, connects to 8 communities
- [[env_guard.py_2]] - degree 10, connects to 5 communities
- [[TestEnvGuardFailOpen]] - degree 9, connects to 5 communities
