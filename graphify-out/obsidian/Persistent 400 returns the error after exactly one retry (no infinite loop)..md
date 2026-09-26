---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "CI test job (matrix ubuntu/macos x py3.11/3.13)"
location: "L4581"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/CI_test_job_matrix_ubuntu/macos_x_py311/313
---

# Persistent 400 returns the error after exactly one retry (no infinite loop).

## Connections
- [[.test_400_retry_no_loop()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/CI_test_job_matrix_ubuntu/macos_x_py311/313