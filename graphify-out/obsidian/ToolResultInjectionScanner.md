---
source_file: "gateway/security/tool_result_injection.py"
type: "code"
community: "Egress & RBAC Security Core"
location: "L173"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress__RBAC_Security_Core
---

# ToolResultInjectionScanner

## Connections
- [[.__init__()_18]] - `calls` [EXTRACTED]
- [[.__init__()_119]] - `method` [EXTRACTED]
- [[._detect_encoded_injection()]] - `method` [EXTRACTED]
- [[._detect_unicode_obfuscation()]] - `method` [EXTRACTED]
- [[.scan_tool_result()_3]] - `method` [EXTRACTED]
- [[.setup_method()_36]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_10]] - `uses` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[PromptGuard]] - `semantically_similar_to` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[Scanner for detecting prompt injection in tool results.]] - `rationale_for` [EXTRACTED]
- [[SecurityPipeline_2]] - `uses` [INFERRED]
- [[TestCleanContent]] - `uses` [INFERRED]
- [[TestEncodedInjection]] - `uses` [INFERRED]
- [[TestHighSeverity]] - `uses` [INFERRED]
- [[TestMediumSeverity]] - `uses` [INFERRED]
- [[TestSanitization]] - `uses` [INFERRED]
- [[TestToolResultInjectionScanner]] - `uses` [INFERRED]
- [[TestUnicodeObfuscation]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[WS-E RT-2 Inbound Encoding Bypass Fix Rationale]] - `rationale_for` [EXTRACTED]
- [[_make_pipeline()_4]] - `calls` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[run()_3]] - `calls` [EXTRACTED]
- [[scanner()]] - `calls` [EXTRACTED]
- [[test_tool_injection_encoded_check_uses_full_ruleset()]] - `calls` [EXTRACTED]
- [[test_tool_injection_hex_encoded_uses_full_ruleset()]] - `calls` [EXTRACTED]
- [[test_tool_injection_scan.py]] - `imports` [EXTRACTED]
- [[test_tool_injection_scan_blocks_encoded_lower_ranked_rule()]] - `calls` [EXTRACTED]
- [[test_tool_result_injection.py]] - `imports` [EXTRACTED]
- [[test_ws_e_rt2_inbound_encoding.py]] - `references` [EXTRACTED]
- [[tool_result_injection.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress__RBAC_Security_Core