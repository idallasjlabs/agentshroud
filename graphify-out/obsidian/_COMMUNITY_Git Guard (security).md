---
type: community
cohesion: 0.03
members: 110
---

# Git Guard (security)

**Cohesion:** 0.03 - loosely connected
**Members:** 110 nodes

## Members
- [[.__init__()_79]] - code - gateway/security/env_guard.py
- [[.__init__()_82]] - code - gateway/security/git_guard.py
- [[._analyze_file_content()]] - code - gateway/security/git_guard.py
- [[._analyze_script_content()]] - code - gateway/security/git_guard.py
- [[._analyze_script_file()]] - code - gateway/security/git_guard.py
- [[._make_hook()]] - code - gateway/tests/test_git_guard.py
- [[._make_record()]] - code - gateway/tests/test_security_audit.py
- [[._quarantine_suspicious_files()]] - code - gateway/security/git_guard.py
- [[._scan_git_hooks()]] - code - gateway/security/git_guard.py
- [[._scan_package_json()]] - code - gateway/security/git_guard.py
- [[._scan_pyproject_toml()]] - code - gateway/security/git_guard.py
- [[._scan_setup_py()]] - code - gateway/security/git_guard.py
- [[.clear_detected_leakages()]] - code - gateway/security/env_guard.py
- [[.export_findings_report()]] - code - gateway/security/git_guard.py
- [[.export_leakage_report()]] - code - gateway/security/env_guard.py
- [[.get_findings_summary()]] - code - gateway/security/git_guard.py
- [[.get_leakage_summary()]] - code - gateway/security/env_guard.py
- [[.monitor_environment_access()]] - code - gateway/security/env_guard.py
- [[.monitor_git_operations()]] - code - gateway/security/git_guard.py
- [[.sanitizer()_2]] - code - gateway/tests/test_security_audit.py
- [[.scan_content()]] - code - gateway/security/git_guard.py
- [[.scan_git_repository()]] - code - gateway/security/git_guard.py
- [[.test_aws_key_redaction()]] - code - gateway/tests/test_security_audit.py
- [[.test_aws_key_redaction_via_pattern()]] - code - gateway/tests/test_security_audit.py
- [[.test_clean_hook_passes()]] - code - gateway/tests/test_git_guard.py
- [[.test_clean_repo_no_findings()]] - code - gateway/tests/test_git_guard.py
- [[.test_credit_card_in_logs()]] - code - gateway/tests/test_security_audit.py
- [[.test_curl_in_hook_flagged()]] - code - gateway/tests/test_git_guard.py
- [[.test_default_mode_is_enforce()_6]] - code - gateway/tests/test_round2_hardening.py
- [[.test_env_guard_command_check()]] - code - gateway/tests/test_security_audit.py
- [[.test_env_guard_detects_data_access()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_env_guard_monitoring()]] - code - gateway/tests/test_security_audit.py
- [[.test_env_guard_scrub_output()]] - code - gateway/tests/test_security_audit.py
- [[.test_env_guard_scrubs_output()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_finding_has_file_path()]] - code - gateway/tests/test_git_guard.py
- [[.test_from_environment_defaults_to_enforce()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_git_guard_detects_credential_patterns()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_git_guard_no_path_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_git_guard_scan_repo()]] - code - gateway/tests/test_security_audit.py
- [[.test_github_token_redaction()]] - code - gateway/tests/test_security_audit.py
- [[.test_jwt_redaction()]] - code - gateway/tests/test_security_audit.py
- [[.test_keyvault_instantiated_and_seeded_in_lifespan()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_llm_stats_endpoint_is_defined()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_natural_language_question_is_allowed()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_nc_flagged()]] - code - gateway/tests/test_git_guard.py
- [[.test_no_git_dir_returns_empty()]] - code - gateway/tests/test_git_guard.py
- [[.test_no_hardcoded_owner_id_in_lifespan()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_pipeline_scans_outbound_for_key_leaks()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_reverse_shell_flagged()]] - code - gateway/tests/test_git_guard.py
- [[.test_sanitize_reason_preserves_simple_text()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_sanitize_reason_strips_file_paths()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_sanitize_reason_strips_module_paths()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_scan_repository_default_enforce()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_ssn_redaction_in_logs()]] - code - gateway/tests/test_security_audit.py
- [[.test_unparseable_text_is_allowed()_1]] - code - gateway/tests/test_round2_hardening.py
- [[.test_v1_endpoint_handles_non_json_upstream_bodies()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_v1_endpoint_is_defined()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_wget_flagged()]] - code - gateway/tests/test_git_guard.py
- [[A security finding in git hooks or install scripts.]] - rationale - gateway/security/git_guard.py
- [[Analyze a script file for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Analyze file content for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Analyze script content string for malicious patterns.]] - rationale - gateway/security/git_guard.py
- [[Any_39]] - code - gateway/security/env_guard.py
- [[Any_41]] - code - gateway/security/git_guard.py
- [[Args             mode 'monitor' (log findings) or 'enforce' (quarantine suspic]] - rationale - gateway/security/git_guard.py
- [[Clear the list of detected leakages.]] - rationale - gateway/security/env_guard.py
- [[Convenience function to scan a repository.]] - rationale - gateway/security/git_guard.py
- [[Environment guard should monitor data access patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Environment guard should scrub sensitive output.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[EnvironmentGuard]] - code - gateway/security/env_guard.py
- [[Export findings to a detailed report.]] - rationale - gateway/security/git_guard.py
- [[Export leakage findings to a report file.]] - rationale - gateway/security/env_guard.py
- [[Get a summary of all findings.]] - rationale - gateway/security/git_guard.py
- [[Get summary of all detected leakages.]] - rationale - gateway/security/env_guard.py
- [[Get the global environment guard instance.]] - rationale - gateway/security/env_guard.py
- [[Git guard errors shouldn't expose full file paths.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Git guard should catch credential patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[GitGuard]] - code - gateway/security/git_guard.py
- [[Guard against environment variable leakage and unauthorized access.]] - rationale - gateway/security/env_guard.py
- [[Monitor an agent's environment access attempts.          Args             agent]] - rationale - gateway/security/env_guard.py
- [[Monitor and analyze git hooks and package installation scripts.]] - rationale - gateway/security/git_guard.py
- [[Monitor for git clone and npm install operations.]] - rationale - gateway/security/git_guard.py
- [[Move suspicious files to quarantine directory.]] - rationale - gateway/security/git_guard.py
- [[Path_12]] - code - gateway/security/git_guard.py
- [[Proxy endpoint must not crash if upstream returns non-JSON body.]] - rationale - gateway/tests/test_round2_hardening.py
- [[Scan a git repository for malicious hooks and scripts.          Args]] - rationale - gateway/security/git_guard.py
- [[Scan arbitrary text content for malicious gitsupply-chain patterns.          Th]] - rationale - gateway/security/git_guard.py
- [[Scan git hooks directory for malicious content.]] - rationale - gateway/security/git_guard.py
- [[Scan package.json for suspicious install scripts.]] - rationale - gateway/security/git_guard.py
- [[Scan pyproject.toml for suspicious build scripts.]] - rationale - gateway/security/git_guard.py
- [[Scan setup.py for suspicious installation scripts.]] - rationale - gateway/security/git_guard.py
- [[SecurityFinding]] - code - gateway/security/git_guard.py
- [[Test log sanitization and information leakage prevention.]] - rationale - gateway/tests/test_security_audit.py
- [[TestDRYOwnerChatID]] - code - gateway/tests/test_round2_hardening.py
- [[TestEgressConfigDefaultEnforce]] - code - gateway/tests/test_round2_hardening.py
- [[TestEnvGuardFailOpen]] - code - gateway/tests/test_round2_hardening.py
- [[TestGitGuard]] - code - gateway/tests/test_git_guard.py
- [[TestGitGuardDefaultEnforce]] - code - gateway/tests/test_round2_hardening.py
- [[TestKeyVaultWired]] - code - gateway/tests/test_round2_hardening.py
- [[TestLLMProxyEndpoints]] - code - gateway/tests/test_round2_hardening.py
- [[TestLoggingSecurity]] - code - gateway/tests/test_security_audit.py
- [[TestNotifyUserBlockedSanitization]] - code - gateway/tests/test_round2_hardening.py
- [[Tests for Round 2 hardening — 9 fixes.]] - rationale - gateway/tests/test_round2_hardening.py
- [[The llm-proxystats endpoint must exist.]] - rationale - gateway/tests/test_round2_hardening.py
- [[The v1{path} endpoint must exist (enabled in v0.9.0).]] - rationale - gateway/tests/test_round2_hardening.py
- [[env_guard.py]] - code - gateway/security/env_guard.py
- [[get_env_guard()]] - code - gateway/security/env_guard.py
- [[scan_repository()]] - code - gateway/security/git_guard.py
- [[test_git_guard.py]] - code - gateway/tests/test_git_guard.py
- [[test_round2_hardening.py]] - code - gateway/tests/test_round2_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Git_Guard_security
SORT file.name ASC
```

## Connections to other communities
- 38 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 32 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 17 edges to [[_COMMUNITY_OAuth & Metadata Guard]]
- 15 edges to [[_COMMUNITY_Privilege Separation & File Sandbox]]
- 15 edges to [[_COMMUNITY_Resource Guard & Local Model Parity]]
- 10 edges to [[_COMMUNITY_Env Guard (security)]]
- 8 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 8 edges to [[_COMMUNITY_Egress Filter]]
- 8 edges to [[_COMMUNITY_Env Guard Class]]
- 5 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 4 edges to [[_COMMUNITY_Security Hardening]]
- 3 edges to [[_COMMUNITY_Key Vault]]
- 2 edges to [[_COMMUNITY_Ingest API Main & Models]]
- 2 edges to [[_COMMUNITY_Browser Security]]
- 2 edges to [[_COMMUNITY_Egress Monitor]]
- 2 edges to [[_COMMUNITY_Security Audit]]
- 2 edges to [[_COMMUNITY_Subagent Monitor]]
- 1 edge to [[_COMMUNITY_Dns Filter]]
- 1 edge to [[_COMMUNITY_Agentshroud.yaml (03 - Configuration)]]
- 1 edge to [[_COMMUNITY_Egress Filter]]
- 1 edge to [[_COMMUNITY_All Modules Enforce]]
- 1 edge to [[_COMMUNITY_Security Regressions V1 2]]

## Top bridge nodes
- [[TestLoggingSecurity]] - degree 47, connects to 14 communities
- [[GitGuard]] - degree 85, connects to 11 communities
- [[EnvironmentGuard]] - degree 74, connects to 10 communities
- [[env_guard.py]] - degree 10, connects to 6 communities
- [[test_round2_hardening.py]] - degree 17, connects to 4 communities