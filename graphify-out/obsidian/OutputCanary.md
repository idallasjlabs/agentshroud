---
source_file: "gateway/security/output_canary.py"
type: "code"
community: "lifespan.py"
location: "L59"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/lifespanpy
---

# OutputCanary

## Connections
- [[.__init__()_12]] - `calls` [EXTRACTED]
- [[.__init__()_97]] - `method` [EXTRACTED]
- [[._create_detection_patterns()]] - `method` [EXTRACTED]
- [[._create_invisible_canary()]] - `method` [EXTRACTED]
- [[._scan_for_canary()]] - `method` [EXTRACTED]
- [[.check_response()_1]] - `method` [EXTRACTED]
- [[.cleanup_expired_canaries()]] - `method` [EXTRACTED]
- [[.generate_canary()]] - `method` [EXTRACTED]
- [[.get_status()_3]] - `method` [EXTRACTED]
- [[.setup_method()_24]] - `calls` [EXTRACTED]
- [[.test_incident_logging()]] - `calls` [EXTRACTED]
- [[.test_output_canary_instantiates()]] - `calls` [EXTRACTED]
- [[.test_partial_canary_match_handling()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[Main Output Canary System for detecting prompt leakage.      This system generat]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[OutboundInfoFilter]] - `conceptually_related_to` [INFERRED]
- [[Output Canary System Tests]] - `references` [EXTRACTED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestGetModuleModeEnforceDefault]] - `uses` [INFERRED]
- [[TestModuleConfigDefaults]] - `uses` [INFERRED]
- [[TestModuleInstantiationInEnforceMode]] - `uses` [INFERRED]
- [[TestOutputCanary]] - `uses` [INFERRED]
- [[TestSecurityConfigDefaults]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[output_canary.py]] - `contains` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `imports` [EXTRACTED]
- [[test_output_canary.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/lifespanpy