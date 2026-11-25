---
source_file: "gateway/security/file_sandbox.py"
type: "code"
community: "FileSandbox"
location: "L186"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/FileSandbox
---

# FileSandbox

## Connections
- [[dot-__init__()]] - `calls` [EXTRACTED]
- [[dot-__init__()_62]] - `method` [EXTRACTED]
- [[dot-_check()]] - `method` [EXTRACTED]
- [[dot-_detect_raw_traversal()]] - `method` [EXTRACTED]
- [[dot-_is_immutable_file()]] - `method` [EXTRACTED]
- [[dot-_match_pattern()]] - `method` [EXTRACTED]
- [[dot-_matches_allowed_paths()]] - `method` [EXTRACTED]
- [[dot-_matches_blocked()]] - `method` [EXTRACTED]
- [[dot-check_read()]] - `method` [EXTRACTED]
- [[dot-check_write()]] - `method` [EXTRACTED]
- [[dot-detect_staging_patterns()]] - `method` [EXTRACTED]
- [[dot-get_audit_log()_3]] - `method` [EXTRACTED]
- [[dot-get_security_violations()]] - `method` [EXTRACTED]
- [[dot-get_temp_files()]] - `method` [EXTRACTED]
- [[dot-monitor_sandbox()]] - `calls` [EXTRACTED]
- [[dot-record_network_activity()]] - `method` [EXTRACTED]
- [[dot-sandbox()]] - `calls` [EXTRACTED]
- [[dot-test_file_sandbox_instantiates()]] - `calls` [EXTRACTED]
- [[dot-test_file_sandbox_mcp_write()]] - `calls` [INFERRED]
- [[dot-test_file_sandbox_staging_detection()]] - `calls` [INFERRED]
- [[dot-test_monitor_mode_allows_everything()]] - `calls` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[TestExfiltrationDetection]] - `uses` [INFERRED]
- [[TestFileSandbox]] - `uses` [INFERRED]
- [[TestMCPSecurity]] - `uses` [INFERRED]
- [[TestModuleInstantiationInEnforceMode]] - `uses` [INFERRED]
- [[TestNormalFileOperations]] - `uses` [INFERRED]
- [[deep_security_test()]] - `uses` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[file_sandbox.py]] - `contains` [EXTRACTED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[middleware.py_2]] - `imports` [EXTRACTED]
- [[run()]] - `calls` [EXTRACTED]
- [[sandbox()]] - `uses` [INFERRED]
- [[strict_sandbox()_1]] - `uses` [INFERRED]
- [[strict_sandbox()]] - `uses` [INFERRED]
- [[t_sandbox()]] - `calls` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `imports` [EXTRACTED]
- [[test_file_sandbox.py]] - `imports` [EXTRACTED]
- [[test_privilege_separation.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/FileSandbox
