---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "code"
community: "Community 64"
location: "L338"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_64
---

# TestSSHProxyValidateWriteFile

## Connections
- [[.test_absolute_path_outside_root_rejected()]] - `method` [EXTRACTED]
- [[.test_absolute_path_under_root_accepted()]] - `method` [EXTRACTED]
- [[.test_content_at_exact_cap_accepted()]] - `method` [EXTRACTED]
- [[.test_dotdot_traversal_from_absolute_path_rejected()]] - `method` [EXTRACTED]
- [[.test_dotdot_traversal_rejected()]] - `method` [EXTRACTED]
- [[.test_invalid_base64_rejected()]] - `method` [EXTRACTED]
- [[.test_null_byte_rejected()]] - `method` [EXTRACTED]
- [[.test_oversized_content_rejected()]] - `method` [EXTRACTED]
- [[.test_prefix_collision_sibling_dir_rejected()]] - `method` [EXTRACTED]
- [[.test_relative_path_resolved_under_root_accepted()]] - `method` [EXTRACTED]
- [[.test_root_itself_rejected()]] - `method` [EXTRACTED]
- [[.test_unknown_host_rejected()]] - `method` [EXTRACTED]
- [[.test_whitespace_only_path_rejected_at_proxy_layer()]] - `method` [EXTRACTED]
- [[ApprovalQueue]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[DataLedger]] - `uses` [INFERRED]
- [[GatewayConfig_1]] - `uses` [INFERRED]
- [[LedgerConfig]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[RouterConfig]] - `uses` [INFERRED]
- [[SSHConfig]] - `uses` [INFERRED]
- [[SSHHostConfig]] - `uses` [INFERRED]
- [[SSHProxy]] - `uses` [INFERRED]
- [[SSHWriteResult]] - `uses` [INFERRED]
- [[Unit tests for SSHProxy.validate_cwd().]] - `rationale_for` [EXTRACTED]
- [[test_ssh_write_file_endpoint.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_64