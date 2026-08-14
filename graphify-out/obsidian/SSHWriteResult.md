---
source_file: "gateway/ssh_proxy/proxy.py"
type: "code"
community: "scripts/sync-cve-registry.py"
location: "L38"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# SSHWriteResult

## Connections
- [[.test_write_file_remote_failure_returns_200_with_success_false()]] - `calls` [EXTRACTED]
- [[.test_write_file_success_and_denial_both_create_distinct_ledger_entries()]] - `calls` [EXTRACTED]
- [[.test_write_file_success_creates_matching_ledger_entry()]] - `calls` [EXTRACTED]
- [[.test_write_file_valid_round_trip()]] - `calls` [EXTRACTED]
- [[.write_file()]] - `references` [EXTRACTED]
- [[Result of a structured SSH file-write operation (SSHProxy.write_file())]] - `rationale_for` [EXTRACTED]
- [[SSHConfig]] - `uses` [INFERRED]
- [[TestSSHProxyValidateWriteFile]] - `uses` [INFERRED]
- [[TestSSHProxyWriteFileTransport]] - `uses` [INFERRED]
- [[TestSSHWriteFileEndpoint]] - `uses` [INFERRED]
- [[TestSSHWriteFileLedgerAudit]] - `uses` [INFERRED]
- [[TestSSHWriteFileShellMetacharacterContentRoundTrip]] - `uses` [INFERRED]
- [[proxy.py]] - `contains` [EXTRACTED]
- [[test_ssh_write_file_endpoint.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/scripts/sync-cve-registrypy