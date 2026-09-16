---
source_file: "gateway/security/metadata_guard.py"
type: "code"
community: "Alert Dispatcher & RBAC Reliability"
location: "L36"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Alert_Dispatcher__RBAC_Reliability
---

# MetadataGuard

## Connections
- [[dot-__init__()_12]] - `calls` [EXTRACTED]
- [[dot-__init__()_19]] - `method` [EXTRACTED]
- [[dot-check_for_exif()]] - `method` [EXTRACTED]
- [[dot-check_oversized_headers()]] - `method` [EXTRACTED]
- [[dot-get_document_tag()]] - `method` [EXTRACTED]
- [[dot-guard()_6]] - `calls` [EXTRACTED]
- [[dot-sanitize_filename()]] - `method` [EXTRACTED]
- [[dot-sanitize_headers()]] - `method` [EXTRACTED]
- [[dot-sanitize_image_metadata()]] - `method` [EXTRACTED]
- [[dot-setup_method()_30]] - `calls` [EXTRACTED]
- [[dot-tag_document()]] - `method` [EXTRACTED]
- [[dot-test_metadata_guard_strips_internal_headers()]] - `calls` [INFERRED]
- [[dot-test_metadata_oversized_headers()]] - `calls` [EXTRACTED]
- [[dot-test_metadata_path_traversal_stripped()]] - `calls` [EXTRACTED]
- [[dot-test_metadata_sanitize_filename()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[Guards against metadata channel attacks and information disclosure.]] - `rationale_for` [EXTRACTED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestAuditTrail]] - `uses` [INFERRED]
- [[TestAuth]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard]] - `uses` [INFERRED]
- [[TestCryptography]] - `uses` [INFERRED]
- [[TestDependencySecurity]] - `uses` [INFERRED]
- [[TestDoSPrevention]] - `uses` [INFERRED]
- [[TestDocumentTagging]] - `uses` [INFERRED]
- [[TestExfiltrationDetection]] - `uses` [INFERRED]
- [[TestFileSandbox]] - `uses` [INFERRED]
- [[TestHTTPSecurity]] - `uses` [INFERRED]
- [[TestInfoLeakage]] - `uses` [INFERRED]
- [[TestLoggingSecurity]] - `uses` [INFERRED]
- [[TestMCPSecurity]] - `uses` [INFERRED]
- [[TestMetadataGuard]] - `uses` [INFERRED]
- [[TestNetworkSecurity]] - `uses` [INFERRED]
- [[TestPIIDetection_1]] - `uses` [INFERRED]
- [[TestPrivilegeEscalation]] - `uses` [INFERRED]
- [[TestPromptGuard]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestSupplyChain]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[metadata_guard.py]] - `contains` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_metadata_guard.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Alert_Dispatcher__RBAC_Reliability