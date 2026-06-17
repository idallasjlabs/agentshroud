---
type: community
cohesion: 0.08
members: 49
---

# Module Group 80

**Cohesion:** 0.08 - loosely connected
**Members:** 49 nodes

## Members
- [[.__init__()_66]] - code - gateway/security/git_guard.py
- [[._analyze_file_content()]] - code - gateway/security/git_guard.py
- [[._analyze_script_content()]] - code - gateway/security/git_guard.py
- [[._analyze_script_file()]] - code - gateway/security/git_guard.py
- [[._make_hook()]] - code - gateway/tests/test_git_guard.py
- [[._quarantine_suspicious_files()]] - code - gateway/security/git_guard.py
- [[._scan_git_hooks()]] - code - gateway/security/git_guard.py
- [[._scan_package_json()]] - code - gateway/security/git_guard.py
- [[._scan_pyproject_toml()]] - code - gateway/security/git_guard.py
- [[._scan_setup_py()]] - code - gateway/security/git_guard.py
- [[.export_findings_report()]] - code - gateway/security/git_guard.py
- [[.get_findings_summary()]] - code - gateway/security/git_guard.py
- [[.monitor_git_operations()]] - code - gateway/security/git_guard.py
- [[.scan_content()]] - code - gateway/security/git_guard.py
- [[.scan_git_repository()]] - code - gateway/security/git_guard.py
- [[.test_clean_hook_passes()]] - code - gateway/tests/test_git_guard.py
- [[.test_clean_repo_no_findings()]] - code - gateway/tests/test_git_guard.py
- [[.test_curl_in_hook_flagged()]] - code - gateway/tests/test_git_guard.py
- [[.test_default_mode_is_enforce()_5]] - code - gateway/tests/test_round2_hardening.py
- [[.test_finding_has_file_path()]] - code - gateway/tests/test_git_guard.py
- [[.test_nc_flagged()]] - code - gateway/tests/test_git_guard.py
- [[.test_no_git_dir_returns_empty()]] - code - gateway/tests/test_git_guard.py
- [[.test_reverse_shell_flagged()]] - code - gateway/tests/test_git_guard.py
- [[.test_wget_flagged()]] - code - gateway/tests/test_git_guard.py
- [[A security finding in git hooks or install scripts.]] - rationale - gateway/security/git_guard.py
- [[Analyze a script file for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Analyze file content for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Analyze script content string for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Any_36]] - code - gateway/security/git_guard.py
- [[Args             mode 'monitor' (log findings) or 'enforce' (quarantine suspic]] - rationale - gateway/security/git_guard.py
- [[Convenience function to scan a repository.]] - rationale - gateway/security/git_guard.py
- [[Export findings to a detailed report.]] - rationale - gateway/security/git_guard.py
- [[Get a summary of all findings.]] - rationale - gateway/security/git_guard.py
- [[GitGuard]] - code - gateway/security/git_guard.py
- [[Monitor and analyze git hooks and package installation scripts.]] - rationale - gateway/security/git_guard.py
- [[Monitor for git clone and npm install operations.]] - rationale - gateway/security/git_guard.py
- [[Move suspicious files to quarantine directory.]] - rationale - gateway/security/git_guard.py
- [[Path_11]] - code - gateway/security/git_guard.py
- [[Scan a git repository for malicious hooks and scripts.          Args]] - rationale - gateway/security/git_guard.py
- [[Scan arbitrary text content for malicious gitsupply-chain patterns.          Th]] - rationale - gateway/security/git_guard.py
- [[Scan git hooks directory for malicious content.]] - rationale - gateway/security/git_guard.py
- [[Scan package.json for suspicious install scripts.]] - rationale - gateway/security/git_guard.py
- [[Scan pyproject.toml for suspicious build scripts.]] - rationale - gateway/security/git_guard.py
- [[Scan setup.py for suspicious installation scripts.]] - rationale - gateway/security/git_guard.py
- [[SecurityFinding]] - code - gateway/security/git_guard.py
- [[TestGitGuard]] - code - gateway/tests/test_git_guard.py
- [[git_guard.py]] - code - gateway/security/git_guard.py
- [[scan_repository()]] - code - gateway/security/git_guard.py
- [[test_git_guard.py]] - code - gateway/tests/test_git_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_80
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 17 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 10 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 3 edges to [[_COMMUNITY_Alert Dispatcher]]
- 3 edges to [[_COMMUNITY_Module Group 110]]
- 2 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 258]]
- 1 edge to [[_COMMUNITY_Module Group 257]]
- 1 edge to [[_COMMUNITY_Subagent Monitor]]
- 1 edge to [[_COMMUNITY_Module Group 66]]
- 1 edge to [[_COMMUNITY_Module Group 137]]

## Top bridge nodes
- [[GitGuard]] - degree 83, connects to 11 communities
- [[git_guard.py]] - degree 5, connects to 1 community
- [[scan_repository()]] - degree 5, connects to 1 community
- [[.test_default_mode_is_enforce()_5]] - degree 2, connects to 1 community