---
source_file: "gateway/security/browser_security.py"
type: "code"
community: "RBAC Middleware & Ingest API"
location: "L103"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/RBAC_Middleware__Ingest_API
---

# BrowserSecurityGuard

## Connections
- [[.__init__()_8]] - `calls` [EXTRACTED]
- [[.__init__()_35]] - `calls` [EXTRACTED]
- [[.__init__()_48]] - `method` [EXTRACTED]
- [[.analyze_content()]] - `method` [EXTRACTED]
- [[.analyze_screenshot()]] - `method` [EXTRACTED]
- [[.can_enter_credentials()]] - `method` [EXTRACTED]
- [[.check_url_reputation()]] - `method` [EXTRACTED]
- [[.register_screenshot_hook()]] - `method` [EXTRACTED]
- [[.test_browser_security_guard_instantiates()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_6]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestCredentialProtection]] - `uses` [INFERRED]
- [[TestGetModuleModeEnforceDefault]] - `uses` [INFERRED]
- [[TestModuleConfigDefaults]] - `uses` [INFERRED]
- [[TestModuleInstantiationInEnforceMode]] - `uses` [INFERRED]
- [[TestScreenshotAnalysis]] - `uses` [INFERRED]
- [[TestSecurityConfigDefaults]] - `uses` [INFERRED]
- [[TestSocialEngineeringDetection]] - `uses` [INFERRED]
- [[TestURLReputation]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[browser_security.py]] - `contains` [EXTRACTED]
- [[guard()]] - `calls` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_all_modules_enforce.py]] - `imports` [EXTRACTED]
- [[web_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/RBAC_Middleware__Ingest_API