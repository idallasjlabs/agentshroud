---
type: community
members: 83
---

# MiddlewareManager (4)

**Members:** 83 nodes

## Members
- [[dot-test_any_python_file_in_gateway_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_case_sensitivity()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_config_yaml_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_docker_compose_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_dockerfile_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_etc_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_gateway_config_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_gateway_source_read_flagged()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_gateway_source_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_modules_source_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_multiple_violations_tracked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_normal_operations_not_violations()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_path_traversal_blocked()_1]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_relative_path_resolution()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_security_module_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_sensitive_config_read_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_soul_md_in_workspace_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_soul_md_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_symlink_resolution()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_system_info_read_allowed()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_system_prompt_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_tmp_write_allowed()_1]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_usr_bin_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_var_log_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_violation_recorded_in_audit()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_wildcard_pattern_matching()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_workspace_read_allowed()_1]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_workspace_subdirectory_write_allowed()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_workspace_write_allowed()_1]] - code - gateway/tests/test_privilege_separation.py
- [[Agent can read basic system info.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can read its own workspace.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can still write to its own workspace.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can write to tmp for temporary files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can write to its own workspace directory.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can write to subdirectories in workspace.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify AgentShroud configuration files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify AgentShroud's own source code.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify Docker Compose configuration.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify Dockerfile.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify SOUL.md behavioral instructions.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify SOUL.md even in workspace path.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify gateway configuration.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify security policies and behavioral instructions.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify system paths.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify system prompt files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot read sensitive configuration.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to etc system configuration.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to usrbin system binaries.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to varlog system logs.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to gateway Python source files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to gateway config directory.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to security framework files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to security module source files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Any .py file in gateway directory should be blocked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Case variations should not bypass protection.]] - rationale - gateway/tests/test_privilege_separation.py
- [[FileSandbox in enforce mode with strict separation.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Middleware manager for request processing tests.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Multiple violations should all be tracked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Normal workspace operations should not be flagged as violations.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Path traversal attempts should be blocked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Reading gateway source should be flaggedblocked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Relative paths should be resolved properly.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Sandbox with separation of privilege enforcement.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Security violations should be recorded in audit log.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Symlinks should be resolved - symlink to blocked path must be caught.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test  wildcard patterns work correctly.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test edge cases and potential bypass attempts.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test file path pattern matching logic.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test read access controls.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test that security violations are properly logged and tracked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[TestAgentShroudSourceCodeProtection]] - code - gateway/tests/test_privilege_separation.py
- [[TestConfigurationProtection]] - code - gateway/tests/test_privilege_separation.py
- [[TestEdgeCases]] - code - gateway/tests/test_privilege_separation.py
- [[TestPatternMatching]] - code - gateway/tests/test_privilege_separation.py
- [[TestReadAccess]] - code - gateway/tests/test_privilege_separation.py
- [[TestSecurityPolicyProtection]] - code - gateway/tests/test_privilege_separation.py
- [[TestSecurityViolationLogging]] - code - gateway/tests/test_privilege_separation.py
- [[TestSystemPathProtection]] - code - gateway/tests/test_privilege_separation.py
- [[TestWorkspaceAccessPreserved]] - code - gateway/tests/test_privilege_separation.py
- [[enforce_config()]] - code - gateway/tests/test_privilege_separation.py
- [[middleware_manager()]] - code - gateway/tests/test_privilege_separation.py
- [[strict_sandbox()_1]] - code - gateway/tests/test_privilege_separation.py
- [[test_privilege_separation.py]] - code - gateway/tests/test_privilege_separation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager_4
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_AlertDispatcher]]
- 11 edges to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[test_privilege_separation.py]] - degree 15, connects to 2 communities
- [[TestAgentShroudSourceCodeProtection]] - degree 9, connects to 2 communities
- [[TestReadAccess]] - degree 9, connects to 2 communities
- [[TestSecurityPolicyProtection]] - degree 9, connects to 2 communities
- [[TestConfigurationProtection]] - degree 8, connects to 2 communities
