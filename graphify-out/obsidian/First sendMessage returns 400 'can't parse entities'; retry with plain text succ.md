---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "test_colima_and_sdk_patch_fallback_resolution.sh"
location: "L4538"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_colima_and_sdk_patch_fallback_resolutionsh
---

# First sendMessage returns 400 'can't parse entities'; retry with plain text succ

## Connections
- [[dot-test_400_retry_succeeds_when_text_strippable()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_colima_and_sdk_patch_fallback_resolutionsh
