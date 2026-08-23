---
type: community
cohesion: 0.05
members: 66
---

# Ssh Write File Endpoint

**Cohesion:** 0.05 - loosely connected
**Members:** 66 nodes

## Members
- [[..' escaping the allowed root is rejected — never reaches proxy.write_file().]] - rationale - gateway/tests/test_ssh_write_file_endpoint.py
- [[.__init__()_133]] - code - gateway/ssh_proxy/proxy.py
- [[.is_auto_approved()]] - code - gateway/ssh_proxy/proxy.py
- [[.test_absolute_path_accepted()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_absolute_path_outside_root_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_absolute_path_under_root_accepted()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_backtick_rejected()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_content_at_exact_cap_accepted()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_content_with_semicolon_backtick_redirect_round_trips_through_full_endpoint()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_dotdot_traversal_from_absolute_path_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_dotdot_traversal_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_home_tilde_accepted()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_invalid_base64_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_null_byte_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_oversized_content_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_pipe_rejected()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_prefix_collision_sibling_dir_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_relative_path_rejected()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_relative_path_resolved_under_root_accepted()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_root_itself_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_semicolon_rejected()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.test_unknown_host_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_whitespace_only_path_rejected_at_proxy_layer()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_absolute_path_outside_root_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_absolute_path_prefix_collision_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_denial_is_audited()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_disallowed_host_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_empty_path_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_no_auth()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_non_numeric_stdout_falls_back_to_zero_bytes()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_oserror_from_subprocess()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_oversized_content_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_path_traversal_dotdot_rejected()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_remote_command_is_identical_across_calls()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_sends_path_and_content_via_stdin()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_ssh_disabled_returns_503()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_timeout()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.test_write_file_unknown_host_raises()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[.validate_command()]] - code - gateway/ssh_proxy/proxy.py
- [[.validate_cwd()]] - code - gateway/ssh_proxy/proxy.py
- [[.validate_write_file()]] - code - gateway/ssh_proxy/proxy.py
- [[.write_file()]] - code - gateway/ssh_proxy/proxy.py
- [[A directory that shares the root as a raw string prefix but is not         actua]] - rationale - gateway/tests/test_ssh_write_file_endpoint.py
- [[A host not present in the SSH allowlist is rejected with 404.]] - rationale - gateway/tests/test_ssh_write_file_endpoint.py
- [[A sibling directory that merely shares the root as a string prefix         (no ']] - rationale - gateway/tests/test_ssh_write_file_endpoint.py
- [[Absolute path outside the approved root is rejected.]] - rationale - gateway/tests/test_ssh_write_file_endpoint.py
- [[Check if a command is auto-approved (no human approval needed).          Auto-ap]] - rationale - gateway/ssh_proxy/proxy.py
- [[Decoded content exceeding the ~500KB cap is rejected with 413, and         proxy]] - rationale - gateway/tests/test_ssh_write_file_endpoint.py
- [[Denied write attempts are logged to the ledger for audit (no raw         content]] - rationale - gateway/tests/test_ssh_write_file_endpoint.py
- [[Direct unit coverage of validate_write_file()'s own empty-path guard         (th]] - rationale - gateway/tests/test_ssh_write_file_endpoint.py
- [[If the remote script exits 0 but its stdout isn't a parseable         integer, b]] - rationale - gateway/tests/test_ssh_write_file_endpoint.py
- [[SSH command proxy with validation and audit support]] - rationale - gateway/ssh_proxy/proxy.py
- [[SSHConfig_1]] - code - gateway/ssh_proxy/proxy.py
- [[SSHProxy]] - code - gateway/ssh_proxy/proxy.py
- [[TestSSHProxyValidateWriteFile]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[TestSSHProxyWriteFileTransport]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[TestSSHValidateCwd]] - code - gateway/tests/test_ssh_endpoints.py
- [[The remote command string must not vary with request content —         proving i]] - rationale - gateway/tests/test_ssh_write_file_endpoint.py
- [[Unit tests for SSHProxy.validate_cwd().]] - rationale - gateway/tests/test_ssh_endpoints.py
- [[Unit tests for SSHProxy.write_file() — verifies pathcontent travel as     DATA]] - rationale - gateway/tests/test_ssh_write_file_endpoint.py
- [[Validate a command against allowdeny lists and injection patterns.          Ret]] - rationale - gateway/ssh_proxy/proxy.py
- [[Validate a remote working-directory path.  Must be absolute and shell-safe.]] - rationale - gateway/ssh_proxy/proxy.py
- [[Validate a structured sshwrite_file request (host, path, content).          Re]] - rationale - gateway/ssh_proxy/proxy.py
- [[Write file content to a remote host via structured (non-shell-string) transport.]] - rationale - gateway/ssh_proxy/proxy.py
- [[_b64()]] - code - gateway/tests/test_ssh_write_file_endpoint.py
- [[ssh binary missing  spawn failure surfaces as exit_code=-1 with         the OSE]] - rationale - gateway/tests/test_ssh_write_file_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Ssh_Write_File_Endpoint
SORT file.name ASC
```

## Connections to other communities
- 67 edges to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]
- 13 edges to [[_COMMUNITY_Ssh Proxy]]
- 9 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 3 edges to [[_COMMUNITY_Queue (approval_queue)]]
- 3 edges to [[_COMMUNITY_Enhanced Approval]]
- 1 edge to [[_COMMUNITY_Ingest API Main & Models]]
- 1 edge to [[_COMMUNITY_Security Fixes]]
- 1 edge to [[_COMMUNITY_Security Fixes]]
- 1 edge to [[_COMMUNITY_Security Fixes]]

## Top bridge nodes
- [[SSHProxy]] - degree 79, connects to 7 communities
- [[TestSSHValidateCwd]] - degree 21, connects to 5 communities
- [[TestSSHProxyValidateWriteFile]] - degree 28, connects to 4 communities
- [[TestSSHProxyWriteFileTransport]] - degree 21, connects to 4 communities
- [[_b64()]] - degree 33, connects to 1 community