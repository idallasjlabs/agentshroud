---
source_file: "gateway/security/tool_result_sanitizer_enhanced.py"
type: "code"
community: "ToolResultSanitizer"
location: "L90"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ToolResultSanitizer
---

# ToolResultSanitizer

## Connections
- [[.__init__()_172]] - `method` [EXTRACTED]
- [[._domain_matches_pattern()]] - `method` [EXTRACTED]
- [[._extract_code_blocks()]] - `method` [EXTRACTED]
- [[._is_domain_allowed()]] - `method` [EXTRACTED]
- [[._is_internal_link()]] - `method` [EXTRACTED]
- [[._restore_code_blocks()]] - `method` [EXTRACTED]
- [[._url_has_blocked_patterns()]] - `method` [EXTRACTED]
- [[.sanitize()_4]] - `method` [EXTRACTED]
- [[.sanitize_images()]] - `method` [EXTRACTED]
- [[.sanitize_links()]] - `method` [EXTRACTED]
- [[.setup_method()_36]] - `calls` [EXTRACTED]
- [[.test_performance_with_large_content()]] - `calls` [EXTRACTED]
- [[.test_realistic_web_scraping_result()]] - `calls` [EXTRACTED]
- [[.test_warn_mode()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[Enhanced markdown sanitizer with configurable domain allowlist.]] - `rationale_for` [EXTRACTED]
- [[Exception_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestIntegration_1]] - `uses` [INFERRED]
- [[TestToolResultSanitizer_1]] - `uses` [INFERRED]
- [[TestToolResultSanitizerConfig]] - `uses` [INFERRED]
- [[ToolResultInjectionScanner]] - `conceptually_related_to` [INFERRED]
- [[ToolResultSanitizer]] - `semantically_similar_to` [INFERRED]
- [[ToolResultSanitizerConfig]] - `references` [EXTRACTED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[sanitize_tool_result()]] - `calls` [EXTRACTED]
- [[test_tool_result_sanitizer_enhanced.py]] - `imports` [EXTRACTED]
- [[tool_result_sanitizer_enhanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ToolResultSanitizer