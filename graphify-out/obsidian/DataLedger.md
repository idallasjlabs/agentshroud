---
source_file: "gateway/ingest_api/ledger.py"
type: "code"
community: "Gateway Config & PII Sanitizer"
location: "L66"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Config__PII_Sanitizer
---

# DataLedger

## Connections
- [[dot-__init__()_69]] - `method` [EXTRACTED]
- [[dot-_hash_content()]] - `method` [EXTRACTED]
- [[dot-close()_10]] - `method` [EXTRACTED]
- [[dot-delete_entry()]] - `method` [EXTRACTED]
- [[dot-disabled_client()]] - `calls` [EXTRACTED]
- [[dot-enforce_retention()]] - `method` [EXTRACTED]
- [[dot-get_entry()]] - `method` [EXTRACTED]
- [[dot-get_stats()_11]] - `method` [EXTRACTED]
- [[dot-initialize()_1]] - `method` [EXTRACTED]
- [[dot-ledger()]] - `calls` [EXTRACTED]
- [[dot-ledger()_1]] - `calls` [EXTRACTED]
- [[dot-no_approval_client()]] - `calls` [EXTRACTED]
- [[dot-query()]] - `method` [EXTRACTED]
- [[dot-record()_2]] - `method` [EXTRACTED]
- [[AppState]] - `uses` [INFERRED]
- [[Async SQLite-backed data ledger      Records all content forwarded through the g]] - `rationale_for` [EXTRACTED]
- [[Data Flow]] - `references` [EXTRACTED]
- [[FastAPI_1]] - `uses` [INFERRED]
- [[GatewayConfig_1]] - `uses` [INFERRED]
- [[LedgerConfig]] - `uses` [INFERRED]
- [[LedgerEntry]] - `uses` [INFERRED]
- [[LedgerQueryResponse]] - `uses` [INFERRED]
- [[LogRecord_2]] - `uses` [INFERRED]
- [[PIISanitizer_1]] - `uses` [INFERRED]
- [[Startup Sequence]] - `references` [EXTRACTED]
- [[TestAuditChainIntegrity]] - `uses` [INFERRED]
- [[TestAuditChainPerformance]] - `uses` [INFERRED]
- [[TestBenchmarkBaseline]] - `uses` [INFERRED]
- [[TestChainExportAndVerification]] - `uses` [INFERRED]
- [[TestConcurrentWrites]] - `uses` [INFERRED]
- [[TestFullPipelineLatency]] - `uses` [INFERRED]
- [[TestPIISanitizerPerformance]] - `uses` [INFERRED]
- [[TestPromptGuardPerformance]] - `uses` [INFERRED]
- [[TestRetention]] - `uses` [INFERRED]
- [[TestSSHDisabledEndpoint]] - `uses` [INFERRED]
- [[TestSSHExec]] - `uses` [INFERRED]
- [[TestSSHHistory]] - `uses` [INFERRED]
- [[TestSSHHosts]] - `uses` [INFERRED]
- [[TestSSHProxyValidateWriteFile]] - `uses` [INFERRED]
- [[TestSSHProxyWriteFileTransport]] - `uses` [INFERRED]
- [[TestSSHRequireApprovalFalse]] - `uses` [INFERRED]
- [[TestSSHValidateCwd]] - `uses` [INFERRED]
- [[TestSSHWriteFileEndpoint]] - `uses` [INFERRED]
- [[TestSSHWriteFileLedgerAudit]] - `uses` [INFERRED]
- [[TestSSHWriteFileShellMetacharacterContentRoundTrip]] - `uses` [INFERRED]
- [[TestSecurityPipelineChainLatency]] - `uses` [INFERRED]
- [[TestTamperDetection]] - `uses` [INFERRED]
- [[TestTrustManagerPerformance]] - `uses` [INFERRED]
- [[_DropInvalidHTTPRequestFilter]] - `uses` [INFERRED]
- [[client()_19]] - `calls` [EXTRACTED]
- [[client()_20]] - `calls` [EXTRACTED]
- [[conftest.py]] - `imports` [EXTRACTED]
- [[ledger()]] - `calls` [EXTRACTED]
- [[ledger()_1]] - `calls` [EXTRACTED]
- [[ledger.py]] - `contains` [EXTRACTED]
- [[ledger.py_1]] - `references` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[state.py]] - `imports` [EXTRACTED]
- [[test_audit_chain.py]] - `imports` [EXTRACTED]
- [[test_initialize_is_idempotent()]] - `calls` [EXTRACTED]
- [[test_ledger()]] - `calls` [EXTRACTED]
- [[test_ledger.py]] - `imports` [EXTRACTED]
- [[test_performance.py]] - `imports` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]
- [[test_ssh_endpoints.py]] - `imports` [EXTRACTED]
- [[test_ssh_write_file_endpoint.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Config__PII_Sanitizer