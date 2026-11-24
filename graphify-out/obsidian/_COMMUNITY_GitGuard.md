---
type: community
members: 63
---

# GitGuard

**Members:** 63 nodes

## Members
- [[dot-__init__()_125]] - code - gateway/security/git_guard.py
- [[dot-_analyze_file_content()]] - code - gateway/security/git_guard.py
- [[dot-_analyze_script_content()]] - code - gateway/security/git_guard.py
- [[dot-_analyze_script_file()]] - code - gateway/security/git_guard.py
- [[dot-_make_hook()]] - code - gateway/tests/test_git_guard.py
- [[dot-_quarantine_suspicious_files()]] - code - gateway/security/git_guard.py
- [[dot-_scan_git_hooks()]] - code - gateway/security/git_guard.py
- [[dot-_scan_package_json()]] - code - gateway/security/git_guard.py
- [[dot-_scan_pyproject_toml()]] - code - gateway/security/git_guard.py
- [[dot-_scan_setup_py()]] - code - gateway/security/git_guard.py
- [[dot-scan_content()]] - code - gateway/security/git_guard.py
- [[dot-scan_git_repository()]] - code - gateway/security/git_guard.py
- [[dot-test_clean_hook_passes()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_clean_repo_no_findings()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_curl_in_hook_flagged()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_default_mode_is_enforce()_6]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_finding_has_file_path()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_keyvault_instantiated_and_seeded_in_lifespan()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_llm_stats_endpoint_is_defined()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_nc_flagged()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_no_git_dir_returns_empty()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_no_hardcoded_owner_id_in_lifespan()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_pipeline_scans_outbound_for_key_leaks()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_reverse_shell_flagged()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_scan_repository_default_enforce()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_v1_endpoint_handles_non_json_upstream_bodies()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_v1_endpoint_is_defined()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_wget_flagged()]] - code - gateway/tests/test_git_guard.py
- [[A security finding in git hooks or install scripts.]] - rationale - gateway/security/git_guard.py
- [[Analyze a script file for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Analyze file content for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Analyze script content string for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Args mode 'monitor' (log findings) or 'enforce' (quarantine suspicious files)]] - rationale - gateway/security/git_guard.py
- [[Convenience function to scan a repository.]] - rationale - gateway/security/git_guard.py
- [[Enum_32]] - code
- [[Git Hook Guard - Security Hardening Module Scan git hooks and package…]] - rationale - gateway/security/git_guard.py
- [[GitGuard]] - code - gateway/security/git_guard.py
- [[Monitor and analyze git hooks and package installation scripts.]] - rationale - gateway/security/git_guard.py
- [[Move suspicious files to quarantine directory.]] - rationale - gateway/security/git_guard.py
- [[Path_40]] - code
- [[Proxy endpoint must not crash if upstream returns non-JSON body.]] - rationale - gateway/tests/test_round2_hardening.py
- [[Scan a git repository for malicious hooks and scripts. Args repo_path Path to…]] - rationale - gateway/security/git_guard.py
- [[Scan arbitrary text content for malicious gitsupply-chain patterns. This is…]] - rationale - gateway/security/git_guard.py
- [[Scan git hooks directory for malicious content.]] - rationale - gateway/security/git_guard.py
- [[Scan package.json for suspicious install scripts.]] - rationale - gateway/security/git_guard.py
- [[Scan pyproject.toml for suspicious build scripts.]] - rationale - gateway/security/git_guard.py
- [[Scan setup.py for suspicious installation scripts.]] - rationale - gateway/security/git_guard.py
- [[SecurityFinding]] - code - gateway/security/git_guard.py
- [[TestDRYOwnerChatID]] - code - gateway/tests/test_round2_hardening.py
- [[TestGitGuard]] - code - gateway/tests/test_git_guard.py
- [[TestGitGuardDefaultEnforce]] - code - gateway/tests/test_round2_hardening.py
- [[TestKeyVaultWired]] - code - gateway/tests/test_round2_hardening.py
- [[TestLLMProxyEndpoints]] - code - gateway/tests/test_round2_hardening.py
- [[Tests for Round 2 hardening — 9 fixes.]] - rationale - gateway/tests/test_round2_hardening.py
- [[The llm-proxystats endpoint must exist.]] - rationale - gateway/tests/test_round2_hardening.py
- [[The v1{path} endpoint must exist (enabled in v0.9.0).]] - rationale - gateway/tests/test_round2_hardening.py
- [[Threat levels for detected issues.]] - rationale - gateway/security/git_guard.py
- [[ThreatLevel_2]] - code - gateway/security/git_guard.py
- [[git_guard.py]] - code - gateway/security/git_guard.py
- [[scan_repository()]] - code - gateway/security/git_guard.py
- [[str_17]] - code
- [[test_git_guard.py]] - code - gateway/tests/test_git_guard.py
- [[test_round2_hardening.py]] - code - gateway/tests/test_round2_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GitGuard
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_EnvironmentGuard]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_FileSandbox]]
- 2 edges to [[_COMMUNITY_PathIsolationManager]]
- 2 edges to [[_COMMUNITY_run]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_LogSanitizer]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_dot-_sanitize_reason]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_TestEgressFilterConfig]]

## Top bridge nodes
- [[GitGuard]] - degree 45, connects to 10 communities
- [[test_round2_hardening.py]] - degree 17, connects to 7 communities
- [[git_guard.py]] - degree 9, connects to 2 communities
