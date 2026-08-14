---
source_file: "gateway/tests/test_context_integrity.py"
type: "code"
community: "Audit Export Pipeline"
location: "L38"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Audit_Export_Pipeline
---

# TestContextIntegrityScorer

## Connections
- [[.test_below_alert_threshold_logs_warning()]] - `method` [EXTRACTED]
- [[.test_duplicate_hashes_detected()]] - `method` [EXTRACTED]
- [[.test_empty_context_scores_clean()]] - `method` [EXTRACTED]
- [[.test_injected_untrusted_segment_lowers_score()]] - `method` [EXTRACTED]
- [[.test_pristine_context_scores_high()]] - `method` [EXTRACTED]
- [[.test_tampered_system_prompt_lowers_score()]] - `method` [EXTRACTED]
- [[ContextIntegrityScorer]] - `uses` [INFERRED]
- [[ContextSegment]] - `uses` [INFERRED]
- [[IntegrityScore]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SystemPromptFingerprint]] - `uses` [INFERRED]
- [[test_context_integrity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Audit_Export_Pipeline