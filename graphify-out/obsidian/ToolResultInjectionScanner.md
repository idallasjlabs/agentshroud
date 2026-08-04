---
source_file: "gateway/security/tool_result_injection.py"
type: "code"
community: "RBAC Middleware & Ingest API"
location: "L173"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RBAC_Middleware__Ingest_API
---

# ToolResultInjectionScanner

## Connections
- [[.__init__()_8]] - `calls` [EXTRACTED]
- [[.__init__()_97]] - `method` [EXTRACTED]
- [[._detect_encoded_injection()]] - `method` [EXTRACTED]
- [[._detect_unicode_obfuscation()]] - `method` [EXTRACTED]
- [[.scan_tool_result()_2]] - `method` [EXTRACTED]
- [[.setup_method()_33]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_6]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[Scanner for detecting prompt injection in tool results.]] - `rationale_for` [EXTRACTED]
- [[TestCleanContent]] - `uses` [INFERRED]
- [[TestEncodedInjection]] - `uses` [INFERRED]
- [[TestHighSeverity]] - `uses` [INFERRED]
- [[TestMediumSeverity]] - `uses` [INFERRED]
- [[TestSanitization]] - `uses` [INFERRED]
- [[TestToolResultInjectionScanner]] - `uses` [INFERRED]
- [[TestUnicodeObfuscation]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[run()]] - `calls` [EXTRACTED]
- [[scanner()]] - `calls` [EXTRACTED]
- [[test_tool_injection_scan.py]] - `imports` [EXTRACTED]
- [[test_tool_result_injection.py]] - `imports` [EXTRACTED]
- [[tool_result_injection.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/RBAC_Middleware__Ingest_API
