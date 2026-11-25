---
type: community
members: 111
---

# FileSandbox

**Members:** 111 nodes

## Members
- [[dot-__init__()_62]] - code - gateway/security/file_sandbox.py
- [[dot-_check()]] - code - gateway/security/file_sandbox.py
- [[dot-_detect_raw_traversal()]] - code - gateway/security/file_sandbox.py
- [[dot-_is_immutable_file()]] - code - gateway/security/file_sandbox.py
- [[dot-_match_pattern()]] - code - gateway/security/file_sandbox.py
- [[dot-_matches_allowed_paths()]] - code - gateway/security/file_sandbox.py
- [[dot-_matches_blocked()]] - code - gateway/security/file_sandbox.py
- [[dot-check_read()]] - code - gateway/security/file_sandbox.py
- [[dot-check_write()]] - code - gateway/security/file_sandbox.py
- [[dot-detect_staging_patterns()]] - code - gateway/security/file_sandbox.py
- [[dot-get_audit_log()_3]] - code - gateway/security/file_sandbox.py
- [[dot-get_security_violations()]] - code - gateway/security/file_sandbox.py
- [[dot-get_temp_files()]] - code - gateway/security/file_sandbox.py
- [[dot-record_network_activity()]] - code - gateway/security/file_sandbox.py
- [[dot-scan()]] - code - gateway/security/file_sandbox.py
- [[dot-test_api_key_pattern_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_audit_has_path()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_context_guard_tool_manipulation()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_credential_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_credit_card_detected()_1]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_blocks_sensitive_paths()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_has_reasonable_allowed_paths()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_mode_is_enforce()_3]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_mode_is_enforce()_4]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_dns_tunneling_detection()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_egress_monitor_loaded()_1]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_email_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_enforce_blocks_outside_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_enforce_blocks_sensitive()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_env_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_env_guard_detects_data_access()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_etc_passwd_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_etc_shadow_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_file_sandbox_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_file_sandbox_mcp_write()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_file_sandbox_staging_detection()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_git_guard_detects_credential_patterns()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_keyvault_instantiated_and_seeded_in_lifespan()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_large_write_then_network_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_large_write_without_network_not_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_llm_stats_endpoint_is_defined()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_mcp_proxy_module_exists()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_monitor_mode_allows_everything()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_no_hardcoded_owner_id_in_lifespan()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_no_pii_clean()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_pii_in_write_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_pipeline_scans_outbound_for_key_leaks()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_project_files_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_read_logged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_small_writes_not_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_ssh_private_key_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_ssn_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_temp_file_tracking()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_tmp_read_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_tmp_write_allowed()_1]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_v1_endpoint_handles_non_json_upstream_bodies()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_v1_endpoint_is_defined()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_workspace_read_allowed()_1]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_workspace_write_allowed()_1]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_write_logged()]] - code - gateway/tests/test_file_sandbox.py
- [[Check if path is within any allowed pattern.]] - rationale - gateway/security/file_sandbox.py
- [[Check if path matches any blocked pattern.]] - rationale - gateway/security/file_sandbox.py
- [[Check if this is an immutable security file by name.]] - rationale - gateway/security/file_sandbox.py
- [[Context guard should detect tool result manipulation.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Detect data staging patterns (collect → compress → exfil).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Detect path traversal attempts in raw input before normalization.]] - rationale - gateway/security/file_sandbox.py
- [[Egress monitoring should be available.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Enhanced pattern matching for file paths.]] - rationale - gateway/security/file_sandbox.py
- [[Environment guard should monitor data access patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Even blocked paths are allowed in monitor mode (just flagged).]] - rationale - gateway/tests/test_file_sandbox.py
- [[FileOperation]] - code - gateway/security/file_sandbox.py
- [[FileSandbox]] - code - gateway/security/file_sandbox.py
- [[FileSandboxConfig]] - code - gateway/security/file_sandbox.py
- [[FileVerdict]] - code - gateway/security/file_sandbox.py
- [[Get all flagged operations that indicate security violations.]] - rationale - gateway/security/file_sandbox.py
- [[Git guard should catch credential patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[High-entropy DNS queries indicate tunneling.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[MCP file writes should go through sandbox.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[MCP proxy module should be importable.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[PIIFinding]] - code - gateway/security/file_sandbox.py
- [[PIIScanResult]] - code - gateway/security/file_sandbox.py
- [[PIIScanner]] - code - gateway/security/file_sandbox.py
- [[Proxy endpoint must not crash if upstream returns non-JSON body.]] - rationale - gateway/tests/test_round2_hardening.py
- [[StagingPattern]] - code - gateway/security/file_sandbox.py
- [[Test MCP tool proxy security controls.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test detection of data exfiltration patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestDRYOwnerChatID]] - code - gateway/tests/test_round2_hardening.py
- [[TestExfiltrationDetection]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestFileAudit]] - code - gateway/tests/test_file_sandbox.py
- [[TestFileSandboxConfig]] - code - gateway/tests/test_file_sandbox.py
- [[TestFileSandboxDefaultEnforce]] - code - gateway/tests/test_round2_hardening.py
- [[TestKeyVaultWired]] - code - gateway/tests/test_round2_hardening.py
- [[TestLLMProxyEndpoints]] - code - gateway/tests/test_round2_hardening.py
- [[TestMCPSecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestNormalFileOperations]] - code - gateway/tests/test_file_sandbox.py
- [[TestPIIScanning]] - code - gateway/tests/test_file_sandbox.py
- [[TestSensitivePathBlocking]] - code - gateway/tests/test_file_sandbox.py
- [[TestStagingPatternDetection]] - code - gateway/tests/test_file_sandbox.py
- [[Tests for Round 2 hardening — 9 fixes.]] - rationale - gateway/tests/test_round2_hardening.py
- [[Tests for file IO sandboxing.]] - rationale - gateway/tests/test_file_sandbox.py
- [[The llm-proxystats endpoint must exist.]] - rationale - gateway/tests/test_round2_hardening.py
- [[The v1{path} endpoint must exist (enabled in v0.9.0).]] - rationale - gateway/tests/test_round2_hardening.py
- [[default_config()_3]] - code - gateway/tests/test_file_sandbox.py
- [[file_sandbox.py]] - code - gateway/security/file_sandbox.py
- [[fixture_49]] - code
- [[sandbox()]] - code - gateway/tests/test_file_sandbox.py
- [[strict_config()_1]] - code - gateway/tests/test_file_sandbox.py
- [[strict_sandbox()_1]] - code - gateway/tests/test_file_sandbox.py
- [[t_sandbox()]] - code - gateway/ingest_api/main.py
- [[test_file_sandbox.py]] - code - gateway/tests/test_file_sandbox.py
- [[test_round2_hardening.py]] - code - gateway/tests/test_round2_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FileSandbox
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_ContextGuard]]
- 7 edges to [[_COMMUNITY_middleware.py]]
- 6 edges to [[_COMMUNITY_TestFileSandbox]]
- 5 edges to [[_COMMUNITY_test_privilege_separation.py]]
- 5 edges to [[_COMMUNITY_GitGuard]]
- 4 edges to [[_COMMUNITY_EnvironmentGuard]]
- 3 edges to [[_COMMUNITY_test_all_modules_enforce.py]]
- 3 edges to [[_COMMUNITY_deep_security_test]]
- 3 edges to [[_COMMUNITY_TestModuleInstantiationInEnforceMode]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_EgressEvent]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_TestHTTPSecurity]]
- 2 edges to [[_COMMUNITY_PromptGuard]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_dot-_sanitize_reason]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[FileSandbox]] - degree 41, connects to 9 communities
- [[FileSandboxConfig]] - degree 31, connects to 9 communities
- [[test_round2_hardening.py]] - degree 17, connects to 6 communities
- [[TestExfiltrationDetection]] - degree 14, connects to 5 communities
- [[TestMCPSecurity]] - degree 12, connects to 4 communities
