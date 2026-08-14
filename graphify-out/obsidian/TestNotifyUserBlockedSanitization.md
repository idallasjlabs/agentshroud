---
source_file: "gateway/tests/test_round2_hardening.py"
type: "code"
community: "Collaborator Response Templates"
location: "L194"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Collaborator_Response_Templates
---

# TestNotifyUserBlockedSanitization

## Connections
- [[.test_sanitize_reason_preserves_simple_text()]] - `method` [EXTRACTED]
- [[.test_sanitize_reason_strips_file_paths()]] - `method` [EXTRACTED]
- [[.test_sanitize_reason_strips_module_paths()]] - `method` [EXTRACTED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EnvironmentGuard]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[ResourceGuard]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[test_round2_hardening.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Collaborator_Response_Templates