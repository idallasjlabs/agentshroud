---
type: community
cohesion: 0.03
members: 107
---

# FileSandbox

**Cohesion:** 0.03 - loosely connected
**Members:** 107 nodes

## Members
- [[dot-__init__()_132]] - code - gateway/security/file_sandbox.py
- [[dot-_check()]] - code - gateway/security/file_sandbox.py
- [[dot-_detect_raw_traversal()]] - code - gateway/security/file_sandbox.py
- [[dot-_is_immutable_file()]] - code - gateway/security/file_sandbox.py
- [[dot-_match_pattern()]] - code - gateway/security/file_sandbox.py
- [[dot-_matches_allowed_paths()]] - code - gateway/security/file_sandbox.py
- [[dot-_matches_blocked()]] - code - gateway/security/file_sandbox.py
- [[dot-check_read()]] - code - gateway/security/file_sandbox.py
- [[dot-check_write()]] - code - gateway/security/file_sandbox.py
- [[dot-detect_staging_patterns()]] - code - gateway/security/file_sandbox.py
- [[dot-get_audit_log()_6]] - code - gateway/security/file_sandbox.py
- [[dot-get_security_violations()]] - code - gateway/security/file_sandbox.py
- [[dot-get_temp_files()]] - code - gateway/security/file_sandbox.py
- [[dot-record_network_activity()]] - code - gateway/security/file_sandbox.py
- [[dot-scan()_2]] - code - gateway/security/file_sandbox.py
- [[dot-test_api_key_pattern_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_audit_has_path()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_config_yaml_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_credential_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_credit_card_detected()_1]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_blocks_sensitive_paths()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_has_reasonable_allowed_paths()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_default_mode_is_enforce()_4]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_email_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_enforce_blocks_outside_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_enforce_blocks_sensitive()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_env_file_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_etc_passwd_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_etc_shadow_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_file_sandbox_mcp_write()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_file_sandbox_staging_detection()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_large_write_then_network_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_large_write_without_network_not_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_monitor_mode_allows_everything()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_no_pii_clean()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_pii_in_write_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_project_files_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_read_logged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_small_writes_not_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_soul_md_in_workspace_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_soul_md_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_ssh_private_key_flagged()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_ssn_detected()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_system_prompt_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_temp_file_tracking()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_tmp_read_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_tmp_write_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_workspace_read_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_workspace_write_allowed()]] - code - gateway/tests/test_file_sandbox.py
- [[dot-test_write_logged()]] - code - gateway/tests/test_file_sandbox.py
- [[Agent cannot modify SOUL.md behavioral instructions.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify SOUL.md even in workspace path.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify gateway configuration.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify security policies and behavioral instructions.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify system prompt files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[AgentShroud Module Inventory (Blue Team)]] - document - skills/custom/agentshroud-blueteam/references/module-inventory.md
- [[AgentShroud Module Inventory (Red Team)]] - document - skills/custom/agentshroud-redteam/references/module-inventory.md
- [[AgentShroud Skills Library]] - document - skills/README.md
- [[CVE-2026-34425 — Preflight Validation Bypass (Shell-Bleed)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Check if path is within any allowed pattern.]] - rationale - gateway/security/file_sandbox.py
- [[Check if path matches any blocked pattern.]] - rationale - gateway/security/file_sandbox.py
- [[Check if this is an immutable security file by name.]] - rationale - gateway/security/file_sandbox.py
- [[Custom Skills]] - document - skills/README.md
- [[Detect data staging patterns (collect → compress → exfil).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Detect path traversal attempts in raw input before normalization.]] - rationale - gateway/security/file_sandbox.py
- [[Directory Structure_1]] - document - skills/README.md
- [[Enhanced pattern matching for file paths.]] - rationale - gateway/security/file_sandbox.py
- [[Enterprise Security Feature Priorities (Steve Hay Assessment, Red Team copy)]] - document - skills/custom/agentshroud-redteam/references/steve-hay-assessment.md
- [[Even blocked paths are allowed in monitor mode (just flagged).]] - rationale - gateway/tests/test_file_sandbox.py
- [[FileOperation]] - code - gateway/security/file_sandbox.py
- [[FileSandbox]] - code - gateway/security/file_sandbox.py
- [[FileVerdict]] - code - gateway/security/file_sandbox.py
- [[Get all flagged operations that indicate security violations.]] - rationale - gateway/security/file_sandbox.py
- [[Large-write-then-network-activity stagingexfiltration pattern detection]] - concept - gateway/tests/test_file_sandbox.py
- [[MCP file writes should go through sandbox.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Module Coverage Heat Map Legend (EMAC—)]] - concept - skills/custom/agentshroud-blueteam/SKILL.md
- [[OpenClaw Built-in Skills]] - document - skills/README.md
- [[PIIFinding]] - code - gateway/security/file_sandbox.py
- [[PIIScanResult]] - code - gateway/security/file_sandbox.py
- [[PIIScanner]] - code - gateway/security/file_sandbox.py
- [[Privilege Separation File Sandbox Tests]] - code - gateway/tests/test_privilege_separation.py
- [[Red Team Assessment Plan (Steve Hay Plan, Red Team copy)]] - document - skills/custom/agentshroud-redteam/references/steve-hay-plan.md
- [[Round 2 Security Hardening Tests]] - code - gateway/tests/test_round2_hardening.py
- [[Rule agentshroud-path-traversal-open]] - concept - .semgrep.yml
- [[STPA-Sec Loss Categories (L-1 Data Disclosure, L-2 Unauthorized Actions, L-3 Agent Integrity, L-4 Audit Integrity)]] - concept - skills/custom/agentshroud-blueteam/references/steve-hay-assessment.md
- [[STPA-Sec Methodology]] - concept - docker/config/openclaw/skills/i-sec-defense/SKILL.md
- [[Sandbox with separation of privilege enforcement.]] - rationale - gateway/tests/test_privilege_separation.py
- [[StagingPattern]] - code - gateway/security/file_sandbox.py
- [[TestFileAudit]] - code - gateway/tests/test_file_sandbox.py
- [[TestFileSandboxConfig]] - code - gateway/tests/test_file_sandbox.py
- [[TestNormalFileOperations]] - code - gateway/tests/test_file_sandbox.py
- [[TestPIIScanning]] - code - gateway/tests/test_file_sandbox.py
- [[TestSecurityPolicyProtection]] - code - gateway/tests/test_privilege_separation.py
- [[TestSensitivePathBlocking]] - code - gateway/tests/test_file_sandbox.py
- [[TestStagingPatternDetection]] - code - gateway/tests/test_file_sandbox.py
- [[Unsafe Control Actions (UCA-1 through UCA-17)]] - concept - skills/custom/agentshroud-blueteam/references/steve-hay-assessment.md
- [[Usage_64]] - document - skills/README.md
- [[agentshroud-blueteamSKILL]] - document - skills/custom/agentshroud-blueteam/SKILL.md
- [[default_config()_1]] - code - gateway/tests/test_file_sandbox.py
- [[file_sandbox.py]] - code - gateway/security/file_sandbox.py
- [[sandbox()]] - code - gateway/tests/test_file_sandbox.py
- [[skillsREADME]] - document - skills/README.md
- [[strict_config()_2]] - code - gateway/tests/test_file_sandbox.py
- [[strict_sandbox()]] - code - gateway/tests/test_file_sandbox.py
- [[strict_sandbox()_1]] - code - gateway/tests/test_privilege_separation.py
- [[test_file_sandbox.py]] - code - gateway/tests/test_file_sandbox.py
- [[xml_leak_filter.py]] - code - gateway/security/xml_leak_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FileSandbox
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_dot-_make_proxy()]]
- 23 edges to [[_COMMUNITY_ContextGuard]]
- 15 edges to [[_COMMUNITY_Any]]
- 9 edges to [[_COMMUNITY_PathIsolationManager]]
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY__wrap_response()]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL.md (2)]]
- 1 edge to [[_COMMUNITY_A2AMethod]]
- 1 edge to [[_COMMUNITY__t]]
- 1 edge to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_Applies to Claude Code (primary) · Gemini CLI (secondary) · Codex CLI (tertiary)]]
- 1 edge to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_tool_chain_analyzer.py]]
- 1 edge to [[_COMMUNITY_GroupConfig]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_test_agent_cve_registry.py (2)]]
- 1 edge to [[_COMMUNITY_AgentShroud Module Inventory]]
- 1 edge to [[_COMMUNITY_Regression guard (2026-08-30) the report scanned latest tags while deploys…]]
- 1 edge to [[_COMMUNITY_DelegationManager]]

## Top bridge nodes
- [[agentshroud-blueteamSKILL]] - degree 28, connects to 18 communities
- [[FileSandbox]] - degree 85, connects to 6 communities
- [[TestSecurityPolicyProtection]] - degree 9, connects to 2 communities
- [[dot-test_file_sandbox_staging_detection()]] - degree 4, connects to 2 communities
- [[dot-test_file_sandbox_mcp_write()]] - degree 4, connects to 2 communities
