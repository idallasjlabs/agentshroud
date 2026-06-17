---
source_file: "gateway/security/prompt_guard.py"
type: "code"
community: "Context Guard & Integrity"
location: "L54"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Context_Guard__Integrity
---

# SystemPromptFingerprint

## Connections
- [[.register_system_prompt()]] - `references` [EXTRACTED]
- [[.verify_system_prompt()]] - `references` [EXTRACTED]
- [[Any_32]] - `uses` [INFERRED]
- [[ContextIntegrityScorer]] - `uses` [INFERRED]
- [[HMAC-SHA256 fingerprint for a registered system prompt.]] - `rationale_for` [EXTRACTED]
- [[IntegrityScore]] - `uses` [INFERRED]
- [[TestContextIntegrityScorer]] - `uses` [INFERRED]
- [[TestNewPatternsV080]] - `uses` [INFERRED]
- [[TestReanchorDelimiters]] - `uses` [INFERRED]
- [[TestSystemPromptHMAC]] - `uses` [INFERRED]
- [[TestToolResultScan]] - `uses` [INFERRED]
- [[context_integrity.py]] - `imports` [EXTRACTED]
- [[prompt_guard.py]] - `contains` [EXTRACTED]
- [[test_context_integrity.py]] - `imports` [EXTRACTED]
- [[test_prompt_guard.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Context_Guard__Integrity