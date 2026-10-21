---
source_file: "gateway/tests/test_security_toolchain.py"
type: "code"
community: "ADR-001: Transparent Proxy vs Agent Modification"
location: "L410"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ADR-001_Transparent_Proxy_vs_Agent_Modification
---

# .test_image_keys_do_not_overwrite_each_other()

## Connections
- [[dot-_clean_report()]] - `calls` [EXTRACTED]
- [[dot-_make_app_state()]] - `calls` [EXTRACTED]
- [[dot-_make_store_result_fn()]] - `calls` [EXTRACTED]
- [[Per-image compound keys are independent — last image doesn't clobber first.]] - `rationale_for` [EXTRACTED]
- [[TestStartupScannerKeying]] - `method` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ADR-001_Transparent_Proxy_vs_Agent_Modification
