---
source_file: "gateway/security/metadata_guard.py"
type: "code"
community: "AlertDispatcher"
location: "L36"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/AlertDispatcher
---

# MetadataGuard

## Connections
- [[dot-__init__()_10]] - `calls` [EXTRACTED]
- [[dot-__init__()_13]] - `method` [EXTRACTED]
- [[dot-check_for_exif()]] - `method` [EXTRACTED]
- [[dot-check_oversized_headers()]] - `method` [EXTRACTED]
- [[dot-get_document_tag()]] - `method` [EXTRACTED]
- [[dot-guard()_5]] - `calls` [EXTRACTED]
- [[dot-sanitize_filename()]] - `method` [EXTRACTED]
- [[dot-sanitize_headers()]] - `method` [EXTRACTED]
- [[dot-sanitize_image_metadata()]] - `method` [EXTRACTED]
- [[dot-setup_method()_20]] - `calls` [EXTRACTED]
- [[dot-tag_document()]] - `method` [EXTRACTED]
- [[dot-test_metadata_guard_strips_internal_headers()]] - `calls` [INFERRED]
- [[dot-test_metadata_oversized_headers()]] - `calls` [EXTRACTED]
- [[dot-test_metadata_path_traversal_stripped()]] - `calls` [EXTRACTED]
- [[dot-test_metadata_sanitize_filename()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any]] - `uses` [INFERRED]
- [[Exception]] - `uses` [INFERRED]
- [[Guards against metadata channel attacks and information disclosure.]] - `rationale_for` [EXTRACTED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
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
- [[TestMetadataGuard_1]] - `uses` [INFERRED]
- [[TestNetworkSecurity]] - `uses` [INFERRED]
- [[TestPIIDetection]] - `uses` [INFERRED]
- [[TestPrivilegeEscalation]] - `uses` [INFERRED]
- [[TestPromptGuard]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestSupplyChain]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[metadata_guard.py]] - `contains` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_metadata_guard.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/AlertDispatcher
