---
type: community
cohesion: 0.04
members: 78
---

# GitGuard

**Cohesion:** 0.04 - loosely connected
**Members:** 78 nodes

## Members
- [[dot-__init__()_159]] - code - gateway/security/git_guard.py
- [[dot-_analyze_file_content()]] - code - gateway/security/git_guard.py
- [[dot-_analyze_script_content()]] - code - gateway/security/git_guard.py
- [[dot-_analyze_script_file()]] - code - gateway/security/git_guard.py
- [[dot-_make_hook()]] - code - gateway/tests/test_git_guard.py
- [[dot-_quarantine_suspicious_files()]] - code - gateway/security/git_guard.py
- [[dot-_scan_git_hooks()]] - code - gateway/security/git_guard.py
- [[dot-_scan_package_json()]] - code - gateway/security/git_guard.py
- [[dot-_scan_pyproject_toml()]] - code - gateway/security/git_guard.py
- [[dot-_scan_setup_py()]] - code - gateway/security/git_guard.py
- [[dot-export_findings_report()]] - code - gateway/security/git_guard.py
- [[dot-get_findings_summary()]] - code - gateway/security/git_guard.py
- [[dot-monitor_git_operations()]] - code - gateway/security/git_guard.py
- [[dot-scan_content()]] - code - gateway/security/git_guard.py
- [[dot-scan_git_repository()]] - code - gateway/security/git_guard.py
- [[dot-test_clean_hook_passes()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_clean_repo_no_findings()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_curl_in_hook_flagged()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_default_mode_is_enforce()_4]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_default_mode_is_enforce()_5]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_finding_has_file_path()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_from_environment_defaults_to_enforce()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_git_guard_detects_credential_patterns()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_git_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_git_guard_no_path_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_keyvault_instantiated_and_seeded_in_lifespan()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_llm_stats_endpoint_is_defined()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_nc_flagged()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_no_git_dir_returns_empty()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_no_hardcoded_owner_id_in_lifespan()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_pipeline_scans_outbound_for_key_leaks()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_reverse_shell_flagged()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_sanitize_reason_preserves_simple_text()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_sanitize_reason_strips_file_paths()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_sanitize_reason_strips_module_paths()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_scan_repository_default_enforce()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_v1_endpoint_handles_non_json_upstream_bodies()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_v1_endpoint_is_defined()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_wget_flagged()]] - code - gateway/tests/test_git_guard.py
- [[A security finding in git hooks or install scripts.]] - rationale - gateway/security/git_guard.py
- [[Analyze a script file for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Analyze file content for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Analyze script content string for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Any_67]] - code - gateway/security/git_guard.py
- [[Args             mode 'monitor' (log findings) or 'enforce' (quarantine suspic]] - rationale - gateway/security/git_guard.py
- [[Convenience function to scan a repository.]] - rationale - gateway/security/git_guard.py
- [[Export findings to a detailed report.]] - rationale - gateway/security/git_guard.py
- [[Get a summary of all findings.]] - rationale - gateway/security/git_guard.py
- [[Git guard errors shouldn't expose full file paths.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Git guard should catch credential patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[GitGuard]] - code - gateway/security/git_guard.py
- [[Monitor and analyze git hooks and package installation scripts.]] - rationale - gateway/security/git_guard.py
- [[Monitor for git clone and npm install operations.]] - rationale - gateway/security/git_guard.py
- [[Move suspicious files to quarantine directory.]] - rationale - gateway/security/git_guard.py
- [[Path_50]] - code - gateway/security/git_guard.py
- [[Proxy endpoint must not crash if upstream returns non-JSON body.]] - rationale - gateway/tests/test_round2_hardening.py
- [[Scan a git repository for malicious hooks and scripts.          Args]] - rationale - gateway/security/git_guard.py
- [[Scan arbitrary text content for malicious gitsupply-chain patterns.          Th]] - rationale - gateway/security/git_guard.py
- [[Scan git hooks directory for malicious content.]] - rationale - gateway/security/git_guard.py
- [[Scan package.json for suspicious install scripts.]] - rationale - gateway/security/git_guard.py
- [[Scan pyproject.toml for suspicious build scripts.]] - rationale - gateway/security/git_guard.py
- [[Scan setup.py for suspicious installation scripts.]] - rationale - gateway/security/git_guard.py
- [[SecurityFinding]] - code - gateway/security/git_guard.py
- [[TestDRYOwnerChatID]] - code - gateway/tests/test_round2_hardening.py
- [[TestEgressConfigDefaultEnforce]] - code - gateway/tests/test_round2_hardening.py
- [[TestFileSandboxDefaultEnforce]] - code - gateway/tests/test_round2_hardening.py
- [[TestGitGuard_1]] - code - gateway/tests/test_git_guard.py
- [[TestGitGuardDefaultEnforce]] - code - gateway/tests/test_round2_hardening.py
- [[TestKeyVaultWired]] - code - gateway/tests/test_round2_hardening.py
- [[TestLLMProxyEndpoints]] - code - gateway/tests/test_round2_hardening.py
- [[TestNotifyUserBlockedSanitization]] - code - gateway/tests/test_round2_hardening.py
- [[Tests for Round 2 hardening — 9 fixes.]] - rationale - gateway/tests/test_round2_hardening.py
- [[The llm-proxystats endpoint must exist.]] - rationale - gateway/tests/test_round2_hardening.py
- [[The v1{path} endpoint must exist (enabled in v0.9.0).]] - rationale - gateway/tests/test_round2_hardening.py
- [[git_guard.py]] - code - gateway/security/git_guard.py
- [[scan_repository()]] - code - gateway/security/git_guard.py
- [[test_git_guard.py]] - code - gateway/tests/test_git_guard.py
- [[test_round2_hardening.py]] - code - gateway/tests/test_round2_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GitGuard
SORT file.name ASC
```

## Connections to other communities
- 35 edges to [[_COMMUNITY_AlertDispatcher]]
- 28 edges to [[_COMMUNITY_MiddlewareManager]]
- 11 edges to [[_COMMUNITY_ResourceGuard]]
- 8 edges to [[_COMMUNITY_EgressFilterConfig]]
- 8 edges to [[_COMMUNITY_TelegramAPIProxy_1]]
- 2 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]

## Top bridge nodes
- [[test_round2_hardening.py]] - degree 17, connects to 5 communities
- [[TestLLMProxyEndpoints]] - degree 10, connects to 5 communities
- [[TestNotifyUserBlockedSanitization]] - degree 10, connects to 5 communities
- [[TestGitGuardDefaultEnforce]] - degree 9, connects to 5 communities
- [[TestKeyVaultWired]] - degree 9, connects to 5 communities
