---
type: community
members: 35
---

# Community 114

**Members:** 35 nodes

## Members
- [[.test_allows_file_named_environ_elsewhere()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_allows_plain_command()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_allows_unrelated_file()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_base64_padding_is_credential()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_blocks_cat_proc_environ_pattern()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_blocks_env_command()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_blocks_exact_proc_self_environ()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_blocks_indirect_var_expansion()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_blocks_printenv()_1]] - code - gateway/tests/test_env_guard_class.py
- [[.test_blocks_wildcard_proc_pid_environ()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_clean_output_unchanged_and_no_leakage()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_clear_resets_leakages()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_critical_leakage_yields_critical_risk()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_empty_command_is_allowed()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_export_writes_valid_json_report()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_long_alphanumeric_is_credential()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_many_medium_yields_medium_risk()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_multiple_high_yields_high_risk()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_named_var_with_short_value_uses_redacted_marker()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_no_activity_is_low_risk()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_plain_word_is_not_credential()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_scrubs_credential_looking_value_for_unknown_var()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_scrubs_named_credential_env_var()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_scrubs_openai_key_pattern()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_short_value_is_not_credential()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_summary_aggregates_by_severity_and_method()]] - code - gateway/tests/test_env_guard_class.py
- [[.test_unparseable_text_is_allowed()]] - code - gateway/tests/test_env_guard_class.py
- [[TestCheckCommandExecution]] - code - gateway/tests/test_env_guard_class.py
- [[TestCheckFileAccess]] - code - gateway/tests/test_env_guard_class.py
- [[TestLooksLikeCredential]] - code - gateway/tests/test_env_guard_class.py
- [[TestMonitorEnvironmentAccess]] - code - gateway/tests/test_env_guard_class.py
- [[TestScrubCommandOutput]] - code - gateway/tests/test_env_guard_class.py
- [[TestSummaryAndExport]] - code - gateway/tests/test_env_guard_class.py
- [[guard()_2]] - code - gateway/tests/test_env_guard_class.py
- [[test_env_guard_class.py]] - code - gateway/tests/test_env_guard_class.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_114
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 14]]

## Top bridge nodes
- [[TestCheckCommandExecution]] - degree 9, connects to 1 community
- [[test_env_guard_class.py]] - degree 8, connects to 1 community
- [[TestScrubCommandOutput]] - degree 7, connects to 1 community
- [[TestCheckFileAccess]] - degree 6, connects to 1 community
- [[TestLooksLikeCredential]] - degree 6, connects to 1 community