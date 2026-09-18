---
source_file: "gateway/security/tool_result_injection.py"
type: "code"
community: "lifespan.py"
location: "L173"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/lifespanpy
---

# ToolResultInjectionScanner

## Connections
- [[.__init__()_12]] - `calls` [EXTRACTED]
- [[.__init__()_23]] - `method` [EXTRACTED]
- [[._detect_encoded_injection()]] - `method` [EXTRACTED]
- [[._detect_unicode_obfuscation()]] - `method` [EXTRACTED]
- [[.scan_tool_result()_2]] - `method` [EXTRACTED]
- [[.setup_method()_3]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
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
- [[ToolResultSanitizer_1]] - `conceptually_related_to` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[WS-E RT-2 Inbound Encoding Bypass Fix Rationale]] - `rationale_for` [EXTRACTED]
- [[_make_pipeline()_1]] - `calls` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[run()_4]] - `calls` [EXTRACTED]
- [[scanner()]] - `calls` [EXTRACTED]
- [[test_tool_injection_encoded_check_uses_full_ruleset()]] - `calls` [EXTRACTED]
- [[test_tool_injection_hex_encoded_uses_full_ruleset()]] - `calls` [EXTRACTED]
- [[test_tool_injection_scan.py]] - `imports` [EXTRACTED]
- [[test_tool_injection_scan_blocks_encoded_lower_ranked_rule()]] - `calls` [EXTRACTED]
- [[test_tool_result_injection.py]] - `imports` [EXTRACTED]
- [[test_ws_e_rt2_inbound_encoding.py]] - `references` [EXTRACTED]
- [[tool_result_injection.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/lifespanpy