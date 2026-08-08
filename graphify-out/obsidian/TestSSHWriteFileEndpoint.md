---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "code"
community: "Forward Routing & Approval"
location: "L119"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Forward_Routing__Approval
---

# TestSSHWriteFileEndpoint

## Connections
- [[.test_write_file_absolute_path_outside_root_rejected()]] - `method` [EXTRACTED]
- [[.test_write_file_absolute_path_prefix_collision_rejected()]] - `method` [EXTRACTED]
- [[.test_write_file_denial_is_audited()]] - `method` [EXTRACTED]
- [[.test_write_file_disallowed_host_rejected()]] - `method` [EXTRACTED]
- [[.test_write_file_empty_path_rejected()]] - `method` [EXTRACTED]
- [[.test_write_file_invalid_base64_rejected()]] - `method` [EXTRACTED]
- [[.test_write_file_no_auth()]] - `method` [EXTRACTED]
- [[.test_write_file_oversized_content_rejected()]] - `method` [EXTRACTED]
- [[.test_write_file_path_traversal_dotdot_rejected()]] - `method` [EXTRACTED]
- [[.test_write_file_remote_failure_returns_200_with_success_false()]] - `method` [EXTRACTED]
- [[.test_write_file_ssh_disabled_returns_503()]] - `method` [EXTRACTED]
- [[.test_write_file_valid_round_trip()]] - `method` [EXTRACTED]
- [[ApprovalQueue]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[DataLedger]] - `uses` [INFERRED]
- [[GatewayConfig_1]] - `uses` [INFERRED]
- [[LedgerConfig]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[RouterConfig_1]] - `uses` [INFERRED]
- [[SSHConfig]] - `uses` [INFERRED]
- [[SSHHostConfig]] - `uses` [INFERRED]
- [[SSHProxy]] - `uses` [INFERRED]
- [[SSHWriteResult]] - `uses` [INFERRED]
- [[test_ssh_write_file_endpoint.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Forward_Routing__Approval