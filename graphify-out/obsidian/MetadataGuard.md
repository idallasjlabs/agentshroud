---
source_file: "gateway/security/metadata_guard.py"
type: "code"
community: "Gateway Test Suite"
location: "L36"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Gateway_Test_Suite
---

# MetadataGuard

## Connections
- [[.__init__()_13]] - `calls` [EXTRACTED]
- [[.__init__()_94]] - `method` [EXTRACTED]
- [[.check_for_exif()]] - `method` [EXTRACTED]
- [[.check_oversized_headers()]] - `method` [EXTRACTED]
- [[.get_document_tag()]] - `method` [EXTRACTED]
- [[.guard()_1]] - `calls` [EXTRACTED]
- [[.sanitize_filename()]] - `method` [EXTRACTED]
- [[.sanitize_headers()]] - `method` [EXTRACTED]
- [[.sanitize_image_metadata()]] - `method` [EXTRACTED]
- [[.setup_method()_12]] - `calls` [EXTRACTED]
- [[.tag_document()]] - `method` [EXTRACTED]
- [[.test_metadata_guard_strips_internal_headers()]] - `calls` [INFERRED]
- [[.test_metadata_oversized_headers()]] - `calls` [EXTRACTED]
- [[.test_metadata_path_traversal_stripped()]] - `calls` [EXTRACTED]
- [[.test_metadata_sanitize_filename()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_8]] - `uses` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[Guards against metadata channel attacks and information disclosure.]] - `rationale_for` [EXTRACTED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestAuditTrail_1]] - `uses` [INFERRED]
- [[TestAuth_1]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard_1]] - `uses` [INFERRED]
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
- [[TestSupplyChain_1]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[metadata_guard.py]] - `contains` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_metadata_guard.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Gateway_Test_Suite