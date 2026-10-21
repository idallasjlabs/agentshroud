---
source_file: "gateway/security/tool_result_injection.py"
type: "code"
community: "MiddlewareManager"
location: "L173"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/MiddlewareManager
---

# ToolResultInjectionScanner

## Connections
- [[dot-__init__()_18]] - `calls` [EXTRACTED]
- [[dot-__init__()_66]] - `method` [EXTRACTED]
- [[dot-_detect_encoded_injection()]] - `method` [EXTRACTED]
- [[dot-_detect_unicode_obfuscation()]] - `method` [EXTRACTED]
- [[dot-scan_tool_result()_3]] - `method` [EXTRACTED]
- [[dot-setup_method()_12]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any]] - `uses` [INFERRED]
- [[Exception]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[RovoBlast Attack (Atlassian Rovo AI)]] - `implements` [EXTRACTED]
- [[Scanner for detecting prompt injection in tool results.]] - `rationale_for` [EXTRACTED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[TestCleanContent]] - `uses` [INFERRED]
- [[TestEncodedInjection]] - `uses` [INFERRED]
- [[TestHighSeverity]] - `uses` [INFERRED]
- [[TestMediumSeverity]] - `uses` [INFERRED]
- [[TestSanitization]] - `uses` [INFERRED]
- [[TestToolResultInjectionScanner]] - `uses` [INFERRED]
- [[TestUnicodeObfuscation]] - `uses` [INFERRED]
- [[ToolResultSanitizer]] - `conceptually_related_to` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[WS-E RT-2 Inbound Encoding Bypass Fix Rationale]] - `rationale_for` [EXTRACTED]
- [[_make_pipeline()_4]] - `calls` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[run()]] - `calls` [EXTRACTED]
- [[scanner()]] - `calls` [EXTRACTED]
- [[test_tool_injection_encoded_check_uses_full_ruleset()]] - `calls` [EXTRACTED]
- [[test_tool_injection_hex_encoded_uses_full_ruleset()]] - `calls` [EXTRACTED]
- [[test_tool_injection_scan.py]] - `imports` [EXTRACTED]
- [[test_tool_injection_scan_blocks_encoded_lower_ranked_rule()]] - `calls` [EXTRACTED]
- [[test_tool_result_injection.py]] - `imports` [EXTRACTED]
- [[test_ws_e_rt2_inbound_encoding.py]] - `references` [EXTRACTED]
- [[tool_result_injection.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/MiddlewareManager
