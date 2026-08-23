---
source_file: "gateway/tests/test_canary.py"
type: "code"
community: "Security Audit & Watchtower Tests"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Security_Audit__Watchtower_Tests
---

# test_canary.py

## Connections
- [[ForwarderConfig]] - `imports` [EXTRACTED]
- [[HTTPForwarder]] - `imports` [EXTRACTED]
- [[PIIConfig]] - `imports` [EXTRACTED]
- [[PIISanitizer]] - `imports` [EXTRACTED]
- [[PromptGuard]] - `references` [EXTRACTED]
- [[SecurityPipeline]] - `imports` [EXTRACTED]
- [[TrustManager_1]] - `references` [EXTRACTED]
- [[canary_pipeline()]] - `contains` [EXTRACTED]
- [[healthy_forwarder()]] - `contains` [EXTRACTED]
- [[run_canary()]] - `imports` [EXTRACTED]
- [[test_canary_fails_without_pipeline()]] - `contains` [EXTRACTED]
- [[test_canary_message_contains_fake_pii()]] - `contains` [EXTRACTED]
- [[test_canary_passes_with_pipeline()]] - `contains` [EXTRACTED]
- [[test_canary_result_serialization()]] - `contains` [EXTRACTED]
- [[test_canary_verifies_audit_chain()]] - `contains` [EXTRACTED]
- [[test_canary_verifies_pii_stripping()]] - `contains` [EXTRACTED]
- [[test_canary_with_healthy_forwarder()]] - `contains` [EXTRACTED]
- [[test_canary_with_unhealthy_forwarder()]] - `contains` [EXTRACTED]
- [[test_clamav_pipeline.py]] - `semantically_similar_to` [INFERRED]
- [[test_e2e.py]] - `semantically_similar_to` [INFERRED]
- [[unhealthy_forwarder()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Security_Audit__Watchtower_Tests