---
source_file: "docs/planning/reviews/enforcement-audit-script.py"
type: "code"
community: "middleware.py"
location: "L12"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/middlewarepy
---

# run()

## Connections
- [[dot-add_protected_content()]] - `indirect_call` [INFERRED]
- [[dot-scan_outbound()]] - `indirect_call` [INFERRED]
- [[Action]] - `uses` [INFERRED]
- [[ApprovalHardening]] - `calls` [EXTRACTED]
- [[ApprovalHardeningConfig]] - `calls` [EXTRACTED]
- [[ApprovalQueue]] - `calls` [INFERRED]
- [[AuditStore]] - `calls` [EXTRACTED]
- [[CanaryTripwire]] - `calls` [EXTRACTED]
- [[ContextGuard]] - `calls` [EXTRACTED]
- [[EgressAction]] - `uses` [INFERRED]
- [[EgressFilter]] - `calls` [EXTRACTED]
- [[EgressFilterConfig]] - `calls` [INFERRED]
- [[EncodingDetector]] - `calls` [EXTRACTED]
- [[FileSandbox]] - `calls` [EXTRACTED]
- [[FileSandboxConfig]] - `calls` [EXTRACTED]
- [[GitGuard]] - `calls` [EXTRACTED]
- [[MiddlewareManager]] - `calls` [EXTRACTED]
- [[PIIConfig]] - `calls` [INFERRED]
- [[PIISanitizer]] - `calls` [EXTRACTED]
- [[PathIsolationConfig]] - `calls` [EXTRACTED]
- [[PathIsolationManager]] - `calls` [EXTRACTED]
- [[PromptGuard]] - `calls` [EXTRACTED]
- [[PromptProtection]] - `calls` [EXTRACTED]
- [[RBACConfig]] - `uses` [INFERRED]
- [[RBACManager]] - `calls` [EXTRACTED]
- [[Resource]] - `uses` [INFERRED]
- [[Role]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `calls` [EXTRACTED]
- [[ToolResultInjectionScanner]] - `calls` [EXTRACTED]
- [[TrustManager]] - `calls` [EXTRACTED]
- [[UserSessionManager]] - `calls` [EXTRACTED]
- [[XMLLeakFilter]] - `calls` [EXTRACTED]
- [[enforcement-audit-script.py]] - `contains` [EXTRACTED]
- [[fail()]] - `calls` [EXTRACTED]
- [[ok()]] - `calls` [EXTRACTED]
- [[warn()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/middlewarepy
