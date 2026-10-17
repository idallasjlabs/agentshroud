---
type: community
members: 54
---

# ResourceGuard

**Members:** 54 nodes

## Members
- [[dot-__init__()_41]] - code - gateway/security/git_guard.py
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
- [[dot-test_default_mode_is_enforce()_3]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_finding_has_file_path()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_git_guard_detects_credential_patterns()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_git_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_git_guard_no_path_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_nc_flagged()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_no_git_dir_returns_empty()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_reverse_shell_flagged()]] - code - gateway/tests/test_git_guard.py
- [[dot-test_wget_flagged()]] - code - gateway/tests/test_git_guard.py
- [[A security finding in git hooks or install scripts.]] - rationale - gateway/security/git_guard.py
- [[Analyze a script file for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Analyze file content for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Analyze script content string for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Any_16]] - code - gateway/security/git_guard.py
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
- [[Path_8]] - code - gateway/security/git_guard.py
- [[Scan a git repository for malicious hooks and scripts.          Args]] - rationale - gateway/security/git_guard.py
- [[Scan arbitrary text content for malicious gitsupply-chain patterns.          Th]] - rationale - gateway/security/git_guard.py
- [[Scan git hooks directory for malicious content.]] - rationale - gateway/security/git_guard.py
- [[Scan package.json for suspicious install scripts.]] - rationale - gateway/security/git_guard.py
- [[Scan pyproject.toml for suspicious build scripts.]] - rationale - gateway/security/git_guard.py
- [[Scan setup.py for suspicious installation scripts.]] - rationale - gateway/security/git_guard.py
- [[SecurityFinding]] - code - gateway/security/git_guard.py
- [[TestGitGuard_1]] - code - gateway/tests/test_git_guard.py
- [[git_guard.py]] - code - gateway/security/git_guard.py
- [[scan_repository()]] - code - gateway/security/git_guard.py
- [[test_git_guard.py]] - code - gateway/tests/test_git_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ResourceGuard
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 16 edges to [[_COMMUNITY_AlertDispatcher]]
- 15 edges to [[_COMMUNITY_AlertDispatcher (2) (2)]]
- 3 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 1 edge to [[_COMMUNITY_AlertDispatcher (2) (3)]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]

## Top bridge nodes
- [[GitGuard]] - degree 84, connects to 6 communities
- [[git_guard.py]] - degree 5, connects to 1 community
- [[scan_repository()]] - degree 5, connects to 1 community
- [[dot-test_git_guard_detects_credential_patterns()]] - degree 3, connects to 1 community
- [[dot-test_git_guard_no_path_leak()]] - degree 3, connects to 1 community
