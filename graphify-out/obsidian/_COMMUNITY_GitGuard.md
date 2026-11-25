---
type: community
members: 49
---

# GitGuard

**Members:** 49 nodes

## Members
- [[dot-__init__()_117]] - code - gateway/security/git_guard.py
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
- [[dot-test_nc_flagged()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_no_git_dir_returns_empty()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_reverse_shell_flagged()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_scan_repository_default_enforce()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_wget_flagged()]] - code - gateway/tests/test_git_guard.py
- [[A security finding in git hooks or install scripts.]] - rationale - gateway/security/git_guard.py
- [[Analyze a script file for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Analyze file content for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Analyze script content string for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Args mode 'monitor' (log findings) or 'enforce' (quarantine suspicious files)]] - rationale - gateway/security/git_guard.py
- [[Convenience function to scan a repository.]] - rationale - gateway/security/git_guard.py
- [[Enum_31]] - code
- [[Git Hook Guard - Security Hardening Module Scan git hooks and package…]] - rationale - gateway/security/git_guard.py
- [[GitGuard]] - code - gateway/security/git_guard.py
- [[Monitor and analyze git hooks and package installation scripts.]] - rationale - gateway/security/git_guard.py
- [[Move suspicious files to quarantine directory.]] - rationale - gateway/security/git_guard.py
- [[Path_39]] - code
- [[Scan a git repository for malicious hooks and scripts. Args repo_path Path to…]] - rationale - gateway/security/git_guard.py
- [[Scan arbitrary text content for malicious gitsupply-chain patterns. This is…]] - rationale - gateway/security/git_guard.py
- [[Scan git hooks directory for malicious content.]] - rationale - gateway/security/git_guard.py
- [[Scan package.json for suspicious install scripts.]] - rationale - gateway/security/git_guard.py
- [[Scan pyproject.toml for suspicious build scripts.]] - rationale - gateway/security/git_guard.py
- [[Scan setup.py for suspicious installation scripts.]] - rationale - gateway/security/git_guard.py
- [[SecurityFinding]] - code - gateway/security/git_guard.py
- [[TestGitGuard]] - code - gateway/tests/test_git_guard.py
- [[TestGitGuardDefaultEnforce]] - code - gateway/tests/test_round2_hardening.py
- [[Threat levels for detected issues.]] - rationale - gateway/security/git_guard.py
- [[ThreatLevel_2]] - code - gateway/security/git_guard.py
- [[git_guard.py]] - code - gateway/security/git_guard.py
- [[scan_repository()]] - code - gateway/security/git_guard.py
- [[str_14]] - code
- [[test_git_guard.py]] - code - gateway/tests/test_git_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GitGuard
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_FileSandbox]]
- 4 edges to [[_COMMUNITY_EnvironmentGuard]]
- 3 edges to [[_COMMUNITY_ContextGuard]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_TestModuleInstantiationInEnforceMode]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_test_all_modules_enforce.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[GitGuard]] - degree 45, connects to 9 communities
- [[git_guard.py]] - degree 9, connects to 2 communities
- [[scan_repository()]] - degree 5, connects to 1 community
- [[TestGitGuardDefaultEnforce]] - degree 4, connects to 1 community
