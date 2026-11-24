---
source_file: "gateway/security/git_guard.py"
type: "code"
community: "GitGuard"
location: "L49"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/GitGuard
---

# GitGuard

## Connections
- [[dot-__init__()]] - `calls` [EXTRACTED]
- [[dot-__init__()_125]] - `method` [EXTRACTED]
- [[dot-_analyze_file_content()]] - `method` [EXTRACTED]
- [[dot-_analyze_script_content()]] - `method` [EXTRACTED]
- [[dot-_analyze_script_file()]] - `method` [EXTRACTED]
- [[dot-_quarantine_suspicious_files()]] - `method` [EXTRACTED]
- [[dot-_scan_git_hooks()]] - `method` [EXTRACTED]
- [[dot-_scan_package_json()]] - `method` [EXTRACTED]
- [[dot-_scan_pyproject_toml()]] - `method` [EXTRACTED]
- [[dot-_scan_setup_py()]] - `method` [EXTRACTED]
- [[dot-scan_content()]] - `method` [EXTRACTED]
- [[dot-scan_git_repository()]] - `method` [EXTRACTED]
- [[dot-test_clean_hook_passes()]] - `calls` [EXTRACTED]
- [[dot-test_clean_repo_no_findings()]] - `calls` [EXTRACTED]
- [[dot-test_curl_in_hook_flagged()]] - `calls` [EXTRACTED]
- [[dot-test_default_mode_is_enforce()_6]] - `calls` [EXTRACTED]
- [[dot-test_finding_has_file_path()]] - `calls` [EXTRACTED]
- [[dot-test_git_guard_detects_credential_patterns()]] - `calls` [INFERRED]
- [[dot-test_git_guard_instantiates()]] - `calls` [EXTRACTED]
- [[dot-test_git_guard_no_path_leak()]] - `calls` [INFERRED]
- [[dot-test_git_guard_scan_repo()]] - `calls` [EXTRACTED]
- [[dot-test_nc_flagged()]] - `calls` [EXTRACTED]
- [[dot-test_no_git_dir_returns_empty()]] - `calls` [EXTRACTED]
- [[dot-test_reverse_shell_flagged()]] - `calls` [EXTRACTED]
- [[dot-test_wget_flagged()]] - `calls` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[Monitor and analyze git hooks and package installation scripts.]] - `rationale_for` [EXTRACTED]
- [[TestExfiltrationDetection]] - `uses` [INFERRED]
- [[TestGitGuard]] - `uses` [INFERRED]
- [[TestGitGuardDefaultEnforce]] - `uses` [INFERRED]
- [[TestInfoLeakage]] - `uses` [INFERRED]
- [[TestLoggingSecurity]] - `uses` [INFERRED]
- [[TestModuleInstantiationInEnforceMode]] - `uses` [INFERRED]
- [[deep_security_test()]] - `uses` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[git_guard.py]] - `contains` [EXTRACTED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[middleware.py_2]] - `imports` [EXTRACTED]
- [[run()]] - `calls` [EXTRACTED]
- [[scan_repository()]] - `calls` [EXTRACTED]
- [[t_git()]] - `calls` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `imports` [EXTRACTED]
- [[test_git_guard.py]] - `imports` [EXTRACTED]
- [[test_round2_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/GitGuard
