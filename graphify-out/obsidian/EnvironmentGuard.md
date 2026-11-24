---
source_file: "gateway/security/env_guard.py"
type: "code"
community: "EnvironmentGuard"
location: "L33"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/EnvironmentGuard
---

# EnvironmentGuard

## Connections
- [[dot-__init__()]] - `calls` [EXTRACTED]
- [[dot-__init__()_26]] - `method` [EXTRACTED]
- [[dot-_contains_env_access_patterns()]] - `method` [EXTRACTED]
- [[dot-_looks_like_credential()]] - `method` [EXTRACTED]
- [[dot-_record_leakage()]] - `method` [EXTRACTED]
- [[dot-check_command_execution()]] - `method` [EXTRACTED]
- [[dot-check_file_access()]] - `method` [EXTRACTED]
- [[dot-clear_detected_leakages()]] - `method` [EXTRACTED]
- [[dot-export_leakage_report()]] - `method` [EXTRACTED]
- [[dot-get_leakage_summary()]] - `method` [EXTRACTED]
- [[dot-monitor_environment_access()]] - `method` [EXTRACTED]
- [[dot-scrub_command_output()]] - `method` [EXTRACTED]
- [[dot-test_env_guard_command_check()]] - `calls` [EXTRACTED]
- [[dot-test_env_guard_detects_data_access()]] - `calls` [INFERRED]
- [[dot-test_env_guard_monitoring()]] - `calls` [EXTRACTED]
- [[dot-test_env_guard_scrub_output()]] - `calls` [EXTRACTED]
- [[dot-test_env_guard_scrubs_output()]] - `calls` [INFERRED]
- [[dot-test_natural_language_question_is_allowed()]] - `calls` [EXTRACTED]
- [[dot-test_unparseable_text_is_allowed()]] - `calls` [EXTRACTED]
- [[Guard against environment variable leakage and unauthorized access.]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[TestEnvGuardFailOpen]] - `uses` [INFERRED]
- [[TestExfiltrationDetection]] - `uses` [INFERRED]
- [[TestInfoLeakage]] - `uses` [INFERRED]
- [[TestLoggingSecurity]] - `uses` [INFERRED]
- [[deep_security_test()]] - `uses` [INFERRED]
- [[env_guard.py]] - `contains` [EXTRACTED]
- [[get_env_guard()]] - `references` [EXTRACTED]
- [[guard()_3]] - `uses` [INFERRED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[middleware.py_2]] - `imports` [EXTRACTED]
- [[t_env()]] - `calls` [EXTRACTED]
- [[test_env_guard_class.py]] - `imports` [EXTRACTED]
- [[test_round2_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/EnvironmentGuard
