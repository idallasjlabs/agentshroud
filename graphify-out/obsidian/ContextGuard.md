---
source_file: "gateway/security/context_guard.py"
type: "code"
community: "ContextGuard"
location: "L67"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ContextGuard
---

# ContextGuard

## Connections
- [[dot-__init__()_112]] - `calls` [EXTRACTED]
- [[dot-__init__()_72]] - `method` [EXTRACTED]
- [[dot-_detect_hidden_instructions()]] - `method` [EXTRACTED]
- [[dot-_detect_instruction_injection()]] - `method` [EXTRACTED]
- [[dot-_detect_rapid_context_growth()]] - `method` [EXTRACTED]
- [[dot-_detect_repetition_attacks()]] - `method` [EXTRACTED]
- [[dot-analyze_message()]] - `method` [EXTRACTED]
- [[dot-get_segment_provenance()]] - `method` [EXTRACTED]
- [[dot-get_session_risk_level()]] - `method` [EXTRACTED]
- [[dot-guard()]] - `calls` [EXTRACTED]
- [[dot-guard()_5]] - `calls` [EXTRACTED]
- [[dot-record_segment()]] - `method` [EXTRACTED]
- [[dot-tag_segment()]] - `method` [EXTRACTED]
- [[dot-test_context_guard_instantiates()]] - `calls` [EXTRACTED]
- [[dot-test_context_guard_session_isolation_under_load()]] - `calls` [INFERRED]
- [[dot-test_context_guard_tool_manipulation()]] - `calls` [INFERRED]
- [[dot-test_deeply_nested_context_attacks()]] - `calls` [INFERRED]
- [[dot-test_empty_inputs_everywhere()]] - `calls` [INFERRED]
- [[dot-test_json_injection_in_context()]] - `calls` [INFERRED]
- [[dot-test_oversized_json_payload()]] - `calls` [INFERRED]
- [[Guard against context window poisoning attacks.]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[TestConcurrency_1]] - `uses` [INFERRED]
- [[TestContextGuard_1]] - `uses` [INFERRED]
- [[TestDoSPrevention]] - `uses` [INFERRED]
- [[TestHTTPSecurity]] - `uses` [INFERRED]
- [[TestMCPSecurity]] - `uses` [INFERRED]
- [[TestModuleInstantiationInEnforceMode]] - `uses` [INFERRED]
- [[TestSourceTagging]] - `uses` [INFERRED]
- [[_make_full_pipeline()]] - `calls` [EXTRACTED]
- [[context_guard.py]] - `contains` [EXTRACTED]
- [[deep_security_test()]] - `uses` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[get_context_guard()]] - `references` [EXTRACTED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[middleware.py_2]] - `imports` [EXTRACTED]
- [[pipeline()]] - `uses` [INFERRED]
- [[run()_1]] - `calls` [EXTRACTED]
- [[t_context()]] - `calls` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `imports` [EXTRACTED]
- [[test_context_guard.py]] - `imports` [EXTRACTED]
- [[test_e2e_watchtower.py]] - `imports` [EXTRACTED]
- [[test_redteam_probes.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ContextGuard
